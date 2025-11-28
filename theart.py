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
