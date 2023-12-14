import pandas as pd
import matplotlib.pyplot as pyplot

data = pd.read_csv("results.csv")

data.plot.line(subplots=True, x="isim")
pyplot.show()
