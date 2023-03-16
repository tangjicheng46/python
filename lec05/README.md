# 程序设计

- 顺序
- 分支(if/elif/else)
- 循环(while/for)

任何for语句，都可以用while语句替换。

证明这一点？

```
for iter in list:
    do_something(iter)
```

```
i = 0
while i < len(list):
    do_something(list[i])
    i += 1
```

语法糖。