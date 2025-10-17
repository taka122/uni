score = input("整数を入力して下さい：")
num_score = int(score)

if num_score >=90:
  print("「A+です」")
elif 89 >= num_score >=80:
  print("「Aです」")
elif 79 >= num_score >=70:
  print("「Bです」")
elif 69 >= num_score >=60:
  print("「Cです」")
else:
  print("「Fです」")