<?php
$mysql_conf = array(
    'host'    => 'localhost:3306',
    'db'      => 'test',
    'db_user' => 'root',
    'db_pwd'  => '',
    );
$mysqli = new mysqli($mysql_conf['host'], $mysql_conf['db_user'], $mysql_conf['db_pwd'],$mysql_conf['db']);
$sql = "select * from user";
$res = $mysqli->query($sql);
/*
 while ($row = $res->fetch_assoc()) {
        //var_dump($row);
        print_r($row);
        //echo json_encode($row);
    }
*/
$row=$res->fetch_all();
echo json_encode($row);
$res->free();
$mysqli->close();
?>
