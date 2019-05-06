// 为 jq  添加一个 插件
$.fn.extend({
	waterfall:function(){
		// 获取 一些 必须要知道的 参数
		
		// 为了使用方便 保存为 一个变量
		/*
			1.方法中的 this 是什么对象 取决于 该方法 由谁点出来
			这里是 由 jq对象 点出来 所有是 jq对象
			
			2.为什么要定义一个 $_this的变量
				为了 让我们知道 他是一个 jq对象 不要 跟dom弄混了
		 */ 
		// console.log(this);
		var $_this = this;

		// 总宽度
		var totalWidth = $_this.width();
		
		// 子元素宽度
		var itemWidth = $_this.children('.item').width();

		// 计算每一行 元素的个数
		//  3.1 3.8 3.9 可能除不尽,直接去掉小数即可
		var colCount = Math.floor(totalWidth/itemWidth);

		// 计算间距
		var margin = Math.floor((totalWidth-itemWidth*colCount)/(colCount+1));

		// console.log(margin);
		
		// 准备 数组 用来 保存 上一行的 高度 默认 是 没有高度的
		// 出于美观考虑 我们数组的 默认值 都是 margin
		var heightArr =[];
		// 动态 为数组 添加了 值
		for (var i = 0; i < colCount; i++) {
			// heightArr[i] = margin;
			heightArr.push(margin);
		}
		// console.log(heightArr);

		// 设置 瀑布流中 子元素的 top 以及 left
		$_this.children('.item').each(function (index,element) {
			// 将dom 转化为 jq对象
			var $_item=$(element);

			// 计算 数组中的 最小值
			// 假设 最小的索引为 0
			var minIndex =0;
			// 假设 最小的 高度为 第一个元素
			var minHeight =heightArr[0];

			// 循环高度 数组 计算 最小的 索引值 以及 最小的高度值
			for (var i = 0; i < heightArr.length; i++) {
				if (minHeight>heightArr[i]) {
					// 保存最小值
					minHeight = heightArr[i];
					//保存最小的索引
					minIndex = i;
				}
			}

			// 到这 就有了 最小的值
			$_item.css({
				top:minHeight,
				left: margin+(margin+itemWidth)*minIndex,
			})

			// 修改 高度 数组中 对应 索引的 高度值
			heightArr[minIndex] +=$_item.height();
			heightArr[minIndex] +=margin;
		})

		// 找到 高度数组的 最大值 设置给 我们的 父容器 这里是 $_this 
		
		// 定义变量
		var maxHeight = heightArr[0];

		for (var i = 0; i < heightArr.length; i++) {
			if (heightArr[i]>maxHeight) {
				maxHeight = heightArr[i];
			}
		}

		// 循环完毕 最高值 就有了
		// 将 作为 提示的 p标签 顶到下面去
		$_this.height(maxHeight);
	}
})