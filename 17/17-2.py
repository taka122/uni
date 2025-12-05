COST = {"N": 10, "O": 15}


def make_palindrome(s):
    chars = list(s)
    cost = 0
    n = len(chars)

    for i in range(n // 2):
        j = n - 1 - i
        a, b = chars[i], chars[j]

        if a != "*" and b != "*":
            if a != b:
                return None, None  # 不可能ケース
            continue

        if a == "*" and b == "*":
            chars[i] = chars[j] = "N"  # 一番安い
            cost += COST["N"] * 2
        elif a == "*":
            chars[i] = b
            cost += COST[b]
        else:  # b == "*"
            chars[j] = a
            cost += COST[a]

    # 奇数長の中央
    if n % 2 == 1:
        mid = n // 2
        if chars[mid] == "*":
            chars[mid] = "N"
            cost += COST["N"]

    return "".join(chars), cost


print("何でも回文にします。入力してください")
s = input("入力：")

result, total = make_palindrome(s)

if result is None:
    print("回文にできません。")
else:
    print(f"変換結果：{result}")
    print("です。")
    print(f"{total}ゴールドになります。")
