'''
Ngoại trừ vòng lặp cơ bản, Vòng lặp for còn có những tham số khác như "break" và "continue" để hỗ trợ người dùng trong việc điều chỉnh logic của một vòng lặp.
Lưu ý: Ở đây, "==" là logic trong ngôn ngữ lập trình Python được sử dụng tương ứng với phép so sánh bằng.

Vòng lặp For với lệnh break
Lệnh break trong Vòng lặp For được sử dụng để kết thúc vòng lặp ngay lập tức, ngay cả khi chưa hoàn thành vòng lặp. Khi gặp lệnh break, chương trình sẽ thoát khỏi vòng lặp và tiếp tục thực hiện các lệnh sau vòng lặp, Chúng ta sẽ sử dụng nó khi muốn dừng vòng lặp với một điều kiện cu thể.
'''

# Minh hoạ cho lệnh break
for i in range(6):
    if i == 2:
        break
    print(i)
    
'''
Vòng lặp For với lệnh continue
Lệnh continue trong Vòng lặp For được sử dụng để bỏ qua các lần lặp cụ thể và tiếp tục với lần lặp tiếp theo. Khi gặp lệnh continue, vòng lặp sẽ ngay lập tức bỏ qua các lệnh còn lại trong lần lặp hiện tại và chuyển sang lần lặp tiếp theo. Điều này hữu ích khi ta muốn bỏ qua một số điều kiện nhất định mà không cần kết thúc hoàn toàn vòng lặp.
'''

# Minh hoạ cho lệnh continue
for i in range(5):
    if i == 3:
        continue
    print(i)