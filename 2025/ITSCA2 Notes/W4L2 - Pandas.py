# Pandas
import pandas as pd
import numpy as np

s = pd.Series([1, 2, 3, 4, 5])
"""0    1
   1    2
   2    3
   3    4
   4    5
   dtype: int64"""
A = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])
df = pd.DataFrame(A)
"""   0   1   2   3
   0  1   2   3   4
   1  5   6   7   8
   2  9  10  11  12"""
dictObj = {"A" : 1.0,
           "B" : pd.Timestamp("20240816"),
           "C" : pd.Series(1, index = list(range(4))),
           "D" : np.array([3]*4),
           "E" : pd.Categorical(["High", "Medium", "Low", "None"]),
           "F" : "foo"}
"""{'A': 1.0, 'B': Timestamp('2024-08-16 00:00:00'), 
'C': 0    1
     1    1
     2    1
     3    1
dtype: int64, 'D': array([3, 3, 3, 3]), 'E': ['High', 'Medium', 'Low', 'None']
Categories (4, object): ['High', 'Low', 'Medium', 'None'], 'F': 'foo'}"""
df = pd.DataFrame(dictObj)
"""     A          B  C  D       E    F
   0  1.0 2024-08-16  1  3    High  foo
   1  1.0 2024-08-16  1  3  Medium  foo
   2  1.0 2024-08-16  1  3     Low  foo
   3  1.0 2024-08-16  1  3    None  foo"""
dates = pd.date_range("20240101", periods = 6)
"""DatetimeIndex(['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04',
                  '2024-01-05', '2024-01-06'],
                 dtype='datetime64[ns]', freq='D')"""
data = np.random.randint(100, 500, size = (6, 4))
"""[[220 263 408 242]
    [104 230 429 200]
    [307 147 413 111]
    [132 180 424 470]
    [390 356 107 294]
    [463 284 115 333]]"""
df = pd.DataFrame(data, index = dates, columns = list("THWP"))
"""              T    H    W    P
   2024-01-01  221  480  195  461
   2024-01-02  127  272  145  406
   2024-01-03  280  433  187  127
   2024-01-04  402  167  319  373
   2024-01-05  408  454  433  432
   2024-01-06  341  398  198  233"""
cars = pd.read_csv("Automobile_data.csv") #Find more files @ www.kaggle.com
# print(cars.head(5))
"""       company   body-style  length engine-type  avg-mileage
   0  alfa-romero  convertible   168.8        dohc           21
   1  alfa-romero    hatchback   171.2        ohcv           19
   2         audi        sedan   176.6         ohc           24
   3         audi        sedan   176.6         ohc           18
   4         audi        sedan   177.3         ohc           19"""
# print(cars.describe())
"""           length  avg-mileage
   count   60.000000    60.000000
   mean   173.170000    25.883333
   std     14.128914     8.174146
   min    141.100000    13.000000
   25%    159.100000    19.000000
   50%    171.450000    25.000000
   75%    179.125000    31.000000
   max    208.100000    47.000000"""
df = pd.DataFrame({'A' : [1, 2, 3, 4, 5],
                   'B' : ['a', 'b', 'c', 'd', 'e']})
"""   A  B
   0  1  a
   1  2  b
   2  3  c
   3  4  d
   4  5  e"""
gdf1 = df['A']
"""0    1
   1    2
   2    3
   3    4
   4    5
   Name: A, dtype: int64"""
gdf2 = df[['A', 'B']]
"""   A  B
   0  1  a
   1  2  b
   2  3  c
   3  4  d
   4  5  e"""
gdf3 = df.loc[0]
print(gdf3)
"""A    1
   B    a
   Name: 0, dtype: object"""