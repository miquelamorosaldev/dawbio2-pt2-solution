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


def map1(df):
    '''Gràfic mapa.'''
    # Primer, agrupar casos per països.Country
   
    # Compta el nombre total de pacients per cada país
    total_pacients_per_pais = df.groupby('Country')['Heart Attack Risk'].count().reset_index(name='Total Patients')

    # Filtra les files amb Heart Attack Risk igual a 1
    df_risc_atac = df[df['Heart Attack Risk'] == 1]

    # Compte el nombre de pacients amb risc d'atac al cor per cada país
    pacients_risc_atac_per_pais = df_risc_atac.groupby('Country')['Heart Attack Risk'].count().reset_index(name='Patients with Heart Attack Risk 1')

    # Combina els dos DataFrames per obtenir el percentatge
    resultat = pd.merge(total_pacients_per_pais, pacients_risc_atac_per_pais, on='Country', how='left')

    # Calcula el percentatge i crea una nova columna
    resultat['Percentatge of Patients with Heart Attack Risk 1'] = (resultat['Patients with Heart Attack Risk 1'] / resultat['Total Patients']) * 100

    # print(resultat)

    # Crea el mapa de cloropets
    fig = px.choropleth(resultat,
                        locations='Country',  # Nom del país
                        locationmode='country names',  # Mode de localització per noms de país [ISO-3, country names]
                        hover_name='Percentatge of Patients with Heart Attack Risk 1',  # Informació que apareixerà en la caixa d'eines en fer hover
                        color='Percentatge of Patients with Heart Attack Risk 1',  # Variable a representar amb colors
                        color_continuous_scale=px.colors.sequential.Reds,
                        title='Mapa percentatge pacients amb risc d\'atac de cor per país'
                    )

    # Mostra el mapa
    fig.update_layout(margin=dict(l=20,r=0,b=0,t=70,pad=0),paper_bgcolor="white",height= 700,font_size=18)
    return fig
