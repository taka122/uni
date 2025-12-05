alphabet = "abcdefghijklmnopqrstuvwxyz .,-"

ciphertext = """qdq-gi.q-a ziatmxxitmdqibtqi-ustbi ri.qmoqrcxi.qbubu zir -ibtqi-qpqaai ripmymsqkir -ibtqi-qy dmxi ri.cnxuoi rruoumxakir -
ibtqiqzmobyqzbkii-q.qmxi -imyqzpyqzbi rixmeaki -puzmzoqai -i-qscxmbu
zaimzpir -i btq-iymbbq-a;iz -iatmxximzgi.q-a zinqiuzimzgiemgipuaouyuzmbqpimsmuzabir -ia. za -uzsiacotiimi.qbubu zj"""


def decode(text, shift):
    decoded = []
    for ch in text:
        if ch in alphabet:
            idx = alphabet.index(ch)
            decoded.append(alphabet[(idx - shift) % len(alphabet)])
        else:
            decoded.append(ch)
    return "".join(decoded)


for s in range(len(alphabet)):
    plain = decode(ciphertext, s)
    if "person" in plain:
        print(plain)
        break
