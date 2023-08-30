# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 22:51:15 2023

@author: subha
"""

import streamlit as st
# import pandas as pd
# from sklearn import datasets
# from sklearn.ensemble import RandomForestClassifier
# import pickle

st.write("""
# Greatest of three numbers

This app predicts the greatest of three numbers
""")
#Get Input

st.header('User Input Numbers')
def user_input_numbers():
     Number_1 = st.number_input("First_Number")
     Number_2 = st.number_input("Second_Number")
     Number_3 = st.number_input("Third_Number")
     
     data = {'First_Number': Number_1,
             'Second_Number': Number_2,
             'Third_Number' : Number_3
             }
     #features = pd.DataFrame(data, index=[0])
     return data

df = user_input_numbers()

st.subheader('User Input numbers')
st.write(df)

st.subheader('Output')

if (df['First_Number'] > df['Second_Number']) and (df['First_Number'] > df['Third_Number']) :
     st.write(df['First_Number'], "is the greatest number")
elif (df['Second_Number'] > df['First_Number']) and (df['Second_Number'] > df['Third_Number'] ):
       st.write(df['Second_Number'], "is the greatest number")
elif (df['Third_Number'] > df['First_Number']) and (df['Third_Number'] > df['Second_Number'] ):
       st.write(df['Third_Number'], "is the greatest number")


