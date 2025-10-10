#name = input("名前は？: ")
#print("こんにちは, " + name + "!!")
#print(f"こんにちは, {name}!!")

# 1) 1人＝辞書（キー＝項目名）
student1 = {"id": 1, "name": "長野一郎", "kokugo": 48, "math": 72, "english": 88}
student2 = {"id": 2, "name": "山口次子", "kokugo": 93, "math": 84, "english": 65}
student3 = {"id": 3, "name": "福井三太", "kokugo": 75, "math": 91, "english": 73}

# 2) リストにまとめる
meibo = [student1, student2, student3]

# 3) ID→辞書の索引を作る
by_id = {s["id"]: s for s in meibo}

# 4) IDで呼ぶ
print(by_id[3]["name"])   # → 福井三太