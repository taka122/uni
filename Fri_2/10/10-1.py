# 以下の文字列から文字列”art”を検索し，”art”に続く文字列を表示するプログラムを作成せよ．
# Someyearsagonevermindhowlongpreciselyhavinglittleornomoneyinmypurseandnothingp
# articulartointerestmeonshoreIthoughtIwouldsailaboutalittleandseethewaterypartofthewo
# rld
# % python3 theart.py
# iculartointerestmeonshoreIthoughtIwouldsailaboutalittleandseethewaterypartoftheworld
# 問題文

# text = """Someyearsagonevermindhowlongpreciselyhavinglittleornomoneyinmypurseandnothingp
# articulartointerestmeonshoreIthoughtIwouldsailaboutalittleandseethewaterypartofthewo
# rld"""

# # 改行を取り除く
# text = text.replace("\n", "")

# target = "art"
# index = text.find(target)

# if index != -1:
#     # "art" の直後から最後までを切り出す
#     result = text[index + len(target):]
#     print(result)
# else:
#     print("art は見つかりませんでした。")
#提出

text = """Someyearsagonevermindhowlongpreciselyhavinglittleornomoneyinmypurseandnothingp
articulartointerestmeonshoreIthoughtIwouldsailaboutalittleandseethewaterypartofthewo
rld"""

text = text.replace("\n", "")

target = "art"
index = text.find(target)

if index == -1:
    print("art は見つかりませんでした。")
else:
    print(text[index + len(target):])


