# 1.判断一个数是否是水仙花数, 水仙花数是一个三位数,
# 三位数的每一位的三次方的和还等于这个数.
# 那这个数就是一个水仙花数,
# 例如: 153 = 1**3 + 5**3 + 3**3

# num = input("请输入一个三位数:")
# if len(num) == 3:
#     result = int(num[0])**3 + int(num[1])**3 + int(num[2])**3
#     if int(num) == result:
#         print("是一个水仙花数")
#     else:
#         print("不是水仙花数")
# else:
#     print("亲, 你输入的不是三位数")
#

# 3.完成彩票36选7的功能. 从36个数中随机的产生7个数. 最终获取到7个不重复的数据作为最终的开奖结果.
# 随机数:
# from random import randint
#
# s = set()
# while len(s) < 7:
#     n = randint(1, 33)
#     s.add(n)
# print(s)


# 税务部门征收所得税. 规定如下: 
#         1). 收入在2000以下的. 免征.
#         2). 收入在2000-4000的, 超过2000部分要征收3%的税. 
#         3). 收入在4000-6000的, 超过4000部分要征收5%的税.
#         4). 收入在6000-10000的, 超过6000部分要征收8%的税.  
#         4). 收入在10000以上的, 超过部分征收20%的税. 
#     注, 如果一个人的收入是8000, 那么他要交2000到4000的税加上4000到6000的税加上6000到8000的税. 
#         收入 = 8000-(4000-2000)*3%-(6000-4000)*4%-(8000-6000)*8%
# 让用户输入它的工资, 计算最终用户拿到手是多少钱.

salary = int(input("请输入你的工资:"))
if salary <= 2000:
    print("你不用交税")
    print("你的实际收入是%s" % salary)
elif salary <= 4000:
    tax = (salary - 2000)*0.03
    print("你要交%s税 " % tax)
    print("你的实际收入是:%s" % (salary-tax))
elif salary <= 6000:
    tax = 2000* 0.03 + (salary-4000) * 0.05
    print("你要交%s税 " % tax)
    print("你的实际收入是:%s" % (salary - tax))
elif salary <= 10000:
    tax = 2000* 0.03 +  2000*0.05 +(salary - 6000) * 0.08
    print("你要交%s税 " % tax)
    print("你的实际收入是:%s" % (salary - tax))
else:
    tax = 2000 * 0.03 + 2000 * 0.05 + 4000 * 0.08 + (salary-10000) * 0.20
    print("你要交%s税 " % tax)
    print("你的实际收入是:%s" % (salary - tax))




# a = 10
# b = 20
# c = a
# a = b
# b = c
# print(a, b)

# a = 10
# b = 20
# a, b = b, a
# print(a, b)

# 大学课程中的数据结构-严蔚敏.
# 冒泡排序(使用两两相邻的数进行比较.) 快排, 插入排序, 归并排序, 堆排序, 希尔排序
#       0    1    2    3   4     5    6
lst = [175, 160, 185, 134, 196, 128, 155, 170, 185, 189, 236]
for j in range(len(lst)):
    # 第i个和第i+1个比较
    for i in range(len(lst)-1): # 自己优化
        if lst[i] > lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]
print(lst)













