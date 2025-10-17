print("勇者の攻撃力とゴブリンの HP、守備力を入力してください。")
brave_power = int(input("勇者の攻撃力: "))
gobu_HP = int(input("ゴブリンのHP: "))
gobu_defence= int(input("ゴブリンの防御力: "))


brave = {"power": brave_power}
gobu = {"defence": gobu_defence, "HP": gobu_HP}

if brave["power"] > gobu["defence"]:
    damage = brave["power"] - gobu["defence"]
    gobu["HP"] = gobu["HP"] - damage

if gobu["HP"] <= 0 :
    print(f"勇者の攻撃！\nゴブリンに {damage} のダメージを与えた！\nゴブリンをたおした！")
else :
    print(f"ゴブリンのHP{gobu["HP"]}")
