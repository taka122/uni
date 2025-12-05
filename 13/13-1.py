print("勇者たちはウッドパルナの村についた。")
answer = int(input("ゲームをセーブしますか。はい->1、いいえ->0："))

if answer == 1:
    filename = input("ゲームをセーブするファイルを選んでください。：")
    location = "ウッドパルナの村"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(location)
    print(f"ファイル {filename} にセーブしました。")
elif answer == 0:
    print("勇者たちは次の村へ向かった。")
