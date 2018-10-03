# Smiling-or-Not-Smiling


Smilling or Not Smiling là project sử dụng việc nhận biết đối tượng người đang có hành động biểu cảm cười hay không . Project này giải quyết 2 bài toán là face detection và facial emotion recognition . 
Input đầu vào là một đoạn video có đối tượng là người , thuật toán sẽ đưa ra kết quả nhận biết người đó có "Smiling" or "Not Smiling" .
Các bước thực hiện :
- Đầu vào sẽ là một đoạn video . Đầu tiên thuật toán sẽ tìm đối tượng khuôn mặt trong đoạn video đó (face detection problem) . 
- Sau khi tìm được đối tượng khuôn mặt có trên video , ngay lập tức thuật toán sẽ nhận biết khuôn mặt của đối tượng đó đang có biểu cảm "Smiling " hoặc "Not Smiling" .

Face detection trong project sử dụng thuật toán haar cascade để tìm đối tượng khuôn măt con người trên trên đoạn video 
