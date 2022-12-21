import pickle
import numpy as np
import streamlit as st

# load save model
model = pickle.load(open('heart_attack.sav', 'rb'))

# Judul web
st.title('Data Mining Prediksi Serangan Jantung')

col1, col2 = st.columns(2)

with col1:
    age = st.number_input('Input Nilai Age')

with col2:
    sex = st.number_input('Input Nilai Sex')

with col1:
    cp = st.number_input(' Input Nilai Cp')

with col2:
    trestbps = st.number_input('Input Nilai Trestbps')

with col1:
    chol = st.number_input('Input Nilai Chol')

with col2:
    fbs = st.number_input('Input Nilai Fbs')

with col1:
    restecg = st.number_input(' Input Nilai Restecg')

with col2:
    thalach = st.number_input('Input Nilai Thalach')

with col1:
    exang = st.number_input('Input Nilai Exang')

with col2:
    oldpeak = st.number_input('Input Nilai Oldpeak')

with col1:
    slope = st.number_input('Input Nilai Slope')

with col2:
    ca = st.number_input('Input Nilai Ca')

with col1:
    thal = st.number_input('Input Nilai Thal')

# code untuk prediksi
    heartatt_diagnosis = ''

# membuat tombol
if st.button('Mulai'):
    heartatt_prediction = model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang,
                                          oldpeak, slope, ca, thal]])

    if (heartatt_prediction[0] == 1):
        heartatt_diagnosis = 'Pasien terkena serangan jantung'
    else:
        heartatt_diagnosis = 'Pasien tidak terkena serangan jantung'

st.success(heartatt_diagnosis)
