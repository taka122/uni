import random
cmp_val = random.randint(0,2)
usr_val = input("0，1，2のいずれかを入力して下さい：")

if cmp_val == int(usr_val) :
   print( "あたり")
else:
   print("はずれ") 
