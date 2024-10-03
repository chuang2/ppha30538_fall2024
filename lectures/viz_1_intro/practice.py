import pandas as pd
import altair as alt

alt.renderers.enable('html')

import altair_viewer



#installed vega through terminal
from vega_datasets import data as vega_data


cars = vega_data.cars()
print(cars.head())

df = pd.DataFrame({
    'city': ['Seattle', 'Seattle', 'Seattle', 'New York', 'New York', 'New York', 'Chicago', 'Chicago', 'Chicago'],
    'month': ['Apr', 'Aug', 'Dec', 'Apr', 'Aug', 'Dec', 'Apr', 'Aug', 'Dec'],
    'precip': [2.68, 0.87, 5.31, 3.94, 4.13, 3.58, 3.62, 3.98, 2.56]
})

print(df.head())

#chart object

chart = alt.Chart(df)
alt.Chart(df).mark_point()


