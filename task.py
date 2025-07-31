import numpy as np
from numpy import mean, std, array
import pandas as pd
import plotly.express as px

data_array = array([5.5, 5.7, 5.9, 6.0, 5.8, 5.6, 5.7, 7.2, 4.8])

category = ['Outlier' if (val < mean(data_array) - 2 * std(data_array) or val > mean(data_array) + 2 * std(data_array)) else 'Normal' for val in data_array]

df = pd.DataFrame({
    'Time (minutes)': data_array,
    'Values': range(1, len(data_array) + 1),
    'category': category
})

fig = px.line(df, x='Values', y='Time (minutes)', color='category', template='plotly_dark',
              title='Tempos de Ciclo',
              markers=True)

fig.show()