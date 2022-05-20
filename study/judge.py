# python 判断
"""
if 条件：
    执行动作 #缩进表示结束

if 条件：
    执行动作
else：
    执行动作

if 条件一：
    执行动作一
elif 条件二：
    执行动作二
elif 条件三：
    执行动作三
else：
    执行动作四
"""
# 举例1
# digit:数字
# lower:小写
# upper:大写
char =input("请输入：")
if char.isdigit():
    print(char,"is digit")
    print("{} is a digit".format(char))
elif char.islower():
    print("{} is lower".format(char))
elif char.isupper():
    print("{} is a upper".format(char))
else:
    print("{} is other char".format(char))

# 判断文件是否存在
import os
file=input("输入文件名：")
if os.path.exists(file):
    print(file,"exists")
else:
    print(file,"not exists")