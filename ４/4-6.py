import math 

a = float(input("AB の長さを入力してください："))
b = float(input("BC の長さを入力してください："))
c = float(input("CA の長さを入力してください："))

s = (a + b + c)/ 2

print(math.sqrt(s * (s - a) * (s - b) * (s - c)))
##S = \sqrt{s(s - a)(s - b)(s - c)}