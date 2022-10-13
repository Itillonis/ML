import streamlit as st
import pandas as pd

df = pd.read_csv('titanic.csv')
df = df[['Age','Survived']].dropna()
df = df.groupby(by='Age').count()

if st.button('Показать данные'):
    st.dataframe(df.reset_index())
if st.button('Вывести график'):
    st.line_chart(df)