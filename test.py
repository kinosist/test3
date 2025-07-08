import random

com = random.randint(1, 100)

while True:
    user = int(input('数字を入力してください(1-1000): '))
    if user == com:
        print('正解です！')
        break
    elif user < com:
        print('もっと大きい数字です')
    else:
        print('もっと小さい数字です')
