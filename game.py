import random
import tkinter.font as tkfont
import tkinter.messagebox
from tkinter import *
import time
from MoveList import move

author = "guoxiaojun"
moon_s_day_end = [2018, 9, 24, 23, 59, 59]
color = ['red', 'green', 'blue', 'yellow']
cell_color = {0: ""
                 "#EEE4DA", 2: "#fef4ea", 4: "#ede0c8", 8: "#f2b179", 16: "#f59563", 32: "#f67c5f", 64: "#f65e3b",
              128: "#edcf72", 256: "#edcc61", 512: "#edc850", 1024: "#edc53f", 2048: "#edc22e"}
num_color = {0: "#EEE4DA", 2: "#776e65", 4: "#776e65", 8: "#f9f6f2", 16: "#f9f6f2", 32: "#f9f6f2", 64: "#f9f6f2",
             128: "#f9f6f2", 256: "#f9f6f2", 512: "#f9f6f2", 1024: "#f9f6f2", 2048: "#f9f6f2"}
bg_color = "#f9f6f2"
stage_color = "#bbada0"
black_cell_color = "#EEE4DA"
_UP = 'W'
_DOWN = 'S'
_LEFT = 'A'
_RIGHT = 'D'
MAX_X = 4
MAX_Y = 4
WIDTH = 400
HEIGHT = 400
rectangle_width = WIDTH / 4
line_wideth = 5


