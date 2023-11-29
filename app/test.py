import numpy as np
import pandas as pd
# def shape(arr):
#     newarr = []
#     for intx, x in enumerate(arr):
#         for inty, y in enumerate(arr):
#             newarr.append(arr[inty][intx])
#     shaped = np.array_split(newarr,len(arr[0]))
#     return shaped

# arr = [[-2, -43, 12],[2, 49,39]]
# print(shape(arr))
df = pd.DataFrame({'X': [0, 1, 2], 'Y': [3, 4, 5]}, index=['A', 'B', 'C'])
print(df.index.values.tolist())
print(df.T.values.tolist())