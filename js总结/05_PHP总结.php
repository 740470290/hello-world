一、基本框架
  <?php
    header("content-type:text/html;charset=utf-8"); //定义字符类型,可以正常显示中文
    echo "apple"; //输出语句1,输出数组只显示数组名
    print_r("banana");  //输出语句2,输出数组格式为[下标]=>值,不换行
    var_dump("国庆"); //输出语句3,可见数据类型及长度,输出数组格式为[下标]=>值,自动换行
    //所有代码末尾必须加分号
  ?>
二、变量
  (一)定义变量
    $变量名=值;
  (二)变量类型
  <?php
    header("content-type:text/html;charset=utf-8");
    #1.字符串类型Stirng
      $userName="apple";
      $userSex="男";
      $school="社会大学";
      //拼接用.
      echo "我的名字是".$userName.",性别为".$userSex.",来自".$school;
    #2.布尔类型Boolean
      $bool=true;
    #3.数值类型
      #(1)整数型Int
        $num1=20;
      #(2)浮点数Float
        $num2=3.1415926;
    #4.数组Array
      #(1)索引数组 
        $arr1=array("apple",10,3.14,true);
      #(2)关联数组
        $arr2=array();
        $arr2["name"]="apple";
        $arr2["age"]="18";
        $arr2["sex"]="男";
      #(3)数组常用属性及API
        #a.输出对应下标的元素
          echo "下标为0的数组元素为".$arr1[0];
        #b.输出数组长度
          echo "数组的长度为".count($arr1);
      #(4)多维数组
        $arr3=array(1,2,3,array(11,12,13),array(21,22,23),array(31,32,33));
    #5.空Null
    #6.对象Object
    ?>
三、流程控制语句
  <?php
  #(一)for循环
    for ($i=0;$i<count($arr1);$i++){
      echo "下标为".$i."的对应数组元素为".$arr1[$i]."<br>";
    }
  #(二)foreach循环,效果同for key in
    foreach(变量名 as [$key=>]$value){
      echo "下标为".$key."的对应数组元素为".$value."<br>";
    }
    //$key为下标,如未调用可省略,$value为对应元素,多层循环嵌套不能使用相同变量名
  #(三)if...else语句
    if($key%2==0){
      echo "<li style=\"color:red;\">".$value."</li>";
    }else{
      echo "<li style=\"color:blue;\">".$value."</li>";
    }
  ?>
四、用php文件接收html网页传递的数据
  (一)接收form表单数据
    1.需要在form标签中设置传输地址,action="后台页面的地址"
    2.需要在form标签中设置数据的传递方式,分为method="get"和method="post"两种,分别通过var_dump($_GET);和var_dump($_POST);来输出,可以通过$_POST["表单控件名"]或$_GET["表单控件名"]来调用
    3.文件上传问题
      (1)需要在form标签中设置数据编码方式,enctype="multipart/form-data"
      (2)$_FILES会以二维数组形式呈现,一维数组为对应控件名,二维数组包括文件名name、文件类型type、文件临时存储路径tmp_name、文件上传状态error,显示为0表示成功和文件大小size,调用tmp_name属性时需要以$_FILES["文件上传控件的名字"]["tmp_name"]的形式
      (3)需要使用var_dump来输出$_FILES
      (4)移动上传文件,move_uploaded_file("被移动对象","目标路径"),设置路径还需要给图片命名,验证是否转移成功,可以直接打印move_uploaded_file("被移动对象","目标路径"),成功为true,失败为false,打印里的代码也会执行,所以不能写两遍
      例:$file=$_FILES["文件上传控件的名字"]["tmp_name"];
         $name=$_FILES["文件上传控件的名字"]["name"];
         var_dump(move_uploaded_file($file,"upload/".$name));
  (二)通过ajax()方法通过HTTP请求加载远程数据
    1.html网页写法
      $("#btn1").click(function(){
        $.ajax({
          url:"01_ajax.php",
          type:"post",
          data:"uname=apple",
          dataType:"json",
          success:function(data){
            console.log(data)
            $(".title").html(data["title"])
            $(".author").html("作者："+data["author"])
            $(".time").html("日期："+data["time"])
            $(".con").html(data["con"])
          }
        })
      })
      一般在事件函数的结构体内调用,通过事件函数的触发进行数据请求,url里写请求的后台页面地址,type可选择post和get两种,data为发送到后台的数据,可以为空,在后台使用$_POST或$_GET调用,dataType返回的数据类型,包括xml、html、script、json、jsonp和text,此处选择了json是为了可以对应传输,success为请求成功后的回调函数,一般在函数结构体内将后台调用的数据加载在页面上
    2.php写法
      <?php
        header("content-type:text/html;charset=utf-8");
        $article=array(
          "title"=>"十一国庆",
          "author"=>"G",
          "time"=>"2018/9/14 17:30:00",
          "con"=>"文章正式内容"
        );
        echo json_encode($article);
      ?>
      写成了json对象的形式,为了方便向对应区块输出对应内容,最后需要打印输出,若不输出就得不到数据
杂项
  1.把整个文件读入一个字符串中
    echo file_get_contents("./10_test4.json");