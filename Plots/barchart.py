import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Olympic2016Rio.csv')

# Sorting values and select first 20 states
df['total medals'] = df.iloc[:, 1:4].sum(axis=1)
new_df = df.sort_values(by=['total medals'], ascending=[False]).head(20)

# Preparing data
data = [go.Bar(x=new_df['NOC'], y=new_df['total medals'])]

# Preparing layout
layout = go.Layout(title='total medals of Olympic 2016 of 20 first top countries', xaxis_title="Names of Countries",
                   yaxis_title="Number of Medals")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='barchart.html')
