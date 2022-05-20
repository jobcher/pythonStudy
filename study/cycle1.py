# python for循环
# 用for循环来实现 1-100之间能被 5整除,同时能被3整除的数的和
sum=0
for i in range(1,101):
    if i%5 == 0 and i%3 == 0:
        sum+=i
print(sum)