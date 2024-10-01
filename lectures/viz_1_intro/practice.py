import pandas as pd
import altair as alt

#installed vega through terminal
from vega_datasets import data as vega_data
cars = vega_data.cars()
cars.head()
