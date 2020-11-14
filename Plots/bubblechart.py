import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('../Datasets/Weather2014-15.csv')


new_df = df.groupby('month').agg({'actual_max_temp': 'mean', 'actual_min_temp': 'mean', 'actual_mean_temp':'mean'
                                    }).reset_index()
print(new_df)
# Preparing data
data = [
go.Scatter(x=new_df['actual_max_temp'],
y=new_df['actual_min_temp'],
text=new_df['month'],
mode='markers',
marker=dict(size=new_df['actual_mean_temp'],color=new_df['actual_mean_temp'], showscale=True))
]

# Preparing layout
layout = go.Layout(title='Max Vs Min Temperature per Month', xaxis_title="Max temperature",
                   yaxis_title="Min temperature", hovermode='closest')

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bubblechart.html')