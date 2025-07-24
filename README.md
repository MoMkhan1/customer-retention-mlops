# 📈 Customer Retention MLOps Intelligence System

## 🧠 Overview

The **Customer Retention MLOps Intelligence System** is an enterprise-grade end-to-end machine learning pipeline designed to predict customer churn and drive retention strategies. This project implements **MLOps best practices** to automate the full ML lifecycle — from data ingestion to monitoring and continuous retraining.

### 🚀 Highlights

- ✅ Automated data ingestion using SQL and Spark SQL
- ✅ Scalable model training with Python ML libraries
- ✅ Continuous delivery via Docker, Kubernetes, and Jenkins
- ✅ Real-time model monitoring (accuracy, drift, retraining)
- ✅ Production-ready containers and CI/CD workflows

---

## 🛠️ Technologies Used

| Category         | Stack |
|------------------|-------|
| Languages        | Python, Java |
| Data Querying    | SQL, Spark SQL |
| ML Libraries     | `scikit-learn`, `pandas`, `matplotlib` |
| Containerization | Docker |
| Orchestration    | Kubernetes |
| CI/CD            | Jenkins |
| Version Control  | Git + GitHub |
| Cloud Ready      | AWS (or your preferred platform) |

---

## 🗂️ Project Structure

```bash
customer-retention-mlops/
├── data/              # Raw and processed data
├── src/               # Source code
│   ├── data_ingestion/
│   ├── preprocessing/
│   ├── model_training/
│   ├── model_serving/
│   └── monitoring/
├── graphs/            # Output visualizations
├── tests/             # Unit tests
├── docker/            # Dockerfiles
├── k8s/               # Kubernetes manifests
├── jenkins/           # Jenkins pipeline
├── notebooks/         # Jupyter notebooks
├── requirements.txt   # Python dependencies
├── Dockerfile         # Main Dockerfile
└── README.md          # Project documentation

📊 Model Evaluation & Visualization

The script src/visualization/model_evaluation.py performs model evaluation with key metrics and visualizations:

    ✅ Accuracy score (example: 0.85)

    ✅ Confusion Matrix → graphs/confusion_matrix.png

    ✅ ROC Curve → graphs/roc_curve.png

📌 How to Run

python src/visualization/model_evaluation.py

🧪 Running Unit Tests

To ensure functionality, unit tests are located in the tests/ directory.
Run all tests:

python -m unittest discover -s tests

Sample Output:

Model Accuracy: 0.85
Confusion matrix saved to: graphs/confusion_matrix.png
ROC curve saved to: graphs/roc_curve.png
.
----------------------------------------------------------------------
Ran 1 test in 0.643s

OK

🐳 Docker Integration
Build the Docker image:

docker build -t customer-retention-mlops .

Run the test container:

docker run --rm customer-retention-mlops

🔁 End-to-End MLOps Pipeline

    Clone the repository:

git clone https://github.com/MoMKhan1/customer-retention-mlops.git
cd customer-retention-mlops

    Set up your environment:

Ensure you have:

    Python 3.12+

    Docker

    Java (for model serving)

    Jenkins (for CI/CD)

    Kubernetes (for orchestration)

    Automate via Jenkins:

Configure Jenkins with jenkins/Jenkinsfile to automate build, test, deploy.

    Deploy via Kubernetes:

Use k8s/ manifests to deploy the system in a containerized production environment.
📁 requirements.txt

All Python dependencies are listed in requirements.txt. Install them locally with:

pip install -r requirements.txt

🤝 Contributing

Contributions are welcome! Please fork the repo and open a pull request.
📬 Contact

📧 zaman.khan123rd@gmail.com
🌐 GitHub: MoMKhan1