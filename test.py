import random

cnt = 0
com = random.randint(1, 1000)

while True:
    cnt = +1
    user = int(input('数字を入力してください(1-100): '))
    if user == com:
        print(str(cnt)+'正解です！')
        break
    elif user < com:
        print('もっと大きい数字です')
    else:
        print('もっと小さい数字です')