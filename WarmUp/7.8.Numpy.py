# Áp dụng một hàm user-defined cho ndarray dùng np.vectorize(). Áp dụng hàm get_max() cho hai mảng ndarray
import numpy as np

# get larger value
def get_max(x, y):
    if x >= y:
        return x
    else:
        return y

# vectorize the function
# np.vectorize biến hàm get_max (chỉ xử lý 1 cặp số) thành hàm có thể áp dụng cho mảng NumPy. Nó chỉ là vòng lặp Python được viết gọn. otypes=[int] chỉ định kiểu dữ liệu đầu ra là int, nếu không có Numpy phải đoán kiểu -> chậm hơn
pair_max = np.vectorize(get_max, otypes=[int])

# create data1 and data2
data1 = np.array([5,3,8,2,7])
data2 = np.array([2,7,3,1,8])

# use pair_max as a function
out1 = pair_max(data1, data2)
print(out1) # [5 7 8 2 8]