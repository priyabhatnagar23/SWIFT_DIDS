# SWIFT_DIDS

A real-time, scalable cybersecurity solution for financial networks built using **Apache Kafka**, **Docker**, **TensorFlow**, and **Scikit-learn**. This system simulates and detects fraudulent SWIFT transactions in a distributed environment.

This project implements a **Distributed Intrusion Detection System (DIDS)** for monitoring SWIFT transactions in real-time. The architecture consists of:

- **Kafka Producer**: Simulates and sends transaction data.
- **Kafka Consumer**: Receives data and applies a machine learning model for fraud detection.
- **ML Model**: Trained using Scikit-learn to classify transactions as normal or fraudulent.
- **Docker**: Ensures containerized, scalable execution of Kafka services (Zookeeper + Kafka broker).

