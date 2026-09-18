import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker
from babel.numbers import format_currency
sns.set(style='dark')

df = pd.read_csv("all_df.csv")
df["dteday_x"] = pd.to_datetime(df["dteday_x"])

custom_palette = {
    'Clear/Slightly Cloudy': '#003F5C',   
    'Light Precipitation': '#7A5195',    
    'Misty/Cloudy': '#EF5675',          
    'Severe Weather': '#FFA600'         
}

def daily_rentals(df):
    daily_rentals = df.resample(rule='D', on='dteday_x').agg({"cnt_x": "sum"}).reset_index()
    daily_rentals.rename(columns={"cnt_x": "rental_count"}, inplace=True)
    return daily_rentals

def rfm_analysis(df):
    revenue_per_renter = 10_000
    rfm = df.groupby("instant").agg({
        "dteday_x": "max", 
        "cnt_x": "sum"  
    }).rename(columns={"dteday_x": "max_order_timestamp", "cnt_x": "monetary"})
    rfm["monetary"] *= revenue_per_renter
    rfm.drop(columns=["max_order_timestamp"], inplace=True)
    rfm["frequency"] = df.groupby("instant")["dteday_x"].count()
    return rfm

def temp_hum_plot(df):
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.scatterplot(x=df['temp_x'], y=df['cnt_x'], alpha=0.6, label='Temperature', ax=ax)
    sns.scatterplot(x=df['hum_x'], y=df['cnt_x'], alpha=0.6, label='Humidity', ax=ax)
    ax.set_xlabel("Value")
    ax.set_ylabel("Total Rentals")
    ax.set_title("Temperature and Humidity Distribution")
    ax.legend()
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{int(x):,}'))
    return fig

def weather_chart(df):
    weather_labels = {1: "Clear/Slightly Cloudy", 2: "Misty/Cloudy", 3: "Light Precipitation", 4: "Severe Weather"}
    df['weather_label'] = df['weathersit_y'].map(weather_labels)
    weather_counts = df.groupby('weather_label')['cnt_x'].sum().reset_index()
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(x='weather_label', y='cnt_x', hue='weather_label', data=weather_counts, ax=ax, palette=custom_palette, legend=False)
    ax.set_xlabel("Weather Condition")
    ax.set_ylabel("Total Rentals")
    ax.set_title("Bike Rentals by Weather Condition")
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{int(x):,}'))
    return fig

def season_chart(df):
    season_labels = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
    df['season_label'] = df['season_x'].map(season_labels)
    season_counts = df.groupby('season_label')['cnt_x'].sum().reset_index()
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(x='season_label', y='cnt_x', hue='season_label', data=season_counts, ax=ax, palette='viridis', legend=False)
    ax.set_xlabel("Season")
    ax.set_ylabel("Total Rentals")
    ax.set_title("Bike Rentals by Season")
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{int(x):,}'))
    return fig

min_date = df["dteday_x"].min()
max_date = df["dteday_x"].max()
with st.sidebar:
    start_date, end_date = st.date_input("Time Range", min_value=min_date, max_value=max_date, value=[min_date, max_date])

main_df = df[(df["dteday_x"] >= str(start_date)) & (df["dteday_x"] <= str(end_date))]
daily_rentals_df = daily_rentals(main_df)
rfm = rfm_analysis(main_df)

st.header("Bike Rentals Dashboard 🚲")
st.subheader("Daily Rentals With Revenue Prediction (10.000 Rupiah/Renters)")
col1, col2 = st.columns(2)

with col1:
    total_rentals = daily_rentals_df.rental_count.sum()
    st.metric("Total Rentals", value=f"{total_rentals:,}")

with col2:
    total_revenue = format_currency(rfm["monetary"].sum(), "IDR", locale='id_ID')
    st.metric("Total Revenue", value=total_revenue)

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(daily_rentals_df["dteday_x"], daily_rentals_df["rental_count"], marker='o', linewidth=2, color="#90CAF9")
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{int(x):,}'))
st.pyplot(fig)

st.subheader("Temperature and Humidity vs Bike Rentals")
st.pyplot(temp_hum_plot(main_df))

st.subheader("Bike Rentals by Weather Condition")
st.pyplot(weather_chart(main_df))

st.subheader("Bike Rentals by Season")
st.pyplot(season_chart(main_df))

max_daily_rentals = daily_rentals_df["rental_count"].max()
st.write(f"### Maximum Daily Rentals: {max_daily_rentals:,}")

