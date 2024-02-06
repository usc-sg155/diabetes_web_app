#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 20:44:14 2024

@author: sandeepgautam
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 12:40:20 2024

@author: sandeepgautam
"""

import pickle
import streamlit as st

#loading the saved models

diabetes_model = pickle.load(open('/Users/sandeepgautam/Documents/machinelearning/diabetes_model.sav','rb'))


#Diabetes Prediction Page
#Page title
st.title('Diabetes Prediction using ML')
 
 #getting the input data from user
 
Pregnancies = st.text_input('Number of Pregnancies')
 
Glucose = st.text_input('Glucose Level')

BloodPressure = st.text_input('Blood Pressure Value')

SkinThickness = st.text_input('Skin Thickness Value')

Insulin = st.text_input('Insulin Level')

BMI = st.text_input('BMI Value')

DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')

Age = st.text_input('Age of the Person')
     
#code for prediction
     
diab_diagnosis = ''
 
if st.button('Diabetes Test Result'):
    diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
    
    if (diab_prediction[0]== 0):
        diab_diagnosis = 'The Person is not diabetic'
    else:
        diab_diagnosis = 'The person is diabetic'
        
    st.success(diab_diagnosis)