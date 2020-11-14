import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')

new_df = df.groupby('month', as_index=False, sort=False).agg({'actual_max_temp': 'max'})

# Preparing data
data = [go.Scatter(x=new_df['month'], y=new_df['actual_max_temp'], mode='lines', name='maxtemp')]

# Preparing layout
layout = go.Layout(title="Actual Max Temperatures Over Months",
                   xaxis_title="Months",
                    yaxis_title="Actual Max Temperature")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='linechart.html')