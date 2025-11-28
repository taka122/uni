print("そなた 名は何と申す？")
name = input("名前を入力してください：")
# name = str("はりー")
for i in range(len(name)) :
    if str(name [i]) == str("は"):
         replaced_name = name.replace("は","ひゃ")  

print("{}と申すのか 良い名じゃな".format(replaced_name))
