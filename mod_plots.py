import pandas as pd
import matplotlib.pyplot as plt
import plotly
import plotly.express as px
import seaborn as sns
import base64
from io import BytesIO

def __draw_plot():
    '''Transforma el gràfic en una imatge.'''
    img = BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')
    return plot_url


def demo_plot():
    '''Carrega un gràfic de prova del dataframe del Titanic. '''
    titanic_df = sns.load_dataset("titanic")
    print(titanic_df.head())
    # Another way to visualize the data is to use FacetGrid to plot multiple kedplots on one plot
    fig = sns.FacetGrid(titanic_df, hue="sex", aspect=4)
    fig.map(sns.kdeplot, 'age', fill=True)
    new_plot = titanic_df['age'].max()
    fig.set(xlim=(0, new_plot))
    fig.add_legend()
    plot_url = __draw_plot()
    return plot_url

def plot1(df):
    '''Carrega el primer gràfic de la web.'''
    # df_Spain = df[df['Country']=='Spain']
    sns.barplot(x = 'Continent', y = 'Cholesterol',
            hue = 'Heart Attack Risk', data = df)
    # df_Spain = df[df['Country']=='Spain']
    plot_url = __draw_plot()
    return plot_url