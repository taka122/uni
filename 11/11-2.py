note = "liesandtruth"
print("合言葉はこの中に隠されている")
print("「{}」".format(note))
print("汝 真の勇者であることを示せ")
str1 = input("合言葉は（ヒント：8 文字目から）：")


found = False
for i in range(len(note) - len(str1) + 1):
    if note[i:i+len(str1)] == str1:  
        found = True
        break
print("扉の中へ入るがよい！" if found else "すぐにここから立ち去られよ！")

