def swap(party1, party2):
    flag = 0 #HP の交換があったかをチェックするためのフラグ
    for name, hp in party2.items():
        hp2 = hp
    for name, hp in party1.items():
        name1 = name 
        hp1   = hp
        if hp1 >= hp2 :
            party1[name1]= hp2
            flag = 1
    return flag #HP の交換が起こったかを呼び出し元に返す
    

party1 = {"勇者":32, "魔法使い":14, "僧侶":22}
party2 = {"ゴースト":15}
for name, hp in party1.items():
    print("{}の HP：{}".format(name, hp))
for name, hp in party2.items():
    print("{}の HP：{}".format(name, hp))

print("ゴーストが現れた！")
print("ゴーストはスワップを唱えた！")
flag = swap(party1, party2)

if(flag == 1):
    for name, hp in party1.items():
        print("{}の HP：{}".format(name, hp))


elif(flag == 0):
    print("何も起こらなかった！")