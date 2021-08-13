class Iron:

    melting = 1538
    evaporation = 2862

    def temperatura(self,t):
        if temp < self.melting:
            print("замерзание")
        elif temp >= self.evaporation:
            print("плавление")
        else:
            print("испарение")

iron = Iron()

temp = int(input("Введите данные: "))

print(iron.temperatura(temp))