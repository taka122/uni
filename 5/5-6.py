n = int(input("数値を入力してください："))
if (n%5 == 0) and (n%7 == 0):
    print (f"{n}は 5 と 7 の公倍数です")
else:
    print(f"{n} は公倍数ではありません")
