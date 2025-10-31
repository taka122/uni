#(S)自身のレベルが敵のレベルよりも 2 以上上回っている場合は敵を一撃で倒す。
#(A)自身のレベルが敵のレベルよりも上回っている場合は武器だけで敵を倒す。
#(B)自身のレベルが敵のレベルと同等か 2 だけ下回っている場合はアイテムや魔法を駆使して倒す。
#(C)自身のレベルが敵のレベルよりも 3 以上下回っている場合は倒せる見込みはないため逃げる。

levels = range(1, 11)
header = "|" + " ".join(f"Lv {lvl}" for lvl in levels)
print(header)
print("-----+-----------------------------------------------------------")

for hero in levels:
    results = []
    for enemy in levels:
        diff = hero - enemy
        if diff >= 2:
            result = "S"
        elif diff == 1:
            result = "A"
        elif diff == 0 or diff == -2:
            result = "B"
        else:
            result = "C"
        results.append(result)
    print(f"Lv {hero}| " + " ".join(results))

