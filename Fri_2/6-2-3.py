while True:
    meter = float(input("長さは何cm？"))
    if meter <= 0 :
       print("変換を終了します")
       break
    else:
       yard = meter / 91.4
       print(f"{meter},cmは, {yard}, ydです")
      