'''
Một trong những người tạo ra softmax là ông Geoffrey Hinton, một nhà nghiên cưu AI nổi tiếng. Hàm softmax do ông tạo ra sử dụng rộng rãi trong các mô hình học sâu để đưa ra dự đoán xác suất chính xác cho nhiều lớp.

'''

#  Ứng dụng trong python
import math

# Given three values
v1 = 1.0
v2 = 2.0
v3 = 3.0

# Compute softmax
total = math.exp(v1) + math.exp(v2) + math.exp(v3)

s1 = math.exp(v1) / total
s2 = math.exp(v2) / total
s3 = math.exp(v3) / total

# Print out
print(f"{s1:.5f} {s2:.5f} {s3:.5f}") # 0.09003 0.24473 0.66524

'''
Softmax giúp ta chuyển đổi các đầu ra thành xác suất, dễ hiểu và dễ so sánh.
Tuy nhiên, nó dễ ảnh hưởng bởi các giá trị cực lớn, gây ra hiện tượng tràn số (overflow) trong quá trình tính toán
'''

# Ngoài lề
# So sánh với **
# math.exp(x) # e^x
# math.e ** x # cũng là e^x
# math.exp(x) chính xác và tối ưu hơn cho số mũ tự nhiên