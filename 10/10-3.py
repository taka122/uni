map = [
    0, 0, 0, 0, 0, 0, 0,
    0, 1, 2, 0, 0, 0, 0,
    0, 2, 0, 0, 0, 0, 2,
    0, 0, 0, 0, 0, 2, 1,
    0, 0, 0, 0, 0, 0, 2,
    0, 0, 2, 1, 2, 0, 0,
    0, 0, 0, 0, 2, 0, 0,
    0, 0, 0, 0, 2, 0, 0,
    0, 0, 0, 0, 1, 2, 0,
]
print("-------")
for i in range(0, 7 * 9, 1):
    cell = map[i]
    if cell == 0:
        print(" ", end="")
    elif cell == 1:
        print("*", end="")
    else:
        print("x", end="")

    if (i + 1) % 7 == 0:
        print("")
print("-------")

print("どこを調べますか？")
x = int(input("横の座標（0 から 6 まで）："))
y = int(input("縦の座標（0 から 8 まで）："))
print("勇者は(" + str(x) + ", " + str(y) + ")を調べた。")

if 0 <= x < 7 and 0 <= y < len(map) // 7:
    tile = map[y * 7 + x]
    if tile == 1:
        print("なんと小さな宝石を見つけた！")
    elif tile == 2:
        print("グールが現れた！")
    else:
        print("しかし何も見つからなかった。")
else:
    print("範囲外の座標です。")
