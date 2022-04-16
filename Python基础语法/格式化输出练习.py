"""
我的名字叫小明,请多多关照！
我的学号是 000001
苹果单价是8.5元/斤，购买了5斤，需要支付42.50元
数据是10.01%
"""

name = "小明"
print("我的名字叫%s,请多多关照！" % name)

num = 1
print("我的学号是 %.6d" % num)

price = 8.5
weight = 5
money = price * weight
print("苹果单价是%.1f元/斤，购买了%d斤，需要支付%.2f元" % (price, weight, money))

scale = 10.01
print("数据是%.2f%%" % scale)
