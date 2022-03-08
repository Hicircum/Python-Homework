import random

i, t = 1, 0
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
            if t == 0:
                NN = random.randint(10000, 9999999)
                Times = 1
            exp += 1
    else:
        N = int(S)
        if NN == N:
            print("猜对了，一共猜了", Times, "次。")
            Judge = input("继续？（y/n）")
            if Judge != 'y' and Judge != 'Y':
                i = 0
            else:
                t = 0
        else:
            k = 1
            while k == 1:
                if N < NN:
                    print("第{}次猜测：所猜数小于实际数字".format(Times))
                    Times += 1
                    t = 1
                    break
                elif N > NN:
                    print("第{}次猜测：所猜数大于实际数字".format(Times))
                    Times += 1
                    t = 1
                    break
