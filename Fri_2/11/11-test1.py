# 実行例に合うように空欄を埋めよ問題ミス

class Cat:
    nakigoe = "nya-"
    def naku(self):
        print(Cat.nakigoe)

mike = Cat()
nora = Cat()
mike.naku()
nora.naku()


#  (入力必須)  = "gorogoro"
mike.naku()
nora.naku()


#  (入力必須) = "sha-"
mike.naku()
nora.naku()

# % python3 quiz_cat.py出力例
# nya-
# nya-
# gorogoro
# sha-
# gorogoro