'''
    https://www.youtube.com/watch?v=lbEuqHPbK2g&t=1918s

    Đọc dữ liệu từ tệp txt, csv

    df = pd.read_csv(file_name, sep, header=None, names = [])
'''

import pandas as pd

df = pd.read_csv("sinhvien.txt", sep=",", header=None, names=["Ma", "Ten", "Lop", "QueQuan"])
print(df)

df1 = df.sort_values(['Lop'])
print(df1)

# df1 =  pd.read_excel("sinhvien.xlsx", sheet_name="Sheet1", header=None, names=["Ma", "Ten", "Lop", "QueQuan"])
# print(df1)