while True:
    num = input("数値を入力：")
    if not num:
        break

    print("元の番号", num)
    g = True
    
    for i in range(len(num) // 2):
        if num[i] != num[-(i + 1)]:
            g = False
            break

    if g:
        print("回文")
    else:
       print("回文ではない")
