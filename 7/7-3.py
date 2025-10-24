print("勇者の攻撃力とゴーレムの HP、守備力を入力してください。")
offense = int(input("勇者の攻撃力："))
hp = int(input("ゴーレムの HP："))
defense = int(input("ゴーレムの守備力："))
while True:
    c = int(input("[0]たたかう/[1]にげる："))
    if c == 0 :
        offense > defense
        damage = offense - defense
        hp -= damage
        print(f"ゴーレムに {damage} のダメージを与えた！\nゴーレムの HP：{hp}")
        if(hp <= 0):
            print("ゴーレムをたおした！")
            break
     
    elif c == 1:
        print("勇者は逃げ出した！")
        break
  
