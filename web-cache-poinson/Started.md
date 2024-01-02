# WEB-CACHE-POISON

Chúng ta sẽ tìm hiểu về lỗ hổng này :
-- Đây là một kĩ thuật nâng cao, được kẻ tấn cong khai thác hành vi của máy chủ web và bộ đệm để cung cấp phản hồi HTTP có hại cho những người người dùng khác.
+ thông thường lỗ hổng này gồm có 2 giai đoạn:
 + Gdd1: kẻ tấn công tìm ra cách gợi ra phản hồi từ máy chủ phụ trợ vô tình chứa một số tải trọng nguy hiểm.
 +Gdd2: Sau khi thành công thì hị cần đảm bảo rằng là phản hồi của họ được lưu vào bộ nhớ đệm sau đó được gửi đến các nạn nhân dự định

# Như mình biết thi web-cache sẽ là một server gần người dùng hơn so với server chính bình thường khi mà client gửi req đến web-cache-server thì nó lần đầu sẽ gửi đến server chính lấy toàn bộ dữ liệu và trả lại cho client - ở những lần sau những req khác từ client này và tất cả những client khác ở trong khu vực này thì nó có kiểm tra có thay đổi gì từ server không nếu có thì sẽ gửi một header để cập nhập nếu mà không thì sẽ trả nguyên dữ liệu này đã được lưu trữ từ trước cho các client để tránh mất thời gian và hao tổn dữ liệu do đường truyền xa và một vài nguyên nhân khác quan khác, ...
-- Thì ở đây có vẻ như là kẻ tấn công muốn thay đổi dữ liệu ở web-cache-server để gửi dữ liệu sai lệch cho các người dùng khác ^^
-- có thể dính nhiều lỗi như XSS, chèn js, chuyển hưởng ,...
-- Được ông giám đốc của Portswiger phát hiện ra vào những năm 2018 và có nhiều bug-bounty từ nó:<
# Thêm một điều quan trọng nữa là các web-cache chỉ lưu trữ dữ liệu trong một khoảng thời gian có định thôi nha
# Thông thường những cái sẽ chứa trọng tiêu đề Host
