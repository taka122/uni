import math
def enshu(r):
    return round(2 * math.pi * r, 2)
r = int(input("半径を入力して下さい: "))
print("半径" + str(r) + "の円の円周は" + str(enshu(r)) + "です")
