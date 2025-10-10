print("勇者の攻撃力とスライムの守備力を入力してください。")
brave_power = int(input("勇者の攻撃力: "))
slime_protection_power = int(input("スライムの守備力: "))

brave = {"power": brave_power}
slime = {"protection_power": slime_protection_power}

if brave["power"] > slime["protection_power"]:
    damage = brave["power"] - slime["protection_power"]
    print(f"勇者の攻撃！\nスライムに {damage} のダメージを与えた！")
else:
    print("勇者の攻撃！\nスライムはダメージを受け付けない!")
