class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


max_speed = int(input("最大速度を入力してください："))
mileage = int(input("走行距離を入力してください："))

modelX = Vehicle(max_speed, mileage)

print(f"modelX の最大速度は {modelX.max_speed}")
print(f"modelX の走行距離は {modelX.mileage}")
