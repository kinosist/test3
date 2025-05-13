import random

com = random.randint(1, 100)

count = 0
while True:
    count = count + 1
    user = int(input('数字を入力してください(1-100): '))
    if user == com:
        print('正解です！')
        print(count, '回目で正解しました')
        break
    elif user < com:
        print('もっと大きい数字です')
    else:
        print('もっと小さい数字です')