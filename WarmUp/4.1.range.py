'''
Một trong các hàm phổ biến và thường được sử dụng nhất khi nhắc tới vòng lặp khi không có sẵn một danh sách hoặc tệp dữ liệu là hàm range(). Hàm này hỗ trợ thực hiện một công việc N lần bằng cách trả về một iterable gồm các số từ 0 đến N - 1 khi truyền vào nó một N cụ thể.

Ví dụ minh hoạ 1: Gỉa sử, ta có TH1: a = range(3), TH2: b = range(10). Vậy các phần tử sẽ được duyệt qua trong các iterable này là:
- TH1: a = range(3) -> N = 3 -> a sẽ bao gồm các số từ 0 tới (3-1).
Do đó, ta có a = [0,1,2]
- TH2: b = range(10) -> N = 10 -> b sẽ bao gồm các số từ 0 tới (10-1).
Do đó, ta có b = [0,1,2,3,4,5,6,7,8,9]

Ngoài, hàm range() có thể được tinh chỉnh nhiều bằng nhiều tham số hơn để thuận lợi trong việc xác định bước nhảy khi duyệt qua các phần tử trong một iterable hay để xác định giá trị bắt đầu và kết thúc cho vòng lặp.
Cụ thể, hàm range() nhận vào cú pháp như sau:

                                range(begin, end, step)
                                
Trong đó,
- begin: là phần tử khởi đầu của một iterable được định nghĩa bởi hàm range(). Tham số này mặc định có giá trị là 0. Ví dụ, khi bỏ qua nó bằng cách truyền vào chỉ mỗi N như ở ví dụ trên, iterable đầu ra sẽ bắt đầu từ 0.
- end: là phần tử kết thúc của một iterable được định nghĩa bởi hàm range(). Vòng lặp sẽ kết thúc ngay trước khi nó đạt đến giá trị này. Ví dụ như khi truyền vào range(5), vòng lặp sẽ dừng tại 4 ngay khi nó đạt tới 5.
- step: là giá trị bước nhảy của vòng lặp trong một iterable. Nó quyết định khoảng cách giữa các số ở mỗi lần nhảy (mặc định của tham số này là 1). Giả sử ta có step = 2 và begin = 0 thì mỗi lần nhảy phần tử kết tiếp sẽ tăng thêm 2 đơn vị: {0;2;4...}

Ví dụ minh hoạ 2: Giả sử, ta có một iterable là range(0,7,3). Vậy khi sử dụng iterable này, thuật toán sẽ duyệt qua những giá trị nào?
- begin = 0 -> phần tử bắt đầu là 0,
- end = 7 -> phần tử kết thúc là 7 -> N = 7 -> giá trị ngay trước 7 là N - 1 = 6
- step = 3 -> Ở đây, bước nhảy là 3 nên ta sẽ duyệt qua các giá trị là {0;0+3;0+3+3} -> {0;3;6}
Kết luận: thuật toán khi sử dụng iterable là range(0,7,3) sẽ duyệt qua các phần tử là {0;3;6}
'''

# Tạo một iterable có begin = 0; end = 7; step = 3
for variable in range(0,7,3):
    
    print("Hello AI Viet Nam")
    print(f"Giá trị phần tử hiện tại là: {variable}")