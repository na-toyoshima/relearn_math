def dec2bin(target): #2進数変換
    amari = []
    
    while target != 0:
        amari.append(target % 2)
        target = target // 2
        
    amari.reverse()
    return amari

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