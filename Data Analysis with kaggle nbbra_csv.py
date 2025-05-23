# -*- coding: utf-8 -*-
"""VoTheAnHao-2474601080006-NBbra.csv

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GWTIGlh9fp5GtQZej5hcuv2LGKAnmzNW
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly as py
import plotly. graph_objs as go
from sklearn.naive_bayes import GaussianNB
import numpy as p

df = pd.read_csv('brca.csv')
df.head()

X = df.iloc[:,1:-1].values
y = df.iloc[:,-1].values

import plotly.express as px
fig = px.pie(df, names='y',
             color_discrete_sequence=['#491D8B','#7D3AC1'],
             title='data distribution',
             template='plotly')
fig.show()

statistics = df.describe()
print(statistics)

fig = px.box(data_frame=df,
             x='y',
             y='x.radius_mean',
             color='y',
             color_discrete_sequence=['#29066B','#7D3AC1'],
             orientation='v')
fig.show()

X = df.iloc[:,1:-1].values
#ma hoa nhan phan loai
label = {"B": 0, "M": 1}
y = df.iloc[:, -1].map(label).values
# chia tap huan luyen va kiem tra
#y = df.iloc[:,-1].values

y

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42)

Numbertest = np.size(y_test)
Numbertrain = np.size(y_train)
print("so tep test va so tep train lan luot la:", Numbertest, Numbertrain)

# Create the Gaussian Naive Bayes classifier
gnb = GaussianNB()
gnb.fit(X_train, y_train)
y_pred = gnb.predict(X_test)
print("ket qua du doan label", y_pred)

accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')

print(classification_report(y_test, y_pred))
# # Confusion matrix
confusion = confusion_matrix(y_test, y_pred)
print('Confusion Matrix:\n', confusion)

plt.figure(figsize=(6, 4))
sns.heatmap(confusion, annot=True, fmt='d', cmap='Blues', cbar=False)
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('True')
plt.show()

"""BTH2: lam viec voi du lieu cua benh nhan A"""

df = pd.read_csv('brca.csv')
df.head()

X = df.iloc[:,1:-1].values
#ma hoa nhan phan loai
label = {"B": 0, "M": 1}
y = df.iloc[:, -1].map(label).values
# chia tap huan luyen va kiem tra
#y = df.iloc[:,-1].values

# Create the Gaussian Naive Bayes classifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
gnb = GaussianNB()
gnb.fit(X,y)

BN = pd.read_csv('KetquaxetNghiem-BenhNhanA.csv')
BN.head()

X_test = BN.iloc[:,1:31].values
X_test

y_pred = gnb.predict(X_test)
print("ket qua du doan label (1: ac tinh, 0: lanh tinh):", y_pred)