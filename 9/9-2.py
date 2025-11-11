print("金の剣と銀の剣の攻撃力を入力してください。")

offense1 = int(input("金の剣の攻撃力："))
offense2 = int(input("銀の剣の攻撃力："))
#合成した武器の攻撃力=高い方の攻撃力×1.2+低い方の攻撃力×1.0 (1)
def synthesize(offense1, offense2):
    if offense1 > offense2:
        offense3 = offense1 * 1.2 + offense2
    else:
        offense3 = offense2 * 1.2 + offense1
    return offense3
print("勇者は金の剣と銀の剣を合成の箱に入れた。")
print("合成の剣を手に入れた！")
print("勇者は金の剣と銀の剣を合成の箱に入れた。")
offense3 = synthesize(offense1, offense2)
print("合成の剣の攻撃力：" + str(int(offense3)))

