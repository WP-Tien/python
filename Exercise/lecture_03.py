"""
    Bài tập 03: Viết một chương trình để kiểm tra xem số nguyên đã cho có phải là bội số của 5 hay không ?
            Ví dụ: input: hãy nhập số nguyên 25
                output: in ra màn hình kết quả: "25 là bội số của 5"
"""

n = int(input("Hãy nhập số nguyên:"))

if n%5 == 0:
    print(n, "là bội số của 5")
else:
    print("Số bạn nhập không phải là bội số của 5")