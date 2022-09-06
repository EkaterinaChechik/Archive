# Задание 13.8.19 (HW-03)
# 1. В начале у пользователя запрашивается количество билетов, 
# которые он хочет приобрести на мероприятие.

# 2. Далее для каждого билета запрашивается возраст посетителя, 
# в соответствии со значением которого выбирается стоимость:

#         Если посетителю конференции менее 18 лет, то он проходит 
#         на конференцию бесплатно.
#         От 18 до 25 лет — 990 руб.
#         От 25 лет — полная стоимость 1390 руб.

# 3. В результате программы выводится сумма к оплате. При этом, если 
# человек регистрирует больше трёх человек на конференцию, то дополнительно 
# получает 10% скидку на полную стоимость заказа.

price = 0
total_amount = 0

try :
    number_of_tickets = int(input('Введите количество билетов (от 1 до 20) '))
    if number_of_tickets < 1 or number_of_tickets > 20 : 
        raise ValueError('Можно купить от 1 до 20 билетов за раз!!!')
except ValueError as messageError :
    print('Неправильное число для покупки билетов!\nИзвините, но такие билеты мы не продаём!!!')
else :
    print("""         Если посетителю конференции менее 18 лет, то он проходит
         на конференцию бесплатно.\n\
         От 18 до 25 лет — 990 руб.\n\
         От 25 лет — полная стоимость 1390 руб.""")
         
#   счетчик билетов
count = 1

# цикл для определения стоимости билетов
while count <= number_of_tickets :
    age_s = (input(f'Введите возраст посетителя {count} (q - выход) '))
    # проверка правильности ввода
    if not age_s.isnumeric() : 
        if age_s == 'q' or age_s == 'Q' : 
            print('выход из программы')
            break
        print('В десятичной системе счисления такого возраста не существует!!!\n\
        воспользуйтесь цифровой клавиатурой и введите возраст заново!')
        continue

    # проверка границ возраста
    age = int(age_s)
    if age < 0 or age > 119 : 
        print('Людей такого возраста не существует!!!')
        continue
            
    # расчет стоимости белетов
    if 18 <= age < 25 : price += 990
    if age >= 25 : price += 1390
    if count == 4 : print('У Вас скидка 10% ')
    if count == number_of_tickets :
        price *= 0.9
        print( f'Количество билетов {count}, общая стоимость {price} р' )
        break 
    else :
        count += 1

