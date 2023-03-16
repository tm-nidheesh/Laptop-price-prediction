import streamlit as st
import pandas as pd
import pickle
import numpy as np

pipe = pickle.load(open("pipe.pkl", "rb"))
df = pickle.load(open("df.pkl", "rb"))

st.title("Laptop price predictor")

company = st.selectbox('Brand', df['Company'].unique())

Type = st.selectbox('Type', df['TypeName'].unique())

ram = st.selectbox('RAM(in GB)', [2, 4, 6, 8, 12, 16, 32])

weight = st.number_input("Weight")

touchscreen = st.selectbox("Touchscreen", ['YES', 'NO'])

ips = st.selectbox("IPS", ['YES', 'NO'])

screen_size = st.number_input("Screen size")

resolution = st.selectbox("Resolution", ['1920x1080', '1366x768', '1600x900', '3840x2160',
                                         '3200x1800', '2880,1800', '2560x1600', '2560x1440',
                                         '2304x1440'])

cpu = st.selectbox('CPU', df['Cpu Brand'].unique())

hdd = st.selectbox('HDD(in GB)', [0, 128, 256, 512, 1024, 2048])

ssd = st.selectbox('SSD(in GB)', [0, 8, 128, 256, 512, 1024])

gpu = st.selectbox('GPU', df['Gpu Brand'].unique())

os = st.selectbox('OS', df['os'].unique())


if st.button("Predict price"):
    ppi = None
    if touchscreen == 'YES':
        touchscreen = 1
    else:
        touchscreen = 0

    if ips == 'YES':
        ips = 1
    else:
        ips = 0

    x_res = int(resolution.split('x')[0])
    y_res = int(resolution.split('x')[1])

    ppi = ((x_res**2) + (y_res**2))**0.5/screen_size

    query = np.array([company, Type, ram, weight, touchscreen, ips, ppi, cpu, hdd, ssd, gpu, os], dtype=object)
    query = query.reshape(1, 12)
    st.title("The price of this configuration is " + str(int(np.exp(pipe.predict(query)[0]))))





