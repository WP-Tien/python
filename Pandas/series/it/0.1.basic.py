import pandas as pd

# Tạo 1 series
s = pd.Series([1, "John", 3.5, "Hey"])

print(s)
print(s[1:2])

# All values
print( s.values )

# Tạo 1 series with index
s2 = pd.Series([1, "Join", 3.5, "Hey"], index=["a", "b", "c", "d"])

print(s2)

# indexing b
print(s2['b'])

# All index
print(s2.index)

