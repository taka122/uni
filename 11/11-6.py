def remove_chars(word, n):
    word = word[n:]
    print(word)

print("0 番目から n 番目までの文字列を削除します")
input_chars = input("文字列を入力してください：")
# input_chars = "qwertyuiop@"
input_n = int(input("n の値を入力してください："))
# input_n = 4
remove_chars(input_chars,input_n)