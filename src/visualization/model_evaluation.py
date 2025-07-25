import os
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay, roc_curve, auc
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def train_and_evaluate_model():
    # Generate data
    X, y = make_classification(n_samples=1000, n_features=20, random_state=42)

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Train model
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    # Predict & accuracy
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy:.2f}")

    # Create graphs folder
    graph_dir = os.path.join(os.getcwd(), 'graphs')
    os.makedirs(graph_dir, exist_ok=True)

    # Confusion Matrix
    cm_disp = ConfusionMatrixDisplay.from_estimator(model, X_test, y_test, cmap=plt.cm.Blues)
    cm_path = os.path.join(graph_dir, 'confusion_matrix.png')
    plt.savefig(cm_path)
    plt.close()

    # ROC Curve
    y_prob = model.predict_proba(X_test)[:, 1]
    fpr, tpr, _ = roc_curve(y_test, y_prob)
    roc_auc = auc(fpr, tpr)

    plt.figure()
    plt.plot(fpr, tpr, color='darkorange', label=f'ROC curve (area = {roc_auc:.2f})')
    plt.plot([0, 1], [0, 1], color='navy', linestyle='--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic')
    plt.legend(loc="lower right")

    roc_path = os.path.join(graph_dir, 'roc_curve.png')
    plt.savefig(roc_path)
    plt.close()

    print(f"Confusion matrix saved to: {cm_path}")
    print(f"ROC curve saved to: {roc_path}")

    return accuracy
