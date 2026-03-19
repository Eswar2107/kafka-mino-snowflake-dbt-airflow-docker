# 🚀 Real-Time Data Engineering Pipeline

An end-to-end real-time data pipeline built using modern data engineering tools:

**Kafka → MinIO → Snowflake → dbt → Airflow → Docker**

---

## 📌 Overview

This project demonstrates a complete real-time data pipeline where:

- Stock data is streamed via Kafka
- Stored as raw JSON in MinIO (S3-compatible)
- Loaded into Snowflake (Bronze layer)
- Transformed using dbt (Bronze → Silver → Gold)
- Orchestrated using Airflow
- Fully containerized using Docker

---

## 🏗️ Architecture
Kafka → MinIO → Snowflake → dbt → Airflow


---

## ⚙️ Tech Stack

- 🟡 Kafka (Streaming)
- 🟠 MinIO (Object Storage)
- ❄️ Snowflake (Data Warehouse)
- 🔴 dbt (Transformation)
- 🔵 Airflow (Orchestration)
- 🐳 Docker (Containerization)
- 🐍 Python, SQL, YAML

---

## 🔄 Pipeline Flow

1. Kafka streams real-time stock data  
2. Data is stored in MinIO (JSON format)  
3. Snowflake ingests data into Bronze tables  
4. dbt transforms data:
   - Bronze → Silver → Gold  
5. Airflow orchestrates the entire pipeline using DAGs  

---

## 🚀 How to Run

### 1️⃣ Start Docker Services

```bash
cd infra
docker-compose up -d
