# python流程控制

- 顺序结构
- 判断结构if/elif/else
- 循环结构

## 循环
### while循环 
和C语言的while类似。  
break：终止循环  
continue：继续执行下一次循环  

### for循环
和C语言，完全不同。  
```
for 变量x in 序列对象：  
    循环体
```

### range
range(start, end)，生成前闭后开[start, end)的可迭代对象。  
range(end)，表示range(0, end)  

for循环可以迭代【可迭代对象】，【可迭代对象】是可以被for循环迭代的。  
目前，用到的两种可迭代对象：序列对象（字符串、列表）、range生成的对象  

# python的类型
数值（整数、浮点数、复数）、字符串、列表  
None  
bool类型   (True、False)  运算符号：or/and/not

# python的常用关键字  
in： 
- for循环里面
- 判断一个元素，是否在一个序列对象里面。返回一个bool变量。
