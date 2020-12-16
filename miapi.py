import yfinance as yf
import streamlit as st
import pandas as pd 
import graficos as gf 
import seaborn as sns
import matplotlib.pyplot as plt


# df = pd.read_csv('data/kagglemusic.csv')
st.title("*Spotify*")


st.header("""
Figure 1 : "Genre"
""")
st.text("Showing the differences genres of the songs")
st.success("dance pop")

gf.figura_1()

st.header("Figure 2")
gf.figura_2()

st.header("Figure 3")
gf.figura_3()

st.header("Figure 4")
gf.figura_4()

#st.header("Figure 5")
#gf.figura_5()

canciones = pd.read_csv('data/genre.csv')
genre = st.selectbox("What is the genre you want?", ["acoustic pop", "art pop", "atl hip hop", "australian dance", "australian pop", "barbadian pop", "baroque pop", "belgian edm", "big room", "boy band", "british soul", "canadian contemporary r&b", "canadian pop", "colombian pop", "complextro", "dance pop", "edm", "electronic trap", "electropop", "hip hop", "neo mellow", "permanent wave", "pop"])
pop = canciones[canciones.genre == genre]
pop



