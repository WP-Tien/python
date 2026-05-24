'''
1.Python là gì ?
- Một ngôn ngữ lập trình
- Có:
    - Cú pháp
    - keyword
    - rules (luật chạy)
- Do Guido van Rossum tạo ra
Ví dụ Python "thuần":

for i in range(3):
    print(i)

=> Miễn là code chạy đúng theo luật của Python, thì đó là Python.

2.Pythonic là gì?
Pythonic KHÔNG phải là ngôn ngữ
=> nó là phong cách viết code Python
Pythonic = viết code đúng tinh thần Python, dễ đọc, rõ ràng, tự nhiên
'''

# Ví dụ Python
result = []
for i in range(10):
    if i % 2 == 0:
        result.append(i)
        
print(result) # [0, 2, 4, 6, 8]

'''
f = open("data.txt")
data = f.read()
f.close()
'''

'''
Trong thiết kế class
value = obj.get_item(0)
'''

# Ví dụ Pythonic
resultPythonic = [i for i in range(10) if i % 2 == 0]
print(resultPythonic)
# Cùng kết quả
# Pythonic: ngắn hơn, rõ hơn

'''
with open("data.txt") as f:
    data = f.read()
'''

'''
Trong thiết kế class
value = obj[0] # dùng __getitem__
'''

# More example
# Không Pythonic
a=[i for i in range(10) if i%2==0 and i>3 and i<8]
# Pythonic (dễ đọc hơn)
evens = [i for i in range(10) if i % 2 == 0]
result = [i for i in evens if 3 < i < 8]

'''
- Pythonic = tuân theo những câu này
Simple is better than complex
Readability counts
Explicit is better than implicit
Errors should never pass silently
'''