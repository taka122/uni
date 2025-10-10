levels = [
    int(input("勇者のレベル: ")),
    int(input("戦士のレベル: ")),
    int(input("魔法使いのレベル: ")),
    int(input("僧侶のレベル: ")),
]

print(f"パーティの中で最もレベルの高いメンバのレベルは {max(levels)} です。")
