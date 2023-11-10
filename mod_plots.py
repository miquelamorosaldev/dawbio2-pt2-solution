import pandas as pd
import matplotlib.pyplot as plt
import plotly
import plotly.express as px
import seaborn as sns
import base64
from io import BytesIO

def plot_to_base64(plt):
    '''Funció per convertir els gràfics en format base64 per a la visualització a la web'''
    img = BytesIO()
    plt.savefig(img, format='png')
    # plt.close()
    img.seek(0)
    return base64.b64encode(img.getvalue()).decode()

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
    barplot_plot = plt.figure(figsize=(10, 6))
    sns.barplot(x = 'Continent', y = 'Cholesterol',
            hue = 'Heart Attack Risk', data = df)
    # df_Spain = df[df['Country']=='Spain']
    bar_plot_base64 = plot_to_base64(barplot_plot)
    return bar_plot_base64

def plot2(df):
    '''Gràfic 2 - Nivell de colesterol vs Pressió arterial'''
    # df_Spain = df[df['Country']=='Spain']
    scatter_plot = plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Cholesterol', y='Blood Pressure', hue='Heart Attack Risk', data=df)
    plt.title('Nivell de colesterol vs Pressió arterial')
    scatter_plot_base64 = plot_to_base64(scatter_plot)
    return scatter_plot_base64

    # Inclou els gràfics en la pàgina principal
    # bar_plot = plt.figure(figsize=(10, 6))
    # sns.barplot(x='Sex', y='Age', data=df)
    # plt.title('Edat dels pacients per gènere')
    # bar_plot_base64 = plot_to_base64(bar_plot)

    # scatter_plot = plt.figure(figsize=(10, 6))
    # sns.scatterplot(x='Cholesterol', y='Blood Pressure', hue='Heart Attack Risk', data=df)
    # plt.title('Nivell de colesterol vs Pressió arterial')
    # scatter_plot_base64 = plot_to_base64(scatter_plot)

    # pie_chart = plt.figure(figsize=(8, 8))
    # df['Diet'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90)
    # plt.title('Distribució de tipus de dieta')
    # pie_chart_base64 = plot_to_base64(pie_chart)
