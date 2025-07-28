#!/usr/bin/env python3
# spark_jobs/cohort_analysis.py

from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    to_date, month, year, min as spark_min,
    countDistinct, sum as spark_sum
)
from pyspark.sql.window import Window

# 1. Initialize Spark
spark = SparkSession.builder \
    .appName("SellerCohortAnalysis") \
    .getOrCreate()

# 2. Read the cleaned CSV
df = spark.read.option("header", True).csv("data/orders_cleaned.csv")

# 3. Parse and enrich dates
df = df.withColumn("order_date", to_date("order_date")) \
       .withColumn("order_year", year("order_date")) \
       .withColumn("order_month", month("order_date"))

# 4. Compute first-order (cohort) date per seller
w = Window.partitionBy("seller_id")
df = df.withColumn("first_order_date", spark_min("order_date").over(w)) \
       .withColumn("cohort_year", year("first_order_date")) \
       .withColumn("cohort_month", month("first_order_date"))

# 5. Aggregate metrics by cohort + month
metrics = df.groupBy("cohort_year","cohort_month","order_year","order_month") \
    .agg(
      countDistinct("seller_id").alias("active_sellers"),
      spark_sum("order_value").alias("total_revenue")
    ) \
    .orderBy("cohort_year","cohort_month","order_year","order_month")

# 6. Write metrics out as Parquet and CSV for SQL & dashboard use
metrics.write.mode("overwrite").parquet("data/metrics.parquet")
metrics.toPandas().to_csv("data/metrics.csv", index=False)

print("Cohort metrics written to data/metrics.parquet and data/metrics.csv")

spark.stop()
