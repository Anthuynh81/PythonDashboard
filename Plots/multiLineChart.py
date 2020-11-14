import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')

new_df = df.groupby('month', as_index=False, sort=False).agg({'actual_max_temp': 'max', 'actual_min_temp' : 'max', 'actual_mean_temp' : 'max'})
print(new_df)
# Preparing data
trace1 = go.Scatter(x=new_df['month'], y=new_df['actual_max_temp'], mode='lines', name='maxtemp')
trace2 = go.Scatter(x=new_df['month'], y=new_df['actual_min_temp'], mode='lines', name='mintemp')
trace3 = go.Scatter(x=new_df['month'], y=new_df['actual_mean_temp'], mode='lines', name='meantemp')
data = [trace1, trace2, trace3]

# Preparing layout
layout = go.Layout(title='Max, min, mean temperature from Weather 2014-2015', xaxis_title="Date", yaxis_title="Temperature")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='multiLineChart.html')