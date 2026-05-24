'''
   Trong lập trình nói chung và lập trình Python nói riêng, mỗi công đoạn lập trình thường sẽ được tích hợp cùng những nhiệm vụ cần phải lặp đi lặp lại nhiều lần. Và những nhiệm vụ đó đôi khi sẽ phức tạp và tốn thời gian nếu được thực hiện một cách thủ công thông thường.
   
   Đặt một trường hợp ta cần cộng các số từ 1 đến 10. Lúc này, ta gọi S là tổng cua kết quả ta cần tính (ban đầu =0). Ta sẽ thực hiện công việc này lần lượt như sau:
   
   S = 0 + 1 = 1
   S = 1 + 2 = 3
   S = 3 + 3 = 6
   S = 6 + 4 = 10
   S = 10 + 5 = 15
   S = 15 + 6 = 21
   S = 21 + 7 = 28
   S = 28 + 8 = 36
   S = 36 + 9 = 45
   S = 45 + 10 = 55
   
   Nếu thực hiện như thông thường, ta sẽ phải tự gõ ra từng dòng lệnh một tương ứng để phù hợp với 10 phép tính sao cho cộng tích luỹ đủ tới số 10: 
'''

# Cách làm thủ công
S = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
print(S) # 55

'''
    Tuy nhiên, không phải lúc nào nhiệm vụ này cũng dễ thực hiện như vậy, ta sẽ có thể phải cộng tới 100 số hay thậm chí là 1000, 1000000 số. Lúc này, việc gõ ra từng số một hay thực hiện nhiệm vụ theo một cách thủ công là không còn hợp lý. Bây giờ, ta mới tìm tới một cách tự động hoá hơn, tiện lợi để lặp các nhiệm vụ này dễ dàng, đây cũng là lúc Vòng lặp For trong Python ra đời.
    
    Vòng lặp For hỗ trợ xử lý các nhiệm vụ lặp đi lặp lại, duyệt qua các phần tử của một danh sách, mảng, hoặc bất kỳ tập hợp nào khác.
    
    Để có thể hiễu rõ qua bối cảnh hiện tại, ta cùng điểm qua một vài khái niệm phổ biến sẽ bắt gặp trong bài này như sau:
    - Element (tạm dịch: phần tử) là đối tượng hay giá trị nằm bên trong một tập hợp. Ví dụ như số 15 nằm trong tập hợp N=[15,17,0].
    - List (tạm dịch: danh sách) giống như là một danh sách thực tế chứa các phần tử, được sắp đặt theo thứ tự và được đánh số tương ứng với mỗi phần tử trong nó. Trong trường hợp của List, các phần tử của danh sách được định vị từ 0 trở đi. Ví dụ, L=[0,1,2,3,4,5,6].
    - Set (tạm dịch: tập hợp) là tập hợp của nhiều phần tử, không có bất kỳ thứ tự nhất định nào quy định các phần tử trong nó nhưng lại không cho phép bất kỳ trung lặp phần tử nào trong một Set. Ví dụ, S={0,1,2,3,4,5,6}
    - Tuple (tạm dịch: bộ) tương tự như List, là tập hợp của các phần tử tuy nhiên lại bất biến không thể thay đổi bên trong nó được. Ví dụ, T=(0,1,2,3)
    - Array (tạm dịch: mảng) cũng tương tự như List, là một dãy các phần tử được sắp xếp liền kề nhau và có thứ tự sao với các phần tử được định vị trí 0-th. Ví dụ, A=[0,1,2]
    - Variable (tạm dịch: biến) là một cái nhãn hay một bình chứa trong lập trình được sử dụng lưu trữ thông tin cho mục đích tương lai.
    - Iterable (tạm dịch: đối tượng lặp) là một đối tượng có thể lặp lại được bằng cách duyệt qua nhiều phần tử bên trong nó, ví dụ List, Set, Array... 
'''