# Smiling-or-Not-Smiling


Smilling or Not Smiling là project sử dụng việc nhận biết đối tượng người đang có hành động biểu cảm cười hay không . Project này giải quyết 2 bài toán là face detection và facial emotion recognition . 
Input đầu vào là một đoạn video có đối tượng là người , thuật toán sẽ đưa ra kết quả nhận biết người đó có "Smiling" or "Not Smiling" .
Các bước thực hiện :
- Đầu vào sẽ là một đoạn video . Đầu tiên thuật toán sẽ tìm đối tượng khuôn mặt trong đoạn video đó (face detection problem) . 
- Sau khi tìm được đối tượng khuôn mặt có trên video , ngay lập tức thuật toán sẽ nhận biết khuôn mặt của đối tượng đó đang có biểu cảm "Smiling " hoặc "Not Smiling" .

Face detection trong project sử dụng thuật toán haar cascade để tìm đối tượng khuôn măt con người trên trên đoạn video . Để viết được thuật toán đó cần phải tạo ra một tập train .Trong tập train gốm hình ảnh khuôn mặt con người . Sau khi đã train xong kết quả là một tập file xml (trong project này là file haarcascade_frontface.xml) . Sau khi đã có tập train này thuật toán có thể nhận biết được khuôn mặt người trên bất kì video hay image .

Facical emotion recognize là bài toán đưa ra kết quả biểu cảm khuôn mặt của người , vì hardware không đủ tốt để train tất cả cảm xúc người nên chỉ train "smiling" biểu cảm con người . Thuật toán dùng để giải cho bài toán này là convolution neural network (CNN) .Loại architecture CNN để giải bài toán này là LeNet-5 . Dùng thuật toán này giúp cho việc học biểu cảm con người (biểu cảm ở đây là "Smiling" or "Not Smiling") . Data để train thuật toán này bao gồm 2 tập "Smiling" (là những tập gồm biểu cảm cười của con người) và tập "Not Smiling" (là những tập không cười ) .

Nhiệm vụ trong nhóm project :
- Kiệt tìm kiếm hình ảnh và cắt ảnh cho dữ liệu face detection
- Hoàng tìm kiếm hình ảnh và cắt ảnh cho dữ liệu facial emotion recognize .
- A.Luân viết thuật cho haar cascade
- Cường viết thuật cho Facial emotion recognize .
