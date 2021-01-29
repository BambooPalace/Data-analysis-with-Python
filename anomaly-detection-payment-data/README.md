# Anomaly detection of payment data
Notebook please view [here.](https://nbviewer.jupyter.org/github/BambooPalace/Anomaly-detection-payment/blob/master/Anomaly_detection_on_payment_data.ipynb)
## Problem statement
In this dataset, each customer is classified as high or low credit risk according to the set of features and payment history. 
If label is 1, the customer is in high credit risk. Dataset imbalance ratio is 20%.

## Data:

payment_data.csv: customer’s card payment history.

id: customer id
OVD_t1: number of times overdue type 1
OVD_t2: number of times overdue type 2
OVD_t3: number of times overdue type 3
OVD_sum: total overdue days
pay_normal: number of times normal payment
prod_code(category feature): credit product code
prod_limit: credit limit of product
update_date: account update date
new_balance: current balance of product
highest_balance: highest balance in history
report_date: date of recent payment
customer_data.csv: customer’s demographic data and category attributes which have been encoded.
Category features are fea_1, fea_3, fea_5, fea_6, fea_7, fea_9.

## Tasks:

Explore data to give insights.
Build features from existing payment data.
Build model to predict high risk customer
Model explanation and evaluation

## Procedures¶
0. Business understanding:¶

- what are the top features of high risks customers?
- Build a surpervised classifier:
- For classifying imbalanced dataset, metrics like precision/recall/f1 of the minor class is more reflective of the predictor instead of the accuracy value.

1. Data exploration:¶

Use data visualization to explore data, this step helps user to select and process data in the later steps.

2. Data preprocessing & feature engineering¶

Impute missing data, encode categorical data, correct data format
A lot of efforts are spent on creating new features for each id based on payment data.
It is worth checking the Feature Enginerring methodology here.

3. Build starter model, check metrics.¶

Run multiple classifier models in the default setting, this step helps to choose a model to furthur finetune.

4. Tuning model hyperparameters.¶

Use grid search to tune model hyperparameters.

5. Summary¶

Answering business questions with data visualization.
