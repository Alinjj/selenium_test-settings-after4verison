amount_ticket = int(input('Введите кол-во билетов: '))
age = [int(input('Введите возраст поситителей для каждого билета: ')) for i in range(amount_ticket)]

Total = 0

for x in age:
    if x < 18:
        Total = Total
        print('До 18 лет бесплатно')
    if 18 <= x < 25:
        Total += 990
        print('От 18 до 25 цена 990р')
    if x >= 25:
        Total += 1390
        print('От 25 лет полная стоимость 1390р')
for y in range(1):
    if amount_ticket >=3:
        Total = (Total / 100) * 90

print(Total)

