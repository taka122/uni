import random

c = int(input("[0]にげる/[1]こうげき："))
if c == 1:
    rand = random.randint(0,3)
    if rand == 0 :
        print("かいしんのいちげき\nドラゴンをたおした!")
    else :
        print("こうげきにしっぱいした！\nゆうしゃたちはぜんめつした...")

elif c == 0 :
    print("にげられない！\nゆうしゃたちはぜんめつした...")