import yfinance as yf
import streamlit as st
import pandas as pd 

st.write("""
# Spotify App

Showing new songs in a playlists

""")

tickerSymbol = 'AAPL'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')


