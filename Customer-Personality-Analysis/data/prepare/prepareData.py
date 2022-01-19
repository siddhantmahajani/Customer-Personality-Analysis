"""
Author: Siddhant Mahajani
prepareData.py - define spending variables, perform clustering, prepare data, plot data
"""

import numpy as np
import pandas as pd
from datetime import date
from sklearn.preprocessing import StandardScaler, normalize
from sklearn.mixture import GaussianMixture


def getspendingvariables(data):
    # Spending variable creation
    data['Age'] = 2014 - data['Year_Birth']

    data['Spending'] = data['MntWines'] + data['MntFruits'] + data['MntMeatProducts'] + data['MntFishProducts'] + data[
        'MntSweetProducts'] + data['MntGoldProds']
    # Seniority variable creation
    last_date = date(2014, 10, 4)
    data['Seniority'] = pd.to_datetime(data['Dt_Customer'], dayfirst=True)
    data['Seniority'] = pd.to_numeric(data['Seniority'].dt.date.apply(lambda x: (last_date - x)).dt.days,
                                      downcast='integer') / 30
    data = data.rename(
        columns={'NumWebPurchases': "Web", 'NumCatalogPurchases': 'Catalog', 'NumStorePurchases': 'Store'})
    data['Marital_Status'] = data['Marital_Status'].replace(
        {'Divorced': 'Alone', 'Single': 'Alone', 'Married': 'In couple', 'Together': 'In couple', 'Absurd': 'Alone',
         'Widow': 'Alone', 'YOLO': 'Alone'})
    data['Education'] = data['Education'].replace(
        {'Basic': 'Undergraduate', '2n Cycle': 'Undergraduate', 'Graduation': 'Postgraduate', 'Master': 'Postgraduate',
         'PhD': 'Postgraduate'})

    data['Children'] = data['Kidhome'] + data['Teenhome']
    data['Has_child'] = np.where(data.Children > 0, 'Has child', 'No child')
    data['Children'].replace({3: "3 children", 2: '2 children', 1: '1 child', 0: "No child"}, inplace=True)
    data = data.rename(
        columns={'MntWines': "Wines", 'MntFruits': 'Fruits', 'MntMeatProducts': 'Meat', 'MntFishProducts': 'Fish',
                 'MntSweetProducts': 'Sweets', 'MntGoldProds': 'Gold'})

    data = data[
        ['Age', 'Education', 'Marital_Status', 'Income', 'Spending', 'Seniority', 'Has_child', 'Children', 'Wines',
         'Fruits', 'Meat', 'Fish', 'Sweets', 'Gold']]
    return data


def performclustering(data):
    """
    1. Stars: Old customers with high income and high spending nature
    2. Need Attention: New customers with below-average income and low spending nature
    3. High Potential: New customers with high-income and high spending nature
    4. Leaky Bucket: Old customers with below-average income and low spending nature
    """
    scaler = StandardScaler()
    dataset_temp = data[['Income', 'Seniority', 'Spending']]
    X_std = scaler.fit_transform(dataset_temp)
    X = normalize(X_std, norm='l2')

    gmm = GaussianMixture(n_components=4, covariance_type='spherical', max_iter=2000, random_state=5).fit(X)
    labels = gmm.predict(X)
    dataset_temp['Cluster'] = labels
    dataset_temp = dataset_temp.replace({0: 'Stars', 1: 'Need attention', 2: 'High potential', 3: 'Leaky bucket'})
    data = data.merge(dataset_temp.Cluster, left_index=True, right_index=True)

    pd.options.display.float_format = "{:.0f}".format
    summary = data[['Income', 'Spending', 'Seniority', 'Cluster']]
    summary.set_index("Cluster", inplace=True)
    summary = summary.groupby('Cluster').describe().transpose()
    return data


def datapreparation(data):
    # Age segment
    Age_labels = ['Young', 'Adult', 'Mature', 'Senior']
    Age_bins = [0, 30, 45, 65, 120]
    data['Age_group'] = pd.cut(data['Age'], bins=Age_bins, labels=Age_labels)

    # Income segments
    Income_labels = ['Low Income', 'Low to Medium Income', 'Medium to High Income', 'High Income']
    data['Income_group'] = pd.qcut(data['Income'], q=4, labels=Income_labels)

    # Seniority segments
    Seniority_labels = ['New Customers', 'Discovering Customers', 'Experienced Customers', 'Old Customers']
    data['Seniority_group'] = pd.qcut(data['Seniority'], q=4, labels=Seniority_labels)

    # Consumer segments
    Consumer_labels = ['Low Consumer', 'Frequent Consumer', 'High Consumer']
    data['Wines_segment'] = pd.qcut(data['Wines'][data['Wines'] > 0], q=[0, .25, .75, 1],
                                    labels=Consumer_labels).astype(
        "object")
    data['Fruits_segment'] = pd.qcut(data['Fruits'][data['Fruits'] > 0], q=[0, .25, .75, 1],
                                     labels=Consumer_labels).astype(
        "object")
    data['Meat_segment'] = pd.qcut(data['Meat'][data['Meat'] > 0], q=[0, .25, .75, 1], labels=Consumer_labels).astype(
        "object")
    data['Fish_segment'] = pd.qcut(data['Fish'][data['Fish'] > 0], q=[0, .25, .75, 1], labels=Consumer_labels).astype(
        "object")
    data['Sweets_segment'] = pd.qcut(data['Sweets'][data['Sweets'] > 0], q=[0, .25, .75, 1],
                                     labels=Consumer_labels).astype(
        "object")
    data['Gold_segment'] = pd.qcut(data['Gold'][data['Gold'] > 0], q=[0, .25, .75, 1], labels=Consumer_labels).astype(
        "object")
    data.replace(np.nan, "Non consumer", inplace=True)
    data = data.astype("object")

    return data


