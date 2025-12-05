import random


def create_target():
    # 1〜9の異なる数字4桁を生成
    return "".join(random.sample("123456789", 4))


def count_hit_blow(guess, target):
    hit = sum(g == t for g, t in zip(guess, target))
    blow = sum(g in target for g in guess) - hit
    return hit, blow


target = create_target()
tries = 0

print("私の思い浮かべた数字を当てることができたら、次に進むべき道を示しましょう。")

while tries < 5:
    guess = input("いくつだと思いますか：")

    # 入力チェック: 1〜9の異なる数字4桁のみ許可
    if not (guess.isdigit() and len(guess) == 4 and "0" not in guess and len(set(guess)) == 4):
        print("1〜9の異なる数字4桁で答えてください。")
        continue

    tries += 1

    if guess == target:
        print("正解です。次に進むべき道はあちらです。")
        print("光の階段があらわれた！")
        break

    hit, blow = count_hit_blow(guess, target)
    print(f"HITは{hit}、BLOWは{blow}です")

if tries == 5 and guess != target:
    print("あなたはまだここを通る資格ないようです。")
    print("勇者は洞窟の入り口まで戻された。。。")
