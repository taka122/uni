class Character:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x = x
        self.y = y


# この下からメインの処理
player = Character("勇者", 5, 5)
monster = Character("オーガ", 6, 6)

while True:
    print("勇者の現在位置は({},{})です。".format(player.x, player.y))
    direction = int(input("どの方向に移動しますか？8->北、6->東、2->南、4->西、0->終了："))

    if direction == 8:
        player.move(player.x, player.y - 1)
    elif direction == 6:
        player.move(player.x + 1, player.y)
    elif direction == 2:
        player.move(player.x, player.y + 1)
    elif direction == 4:
        player.move(player.x - 1, player.y)
    elif direction == 0:
        print("探索をやめた。")
        break
    else:
        print("選択肢の中から選んでください。")
        continue

    if player.x == monster.x and player.y == monster.y:
        print("オーガが現れた！")
        break
