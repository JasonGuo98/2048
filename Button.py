#!/usr/bin/python
# -*- coding:utf-8 -*-

from tkinter import *
import random
from functools import reduce
from MoveList import move
import time  # 引入时间模块使用sleep函数

tk = Tk()
tk.title('Button')


def g():
    print('okok')


bt = Button(tk, text="输入数字",font =('KaiTi',36,'bold'),bg = 'pink', fg="green",bd=2,width=10,command = g).pack()


    
tk.mainloop()