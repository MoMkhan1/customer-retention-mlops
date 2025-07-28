
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

| Category         | Stack                                 |
|------------------|----------------------------------------|
| Languages        | Python, Java                          |
| Data Querying    | SQL, Spark SQL                        |
| ML Libraries     | `scikit-learn`, `pandas`, `matplotlib` |
| Containerization | Docker                                |
| Orchestration    | Kubernetes                            |
| CI/CD            | Jenkins                               |
| Version Control  | Git + GitHub                          |
| Cloud Ready      | AWS (or your preferred platform)      |

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
```

---

## 📊 Model Evaluation & Visualization

The script `src/visualization/model_evaluation.py` performs model evaluation with key metrics and visualizations:

- ✅ Accuracy score (example: 0.85)  
- ✅ Confusion Matrix → `graphs/confusion_matrix.png`  
- ✅ ROC Curve → `graphs/roc_curve.png`  

### 📌 How to Run

```bash
python src/visualization/model_evaluation.py
```

---

## 🧪 Running Unit Tests

To ensure functionality, unit tests are located in the `tests/` directory.  
Run all tests:

```bash
python -m unittest discover -s tests
```

**Sample Output:**
```
Model Accuracy: 0.85  
Confusion matrix saved to: graphs/confusion_matrix.png  
ROC curve saved to: graphs/roc_curve.png  
.
----------------------------------------------------------------------
Ran 1 test in 0.643s

OK
```

---

## 🐳 Docker Integration

### Build the Docker image:

```bash
docker build -t customer-retention-mlops .
```

### Run the test container:

```bash
docker run --rm customer-retention-mlops
```

---

## 🔁 End-to-End MLOps Pipeline

### Clone the repository:

```bash
git clone https://github.com/MoMKhan1/customer-retention-mlops.git
cd customer-retention-mlops
```

### Set up your environment:

Ensure you have:

- Python 3.12+  
- Docker  
- Java (for model serving)  
- Jenkins (for CI/CD)  
- Kubernetes (for orchestration)  

### Automate via Jenkins:

Configure Jenkins with `jenkins/Jenkinsfile` to automate build, test, deploy.

### Deploy via Kubernetes:

Use `k8s/` manifests to deploy the system in a containerized production environment.

---

## 📁 requirements.txt

All Python dependencies are listed in `requirements.txt`. Install them locally with:

```bash
pip install -r requirements.txt
```

---

## 🤝 Contributing

Contributions are welcome! Please fork the repo and open a pull request.

---

## 📬 Contact

📧 zaman.khan123rd@gmail.com  
🌐 GitHub: [MoMKhan1](https://github.com/MoMKhan1)

---

## ☁️ Docker & AWS ECR Integration

This section documents how we containerize the project and push it to AWS Elastic Container Registry (ECR).

### ✅ Prerequisites

- AWS account with ECR access  
- AWS CLI installed and configured (`aws configure`)  
- Docker installed and running  

---

### 🐳 1. Build Docker Image

```bash
docker build -t customer-retention-app .
```

---

### 🔍 2. View Docker Images

```bash
docker images
```

Sample output:
```
REPOSITORY               TAG       IMAGE ID       CREATED        SIZE
customer-retention-app   latest    b47310606984   3 hours ago    563MB
```

---

### 🔐 3. Authenticate Docker to ECR

```bash
aws ecr get-login-password --region eu-north-1 | docker login --username AWS --password-stdin 443293291194.dkr.ecr.eu-north-1.amazonaws.com
```

---

### 🏷️ 4. Tag the Docker Image

```bash
docker tag customer-retention-app:latest 443293291194.dkr.ecr.eu-north-1.amazonaws.com/customer-retention-app:latest
```

---

### 🚀 5. Push the Image to ECR

```bash
docker push 443293291194.dkr.ecr.eu-north-1.amazonaws.com/customer-retention-app:latest
```

---

### 🔎 6. Confirm Upload to ECR

```bash
aws ecr describe-images --repository-name customer-retention-app --region eu-north-1
```

---

### 📂 7. Verify in AWS Console

Navigate to [AWS ECR Console – eu-north-1](https://eu-north-1.console.aws.amazon.com/ecr/home?region=eu-north-1)  
Go to **Repositories → customer-retention-app → Images**
