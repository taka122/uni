print("勇者の最大 HP と現在の HP を入力してください。")
max_hp = 100#int(input("勇者の最大 HP："))
hp = 5#int(input("現在の HP："))
while hp < max_hp:
    hp += 8
    if hp > max_hp:
        hp = max_hp
    print(f"僧侶はホイミを唱えた\n勇者の HP が {hp} になった")