print("勇者の攻撃力とオークの守備力を入力してください。")
a = int(input("勇者の攻撃力:"))
b = int(input("オークの守備力:"))
c = int(input("何回攻撃しますか?:"))

if a > b :
    damage = a - b 

    for i in range(c):
        sum_damage = damage * i
        print(f"""勇者の攻撃！({i}回目)
              オークに {damage} のダメージを与えた！
              {i}回の攻撃でオークに合計 {sum_damage} のダメージを与えた！
              """)

else:
    print("「オークはダメージを受け付けない！」")