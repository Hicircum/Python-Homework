import random

i = 1
while i == 1:
    S = input("请输入一个自然数：")
    exp = 0
    for c in S:
        if ord(c) < ord('0') or ord(c) > ord('9'):
            print("错误：输入内容不是自然数！")
            break
        elif exp == 0 and ord(c) == ord('0'):
            print("错误：最高位数字为0！")
            break
        else:
            exp += 1
    else:
        N = int(S)
        Nmax = 10 ** (exp + 1) - 1
        Nmin = 0
        Times = 1
        NN = random.randint(Nmin, Nmax)
        if NN == N:
            print("你输入的自然数是：", NN, "，一共猜了", Times, "次。")
        else:
            k = 1
            while k == 1:
                if NN > N:
                    print("第{}次猜测到的数字为：{}".format(Times, NN))
                    Nmax = NN
                    NN = random.randint(Nmin, Nmax)
                    Times += 1
                elif NN < N:
                    print("第{}次猜测到的数字为：{}".format(Times, NN))
                    Nmin = NN
                    NN = random.randint(Nmin, Nmax)
                    Times += 1
                else:
                    print("所猜自然数是：", NN, "，一共猜了", Times, "次。")
                    k = 0
            Judge = input("你希望再玩一次猜数游戏吗？（y/n）")
            if Judge != 'y' and Judge != 'Y':
                i = 0
