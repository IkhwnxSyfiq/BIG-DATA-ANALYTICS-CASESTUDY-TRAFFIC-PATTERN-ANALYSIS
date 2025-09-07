# Big Data Analytics in Transportation: Traffic Pattern Analysis

This repository contains the code and presentation for a university case study on Big Data Analytics, focusing on its application in the transportation sector. The project demonstrates how clustering algorithms can be used to analyse and identify patterns in traffic flow data.

## 📄 Project Overview
This project was completed as part of the Big Data Analytics course at Universiti Kuala Lumpur (UniKL British Malaysian Institute). The goal was to propose a big data application, demonstrate its process, implement a proof-of-concept, and discuss its implications.

## 👥 Team Members
Name	Student ID
Anis Suriani binti Azizan	51221221056
Nurul Izzati binti Mahamad Ismail	51221221147
Ahmad Syahmi bin Ahmad Pauzi	51221221003
Muhammad Waiz bin Nor Kamal	51221221053
Muhammad Ikhwan Syafiq bin Norsham	51221221125

## 🚀 Proposed Application: Traffic Analytics & Prediction
We proposed a Big Data Analytics system for the transportation industry to optimise traffic flow, predict congestion, and improve urban mobility. The system uses real-time data from various sources (GPS, traffic cameras, toll booths) to make data-driven decisions.

System Block Diagram
The proposed data pipeline involves:

Real-time Data Ingestion: Collecting data from sensors and cameras.

Data Storage: Storing streaming and batch data in a scalable system.

Traffic Prediction: Using ML models on historical + real-time data to forecast patterns.

Model Updates: Continuously retraining models for accuracy.

Alerts: Generating notifications for critical events or anomalies.

## 💻 Code Implementation: K-Means Clustering for Traffic Pattern Analysis
We implemented a K-Means Clustering algorithm to analyse hourly traffic volume data from a specific location (Sungai Pusu, Combak) and identify distinct patterns or clusters of traffic behavior throughout the day.

Prerequisites
Python 3.x

Libraries: pandas, scikit-learn, matplotlib

Dataset
The dataset (traffic_flow.csv) is a simple table with two columns:

hour (0-23)

traffic_volume (number of vehicles)

Code Explanation
Data Loading & Preprocessing: The data is loaded, and the relevant features (hour and traffic_volume) are standardised.

Finding Optimal Clusters (k): The Elbow Method is used to determine the best number of clusters by plotting the Within-Cluster Sum of Squares (WCSS) for different values of k.

Applying K-Means: The K-Means algorithm is used with the chosen optimal k.

Visualisation: The results are plotted to show the different traffic patterns identified by the clusters.


The Elbow Method graph to help choose the optimal k.

A scatter plot showing the data points colored by their assigned cluster.

## 📈 Results
The clustering analysis successfully grouped times of the day into distinct traffic patterns (e.g., early morning light traffic, morning/evening rush hours, moderate daytime traffic). This insight can help traffic management authorities allocate resources more efficiently and provide drivers with accurate congestion forecasts.

## ✔️ Benefits & Challenges
Benefits
Optimised Traffic Management

Improved Customer Experience

Environmental Sustainability

Cost Reduction and Resource Optimisation

Innovations in Autonomous Vehicles

Challenges
Data privacy and security

Cost and infrastructure requirements

Data quality and integration issues

Public acceptance and trust

Technological limitations

## 🏗️ Recommended Platform: Apache Kafka
We recommend Apache Kafka as the best platform for this application due to its:

Real-time Data Processing: Perfect for handling continuous streams of traffic data.

Scalability: Can handle massive volumes of data from city-wide sensors.

Event-Driven Architecture: Ideal for triggering immediate alerts and model updates.

Strong Integration: Easily connects with various data storage and processing systems like Hadoop and Spark.

## 🔧 Other Suggested Algorithms
K-Means Clustering (Unsupervised Learning): Used for pattern discovery and grouping similar data points, as demonstrated in this project.

Recurrent Neural Networks - RNNs (Supervised Learning): Particularly LSTMs, are excellent for time-series forecasting and would be ideal for predicting future traffic congestion based on historical sequences of data.


