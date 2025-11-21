defenses = [46, 37, 88, 21, 17] #コカトリスの魔法防御力
print("魔法使いの魔力を入力してください。")
offense = int(input("魔法使いの魔力："))

for index in range(1, len(defenses)+1, 1):
    print(f"コカトリス {index} が現れた！")

print("魔法使いはブリザードを唱えた！")

def compare(hero,enemy):
    if hero > enemy:
        damage = hero - enemy
        return damage
    else :
        return False

for index in range(len(defenses)):
    n = compare(offense,defenses[index])
    if n == False:
        print(f"コカトリス{index + 1}はダメージを受け付けない！")
    else:
        print(f"コカトリス{index + 1} に {n} のダメージを与えた！")

    


    