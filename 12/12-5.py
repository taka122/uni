sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

print("元のリスト：", sample_list)

count_dict = {}
for num in sample_list:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

print("カウントした結果：", count_dict)


