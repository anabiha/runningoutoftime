import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from dash.dependencies import Input, Output
import pandas as pd
import os
import numpy as np


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__,external_stylesheets=external_stylesheets)

colors = {
    'text': '#7FDBFF'
}

# data formatting for global temperatures 
with open('GLB.Ts+dSST.csv') as f:
    temp = pd.read_csv(f)

temp = temp.drop(columns=['J-D','D-N','DJF','MAM','JJA','SON'])
months = temp.drop(columns=['Year'])
years = temp['Year'].tolist()
col_names = temp.columns.values.tolist()
col_names.remove('Year')

# markdown text to explain the chart
markdown_text = '''
Global climate change has been slowly creeping up on mankind like a slow leak on a bike tire, and we’ve only just realized the repercussions our actions have had on Earth. There’s a brief window of opportunity for mankind to enact policy changes in order to minimize our impact, but even if we are able to patch up the tire in time, our impacts will not be reversed. Mankind’s role in global climate change is evident, and it marks the new geological epoch called the Anthropocene. Society is aware of the environmental changes, but it appears to happen very slowly which the term “ennuipocalypse” perfectly captures. We’re living in a “a doomsday that [is occuring] at an excruciatingly slow day to day time scale.” This feeling contradicts the alarming data mankind is faced with.
'''

# data formatting for sea levels
# https://raw.githubusercontent.com/plotly/datasets/master/Emissions%20Data.csv'
sea_levels = pd.read_csv('sea_level.csv')
sea_levels = sea_levels.drop(columns=['Unnamed: 2','Unnamed: 3','Unnamed: 4','Unnamed: 5','Unnamed: 6'])
years = sea_levels['Year']
sea = sea_levels['Adjusted_Sea_Level']

app.layout = html.Div(children=[

    html.H1(
        children='Surface Temperature of the Earth (1880-2016)',
        style={
            'textAlign': 'center',
            'color': 'rgb(56,75,211)'
        }
        ),

    dcc.Graph(
        id='temp-around-the-globe',
        figure={
            'data': [
                go.Heatmap(
                   z=months,
                   x=col_names,
                   y=years)
            ]
        },
        style={
            'height':800,
            'width':1500
        }
    ),

    # Source: https://data.world/agriculture/nasa-giss-global-temperature/workspace/project-summary?agentid=agriculture&datasetid=nasa-giss-global-temperature

    

    html.H1(
        children='Global Average Absolute Sea Level Change (inches) (1880-2013)',            
        style={
            'textAlign': 'center',
            'color': 'rgb(56,75,211)'
        }
    ),

    dcc.Graph(
        id='sea-levels',
        figure={
            'data': [
                go.Bar(
                    x=years,
                    y=sea
                )
            ]
        },
        style={
            'width':1500
        }
    ),

    #Source: https://www.epa.gov/sites/production/files/2016-08/sea-level_fig-1.csv

    dcc.Markdown(children=markdown_text)
])


if __name__ == '__main__':
    app.run_server(debug=True)