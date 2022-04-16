"""
请输入苹果的单价：10
请输入要购买的重量:10
总金额为100.00 元
"""

price = float(input("请输入苹果的单价："))
weiht = float(input("请输入要购买的重量:"))
# money = price * weiht
print("总金额为%.2f 元" % (price * weiht))
# %f      小数格式化输出
# %d      整数格式化输出
# %s      字符串格式化输出
# %.2f    格式化输出2个小数
