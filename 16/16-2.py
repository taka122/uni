import random


target = random.randrange(1, 101)
tries = 0

print("わしが思い浮かべた数を当ててみよ。")

while tries < 5:
    guess = int(input("いくつだと思う："))
    tries += 1

    if guess == target:
        print("正解じゃ。通るが良い")
        break
    elif guess > target:
        print("もっと少ないわい")
    else:
        print("もっと大きいわい")

if tries == 5 and guess != target:
    print("愚か者め！ここは通さぬ！")
    print("勇者はドラゴンにたおされた。。。")
