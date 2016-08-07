# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 02:19:07 2016

@author: Reshma
"""
from pandas import Series,DataFrame
import pandas as pd

def feature_summary(data):
    features=pd.DataFrame()
    features_names=[]
    features_counts=[]
    features_missing=[]
    names=data.columns.values
    for i in names:
        features_names.append(i)
        features_counts.append(data[i].value_counts().count())
        features_missing.append(data[data[i].isnull()].shape[0])
    features['name']=features_names
    features['value counts']=features_counts
    features['missing']=features_missing
    return (features)
        