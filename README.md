# Uber Data Analytics Pipeline

Welcome to the Uber Data Analytics pipeline. This repository provides an overview of an end-to-end data transformation, storage, processing, and visualization architecture.

## Table of Contents
- [Overview](#overview)
- [Architecture](#architecture)
  - [Star Schema Transformation](#data-schema-definition)
  - [Google Cloud Storage](#google-cloud-storage)
  - [Mage.ai & Google Compute Engine](#mageai--google-compute-engine)
  - [BigQuery](#bigquery)
  - [Looker](#looker)
- [Extract](#extract)
- [Transform](#transform)
- [Load](#load)



## Overview

The pipeline focuses on transforming raw Uber data into actionable insights using a series of modern cloud-based tools and services.

## Access the Data
You can access the publicly available `data.csv` file via the following URL:

[click here](https://storage.googleapis.com/uber_dataset1/uber_data.csv)

## Architecture
![Blank diagram](https://github.com/LogicAL007/Uber-analytics-data-engineerinig-pipeline/assets/122959675/f26b9a37-27a9-4ab6-8105-c2f709aa427a)

# Tools Used

### Google Cloud Storage
The processed data is stored in GCS (Google Cloud Storage) buckets, ensuring its availability for further processing or analytics. It's an efficient intermediary stage between raw data sources and our analytics tools.

### Mage.ai & Google Compute Engine
[Mage.ai](https://www.mage.ai/) is our chosen tool for managing and orchestrating the data pipeline. Running on Google Compute Engine (GCE), Mage.ai provides the scalability required for large-scale data processing.

### BigQuery
Post-transformation, our data resides in Google BigQuery, a serverless and highly scalable data warehouse. Here, we can perform fast queries, advanced analytics, and even delve into machine learning tasks.

### Looker
Visualization and business intelligence are executed using Looker, integrated tightly with BigQuery post Google's acquisition. It serves as our platform for dashboards, reports, and ad-hoc analyses.

### Data Schema Definition
For the Uber data analytics project, the Star Schema was chosen, a renowned data modeling technique, to ensure swift querying and ease of use, especially when interfacing with BI (Business Intelligence) tools like Looker.

![uber data model (2)](https://github.com/LogicAL007/Uber-analytics-data-engineerinig-pipeline/assets/122959675/ac9ea719-a597-465d-a756-0ffc6d2a4f18)

### **Why Star Schema?**
- **Simplicity**: It's easy to understand, making it approachable for users who want to run ad-hoc queries.
- **Performance**: Designed for fast query performance. This is crucial when dealing with large datasets, like Uber's ride data.
- **Scalability**: Easily accommodates new data, making future expansions a breeze.

### **Breakdown of the Model**:

#### **Fact Table**: 
Central to the Star Schema is the **Fact Table**. This table accumulates the core metrics of the dataset. Think of it as the heart pumping essential data to other connected tables. For Uber, metrics like the number of rides, total fare, and trip duration would be here.

#### **Dimension Tables**: 
Orbiting the fact table are multiple **Dimension Tables**. These contain descriptive or categorical details - essentially the 'context' for the facts. A few examples from the Uber dataset:

- **Time Dimension**: Instead of just having a timestamp, details are broken down to provide insights like the day, month, or even the year of a trip.
- **Location Dimension**: Delve into details about where a ride started (pickup) and where it ended (drop-off).
- **Payment Dimension**: Understand more about how riders choose to pay for their trips.

By structuring the data in this manner, the stage is set for insightful analytics, ensuring that each query on the data can be executed swiftly and can pull out meaningful insights.




## Setup Instructions for Mage

To set up `mage.ai` on a Google Compute Engine instance(click SSH), follow the steps below:

### Install Python and Pip

```bash
sudo apt-get update
sudo apt-get install python3-distutils
sudo apt-get install python3-apt
sudo apt-get install wget
wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py
```

### Install Mage

```bash
sudo pip3 install mage-ai
```

### Install Pandas

```bash
sudo pip3 install pandas
```

### Start Mage Project
```bash
mage start uber_project
```

# The Pipeline

## Extract
We extract data directly from a Google Cloud Storage bucket using Python's `requests` library. The dataset is fetched from its URL and read into a DataFrame using `pandas` for subsequent operations. The extraction process includes basic validation to ensure data integrity.

<img width="1280" alt="Screenshot 2023-09-12 221818" src="https://github.com/LogicAL007/Uber-analytics-data-engineerinig-pipeline/assets/122959675/34e9eca2-5597-4814-a6eb-a8388f50fb03">

## Transform

We use `mage_ai` and `pandas` to change and organize our Uber data. We change the date and time information to a format that's easy to understand and use. We then create separate tables for trip details, payment types, and locations. After that, we combine these tables into one main table. This step makes sure our data is neat, easy to read, and ready for deeper study.

<img width="1280" alt="Screenshot 2023-09-14 000511" src="https://github.com/LogicAL007/Uber-analytics-data-engineerinig-pipeline/assets/122959675/0c983ed1-48c8-4660-b48d-840e1e8d88d9">

## Load

We've set up a system to move our organized Uber data into Google's BigQuery, a place where we can do more analysis. Here's how it works:

When we want to send our data, we look at our settings in the `io_config.yaml` file. This file tells our code how to connect to BigQuery. For each piece of data we've prepared, we give it a special name in BigQuery. This way, we know exactly where each piece of data is stored. If there's already data with the same name, we replace it with the new data. This ensures our BigQuery storage is always up-to-date.

<img width="1280" alt="Screenshot 2023-09-12 231318" src="https://github.com/LogicAL007/Uber-analytics-data-engineerinig-pipeline/assets/122959675/8a3ed010-b44f-44d6-aef4-0a91389e66e0">

## Bigquery
In order to provide a comprehensive view of the data and make it accessible for analysis, an aggregated table called tbl_analytics was created. This table essentially "flattens" the data, pulling in details from all the dimensional tables and centralizing it for easier querying.

<img width="1280" alt="Screenshot 2023-09-13 001942" src="https://github.com/LogicAL007/Uber-analytics-data-engineerinig-pipeline/assets/122959675/d4ece934-e466-494a-901f-39b87528bbe4">


## visualization. . .
