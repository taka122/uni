def hanoi(n, source, auxiliary, target):
    if n == 0:
        return
    hanoi(n - 1, source, target, auxiliary)
    print(f"{n}番を{target}の杭に移動させた")
    hanoi(n - 1, auxiliary, source, target)


# 円盤3枚を A から C へ移動（B を補助に使う）
hanoi(3, "A", "B", "C")

print("パズルが解けた！")
print("神殿の扉が開いた！")
print("勇者は宝箱をあけた！")
print("勇者は天空の剣を手に入れた！")
