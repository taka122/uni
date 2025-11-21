def heal(hps):
    for i  in range(len((hps))):
        hps[i] += 80
    return hps

hps = [0,0,0,0]

for i in range(len(hps)):
    hps[i] = int(input(f"プレイヤ{i+1}の HP："))

print("僧侶はヒールを唱えた！")
for i in range(len(hps)):
    print(f"プレイヤ {i+1} の HP が 80 回復した！")

heal(hps)
for i in range(len(hps)):
    print(f"プレイヤ {i+1} の HP：{hps[i]}")
