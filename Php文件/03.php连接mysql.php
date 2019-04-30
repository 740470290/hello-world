<?php
$mysql_conf = array(
    'host'    => 'localhost:3306',
    'db'      => 'test',
    'db_user' => 'root',
    'db_pwd'  => '',
    );

$mysqli = @new mysqli($mysql_conf['host'], $mysql_conf['db_user'], $mysql_conf['db_pwd']);
if ($mysqli->connect_errno) {
    die("could not connect to the database:\n" . $mysqli->connect_error);//诊断连接错误
}
$mysqli->query("set names 'utf8';");//编码转化
$select_db = $mysqli->select_db($mysql_conf['db']);
if (!$select_db) {
    die("could not connect to the db:\n" .  $mysqli->error);
}$sql = "select * from user where name = 'google';";
$res = $mysqli->query($sql);
if (!$res) {
    die("sql error:\n" . $mysqli->error);
}
 while ($row = $res->fetch_assoc()) {
        var_dump($row);
    }

$res->free();
$mysqli->close();
?>
