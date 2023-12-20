xin chào các bạn nha ^^

Bài này chúng ta sẽ biết thêm về các hàm(method) "magic" trong php liên quan đến Insecure deserialization vulnerabilities

thường bắt đầu bằng 2 kí tự là "__"

__construct()
__destruct()
__toString()
__sleep()
__wakeup()

# __construct()
đây là một phương thức dùng để khởi tạo đối tượng phương thức này tự động được tạo ngay khi một đói tượng được tạo ra bằng từ khóa new ví dụ:

class Person {
    public $name;
    public function __construct($name) {
        $this->name = $name;
        echo "My name is $this->name";
    }
}

$person = new Person("lamhihi");
phương thức __construct() sẽ tự gán name của persion bằng name person và in ra tên;

# __destruct()

đây là phương thức được xứ lí các tác vụ cuối cùng khi một đối tượng bị hủy hoặc giải phóng bộ nhớ

class Person {
    public $name;
    public function __construct($name) {
        $this->name = $name;
    }
    public function __destruct() {
        echo "function __destruct() is executed";
    }
}

$person = new Person("Viblo");
echo "program running\n";


# __toString()
khi một đối tượng được gọi hoặc sử dụng với vai trò là chuỗi thì phương thức này sẽ được thực thi lưu ý method này luôn phải return ra một chuỗi
ví dụ:
class Person {
    public $name;
    public function __construct($name, $age) {
        $this->name = $name;
        $this->age = $age;
    }
    public function __toString() {
        return "function __toString() is executed";
    }
}

$person = new Person("John", 25);
echo $person;

