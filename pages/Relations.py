import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import os

st.title(":blue[Relation Between Laptop Price and Features]")

#resources path
FILE_DIR1 = os.path.dirname(os.path.abspath(__file__))
FILE_DIR = os.path.join(FILE_DIR1,os.pardir)
dir_of_interest = os.path.join(FILE_DIR, "resources")
DATA_PATH = os.path.join(dir_of_interest, "data")

#Load data
DATA_PATH1=os.path.join(DATA_PATH, "laptop_price.csv")
df=pd.read_csv(DATA_PATH1)
df1=df.copy()
df1.drop("MRP", axis=1, inplace=True)


st.set_option('deprecation.showPyplotGlobalUse', False)

feature = st.selectbox("Select a feature", df1.columns)
plt.figure(figsize=(15, 10))


st.header(":violet[Histogram]")
sns.histplot(x=feature,data=df)
plt.title(f"Histplot of {feature}")
plt.xlabel(feature)
st.pyplot()


st.header(":violet[Boxplot]")
sns.boxplot(x=feature, y="MRP", data=df)
plt.title(f"Boxplot of {feature} vs MRP")
plt.xlabel(feature)
plt.ylabel("MRP")
st.pyplot()



st.header(":violet[Barplot]")
sns.barplot(x=feature, y="MRP", data=df,errorbar=None)
plt.title(f"Barplot of {feature} vs MRP")
plt.xlabel(feature)
plt.ylabel("MRP")
st.pyplot()

st.header(":violet[Aggregations]")
grouped_data = df.groupby([feature]).agg({'MRP' : ['min', 'max', 'mean']})
st.write(grouped_data)

