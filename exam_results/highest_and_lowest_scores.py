import pandas as pd

data = pd.read_csv("results.csv")

for i in data.drop("isim", axis=1):
    print(f"Highest {i} score is {data.loc[data[i] == data[i].max()]['isim'].to_string(index=False)}\'s one "
          f"with {data[i].max()}.")
    print(f"Lowest {i} score is {data.loc[data[i] == data[i].min()]['isim'].to_string(index=False)}\'s one "
          f"with {data[i].min()}.")
