xin chào các bạn đã trở lại với chuỗi bài trên port của mình
+ thì hôm nay mình có tìm hiểu thêm một dạng bài về prototype pollution tạm dịch là ô nhiêm nguyên mẫu

+ Thường thì chúng ta sẽ gặp lỗ hổng này trong javascript và mình cũng từ bài file-storage trên cookie-hanhoan mới biết đến dạng này

## Prototype pollution là gì ?
+ đây là mọt lỗ hổng javascript cho phép kẻ tấn công thêm các thuộc tính nguyên mẫu vào đối tượng chung, sau đó các thuộc tính này có thể được kế thừa bởi các đối tượng do người dùng xác định

+ Thông thường thì lỗ hổng này sẽ được khai thác đi cùng với những các tấn công khác nhau như XSS,.. thậm chí có thể dẫn đến RCE

+ giải thích một chút về prototype và kế thừ trong js

-- thông thường js sẽ có khái niệm là object bạn cũng có thể gặp trong nhiều ngôn ngữ lập trình khác ví dụ khai báo

const hihi = {
   name : "meomeo",
   age : 18,
   isMom : false
}

thì bạn có thể truy xuất đến các giá trị của thuộc tính  đối tượng này bằng các cách:
user.username hay user['age']
* ngoài ra thì object có thể chứa value là một hàm thực thi ví dụ

const hihi = {
   name : "meomeo",
   age : 18,
   isMom : false,
   say : function (){
 console.log("meomemoemoe");
   }
}

- nói nhiều như vậy vạy thì object-prototype là gì :

> mọi đối tượng trong js ddeuf được liên kết với một loại đối tương khác gọi là nguyên mẫu của nó
trong js thì có một thuộc tính __proto__
username.__proto__
username['__proto__']
thậm chí
username.__proto__                        
username.__proto__.__proto__              
username.__proto__.__proto__.__proto__

-- lỗ hổng ở đây là chúng ta có thể thay đổi nguyên mẫu của một đối tượng ví dụ thêm một phương thức
Object.prototype.remove = function(){
  // anything in here
}