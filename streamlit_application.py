import numpy as np 
import pandas as pd
import streamlit as st
import pickle
from PIL import Image
import seaborn as sns
import matplotlib.pyplot as plt


# Page setting
st.set_page_config(layout="wide")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Data
Telcom_Data = pd.read_csv("telcom_data.csv")
Telcom_data1= pickle.load(open("telco_model.pkl","rb"))

try:
    telco_data = pd.read_csv("telcom_data.csv")
    is_data_loaded = True
except Exception as e:
    is_data_loaded = False
    st.error(f"Error loading data: {e}")

st.title ('Telecommunication Analysis')
image = Image.open('telcom logo.jpg')
st.image(image,'')

st.title('Task 1 User Overview Analysis')
#Display general statistics
st.subheader("General Statistics")
st.write(Telcom_Data.describe())

# Display null values
st.subheader('Null Values:')
st.write(Telcom_Data.isnull().sum())


# Display a histogram of the top 10 handsets used by customers
st.subheader('Top 10 Handsets Used by Customers:')
top_handsets = Telcom_Data['Handset Type'].value_counts().nlargest(10)
        
plt.figure(figsize=(10, 6))
plt.bar(top_handsets.index, top_handsets.values, color='skyblue')
plt.xlabel('Handset')
plt.ylabel('Count')
plt.title('Top 10 Handsets Used by Customers')
plt.xticks(rotation=45, ha='right')
        
st.pyplot()

#Identifying The Top 3 Handset's Manufactures
st.subheader('Identifying The Top 3 Handsets Manufactures')
top_handsets_Manufacture = Telcom_Data['Handset Manufacturer'].value_counts().nlargest(10)

plt.figure(figsize=(10, 6))
plt.bar(top_handsets_Manufacture.index, top_handsets_Manufacture.values, color='skyblue')
plt.xlabel('Handset')
plt.ylabel('Count')
plt.title('Identifying The Top 3 Handsets Manufactures')
plt.xticks(rotation=45, ha='right')

st.pyplot()

# Analyze the total downloads and uploads of each application
# Select relevant columns for scatter plot
selected_columns = [
            'Google DL (Bytes)', 'Google UL (Bytes)',
            'Email DL (Bytes)', 'Email UL (Bytes)',
            'Youtube DL (Bytes)', 'Youtube UL (Bytes)',
            'Netflix DL (Bytes)', 'Netflix UL (Bytes)',
            'Gaming DL (Bytes)', 'Gaming UL (Bytes)',
            'Other DL (Bytes)', 'Other UL (Bytes)',
            'Total UL (Bytes)', 'Total DL (Bytes)'
        ]

        # Scatter plot for each pair of download and upload columns
st.subheader('Scatter Plots for Each Pair of Download and Upload Columns:')
for i in range(0, len(selected_columns), 2):
            plt.figure(figsize=(10, 6))
            sns.scatterplot(x=selected_columns[i], y=selected_columns[i + 1], data=Telcom_Data, s=100)
            plt.title(f'Scatter Plot of {selected_columns[i]} vs {selected_columns[i + 1]}')
            plt.xlabel(selected_columns[i])
            plt.ylabel(selected_columns[i + 1])
            st.pyplot()




