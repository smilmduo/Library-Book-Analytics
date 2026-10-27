# Library Book Analytics

A Big Data Analytics academic project that analyzes library book issue records using Hadoop HDFS and Apache Hive.

## Objectives

- Identify the most frequently issued books.
- Analyze popular book categories.
- Study monthly borrowing trends.
- Identify frequent borrowers.

## Technologies Used

- Apache Hadoop
- Hadoop Distributed File System (HDFS)
- Apache Hive
- SQL
- CSV dataset

## Project Structure

```text
Library-Book-Analytics/
├── library_data.csv
├── hive/
│   └── analytics.sql
├── screenshots/
└── README.md
## Dataset

The sample CSV contains book ID, book title, category, student ID, and issue date.

## Setup Overview

1. Install Java, Hadoop, and Apache Hive.
2. Start HDFS.
3. Upload the CSV dataset to HDFS.
4. Create the `library_books` external table in Hive.
5. Run the queries in `hive/analytics.sql`.

## Storage

The dataset is stored in HDFS at `/library/input/`.

## Limitations

This is a single-machine learning project using a local Hadoop and Hive setup. The included dataset is sample data for academic demonstration.

## Future Improvements

- Add a Python Streamlit dashboard.
- Visualize borrowing trends and popular categories.
- Expand the dataset with more library records.

## Academic Use

Developed for a Big Data Analytics college project.
