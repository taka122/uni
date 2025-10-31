import random

hands = {1: "グー", 2: "チョキ", 3: "パー"}

def compare(u1, enemy_seed):
    if enemy_seed <= 10:
        u2 = 1
    elif enemy_seed <= 20:
        u2 = 2
    else:
        u2 = 3

    if u1 == u2:
        return "あいこ"
    elif (u1 == 1 and u2 == 2) or \
         (u1 == 2 and u2 == 3) or \
         (u1 == 3 and u2 == 1):
        return f"勇者の{hands[u1]}の勝ち"
    else:
        return f"村人の{hands[u2]}の勝ち"

hero = int(input("勇者の手を入力してください．グーは 1，チョキは 2，パーは 3："))
villager_seed = random.randint(0, 30)
print(compare(hero, villager_seed))
