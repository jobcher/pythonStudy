# 运算符计算
#is和==区别
#is 用于判断两个变量引用对象是否为同一个(同一个内存空间)， == 用于判断引用变量的值是否相等。
a=[1,2,3]
b=a[:]
c=a
print(b is a)
print(b == a)

print(c is a)
print(c == a)

# x+=y 等同于 x=x+y
x=3
y=2
x += y
print(x)

# x-=y 等同于 x=x-y
x=3
y=2
x -= y
print(x)