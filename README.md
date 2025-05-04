# 🏨 Hotel Reservation Cancellation Prediction - End-to-End ML System

This project predicts whether a hotel reservation will be cancelled based on booking details. It demonstrates a full-stack MLOps workflow using scalable, modular components across development, experimentation, and production.

> 🔍 Built for reproducibility, automation, and real-time inference using best-in-class tools.

![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white&style=for-the-badge) ![Jenkins](https://img.shields.io/badge/Jenkins-D24939?logo=jenkins&logoColor=white&style=for-the-badge) ![GCP](https://img.shields.io/badge/GCP-4285F4?logo=googlecloud&logoColor=white&style=for-the-badge) ![MLflow](https://img.shields.io/badge/MLflow-0194f3?logo=mlflow&logoColor=white&style=for-the-badge) ![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white&style=for-the-badge) ![HTML](https://img.shields.io/badge/HTML-E34F26?logo=html5&logoColor=white&style=for-the-badge) ![CSS](https://img.shields.io/badge/CSS-1572B6?logo=css3&logoColor=white&style=for-the-badge) ![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?logo=bootstrap&logoColor=white&style=for-the-badge)




---

## 📌 Tech Stack

| Category              | Technologies                                                                 |
|-----------------------|------------------------------------------------------------------------------|
| **Languages**         | Python                                                                       |
| **ML & Preprocessing**| Pandas, NumPy, Scikit-learn, LightGBM, Jupyter                               |
| **Visualization**     | Seaborn, Matplotlib                                                          |
| **Tracking**          | MLflow                                                                       |
| **Containerization**  | Docker                                                                       |
| **CI/CD Orchestration** | Jenkins, Git                                                               |
| **Cloud & Hosting**   | Google Cloud Platform (GCS, Artifact Registry, GKE)                          |
| **Deployment**        | Kubernetes,                                                                  |

---

# 🧠 ML Pipeline Overview

## 📥 Data Ingestion
> **Tech Used:** `Pandas`, `GCS`, `Python`

- Loads raw CSV data either from local or GCS buckets.
- Handles missing values, schema validation, and basic sanity checks.

## 🔧 Feature Engineering
> **Tech Used:** `Pandas`, `NumPy`, `Scikit-learn`

- Transforms categorical data, encodes features, and scales numericals.
- Derives domain-specific metrics like `total_nights`, `is_weekend`, etc.

## 🏋️ Model Training
> **Tech Used:** `Scikit-learn`, `LightGBM`, `GridSearchCV`

- Models: `LightGBM`, `Random Forest`, optionally `XGBoost`.
- Uses `GridSearchCV` for hyperparameter tuning.

## 🧪 Experiment Tracking
> **Tech Used:** `MLflow`

- Tracks runs, models, metrics, parameters, and artifacts.
- Registers best models for later deployment.

## 📦 Model Packaging
> **Tech Used:** `Docker`

- Creates reproducible containers of the entire pipeline (training + inference).
- Ensures consistency across all environments.

## 🚀 CI/CD Pipeline
> **Tech Used:** `Jenkins`, `Git`, `Docker`, `Kubernetes`, `Artifact Registry`

- Jenkins triggers builds, trains models, creates Docker images, and deploys them to Kubernetes.
- Artifacts are stored in GCP’s Artifact Registry.

## ☁️ Model Deployment
> **Tech Used:** `Google Kubernetes Engine (GKE)`, `FastAPI`, `Streamlit`

- Deploys trained model as an API (via FastAPI) or UI (via Streamlit).
- Handles real-time prediction requests.

## 📈 Monitoring & Observability *(Future Enhancement)*
> **Tech Planned:** `Prometheus`, `Grafana`, `Pub/Sub`, `Dataflow`

- Monitor model inference latency, API uptime, and feature drift.
- Setup batch/streaming prediction workflows with Pub/Sub & Dataflow.

---

# 🚀 Technologies Explained

## 🐳 Docker — *Containerization*

- Packages code and dependencies into isolated containers.
- Ensures reproducibility across dev, CI, and cloud.
- Integrates with Jenkins and Kubernetes effortlessly.

---

## 🔁 Jenkins — *CI/CD Automation*


- Automates ML lifecycle from build → train → package → deploy.
- Reduces manual effort and allows scalable team collaboration.
- Pushes images to Artifact Registry and deploys on GKE.

---

## ☁️ GCP — *Cloud Compute, Storage & Hosting*

- **GCS (Cloud Storage):** Stores datasets and trained models.
- **Artifact Registry:** Maintains Docker images used in production.
- **GKE:** Deploys and auto-scales the inference API.

---

## 🧪 MLflow — *Experiment Tracking*


- Logs and compares model training runs.
- Supports model registry for deployment.
- Improves transparency and reproducibility in training.

---

## 🧠 Streamlit / FastAPI — *Model Interfaces*


- **Streamlit:** Rapidly creates data-driven UIs for model demonstration.
- **FastAPI:** Provides fast, async REST APIs for serving predictions.

---

# 🔮 Future Enhancements

- 📊 **Monitoring Dashboards:** Use Prometheus + Grafana for performance monitoring.
- 📦 **Kubeflow Pipelines:** For orchestrated model training & deployment.
- 🔁 **Batch/Streaming Inference:** Using Pub/Sub + Dataflow pipelines.
- 📊 **Admin Dashboard:** Build a React + FastAPI admin panel for analytics & insights.

---

## 🖼️ Suggested Diagrams (To Add Later)

- ✅ **CI/CD Workflow** – Visualizing Jenkins → Docker → GKE flow
- ✅ **Kubernetes Deployment Architecture** – Pods, Services, Load Balancer
- ✅ **ML Pipeline Flowchart** – From ingestion to deployment
- ✅ **Monitoring Stack Diagram** – Prometheus + Grafana + AlertManager setup

---

## 👨‍💻 Author

**Tilak Varma**  
_AI Product Developer_

📧 [varmatilak22@example.com]  
🔗 [LinkedIn](https://www.linkedin.com/in/varmatilak) • [GitHub](https://github.com/varmatilak22)

---

