import pandas as pd
import numpy as np
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
import datetime as dt

def create_busy_hour_df(df):
    df_hour['dteday'] = pd.to_datetime(df_hour['dteday'])
    df_hour['datetime'] = df_hour['dteday'] + pd.to_timedelta(df_hour['hr'], unit='h')
    hourly_usage = df_hour.groupby(by="hr").cnt.sum()
    return hourly_usage

def create_comparison_casual_reg_df(df):
    df_day['dteday'] = pd.to_datetime(df_day['dteday'])
    return df_day['dteday']
    
df_day = pd.read_csv("dashboard/day.csv")
df_hour = pd.read_csv("dashboard/hour.csv")

hourly_usage = create_busy_hour_df(df_hour)
df_day['dteday'] = create_comparison_casual_reg_df(df_day)

st.header('Capital Bike Share :sparkles:')

min_date = df_hour["dteday"].min()
max_date = df_hour["dteday"].max()

with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://raw.githubusercontent.com/salsabilafaiha/Proyek-Analisis-Data/main/CapitalBikeshare-main.png")
    
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

st.subheader("Jam Puncak Penggunaan Sepeda dalam Satu Hari")
# no 1 Kapan jam puncak penggunaan sepeda terjadi dalam satu hari?
fig, ax = plt.subplots(figsize=(8, 4))
plt.plot(hourly_usage.index, hourly_usage.values, marker='o', linestyle='-', color='b')
ax.set_title('Penggunaan Sepeda per Jam')
ax.set_xlabel('Jam')
ax.set_ylabel('Jumlah Sepeda')
ax.set_xticks(hourly_usage.index)
ax.grid()
st.pyplot(fig)

st.subheader("Perbandingan Pengguna Sepeda Casual dan Terdaftar per Hari")
# no 2 Pastikan kolom 'dteday' sudah dalam format datetime

fig, ax = plt.subplots(figsize=(8, 4))

ax.bar(df_day['dteday'], df_day['casual'], label='Casual', color='b', alpha=0.7)
ax.bar(df_day['dteday'], df_day['registered'], label='Registered', color='r', alpha=0.7)
ax.set_title('Perbandingan Pengguna Sepeda Casual dan Terdaftar per Hari')
ax.set_xlabel('Tanggal')
ax.set_ylabel('Jumlah Sepeda')
ax.legend()
ax.tick_params(axis='x', rotation=45)
ax.grid(True)
st.pyplot(fig)

st.caption('Copyright (c) Salsabila Faiha 2023')
