"""
Author: Siddhant Mahajani
aprioriAlgo.py - Python code to execute the apriori algorithm to get customer personality analysis
"""

import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules


def performanalysis(data):
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_colwidth', 999)
    pd.options.display.float_format = "{:.3f}".format
    association = data.copy()
    df = pd.get_dummies(association)
    min_support = 0.08
    max_len = 10
    frequent_items = apriori(df, use_colnames=True, min_support=min_support, max_len=max_len + 1)
    rules = association_rules(frequent_items, metric='lift', min_threshold=1)

    product = 'Fruits'
    segment = 'High Consumer'
    target = '{\'%s_segment_%s\'}' % (product, segment)
    results_personnal_care = rules[rules['consequents'].astype(str).str.contains(target, na=False)].sort_values(
        by='confidence', ascending=False)
    return results_personnal_care
