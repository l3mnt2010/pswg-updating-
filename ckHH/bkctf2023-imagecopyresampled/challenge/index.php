<?php

if(isset($_FILES['image'])){
    
    
    $upload_dir = "./uploads/";
    $file_name = $_FILES['image']['name'];
    $file_tmp = $_FILES['image']['tmp_name'];
    $file_type = $_FILES['image']['type'];
    $file_ext = strtolower(pathinfo($file_name, PATHINFO_EXTENSION));
    $size_check = getimagesize($file_tmp);

    $allowed_ext = array('jpg', 'png', 'php');

    
    if(in_array($file_ext, $allowed_ext)){

        $image = imagecreatefromstring(file_get_contents($file_tmp));
        $cropped_image = imagecreatetruecolor(40, 40);
        imagecopyresampled($cropped_image, $image, 0, 0, 0, 0, 40, 40, imagesx($image), imagesy($image));
        $random_name = md5(uniqid(rand(), true));
        $new_file_name = $random_name . '.' . $file_ext;
        
        if ($file_ext === 'jpg' || $file_ext === 'png'  ) {
            //check size
            if ($size_check[0] < 40 || $size_check[1] < 40) { 
                echo "Ảnh của bạn hơi nhỏ. Chúng tôi cần ảnh lớn hơn 40x40 pixels\n<br>";
            } else {
                if($file_ext === 'jpg'){
                    imagejpeg($cropped_image, $upload_dir . $new_file_name);
                } else {
                    imagepng($cropped_image, $upload_dir . $new_file_name);
                }
                echo "ảnh đã được lưu tại đây\n<br>";
                echo $upload_dir;
                echo $new_file_name;  

                imagedestroy($image);
                imagedestroy($cropped_image);
            }
        } else {
            imagepng($cropped_image, $upload_dir . $new_file_name);
            echo "ảnh đã được lưu tại đây\n<br>";
            echo $upload_dir;
            echo $new_file_name;  

            imagedestroy($image);
            imagedestroy($cropped_image);
        }
    } else {        
        echo "Chỉ cho phép tải lên tệp JPG hoặc PNG và pHp ;D ? ? ?";
    }
}
?>
<!-- HTML Form để tải lên tệp -->
<h3>upload file ảnh miễn phí nhưng tôi sẽ nén chất lượng của bạn xuống 40px</h3>
<form action="" method="POST" enctype="multipart/form-data">
    <input type="file" name="image">
    <input type="submit" value="Tải Lên">
</form>