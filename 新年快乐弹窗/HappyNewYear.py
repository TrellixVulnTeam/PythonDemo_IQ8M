import os
import sys
import tkinter as tk
import random
import threading
import time


def dow():
    window = tk.Tk()
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    a = random.randrange(0, width)
    b = random.randrange(0, height)
    window.title('新年快乐')
    li = ["pink", "yellow", "plum"]
    c = random.randint(0, 2)
    print(c)
    window.geometry("480x100" + "+" + str(a) + "+" + str(b))
    tk.Label(window,
             # text='新年快乐！',  # 标签的文字
             text='Happy new year！',  # 标签的文字
             bg=li[c],  # 背景颜色
             font=('楷体', 30),  # 字体和字体大小
             width=40, height=15  # 标签长宽
             ).pack()  # 固定窗口位置
    window.mainloop()


threads = []
frequency = 98
for i in range(frequency):  # 需要的弹框数量
    if i <= frequency:
        t = threading.Thread(target=dow)
        threads.append(t)
        time.sleep(0.01)
        threads[i].start()
    else:
        time.sleep(1)
        break
