import sys


class Human:
    cyear = 2025

    def __init__(self, arguments):
        self.name = arguments[1]
        self.yob = arguments[2]

    def calc_age(self):
        return Human.cyear - int(self.yob)

    def watch(self, target):
        self.watch = target
        print(self.name + "は" + self.watch + "を⾒ています")

    def walk(self):
        print("歩いて" + self.watch + "に着きました")


if len(sys.argv) < 4:
    print("使い方: python 11-2.py <name> <birth_year> <target>")
    sys.exit(1)

human = Human(sys.argv)
print("年齢は" + str(human.calc_age()) + "歳です")
human.watch(sys.argv[3])
human.walk()
