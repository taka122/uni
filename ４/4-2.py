medical = int(input("道具屋 「 薬草(8G)をいくつ買いますか?」:"))
pison_medical = int(input("道具屋 「 毒消し(12G)をいくつ買いますか?」:"))
master_medical = int(input("道具屋 「 万能薬(50G)をいくつ買いますか?」:"))

sum_medical = medical * 8
sum_pison_medical = pison_medical * 12
sum_master_medical = master_medical * 50
sum = sum_medical + sum_pison_medical + sum_master_medical



print(f"道具屋 「 薬草 {medical}個、毒消し {pison_medical}個、万能薬 {master_medical}個ですね。合計で {sum}G になります。」")