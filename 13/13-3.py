print("勇者はエンカウントしたモンスターを見てみた。")

# モンスターの名前とエンカウント数を読み込む辞書を初期化
monsters = {}

try:
    with open("encount.txt", "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            if len(parts) < 2:
                continue
            name = " ".join(parts[:-1])
            try:
                counts = int(parts[-1])
            except ValueError:
                continue
            monsters[name] = counts
except FileNotFoundError:
    print("encount.txt が見つかりません。")
    exit()

for name, counts in monsters.items():
    print(f"{name} {counts}")

# 最も多いエンカウント数とモンスター名を算出
if monsters:
    maxname, maxcounts = max(monsters.items(), key=lambda item: int(item[1]))
    print(f"最もエンカウント数が多いのは{maxname}で{maxcounts}回だった！")
