import os
import unittest

from datasets import load_dataset, Dataset

class TestDataset(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.dataset_dict = load_dataset("G:/AI/AI2/2-dataset/data", name="default", data_dir="G:/AI/AI2/2-dataset/data", trust_remote_code=True)

    def _test_dataset(self, dataset: Dataset):
        self.assertEqual(dataset.version, "1.0.0")

        features = {"text": "string", "label": "int8"}
        self.assertEqual(len(dataset.features), len(features))
        for key, val in features.items():
            self.assertTrue(key in dataset.features)
            self.assertEqual(dataset.features[key].dtype, val)

    def test_train_dataset(self):
        self._test_dataset(self.dataset_dict["train"])

    def test_test_dataset(self):
        self._test_dataset(self.dataset_dict["test"])


if __name__ == "__main__":
    unittest.main()
