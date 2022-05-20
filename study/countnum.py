# 求1-100偶数之和
# func 1
i=2
sum=0
while i<101:
    sum+=i
    i+=2
print(sum)
# func 2
sum=0
for i in range(2,101,2):
    sum+=i
print(sum)
#func 3
sum=0
for i in range(1,101):
    if i%2 == 0:
        sum+=i
print(sum)
#func 4
sum=0
for i in range(1,101):
    if i%2 == 1:
        continue
    else:
        sum+=i
print(sum)
#1到100的质数求和
sum=0
for i in range(2,101):
    for j in range(2,i):
        if i%j == 0:
            break
    else:
            sum+=i
print(sum)