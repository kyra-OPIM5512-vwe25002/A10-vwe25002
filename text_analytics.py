import sklearn as sk
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from imblearn.over_sampling import SMOTENC
from imblearn.over_sampling import SMOTE
from imblearn.over_sampling import SVMSMOTE
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.inspection import permutation_importance
from pycebox.ice import ice, ice_plot
import os
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
# from tpot import TPOTClassifier
import time
from sklearn.metrics import accuracy_score
import joblib

# c:\Users\kyraa\OneDrive\Documents\UConn - Business Analytics Certifcate\OPIM 5512 - Data Science\FoodRecalls.xlsx
df = pd.read_excel("c:/Users/kyraa/OneDrive/Documents/GitHub/A10-vwe25002/FoodRecalls.xlsx")

# examine data
print(df.head())
#df.drop('Loan_ID', axis=1, inplace=True)
print(df.shape)

# check for missing values
print(df.isnull().sum())

# check class distribution of target variable
print(df['Product Classification'].value_counts())

