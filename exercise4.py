# temperatures = [35,25,26,23,29,27,38]
# average = sum(temperatures)/len(temperatures)

# for i, temp in enumerate(temperatures):
#     print(f"วันที่ {i+1} มีค่า {temp} องศา")

# def classify_temp(t, avg):
#     return "ร้อน" if t > avg else "เย็น"

# print(classify_temp(20, average))

import pandas as pd

df = pd.read_csv("/workspaces/deb-pre-class-workshop/data_folder/pokemon.csv")
print(df.head())