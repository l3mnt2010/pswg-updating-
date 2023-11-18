
++ Để giải quyết bài lab, hãy thực hiện một cuộc tấn công SQL SQL đăng nhập vào ứng dụng với tư cách là administratorngười dùng.
++ Vì vậy ta có thể đoán rằng câu truy vấn SQL như sau : 
                                        SELECT * FROM users WHERE username = ${POST['USERNAME]} AND password = ${POST['PASSWD']};

++ Mà ta lại biết được username là administrator vì vậy nếu như post của username là administrator' -- hay là administrator' OR 1=1 -- còn mật khẩu tùy ý @@
++ Lúc này câu truy vấn của bạn sẽ trở thành như này :
                                        SELECT * FROM users WHERE username = 'administrator' -- AND password = 'blabla@@@@'
                                        hay là như này SELECT * FROM users WHERE username = 'administrator' OR 1=1 -- AND password = 'blabla@@@@'
                                        thì nó cũng đúng đúng không nhưng mà mấu chốt của đăng nhập thì thường sẽ trả ra 1 object user nên ta sẽ dùng cách 
                                         1 để bypass đăng nhập ... vậy là xong
                                         à trường hợp này chắc họ chỉ check quoa loa nên cả 2 đều được :)))

@@ Vậy là đã thành công chúc bạn thành công :)) WU By l3mh0cr3d