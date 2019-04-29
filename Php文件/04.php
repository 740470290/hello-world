<?php
header('Content-Type: text/html; charset=utf-8');
if($_SERVER['REQUEST_METHOD'] == 'GET'){
    $name=$_GET["name"];
    $value=$_GET["value"];
    $arr=array('tom','ming');
    if($name=='uname'){
        if(preg_match("/^[A-z0-9_]{1,11}$/",$value)){
            if(in_array($value,$arr)){
                echo '用户名已注册';
            }else{echo '用户名正确';}
        }else{
            echo '用户名应为1-11位字母数字或下划线';
        }
    }else if($name=='upass'){
        if(preg_match("/^[A-z0-9_]{8}$/",$value)){
            echo '密码正确';
        }else{
            echo '密码应为8位字母数字或下划线';
        }
    }else{
        $password=$_GET["pass"];
        if(strlen($value)==8 && $password==$value){
                echo '确认密码正确';
        }else{
            echo '确认密码错误';

        }
    }
}else{
echo '注册成功';
}
?>
