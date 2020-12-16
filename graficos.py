from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 
import streamlit as st 




def figura_1():
    df = pd.read_csv('data/kagglemusic.csv')
    fig = sns.catplot(y = "genre", kind = "count",palette = "pastel", edgecolor = ".6", data = df)
    st.pyplot(fig)


def figura_2():
    df = pd.read_csv('data/kagglemusic.csv')
    fig = sns.jointplot(x=df["bpm"].values, y=df['pop'].values, size=10, kind="kde",)
    plt.ylabel('pop', fontsize=12)
    plt.xlabel("bpm", fontsize=12)
    plt.title("Beats.Per.Minute Vs Popularity", fontsize=15)
    st.pyplot(fig)


def figura_3():
    df = pd.read_csv('data/kagglemusic.csv')
    fig = sns.lmplot(x="nrgy",y="pop",data=df,size=10,hue="genre")
    st.pyplot(fig)


def figura_4():
    df = pd.read_csv('data/kagglemusic.csv')
    x = "dnce"
    y = "val"

    fig, (ax1, ax2) = plt.subplots(1, 2, sharey=False, sharex=False, figsize=(10, 5))
    fig.suptitle("Histograms")
    h = ax2.hist2d(df[x], df[y], bins=20)
    ax1.hist(df["nrgy"])

    ax2.set_xlabel(x)
    ax2.set_ylabel(y)

    ax1.set_xlabel("nrgy")

    plt.colorbar(h[3], ax=ax2)

    plt.show()
    st.pyplot(fig)


def figura_5():
    df = pd.read_csv('data/kagglemusic.csv')
    plt.figure(figsize=(10,10))
    plt.title('Correlation Map')
    fig = sns.heatmap(df.corr(),linewidth=3.1, annot=True, center=1)
    st.plt.savefig(fig)
    # st.pyplot(fig)


def genero_canciones(genero:str):
    canciones = pd.read_csv('data/genre.csv')
    pop = canciones[canciones.genre == genero]
    return (pop)

