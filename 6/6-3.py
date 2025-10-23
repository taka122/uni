#(S)自身のレベルが敵のレベルよりも 2 以上上回っている場合は敵を一撃で倒す。
#(A)自身のレベルが敵のレベルよりも上回っている場合は武器だけで敵を倒す。
#(B)自身のレベルが敵のレベルと同等か 2 だけ下回っている場合はアイテムや魔法を駆使して倒す。
#(C)自身のレベルが敵のレベルよりも 3 以上下回っている場合は倒せる見込みはないため逃げる。

def battle_outcome(hero_level: int, enemy_level: int) -> str:
    """Return the battle result symbol based on hero-enemy level difference."""
    diff = hero_level - enemy_level
 #差が2以上ならS、1ならA、0か-2ならB、それ以外（-1や-3以下）はCです。
    if diff >= 2:
        return "S"
    if diff == 1:
        return "A"
    if diff == 0 or diff == -2:
        return "B"
    return "C"
levels = range(1, 11)
header = "|" + " ".join(f"Lv {lvl}" for lvl in levels)
print(header)
print("-----+-----------------------------------------------------------")

for hero in levels:
    results = [battle_outcome(hero, enemy) for enemy in levels]
    print(f"Lv {hero}| " + " ".join(results))