class Game(object):
    def __init__(self):
        self.times = 0
        self.score = 0
        self.max = 0
        self.tk = Tk()
        #self.tk.iconbitmap(".\\exe.ico")
        self.canvas = Canvas(self.tk, width=WIDTH, height=HEIGHT + 35, bd=0, highlightthickness=0, bg=stage_color)
        self.text = self.canvas.create_text(0, HEIGHT + 20, anchor=SW, text=str('score: %d' % self.score),
                                            font=tkfont.Font(family='Arial Rounded MT Bold', size=30,
                                                             weight=tkfont.BOLD))
        restart = Button(self.tk, text="重新开始", font=('Arial Rounded MT Bold', 12, 'bold'), bg='orange', fg="white",
                         bd=2, width=10,
                         command=self.restart)
        restart.place(x=WIDTH - 250, y=HEIGHT)
        undo = Button(self.tk, text="后退", font=('Arial Rounded MT Bold', 12, 'bold'), bg='orange', fg="white", bd=2,
                      width=10,
                      command=self.undo)
        undo.place(x=WIDTH - 120, y=HEIGHT)
        self.tk.title("2048只在中秋特别版")
        self.tk.resizable(0, 0)
        self.tk.wm_attributes('-topmost', 1)
        self.win = False
        self.createbg()
        self.NBL = []
        for i in range(MAX_X):
            for j in range(MAX_Y):
                self.NBL.append(NumberBlock(self.canvas, self.tk, i, j))  # 初始块
        self.history = []  # 记录历史
        self.canvas.pack(side=TOP)

    def setting(self):
        self.times = 0
        self.score = 0
        self.max = 0
        self.win = False
        self.history = []  # 记录历史

    def createbg(self):
        for i in range(4):
            for j in range(4):
                self.canvas.create_rectangle(i * rectangle_width + line_wideth, j * rectangle_width + line_wideth,
                                             (i + 1) * rectangle_width - line_wideth,
                                             (j + 1) * rectangle_width - line_wideth, outline=black_cell_color,
                                             fill=black_cell_color)
        self.tk.update()

    def randomnewblock(self, max_x=MAX_X, max_y=MAX_Y):
        x, y = random.randrange(max_x), random.randrange(max_y)
        while self.NBL[y * max_x + x].num != 0:
            x, y = random.randrange(max_x), random.randrange(max_y)
        return x, y

    def newnum(self):
        x, y = self.randomnewblock()
        self.NBL[y * MAX_X + x].num = 2

    def move(self, command):
        moved = 0  # 是否有更新

        step_now = []  # 记录上一步局面
        for i in range(4):
            for j in range(4):
                step_now.append(self.NBL[i * 4 + j].num)
        self.history.append([step_now, self.score])

        if command == _UP:  # 分成每一列从上到下处理
            for i in range(MAX_X):
                up = []
                for j in range(MAX_Y):
                    up.append(self.NBL[i + j * MAX_X].num)  # 把一列上的数字存入一个长度为MAX_Y的list
                    self.NBL[i + j * MAX_X].num = 0
                new_up_and_score_and_win = move(up)
                new_up = new_up_and_score_and_win[0]
                self.score = self.score + new_up_and_score_and_win[1]
                self.win = self.win + new_up_and_score_and_win[2]
                if not new_up == up:
                    moved = moved + 1
                else:
                    pass
                for j in range(len(up)):
                    self.NBL[i + j * MAX_X].num = new_up[j]

        elif command == _DOWN:
            for i in range(MAX_X):
                up = []
                for j in range(MAX_Y):
                    up.append(self.NBL[i + (MAX_Y - j - 1) * MAX_X].num)  # 把一列上的数字存入一个长度为MAX_Y的list
                    self.NBL[i + (MAX_Y - j - 1) * MAX_X].num = 0
                new_up_and_score_and_win = move(up)
                new_up = new_up_and_score_and_win[0]
                self.score = self.score + new_up_and_score_and_win[1]
                self.win = self.win + new_up_and_score_and_win[2]
                if not new_up == up:
                    moved = moved + 1
                else:
                    pass
                for j in range(len(up)):
                    self.NBL[i + (MAX_Y - j - 1) * MAX_X].num = new_up[j]

        elif command == _LEFT:
            for i in range(MAX_X):
                up = []
                for j in range(MAX_Y):
                    up.append(self.NBL[i * MAX_X + j].num)  # 把一列上的数字存入一个长度为MAX_Y的list
                    self.NBL[i * MAX_X + j].num = 0
                new_up_and_score_and_win = move(up)
                new_up = new_up_and_score_and_win[0]
                self.score = self.score + new_up_and_score_and_win[1]
                self.win = self.win + new_up_and_score_and_win[2]
                if not new_up == up:
                    moved = moved + 1
                else:
                    pass
                for j in range(len(up)):
                    self.NBL[i * MAX_X + j].num = new_up[j]

        elif command == _RIGHT:
            for i in range(MAX_X):
                up = []
                for j in range(MAX_Y):
                    up.append(self.NBL[i * MAX_X + (MAX_Y - j - 1)].num)  # 把一列上的数字存入一个长度为MAX_Y的list
                    self.NBL[i * MAX_X + (MAX_Y - j - 1)].num = 0
                new_up_and_score_and_win = move(up)
                new_up = new_up_and_score_and_win[0]
                self.score = self.score + new_up_and_score_and_win[1]
                self.win = self.win + new_up_and_score_and_win[2]
                if not new_up == up:
                    moved = moved + 1
                else:
                    pass
                for j in range(len(up)):
                    self.NBL[i * MAX_X + (MAX_Y - j - 1)].num = new_up[j]
        return moved

    def gameover(self):
        end = True
        self.max = self.NBL[0].num
        for i in range(MAX_X):
            for j in range(MAX_Y):
                n = self.NBL[i * MAX_X + j].num
                if n > self.max:
                    self.max = n
                if n == 0:
                    return False
                if i > 0:
                    if n == self.NBL[(i - 1) * MAX_X + j].num:
                        return False
                if j > 0:
                    if n == self.NBL[i * MAX_X + j - 1].num:
                        return False
            print()
        print('GameOver!!!')
        return end

    def echo_event(self, evt):
        # 键盘事件
        moved = 0
        if evt.type == "2":
            if evt.keysym == 'Up':
                moved = self.move(_UP)
            elif evt.keysym == 'Down':
                moved = self.move(_DOWN)
            elif evt.keysym == 'Left':
                moved = self.move(_LEFT)
            elif evt.keysym == 'Right':
                moved = self.move(_RIGHT)
            if moved:
                print('moved=%d' % moved)
                self.newnum()
            self.printnum()

        if self.win:
            self.won()
        if self.gameover():
            self.end()

    def printnum(self):
        for i in range(4):
            for j in range(4):
                print("%4d" % self.NBL[i * 4 + j].num, end=' ')
                self.NBL[i * 4 + j].fresh()
            print()
        self.scorefresh()
        print('--score_now: %d--' % self.score)

    def undo(self):
        self.times += 1
        if len(self.history) == 0:
            now = time.strftime('%Y.%m.%d.%H.%M.%S', time.localtime(time.time()))
            flag = False
            is_today = now.split('.')
            print(is_today)
            for k in range(len(is_today)):
                if int(is_today[k]) <= moon_s_day_end[k]:
                    flag = True
            if flag and self.times > 10:
                my_image = PhotoImage(file='.\\group1.gif')  # 注意是两个反斜
                img = self.canvas.create_image(0, 0, anchor=NW, image=my_image)  # 这里的NW是northwest的意思，靠左上放置图片，否则是居中放置
                tkinter.messagebox.showinfo(message="又回到最初的起点，记忆中你青涩的脸~")
                self.canvas.delete(img)
                my_image = PhotoImage(file='.\\group2.gif')  # 注意是两个反斜
                img = self.canvas.create_image(0, 0, anchor=NW, image=my_image)  # 这里的NW是northwest的意思，靠左上放置图片，否则是居中放置
                tkinter.messagebox.showinfo(message="我们终于，来到了这一天~")
                self.canvas.delete(img)
                my_image = PhotoImage(file='.\\group3.gif')  # 注意是两个反斜
                img = self.canvas.create_image(0, 0, anchor=NW, image=my_image)  # 这里的NW是northwest的意思，靠左上放置图片，否则是居中放置
                tkinter.messagebox.showinfo(message="桌垫下的老照片，无数回忆连结~")
                tkinter.messagebox.showinfo(message="小伙伴们中秋快乐！")
                self.canvas.delete(img)
                self.times = 0
            return
        laststep = self.history[-1][0]
        lastscore = self.history[-1][1]
        for i in range(4):
            for j in range(4):
                # self.NBL[i * 4 + j].fresh(j,i)
                self.NBL[i * 4 + j].num = laststep[i * 4 + j]
                self.NBL[i * 4 + j].fresh()
            print()
        self.score = lastscore
        self.scorefresh()
        print('--score_now: %d--' % self.score)
        self.history.pop()

    def scorefresh(self):
        self.canvas.delete(self.text)
        self.canvas.pack()
        self.text = self.canvas.create_text(5, HEIGHT + 25, anchor=SW, text=str('得分: %d' % self.score),
                                            font=tkfont.Font(family='Arial Rounded MT Bold', size=10,
                                                             weight=tkfont.BOLD))
        self.tk.update()

    def start(self):
        self.setting()
        self.newnum()
        self.newnum()  # 两个数字才能玩
        self.printnum()
        self.canvas.bind_all("<KeyPress>", self.echo_event)
        self.tk.update()
        self.tk.mainloop()

    def end(self):
        now = time.strftime('%Y.%m.%d.%H.%M.%S', time.localtime(time.time()))
        flag = False
        is_today = now.split('.')
        print(is_today)
        for k in range(len(is_today)):
            if int(is_today[k]) <= moon_s_day_end[k]:
                flag = True
        if flag:
            messages = {64: '这么低？（怀疑的眼神@_@）老哥你是作弊了吧！！？', 128: '岂可修，明明离2048只差256，512,1024了，月亮节吃月饼了没有啊？',
                        256: '256水平的祝福也就只好是万事如意事事顺心而已，哼~', 512: '到晚上了吗？看得到月亮吗？那啥，我说今晚月光那么美，你说：',
                        1024: "烛光和月光一起流淌，我不奢求奇迹，只在此刻祝福你"}
            if self.max < 64:
                self.max = 64
            tkinter.messagebox.showinfo(title="o(￣ヘ￣o＃)", message=messages[self.max])
        else:
            tkinter.messagebox.showinfo(title="o(￣ヘ￣o＃)", message="再来一次")
        print('restart')
        self.restart()

    def won(self):
        now = time.strftime('%Y.%m.%d.%H.%M.%S', time.localtime(time.time()))
        flag = False
        is_today = now.split('.')
        print(is_today)
        for k in range(len(is_today)):
            if int(is_today[k]) <= moon_s_day_end[k]:
                flag = True

        if flag:
            if self.win:
                print('you win!')
                tkinter.messagebox.askquestion(title="(◆゜∀゜）b", message='咚咚咚，有人敲门哦！是月光哦！')
        else:
            print('you win!')
            tkinter.messagebox.askquestion(title="(◆゜∀゜）b", message='你成功了勇士！')
        self.restart()

    def restart(self):
        for i in range(MAX_X):
            for j in range(MAX_Y):
                self.NBL[i * MAX_X + j].num = 0  # 初始块
        self.start()


