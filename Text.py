# #!/usr/bin/python
# # -*- coding:utf-8 -*-
# from tkinter import *
# import random
# from functools import reduce
# from MoveList import move
# import time  # 引入时间模块使用sleep函数
#
# WIDTH = 400
# HEIGHT = 400
# tk = Tk()
# tk.title('Text')
#
# # text.insert(0.0, 'I111111111111111111111 Love\n')  #index = x.y的形式,x表示行，y表示列
# # text.delete(0.0,END)
# # text.insert(0.0, 'I111111111111111111111 Love\n')  #index = x.y的形式,x表示行，y表示列
#
# canvas= Canvas(tk, width=WIDTH, height=HEIGHT, bd=0, highlightthickness=0)
# text2=canvas.create_text(70,20,text = 'hello world',fill = 'red',font = ('Times',20))
# tk.update()
# tk.mainloop()

#!/usr/bin/python
# -*- coding:utf-8 -*-

from tkinter import *
import time
import random
from functools import reduce

WIDTH = 400
HEIGHT = 400

tk = Tk()

canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
canvas.pack()
canvas.create_rectangle(70,20,100,100,fill = '')
id = canvas.create_text(70,20,text = 'hello world',fill = 'red',font = ('Times',20))
# 从左至右分别是文字中心的坐标，文字内容，颜色，字体和字体大小
tk.update()
canvas.delete(id)
tk.update()
tk.mainloop()