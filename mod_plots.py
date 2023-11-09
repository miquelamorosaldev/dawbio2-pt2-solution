import pandas as pd
import matplotlib.pyplot as plt
import plotly
import plotly.express as px
import seaborn as sns
import base64
from io import BytesIO

def demo_plot():
    '''Carrega un gràfic de prova del dataframe del Titanic. '''
    titanic_df = sns.load_dataset("titanic")
    print(titanic_df.head())
    # Another way to visualize the data is to use FacetGrid to plot multiple kedplots on one plot
    fig = sns.FacetGrid(titanic_df, hue="sex", aspect=4)
    fig.map(sns.kdeplot, 'age', fill=True)
    oldest = titanic_df['age'].max()
    fig.set(xlim=(0, oldest))
    fig.add_legend()
    img = BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')
    return plot_url

def plot1():
    '''Carrega el primer gràfic de la web.'''
    titanic_df = sns.load_dataset("titanic")
    print(titanic_df.head())
    # Another way to visualize the data is to use FacetGrid to plot multiple kedplots on one plot
    fig = sns.FacetGrid(titanic_df, hue="sex", aspect=4)
    fig.map(sns.kdeplot, 'age', fill=True)
    oldest = titanic_df['age'].max()
    fig.set(xlim=(0, oldest))
    fig.add_legend()
    img = BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')
    return plot_url