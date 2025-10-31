def	multiplication_or_sum(num1,	num2):
    multiplication = num1 * num2
    sum = num1 + num2
    if multiplication <= 1000:
        return multiplication
    else :
        return sum



num1	=	int(input("1 つ目の数字："))
num2	=	int(input("2 つ目の数字："))
result	=	multiplication_or_sum(num1,	num2)
print("結果は",	result)