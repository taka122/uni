numbers = [4,2,7,1,8,3,6]
x = int(input("リストから探す数値を入力してください："))
result = False
for i in range (len(numbers)):

    if (numbers[i]) == x :
        result = True

if result == True :
    print(f"True. Index は {x}")
else :
    print ("False")


                