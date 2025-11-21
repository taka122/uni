defenses = [46, 37, 88, 21, 17]


def read_offense():
    """魔力の入力を整数で受け取る。"""
    while True:
        try:
            return int(input("魔法使いの魔力："))
        except ValueError:
            print("数値で入力してください。")


def announce_enemies(values):
    for index, _ in enumerate(values, start=1):
        print(f"コカトリス {index} が現れた！")


def calculate_damage(hero, enemy):
    return max(hero - enemy, 0)


def main():
    print("魔法使いの魔力を入力してください。")
    offense = read_offense()
    announce_enemies(defenses)
    print("魔法使いはブリザードを唱えた！")

    for index, defense in enumerate(defenses, start=1):
        damage = calculate_damage(offense, defense)
        if damage == 0:
            print(f"コカトリス {index} はダメージを受け付けない！")
        else:
            print(f"コカトリス {index} に {damage} のダメージを与えた！")


if __name__ == "__main__":
    main()
