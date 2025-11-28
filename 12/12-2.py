class Monster:
    def __init__(self, name, hp, offense, defense):
        self.name = name
        self.hp = hp
        self.offense = offense
        self.defense = defense


# この下からメインの処理
golem = Monster("ゴーレム", 256, 123, 111)
dragon = Monster("ドラゴン", 489, 131, 99)
slime = Monster("スライム", 12, 11, 19)

monsters = []  # モンスター図鑑
monsters.append(golem)
monsters.append(dragon)
monsters.append(slime)

for index in range(len(monsters)):
    m = monsters[index]
    print("{}\t{}\t{}\t{}".format(m.name, m.hp, m.offense, m.defense))
