original_money = 1500
original_protection_power = 8
shied = {"cost":600,"protection power":25}

print("勇者は鉄の盾を購入した。")

current_money = original_money - shied["cost"]
current_protection_power = original_protection_power + shied["protection power"]

print(f"勇者の所持金は{current_money} G になった")
print(f"勇者の防御力が {original_protection_power} から 33 に上がった！")