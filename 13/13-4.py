def sold_count(count):
    if count >= 11:
        return count - 10
    if 5 <= count <= 10:
        return count - 5
    return 0


sales = []

with open("item.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        name, count_str = line.split(",")
        count = int(count_str)
        sold = sold_count(count)
        if sold > 0:
            msg = f"{name}を {sold} 個売り払った"
            print(msg)
            sales.append(msg)

with open("sold.txt", "w", encoding="utf-8") as f:
    for msg in sales:
        f.write(msg + "\n")
