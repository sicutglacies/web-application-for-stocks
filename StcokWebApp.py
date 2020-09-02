#Description: This is a stock market dashboard to show some charts and data on some stock

#Import the libraries
import streamlit as st
import pandas as pd
from PIL import Image
from cik_match import get_ticker
from pandas_datareader import data as web
from datetime import datetime


#Add a title and an image
st.write("""
# Stock Market Web Application
**Visually** show data on a stock
""")

image = Image.open('stock_image.jpg')
st.image(image, use_column_width=True)

#Create sidebar header
st.sidebar.header('User Input')

#Create a function to get the users input
def get_input():
    start_date = st.sidebar.text_input('Start Date', '2020-01-02')
    end_date = st.sidebar.text_input('End Date', '2020-01-02')
    stock_symbol = st.sidebar.text_input('Stock Symbol', 'AMZN')
    return start_date, end_date, stock_symbol

#Create a function to get the proper company data and the proper timeframe 
def get_data(symbol, start, end):
    df = web.DataReader(symbol.upper(), data_source='yahoo', start=start, end=end)
    return df

#Get the users input
start, end, symbol = get_input()
#Get the data
df = get_data(symbol, start, end)
#Get the company name
_ , company_name, _ = get_ticker(symbol.upper())


#Display the close price
st.header(company_name + ' ' + 'Close Price\n')
st.line_chart(df['Close'])

#Display the volume
st.header(company_name + ' ' + 'Volume\n')
st.line_chart(df['Volume'])

#Get statistics on the data
st.header('Data Statistics')
st.write(df.describe().drop(['count', '25%', '50%', '75%'], axis=0))

    
    

