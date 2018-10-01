#!/usr/bin/python
# -*- coding:utf-8 -*-

def move(list):
    # for n in list:
    #     print(n,end=" ")
    # print()
    score = 0
    win = False
    L = len(list)
    up = []
    new_up = []
    for i in range(L):
        up.append(list[i])
    p=0
    newPos=[x for x in range(L)]#默认无移动
    i = 0
    while i < L:
        if up[i] == 0:
            i = i + 1
            pass
        else:
            local_n = up[i]
            newPos[i] = p
            p=p+1
            if i == L - 1:
                new_up.append(local_n)
            i = i + 1
            while (i < L):
                if up[i] == 0:
                    if i == L - 1:  # 最后还是没有找到
                        new_up.append(local_n)
                    pass
                elif up[i] == local_n:
                    new_up.append(local_n * 2)
                    newPos[i]=p-1
                    if local_n == 1024:
                        win = True
                    score = score + local_n*2
                    i = i + 1
                    break
                else:
                    new_up.append(local_n)
                    break
                i = i + 1
    for i in range(L)[len(new_up):]:
        new_up.append(0)
    # print('len(new_up)=%d'%len(new_up))
    return [new_up,score,win,newPos]


if __name__ == '__main__':
    list = [0, 0, 1, 2, 1, 1, 2, 2, 2]
    print(list)
    print()
    for n in move(list):
        print(n, end=" ")
    print()
