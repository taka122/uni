class Monster:
    def __init__(self, name, hp, offense, defense):
        self.name = name
        self.hp = hp
        self.offense = offense
        self.defense = defense

# ここからメインの処理
golem = Monster("ゴーレム", 256, 123, 111)

print("名前：{}".format(golem.name))
print("HP：{}".format(golem.hp))
print("攻撃力：{}".format(golem.offense))
print("守備力：{}".format(golem.defense))