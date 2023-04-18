import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
st.set_option('deprecation.showPyplotGlobalUse', False)

def main():
            
    html_temp = """ <div style="padding:1.5px">
                    <h1 style="color:black;text-align:center;">Earthquake Detection</h1></div><br>"""
    st.markdown(html_temp,unsafe_allow_html=True)
    df = load_data()
    if st.checkbox("Dataset Analyze"):
        select1 = st.selectbox("Please select a section:", ["", "Head", "Describe"])
     
        if select1 == "Head":
            st.table(df.head())
        elif select1 == "Describe":
            select2 = st.selectbox("Please select value type:", ["", "Numerical", "Categorical"])
            if select2 == "Numerical":
                st.table(df.describe())
            elif select2 == "Categorical":
                st.table(df.describe(include='all'))
    if st.checkbox("Visualization of Past Earthquakes"):
            rounding_factor = 10
            fig, ax = plt.subplots(figsize=(15,8))

            # latitude and longitude of earthquake site of top 10500 samples.
            plt.plot(np.round(df['longitude'].head(10500),rounding_factor), 
                     np.round(df['latitude'].head(10500),rounding_factor),
                     linestyle='none', marker='.')

            plt.suptitle('Earthquakes from ' + str(np.min(df['time']))[:20] + ' to ' + str(np.max(df['time']))[:20])
            plt.xlabel('Longitude')
            plt.ylabel('Latitude')
            st.pyplot()

def load_data():
    df = pd.read_csv('all_month.csv')
    return df 

if __name__ == "__main__":
    main()