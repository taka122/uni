offenses = [29, 31, 26, 33, 22, 27, 25, 24]

defense = int(input("勇者の守備力を入力してください："))

for i in range(1, len(offenses) + 1):
    print(f"スライム{i}が現れた！")

print("なんとスライムたちは合体して体当たりしてきた！")
damage = max(sum(offenses) - defense, 0)
result = f"勇者は{damage}のダメージを受けた！" if damage else "勇者はダメージを受け付けない！"
print(result)
