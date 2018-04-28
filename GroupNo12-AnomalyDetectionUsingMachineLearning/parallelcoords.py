import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
import numpy as np

df = pd.read_csv("with_clusters.csv")
df['SourceName']=df['SourceName'].astype('category')
df['TaskCategory']=df['TaskCategory'].astype('category')
abc=df.select_dtypes(['category']).columns
df[abc] = df[abc].apply(lambda x: x.cat.codes)

data = [
    go.Parcoords(
        line = dict(color = df['cluster'],
                   colorscale = 'Jet',
                   showscale = True,
                   reversescale = True,
                   cmin = -4000,
                   cmax = -100000),
        dimensions = list([
            dict(range=[10,50000],
            label='Record Number', values=df['RecordNumber']
            ),
            dict(range=[0,55],
            label='Source Name', values=df['SourceName']
            ),
            dict(range=[0,40],
            label='TaskCategory', values=df['TaskCategory']
            ),
            dict(range= [0, 40000],
                 ticktext = ['A','AB','B','Y','Z'],
                 label = 'Event Code', values = df['EventCode']),
            dict(range = [1,4],
                 tickvals =[1, 2, 3, 4],
                 label = 'Event Type', values = df['EventType']),
            
        ])
    )
]
py.plot(data, filename = 'parcoords-advanced')
