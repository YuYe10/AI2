# %%
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
from datasets import load_dataset

# %%
dataset = load_dataset("G:/AI/AI2/2-dataset/data/data.py",name="default")
# dataset

# %%
import torch

tokenizer = AutoTokenizer.from_pretrained('G:/Model/bert-base-uncased')

def tokenize(batch):
    return tokenizer(batch['text'], padding=True, truncation=True)
tokenized_datasets = dataset.map(tokenize, batched=True)
tokenized_datasets = tokenized_datasets.rename_column("label", "labels")
tokenized_datasets.set_format('torch', columns=['input_ids', 'attention_mask', 'labels'])
# tokenized_datasets

# %%
model = AutoModelForSequenceClassification.from_pretrained('G:/Model/bert-base-uncased', num_labels=2)

# %%
training_args = TrainingArguments(
    output_dir='./results',
    evaluation_strategy='epoch',
    save_strategy='epoch',
    learning_rate=2e-5,
    per_device_train_batch_size=8,
    gradient_accumulation_steps=32,  # *** 梯度累加 ***
    gradient_checkpointing=True,     # *** 梯度检查点 ***
    optim="adafactor",               # *** adafactor优化器 *** 
    per_device_eval_batch_size=8,
    logging_steps=10,
    num_train_epochs=1,
    weight_decay=0.01,
    report_to="none",
    load_best_model_at_end=True,
)

CLASS_NAME = {0: "negative", 1: "positive"}

# %%
from transformers import DataCollatorWithPadding

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets['train'],
    eval_dataset=tokenized_datasets['test'],
    tokenizer=tokenizer,
    data_collator=DataCollatorWithPadding(tokenizer=tokenizer),
)

# %%
trainer.train()

# %%
model.save_pretrained('./sentiment_model')
tokenizer.save_pretrained('./sentiment_model')

# %%
test_reviews = [
    "I absolutely loved this movie! The storyline was captivating and the acting was top-notch. A must-watch for everyone.",
    "This movie was a complete waste of time. The plot was predictable and the characters were poorly developed.",
    "An excellent film with a heartwarming story. The performances were outstanding, especially the lead actor.",
    "I found the movie to be quite boring. It dragged on and didn't really go anywhere. Not recommended.",
    "A masterpiece! The director did an amazing job bringing this story to life. The visuals were stunning.",
    "Terrible movie. The script was awful and the acting was even worse. I can't believe I sat through the whole thing.",
    "A delightful film with a perfect mix of humor and drama. The cast was great and the dialogue was witty.",
    "I was very disappointed with this movie. It had so much potential, but it just fell flat. The ending was particularly bad.",
    "One of the best movies I've seen this year. The story was original and the performances were incredibly moving.",
    "I didn't enjoy this movie at all. It was confusing and the pacing was off. Definitely not worth watching."
]


id2_label = {0: "nagetive！", 1: "positive！"}
model.eval()
for sen in test_reviews:
    with torch.inference_mode():
        inputs = tokenizer(sen, return_tensors="pt")
        inputs = {k: v.cuda() for k, v in inputs.items()}
        logits = model(**inputs).logits
        pred = torch.argmax(logits, dim=-1)
        print(f"输入：{sen}\n模型预测结果:{id2_label.get(pred.item())}")

# %%
from transformers import pipeline

model.config.id2label = id2_label
pipe = pipeline("text-classification", model=model, tokenizer=tokenizer, device=0)

# %%
for sen in test_reviews:
    print(pipe(sen))


