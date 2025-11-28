numbers_x = [10, 20, 30, 40, 10]
# print(numbers_x[len(numbers_x)])
def first_last_same(numberList):
    if (numbers_x[len(numberList) - 1]) == (numberList[0]):
        return True
    else :
        return False
print(f"与えられたリスト:{numbers_x} \n結果は", first_last_same(numbers_x))
numbers_y = [75, 65, 35, 75, 30]

print(f"与えられたリスト:{numbers_y} \n結果は", first_last_same(numbers_y))