class NumberBlock(object):
    def __init__(self, canvas, tk, x, y):
        self.black = 0  # 边框距离
        black = self.black
        self.canvas = canvas
        self.num = 0
        self.ft = tkfont.Font(family='Arial Rounded MT Bold', size=25,
                              weight=tkfont.BOLD)  # -family, -size, -weight, -slant, -underline, or -overstrike
        # slant 斜体
        self.id = canvas.create_rectangle(y * rectangle_width + line_wideth + black,
                                          x * rectangle_width + line_wideth + black,
                                          (y + 1) * rectangle_width - line_wideth - black,
                                          (x + 1) * rectangle_width - line_wideth - black, outline=black_cell_color,
                                          fill=cell_color[self.num])

        self.text = canvas.create_text(rectangle_width / 2 + y * rectangle_width,
                                       rectangle_width / 2 + x * rectangle_width, text=str(self.num),
                                       fill=black_cell_color,
                                       font=self.ft)

        self.tk = tk
        canvas.pack()

    def fresh(self):
        self.canvas.itemconfig(self.text, text=str(self.num), fill=num_color[self.num],
                               font=self.ft)
        self.canvas.itemconfig(self.id, outline=black_cell_color,
                               fill=cell_color[self.num])  # 这个是更新的方法有小bug（已修复，更换创建时的xy位置

        # 以下是采用重新创建的方法
        # self.canvas.delete(self.text)
        # self.canvas.delete(self.id)
        # self.id = self.canvas.create_rectangle(x * rectangle_width + line_wideth + black,
        #                                   y * rectangle_width + line_wideth + black,
        #                                   (x + 1) * rectangle_width - line_wideth - black,
        #                                   (y + 1) * rectangle_width - line_wideth - black,outline = black_cell_color,
        #                                    fill=cell_color[self.num])
        # self.canvas.pack()
        # if self.num  == 0:
        #     pass
        # else:
        #     self.text = self.canvas.create_text(rectangle_width / 2 + x * rectangle_width,
        #                                     rectangle_width / 2 + y * rectangle_width, text=str(self.num),
        #                                     fill=num_color[self.num],
        #                                     font=self.ft)
        self.tk.update()


if __name__ == '__main__':
    game = Game()
    game.start()