#!/usr/bin/env python3
# spark_jobs/etl.py

import pandas as pd
import os

# 1. Paths to your raw Kaggle CSVs
ORDERS_CSV      = os.path.join('data', 'List of Orders.csv')
ORDER_DETAILS   = os.path.join('data', 'Order Details.csv')
SALES_TARGET    = os.path.join('data', 'Sales target.csv')  # optional, unused in cohort

# 2. Read in the orders and order-details tables
orders_df = pd.read_csv(ORDERS_CSV, parse_dates=['order_date'])
details_df = pd.read_csv(ORDER_DETAILS)

# 3. Compute order_value = UnitPrice * Quantity
details_df['order_value'] = details_df['UnitPrice'] * details_df['Quantity']

# 4. Merge to get one row per order item with its value
merged = pd.merge(
    orders_df,
    details_df[['OrderID', 'order_value']],
    left_on='OrderID',
    right_on='OrderID',
    how='inner'
)

# 5. If there are multiple items per order, aggregate to seller-level
#    (assuming 'SellerID' is in orders_df; if not, adjust accordingly)
if 'SellerID' not in merged.columns:
    # If the dataset doesn't have SellerID, generate a dummy one for demo
    merged['SellerID'] = merged['CustomerID'].astype(str).str.slice(0,5)

# 6. Final cleaned dataset
cleaned = merged.rename(columns={
    'OrderID': 'order_id',
    'SellerID': 'seller_id',
    'order_date': 'order_date',
    'order_value': 'order_value'
})[['order_id', 'seller_id', 'order_date', 'order_value']]

# 7. Write out to CSV for Spark ingestion
out_path = os.path.join('data', 'orders_cleaned.csv')
cleaned.to_csv(out_path, index=False)
print(f"Written cleaned orders to {out_path}")
