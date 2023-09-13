# Uber Data Analytics Pipeline

Welcome to the Uber Data Analytics pipeline. This repository provides an overview of an end-to-end data transformation, storage, processing, and visualization architecture.

## Table of Contents
- [Overview](#overview)
- [Architecture](#architecture)
  - [Star Schema Transformation](#star-schema-transformation)
  - [Google Cloud Storage](#google-cloud-storage)
  - [Mage.ai & Google Compute Engine](#mageai--google-compute-engine)
  - [BigQuery](#bigquery)
  - [Looker](#looker)
- [Extract](#extract)
- [Transform](#transform)
- [Load](#load)
- [bigquery dataset](#bigquery)
- [License](#license)

## Overview

the pipeline focuses on transforming raw Uber data into actionable insights using a series of modern cloud-based tools and services.

## Architecture

### Star Schema Transformation
We utilize the Star Schema, a popular data modeling technique, to organize our data into facts and dimensions. This structure is specially designed for query performance and ease of use in BI tools.

### Google Cloud Storage
Our processed data is stored in GCS (Google Cloud Storage) buckets, ensuring its availability for further processing or analytics. It's an efficient intermediary stage between raw data sources and our analytics tools.

### Mage.ai & Google Compute Engine
[Mage.ai](#) is our chosen tool for managing and orchestrating the data pipeline. Running on Google Compute Engine (GCE), Mage.ai provides the scalability required for large-scale data processing.

### BigQuery
Post-transformation, our data resides in Google BigQuery, a serverless and highly scalable data warehouse. Here, we can perform fast queries, advanced analytics, and even delve into machine learning tasks.

### Looker
Visualization and business intelligence are executed using Looker, integrated tightly with BigQuery post Google's acquisition. It serves as our platform for dashboards, reports, and ad-hoc analyses.

## Access the Data

You can access the publicly available `data.csv` file via the following URL:

[LINK_TO_DATA_CSV](#)

## Setup Instructions

To set up `mage.ai` on a Google Compute Engine instance, follow the steps below:

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

# The Pipeline

## Extract
We extract data directly from a Google Cloud Storage bucket using Python's `requests` library. The dataset is fetched from its URL and read into a DataFrame using `pandas` for subsequent operations. The extraction process includes basic validation to ensure data integrity.

## Transform

We use `mage_ai` and `pandas` to change and organize our Uber data. We change the date and time information to a format that's easy to understand and use. We then create separate tables for trip details, payment types, and locations. After that, we combine these tables into one main table. This step makes sure our data is neat, easy to read, and ready for deeper study.


## Load

We've set up a system to move our organized Uber data into Google's BigQuery, a place where we can do more analysis. Here's how it works:

When we want to send our data, we look at our settings in the `io_config.yaml` file. This file tells our code how to connect to BigQuery. For each piece of data we've prepared, we give it a special name in BigQuery. This way, we know exactly where each piece of data is stored. If there's already data with the same name, we replace it with the new data. This ensures our BigQuery storage is always up-to-date.


## Bigquery
