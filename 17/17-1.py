import random


def fizzbuzz_value(n):
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)


status = None  # "hero_win" or "hero_lost"
win_printed = False

for n in range(1, 31):
    expected = fizzbuzz_value(n)

    if n % 2 == 1:
        # 女主人の番
        if random.random() < 0.25:
            # わざと間違える
            said = str(n) if str(n) != expected else "Fizz"
        else:
            said = expected

        print(f"女主人：{said}")

        if said != expected:
            print("女主人は間違えた！")
            print("勇者は勝負に勝った！")
            status = "hero_win"
            win_printed = True
            break
    else:
        # 勇者の番
        said = input("勇者：")

        if said != expected:
            print("勇者は間違えた！")
            print("勇者は酒場から叩き出された！")
            status = "hero_lost"
            break

else:
    status = "hero_win"

if status == "hero_win" and not win_printed:
    print("勇者は勝負に勝った！")
