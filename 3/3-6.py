from datetime import datetime
current_year = datetime.now().year
age = int(input("今、何歳ですか？:"))
era_100 = current_year + 100 - age

print(f"あなたが 100 歳になるのは {era_100}年です")