function checkId() {
    var x = document.forms["del"]["userId"].value;
    var b = document.getElementsByTagName("tr").length;
    if (isNaN(x) || x < 1 || x > b-1) {
        alert("id输入错误");
        return false;
    }
}
function checkIdBelow() {
    var c = document.forms["update"]["userId"].value;
    var b = document.getElementsByTagName("tr").length;
    var x = document.forms["sub"]["say_password"].value;
    var a = document.forms["sub"]["say_user"].value;
    var str="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM";
    var pas="_1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM";
    var i,j;
    if(x.length<6 || a.length<6){
        alert("至少输入6位")
        return false;
    }
    if (isNaN(c) || c < 1 || c > b-1) {
        alert("id输入错误");
        return false;
    }
    for(i=0;i<x.length;i++){
        if(pas.indexOf(x[i])==-1){
        alert("不合法的密码");
        return false;
            }
    }
    for(j=0;j<a.length;j++){
        if(str.indexOf(a[j])==-1){
        alert("不合法的用户名");
        return false;
            }
    }
}
function checkPassword() {
    var x = document.forms["sub"]["say_password"].value;
    var a = document.forms["sub"]["say_user"].value;
    var str="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM";
    var pas="_1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM";
    var i,j;
    if(x.length<6 || a.length<6){
        alert("至少输入6位")
        return false;
    }
    for(i=0;i<x.length;i++){
        if(pas.indexOf(x[i])==-1){
        alert("不合法的密码");
        return false;
            }
    }
    for(j=0;j<a.length;j++){
        if(str.indexOf(a[j])==-1){
        alert("不合法的用户名");
        return false;
            }
    }
}
