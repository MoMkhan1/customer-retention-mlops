{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f318c5a0-1988-4386-8e85-a5cd306ae6ca",
   "metadata": {},
   "outputs": [],
   "source": [
    "import unittest\n",
    "import os\n",
    "from your_model_script import train_and_evaluate_model  # Import your function here\n",
    "\n",
    "class TestModelTraining(unittest.TestCase):\n",
    "\n",
    "    def test_train_and_evaluate_model(self):\n",
    "        accuracy = train_and_evaluate_model()\n",
    "        \n",
    "        # Test that accuracy is a float and between 0 and 1\n",
    "        self.assertIsInstance(accuracy, float)\n",
    "        self.assertGreaterEqual(accuracy, 0)\n",
    "        self.assertLessEqual(accuracy, 1)\n",
    "        \n",
    "        # Test that files are created\n",
    "        graph_dir = os.path.join(os.getcwd(), 'graphs')\n",
    "        cm_path = os.path.join(graph_dir, 'confusion_matrix.png')\n",
    "        roc_path = os.path.join(graph_dir, 'roc_curve.png')\n",
    "\n",
    "        self.assertTrue(os.path.exists(cm_path), \"Confusion matrix image not found!\")\n",
    "        self.assertTrue(os.path.exists(roc_path), \"ROC curve image not found!\")\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    unittest.main()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
