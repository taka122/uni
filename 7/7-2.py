#勇者の攻撃力とガーゴイルの HP、守備力を入力してください。
power =int(input("勇者の攻撃力:"))
hp = int(input("ガーゴイルの HP:"))
defence = int(input("ガーゴイルの防御力:"))
while True :
    if power > defence :
        damage = power - defence
        hp = hp - damage
        print(f"ガーゴイルに {damage} のダメージを与えた！\nガーゴイルの HP:{hp}")
        if hp <= 0 :
            print("ガーゴリルをたおした！")
            break