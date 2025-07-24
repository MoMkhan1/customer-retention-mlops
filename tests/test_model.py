import unittest
from src.visualization.model_evaluation import train_and_evaluate_model


class TestModelTraining(unittest.TestCase):
    def test_accuracy_range(self):
        accuracy = train_and_evaluate_model()
        self.assertGreaterEqual(accuracy, 0.0)
        self.assertLessEqual(accuracy, 1.0)

if __name__ == '__main__':
    unittest.main()

