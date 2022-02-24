# 1.
a = [1, 2, 4, 2, 5, 7, 1]
for i in range(len(a)):
    s = a.count(a[i])
    if s == 1:
        print(a[i])

# 2.
a = [1, 2, 4, 2, 5, 7, 1]
count1 = 0
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] == a[j]:
            count1 += 1
print(count1)

# 3.

c_1 = (35, 78, 21, 37, 2, 98, 6, 100, 231)
c_2 = (45, 21, 124, 76, 5, 23, 91, 234)

sum1 = sum(c_1)
sum2 = sum(c_2)
print(sum1)
print(sum2)
if sum1 > sum2:
    print("Сумма больше в кортеже - a")
else:
    print("Сумма больше в кортеже - b")
print('min c_1: ', min(c_1), 'Номер -', c_1.index(min(c_1)))
print('min c_2: ', min(c_2), 'Номер -', c_2.index(min(c_2)))

# 4.

str = "An aplle a day keeps the doctor away"
dict1 = {i: str.count(i) for i in str}
print(dict1)

# 6.
a = [35, 78, 21, 37, 2, 98, 6, 100, 231]
b = [45, 21, 124, 76, 5, 23, 91, 234]
c = []
for i in a:
    if i in b:
        c.append(i)
print(c)

# 7.

a = int(input("Введите число1:"))
b = int(input("Введите число2:"))

try:
    result = a / b
except ZeroDivisionError:
    print("На ноль нельзя")
finally:
    print("Все")

# 8.

my_file = open("klass.txt", 'r')
content = my_file.read()
my_file.close()
content = content.split("\n")
print(content)

pupils = []
for line in content:
    line = line.split(" ")
    pupils.append([line[0], line[1], int(line[2])])
    srednia = 0
print("Ниже 3 баллов:")
for i in pupils:
    srednia += int(i[2])
    if i[2] < 3:
        print(f"{i[0]} {i[1]}: {i[2]}")
srednia /= len(pupils)
print(f"Средняя оценка по классу: {srednia}")

# 5.

cakes = {"Медовик": ["мед, сахар , мука", 10, 18],
         "Сказка": ["яйца, сахар, мука", 8, 9],
         "Маффин": ["какао, шоколад, мука", 2, 10],
         "Муровейник": ["печенье, сгущенка, арахис", 5, 4]}
for key, value in cakes.items():
    print(key, '-', value[0])
for key, value in cakes.items():
    print(key, '-', value[1])
for key, value in cakes.items():
    print(key, '-', value[2])
for key, value in cakes.items():
    print(key, '-', value[0], '-', value[1], '-', value[2])
cost = 0
while True:
    cake = input("Ваш выбор? (a - all) ")
    if cake == 'a' or cake not in cakes.keys():
        break
    quantity = int(input("Количество? "))
    if quantity > cakes[cake][2]:
        print("Извините, у нас нет такого количества")
        continue
    cost += cakes[cake][1] * quantity
    cakes[cake][2] -= quantity
print("price: ", cost)
print("Спасибо за покупку! До свидания!")
print("------------------------------------------")
for key, value in cakes.items():
    print(key, '-', value[0], '-', value[1], '-', value[2])
