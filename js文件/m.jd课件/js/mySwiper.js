/* 初始化值：
   Number ： 0
   String :  ""
   Object :  null
   Boolean:  false / true
*/

var mySwiper = {
  jdBox: null,
  imageBox: null,
  pointBox: null,
  points: null,
  w: 0,
  h:0,
  index: 1,
  timer: null,
  startX: 0,
  moveX: 0,
  distanceX: 0,
  isMove: false,
  countdown:3666,
  init: function () {
    this.jdBox = document.querySelector(".jd_banner");
    this.jd_header_box = document.querySelector(".jd_header_box");
    this.spans = document.querySelectorAll(".sk_time span");
    this.imageBox = this.jdBox.children[0];
    this.pointBox = this.jdBox.children[1];
    this.points = this.pointBox.querySelectorAll("li");
    this.w = this.jdBox.clientWidth;
    this.h = this.jdBox.clientHeight;
    var self = this;
    this.imageBox.addEventListener("webkitTransitionEnd", function () {
      // 处理过渡结束的逻辑self.
      if (self.index >= 9) {
        self.index = 1; // 初始化 index
        // 清除过渡
        self.clearTransition();
        // 调用位移方法 定位回去
        self.addTransform(-self.w * self.index);
      } else if (self.index <= 0) {
        self.index = 8;
        self.clearTransition();
        // 调用位移方法 定位回去
        self.addTransform(-self.w * self.index);
      }
    });
    // 启动定时器
    this.setTimer();
    self.setTimer1();
    // 绑定页面可见性改变事件 visibilitychange
    document.addEventListener('visibilitychange',function(){
      if(document.hidden){
        clearInterval(self.timer);
        self.timer = null;
      }else{
        self.setTimer();
      }
    })
    document.body.onscroll=function () {
// 滚动条距离顶部的距离 > (总高度-窗口高度)*0.8
        self.jd_header_box.style.background='rgba(201,21,35,'+document.documentElement.scrollTop/self.h+')';
        console.log(document.documentElement.scrollTop/self.h)
    }
    /* 绑定touchstart */
    this.imageBox.addEventListener("touchstart", function (e) {
      e.preventDefault();
      self.startX = e.touches[0].pageX;
      // 停止轮播
      clearInterval(self.timer);
    });
    /* 绑定touchmove */
    this.imageBox.addEventListener("touchmove", function (e) {
      // 取消上一个事件
      e.preventDefault();
      // 计算滑动距离 distanceX
      self.moveX = e.touches[0].pageX;
      self.distanceX = self.moveX - self.startX;
      // 表示 当前已滑动
      self.isMove = true;
      // 清除过渡
      self.clearTransition();
      // 重新定位位移
      self.addTransform(-self.w * self.index + self.distanceX);
    });
    /* 绑定touchend */
    this.imageBox.addEventListener("touchend", function (e) {
      // 当滑动距离超过图片 w/3 , 是有效滑动，否则滑动无效
      if (Math.abs(self.distanceX) > self.w / 3) {
        // 有效滑动逻辑 ，分两种情况 左滑 右滑
        if (self.distanceX > 0) {
          // 右滑 -> 上一张
          self.index--;
        } else if (self.distanceX < 0) {
          // 左滑 -> 下一张
          self.index++;
        }
      }
        // 调用位移和过渡
        self.addTransform(-self.w * self.index);
        self.addTransition();
      // 重新初始化 startX moveX distanceX isMove
      // 防止对下一次滑动产生影响
      self.startX = 0, self.moveX = 0, self.distanceX = 0, self.isMove = false;
        // 再次启动定时器
      self.setTimer();
    });
  },
  addTransition: function () {
    this.imageBox.style.transition = "all 1s ease-out";
    /* 兼容写法 */
    this.imageBox.style.webkitTransition = "all 1s ease-out";
  },
  // 位移方法 addTransform
  addTransform: function (x) {
    this.imageBox.style.transform = "translateX(" + x + "px)";
    this.imageBox.style.webkitTransform = "translateX(" + x + "px)";
  },
  // 清除过渡方法 clearTransition
  clearTransition: function () {
    this.imageBox.style.transition = "none";
    this.imageBox.style.webkitTransition = "none";
  },
  setTimer: function () {
    // 留住 this
    var self = this;
    this.timer = setInterval(function () {
      self.index++;
      // 调用 过渡 和 位移
      self.addTransform(-self.index * self.w);
      self.addTransition();
        // 调用setPoint()
      self.setPoint();
    }, 2000);
  },
  setTimer1: function () {
  this.timer1 = setInterval( () =>{
    var h=(this.countdown/3600|0).toString()
    var m=(this.countdown%3600/60|0).toString()
    var s=(this.countdown%60).toString()
    this.spans[0].innerHTML=h.length==1?0:h[0];
    this.spans[1].innerHTML=h.length==1&&h||h[1];
    this.spans[3].innerHTML=m.length==1?0:m[0];
    this.spans[4].innerHTML=m.length==1?m:m[1];
    this.spans[6].innerHTML=s.length==1?0:s[0];
    this.spans[7].innerHTML=s.length==1?s:s[1];
    this.countdown--;
    this.countdown==-1&&clearInterval(this.timer1)
    }, 1000);
  },
  setPoint: function () {
    for (var i = 0; i < this.points.length; i++) {
      this.points[i].className = "";
    }
    if(this.index==9){
        this.points[0].className = "now";
    }else{
        this.points[this.index - 1].className = "now";
    }
  }
};

window.onload = function () {
  mySwiper.init();
}
