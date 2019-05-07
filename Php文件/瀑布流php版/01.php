<?php
header('Content-Type: text/html; charset=utf-8');
$json=file_get_contents('./info/data.json');
echo $json;
//echo json_decode($json);
//$parr=json_decode($json);
/*
//从数组中取10个随机下标
$randArr=array_rand($parr,10);
$arr=array();
for($i=0;$i<count($randArr);$i++){
    $randIndex=$randArr[$i];
    array_push($arr,$parr[$randIndex]);
}
echo json_encode($arr);
*/
?>
