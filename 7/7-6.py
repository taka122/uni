sum = 0
number = int(input("数値を入力してください："))
digit_sum = 0
for digit in str(abs(number)):
    digit_sum += int(digit)
print("各桁の合計は：", digit_sum)
