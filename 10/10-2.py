offenses = [29, 31, 26, 33, 22, 27, 25, 24]
print("勇者の守備力を入力してください。")
defense = int(input("勇者の守備力："))

print("なんとスライムたちは合体して体当たりしてきた！")
sum = 0

for i in range (1,len(offenses)+1):
    print(f"スライム{i}が現れた！")
    sum += offenses[i-1]
print("なんとスライムたちは合体して体当たりしてきた！")
damage = sum - defense
if(damage > 0):
    print("勇者は" + str(damage) + "のダメージを受けた！")
else :
    print("勇者はダメージを受け付けない！")