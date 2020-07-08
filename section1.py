def dec2bin_ex(target): #2進数変換
    #targetを整数部と小数部に分ける
    i = int(target) #整数部
    f = target - i #小数部

    #整数部を2進数に変換
    a = []  #あまりを入れるリスト

    # 割り算の商が0になるまで
    while i != 0:
        a.append(i % 2) #余り
        i = i // 2 #商
    #要素を逆順に
    a.reverse()

    #小数部を2進数に変換
    b = [] #整数部を入れるリスト
    n = 0  #繰り返した回数

    # 2をかけた後の小数部が0になるまで
    while (f != 0):
        temp = f * 2 #小数部×2
        b.append(int(temp)) #整数部
        f = temp - int(temp) #小数部 
        n += 1
        if (n >= 10):
            break

    return a,b

def dec2hex(target):
    amari = []

    while target != 0:
        amari.append(target % 16)
        target = target // 16

    for i in range(len(amari)):
        if amari[i] == 10:
            amari[i] = 'A'
        elif amari[i] == 11:
            amari[i] = 'B'
        elif amari[i] == 12:
            amari[i] = 'C'
        elif amari[i] == 13:
            amari[i] = 'D'
        elif amari[i] == 14:
            amari[i] = 'E'
        elif amari[i] == 15:
            amari[i] = 'F'

    amari.reverse()
    return amari

def any2dec(target, m):

    n = len(target) -1
    sum = 0

    for i in range(len(target)):
        if target[i] == 'A':
            num = 10
        elif target[i] == 'B':
            num = 11
        elif target[i] == 'C':
            num = 12
        elif target[i] == 'D':
            num = 13
        elif target[i] == 'E':
            num = 14
        elif target[i] == 'F':
            num = 15
        else:
            num = int(target[i])

        sum += (m ** n)*num
        n -= 1 #参照のケタを減らして次のループに入る
    return sum
