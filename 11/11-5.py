# n = str(input("文字列を入力してください："))
n = "wertyuiop"
for i in range (len(n)):
    if i % 2 == 0 :
        print(f"index[{i}]{n[i]}")