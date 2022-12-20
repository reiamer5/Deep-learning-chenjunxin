import pandas as pd
import numpy as np

data = pd.read_csv("train.csv")["image_id"]
print(data)
data = pd.read_csv("train.csv")
is_male = np.array(data['is_male'])
male_count = 0
female_count = 0
for i in is_male:
    if i==1:
        male_count+=1
    else:
        female_count +=1

print(male_count/(male_count+female_count))
print(female_count/(male_count+female_count))