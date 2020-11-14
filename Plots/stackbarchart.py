import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Olympic2016Rio.csv')

# Sorting values and select first 20 states
df['total medals'] = df.iloc[:, 1:4].sum(axis=1)
new_df = df.sort_values(by=['total medals'], ascending=[False]).head(20)


# Preparing data
trace1 = go.Bar(x=new_df['NOC'], y=new_df['Gold'], name='Gold Medal',
marker={'color': '#CD7F32'})
trace2 = go.Bar(x=new_df['NOC'], y=new_df['Silver'], name='Silver Medal',
marker={'color': '#9EA0A1'})
trace3 = go.Bar(x=new_df['NOC'], y=new_df['Bronze'], name='Bronze Medal',
marker={'color': '#FFD700'})
data = [trace1, trace2, trace3]

# Preparing layout
layout = go.Layout(title='Top 20 Countries\' Medals in 2016 Olympics', xaxis_title="Name of Country",
                     yaxis_title="Number of Medals", barmode='stack')

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='stackbarchart.html')