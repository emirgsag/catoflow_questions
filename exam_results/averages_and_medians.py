import pandas as pd
import numpy as np

data = pd.read_csv("results.csv")

index = 0
for name in data["isim"]:
    sum_score = 0
    score_list = []
    for i in data.drop("isim", axis=1).iloc[index]:
        sum_score += i
        score_list.append(i)
    index += 1
    average = sum_score/4
    print(f"{name}'s; \n  Average score: {average}\n  Median: {np.median(np.array(score_list))}")
