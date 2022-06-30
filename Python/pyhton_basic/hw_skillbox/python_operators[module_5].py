# Калькулятор опыта.
experience = int(input('Введите количество опыта: '))
if experience < 1000:
  print('Ваш уровень: 1')
elif experience < 2500:
  print('Ваш уровень: 2')
elif experience < 5000:
  print('Ваш уровень: 3')
else:
  print('Ваш уровень: 4')

# Максимум из трёх чисел 2.
a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
c = int(input('Введите число с: '))
if a > b and a > c:
  max = a
elif b > a and b > c:
  max = b
else:
  max = c
print('Максимальное число =',max)

# Функция.
x = int(input('Введите число X = '))
if x > 0:
  y = x - 12
elif x == 0:
  y = 5
elif x < 0:
  y = x * x
print('Y равен',y)

# Поступление.
index = int(input('Введите место в списке поступающих: '))
if index <= 10:
  points = int(input('Введите количество баллов за экзамены: '))
  print('Поздравляем, Вы поступили!')
  if points >= 290:
    print('Бонусом Вам будет начисляться стипендия')
  else:
    print('Но Вам не хватило баллов для стипендии.')
else:
  print('К сожалению, вы не поступили.')

# Опять двойка.
rating = int(input('Что получил по математике? '))
if rating == 2 or rating == 3:
  print('Плохо. Марш учиться!')
if rating == 4 or rating == 5:
  print('Молодец! Можешь отдохнуть.')

# Защита от дурака.
a = int(input('Введите число: '))
if (a < 100  and a > 9) or (a > -100 and a < -9):
  print('двузначное')
else:
  print('недвузначное')

# Костя хочет выигрывать.
a = int(input('Введите число: '))
b = int(input('Введите число: '))
c = int(input('Введите число: '))
if a == b == c:
  print('все сеовпадаю')
elif a == b or a == c or b == c:
  print('2 совпадают')
else:
  print('0 совпадений')

# Новоселье.
s = int(input('Прощадь квартиры: '))
price = int(input('Цена: '))
if (s >= 100 and price <= 10) or (s >= 80 and price <= 7):
  print('Подходит')
else:
  print('НЕ подходит')

# Прогрессивный налог 2.
p = int(input('доход? = '))
if p > 50000:
  tax = 0.3 * (p - 50000) + 9300
elif p > 10000 and p < 50000:
  tax = 0.2 * (p - 10000) + 1300
else:
  tax = 0.13 * p
print('налог =', tax)

# Почта.
# 1й вариант
t = int(input('время? от 0 до 23 = '))
if (t >= 8 and t < 10) or (t >= 12 and t < 14) or (t >= 15 and t < 18) or (t > 20 and t < 22):
  print('Можно получить посылку')
else:
  print('Посылку получить нельзя')

# 2й вариант
t = int(input('время? от 0 до 23 = '))
if (t >= 0 and t < 8) or (t >= 10 and t < 12) or (t >= 14 and t < 15) or (t >= 18 and t < 20) or (t >= 22 and t <= 24):
  print('Посылку получить нельзя')
else:
  print('Можно получить посылку')