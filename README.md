🚀 Smart Supply Chain Analytics Platform
📌 Project Overview

This project is an end-to-end Data Engineering pipeline built to simulate a real-world Supply Chain Analytics system. It processes streaming order data, applies Medallion Architecture (Bronze → Silver → Gold), orchestrates workflows using Airflow, and visualizes KPIs using Power BI.

The goal is to demonstrate practical experience with modern data engineering tools and real-world pipeline design.

🏗️ Architecture
Data Generation (CSV)
        ↓
Kafka Producer
        ↓
Kafka Topic (Streaming Orders)
        ↓
Kafka Consumer → Bronze Layer (Raw Data)
        ↓
Silver Layer (Cleaned & Transformed Data)
        ↓
Gold Layer (Aggregated Business Metrics)
        ↓
Airflow (Pipeline Orchestration)
        ↓
Power BI (Business Dashboard)

🛠️ Tech Stack

Python

Apache Kafka

Apache Airflow

Medallion Architecture (Bronze, Silver, Gold)

Power BI

Git & GitHub

Ubuntu (Linux environment)

📂 Project Structure
SUPPLY_CHAIN_PROJECT/
│
├── Data_generation/
├── kafka_producer/
├── kafka_consumer/
├── airflow_dags/
│   ├── bronze_dag.py
│   ├── silver_dag.py
│   ├── gold_dag.py
│   └── master_pipeline_dag.py
│
├── data/
│   ├── bronze/
│   ├── silver/
│   └── gold/
│
└── README.md

🔄 Pipeline Explanation
🥉 Bronze Layer

Ingests raw Kafka order data

Stores unprocessed data

Acts as single source of truth

🥈 Silver Layer

Cleans data

Handles null values

Standardizes formats

Prepares structured dataset

🥇 Gold Layer

Creates business-ready aggregations

Revenue by Product

Revenue by Warehouse

Orders by Status

🎯 Airflow Orchestration

Airflow is used to:

Automate execution of Bronze → Silver → Gold

Maintain task dependency

Retry on failure

Monitor pipeline health

Schedule daily execution

Without Airflow:

Manual script execution required

No automation

No monitoring

No retry logic

📊 Power BI Dashboard

Built dashboards showing:

Revenue by Product

Revenue by Warehouse

Order Status Distribution

Total Units Sold

KPI Cards for Revenue & Orders

🧠 Key Challenges & Learnings

Kafka offset handling issues

Authentication failures

Airflow environment conflicts

Python version compatibility

Folder structure confusion in Linux

Resolved using:

Proper environment isolation (venv)

Correct DAG folder configuration

Clear architecture separation

Step-by-step debugging

🚀 How to Run

Activate virtual environment

Start Kafka

Run producer & consumer

Start Airflow:

airflow webserver -p 8080
airflow scheduler


Trigger Master DAG

Connect Power BI to Gold layer

🔮 Future Enhancements

Add FastAPI for external client access

Deploy on Cloud (Azure / AWS)

Use Docker for full containerization

CI/CD Integration

Data Quality Checks


ARCHITECTURE
------------

<img width="1844" height="1005" alt="image" src="https://github.com/user-attachments/assets/15a379bb-c495-49ab-acf3-e4a48a473270" />


👨‍💻 Author

Sathwik Kotian
Data Engineering Enthusiast
