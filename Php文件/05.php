<?php
header('Content-Type: text/html; charset=utf-8');
$arr=array('15952119716');
if($_GET['way']=='login'){
echo '登录';
}else if($_GET['way']=='check'){
//print_r($arr);
echo json_encode($arr);
}else if($_POST['name']=='jack'){
//print_r($arr);
echo 'ok';
}else{
echo '注册';
}

?>
