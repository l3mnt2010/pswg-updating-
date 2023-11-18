Đây là lab yêu cầu về query là sử dụng để lấy dữ liệu trong database

+ Có vẻ như tác giả đã sử dụng lệnh như này : SELECT items from table where category = ${query} RELEASE 1;
    - Vì vậy cho nên là sẽ chỉ lấy 1 <tức là đã phát hành còn 2 hoặc khác 2 sẽ là lấy cả chưa phát hành> 
    - Yêu cầu đưa ra là lấy cả chưa phát hành
    - Vì vậy nếu ta chọn 1 vật phẩm fillter thì câu truy vẫn sẽ ra như sau :

                                        SELECT items from table where category = 'Gifts' RELEASE 1; sẽ trả ra Gitf đã phát hành;

    + Giải pháp đưa ra là BYPass nó như sau <query = 'Gifts'OR 1=1 --'> ta sẽ comment lại hết tất cả phần đằng sau và từ đó câu truy vấn trở thành :

                                        SELECT items from table where category = 'Gifts'OR 1=1 --' RELEASE 1; sẽ trả ra Gitf đã phát hành và chưa phát hành;

       @@ Vậy là đã thành công chúc bạn thành công :)) WU By l3mh0cr3d