'''
Một cách hiệu quả để giải quyết overflow là Stable Softmax. Thay vì thực hiện phép toán trực tiếp trên các số, ta điều chỉnh chúng trước khi tính toán để tránh các giá trị quá lớn hoặc quá nhỏ.
'''

import math

# Given three values
v1 = 1.0
v2 = 1001.0
v3 = 1002.0

# get max
max_value = v3

# Compute stable softmax
e_v1 = math.exp(v1 - max_value)
e_v2 = math.exp(v2 - max_value)
e_v3 = math.exp(v3 - max_value)

total = e_v1 + e_v2 + e_v3

s1 = e_v1/total
s2 = e_v2/total
s3 = e_v3/total

# Print out
print(f"{s1:.5f} {s2:.5f} {s3:.5f}") # 0.00000 0.26894 0.73106

'''
    Ưu điểm
    - Tránh overflow và underflow trong tính toán.
    - Kết quả ổn định, không làm thay đổi phân phối xác suất.


    Kết luận
    Trong bài này, ta đã tìm hiểu:
    - Hiện tượng overflow và underflow trong tính toán.
    - Cách Softmax chuyển đổi đầu ra mô hình thành xác suất.
    - Ứng dụng Stable Softmax để đảm bảo tính ổn định và chính xác.
    
    Ghi nhớ: Stable Softmax là bước xử lý thiết yếu trong học sâu, giúp tránh lỗi số học và đảm bảo mô hình dự đoán ổn định hơn.
'''

