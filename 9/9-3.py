print("魔法使いの魔力とゴーレムの HP、魔法防御力を入力してください。")
offense = int(input("魔法使いの魔力："))
hp = int(input("ゴーレムの HP："))
defense = int(input("ゴーレムの魔法防御力："))

def fire (offence,defense):
    if offence > defense :
        damage = offence - defense
        return damage
    else :
        damage = 1 
        return damage 
while hp >= 0:
    c = int(input("[0]魔法/[1]にげる:"))
    if c == 0 :
        print("魔法使いはファイアを唱えた！")
        damage = fire(offense,defense)
        hp = hp - damage
        print(f"ゴーレムに{damage}のダメージを与えた！\nゴーレムの HP:{hp}")
        if hp <= 0:
            print("ゴーレムをたおした！")
            break
    elif c == 1:
        print("勇者は逃げた")
        break
