'''
Qua các phần vừa rồi, ta đã hiểu về sự quan trọng của việc đo lường bằng phần trăm. Tuy nhiên, làm thế nào ta có thể áp dụng khái niệm phần trăm khi đối mặt với các số âm ?

# Tính phần trăm với số âm
Trong học máy và học sâu, đầu ra của mô hình thường là một dãy số không chỉ có các số dương mà còn có các số âm. Nếu ta cố ý tính phần trăm trực tiếp từ các số này, kết quả nhận được có thể sẽ không đúng với thực tế.

Ví dụ dự đoán thời tiết
Giả sử ta có một mô hình dự đoán xác suất mưa (P rain) và nắng (P sun) dựa trên các yếu tố như nhiệt độ, dộ ẩm, và áp suất không khí. Đầu ra của mô hình là một dãy số:

Đầu ra của mô hình = [1.2,-0.8,3.5]

P rain = ( 2.0 / ( 2.0 - 10.0 + 0.1 ) ) * 100 = -25.32%

Vấn đề xuất hiện ở đây là P rain âm, khiến kết quả phần trăm không có ý nghĩa. Giải pháp cho vấn đề trên là softmax, một phép toán giúp ta chuyển đổi một dãy số thành một phân phối xác suất. Nó có tổng của các xác suất bằng 1, và tất nhiên có thể tính toán chính xác với số âm.
'''