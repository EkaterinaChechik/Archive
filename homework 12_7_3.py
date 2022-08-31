# задание 12.7.3
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
print( per_cent )

money = input('Введите денежную сумму ')
deposit = list( map( lambda x : int(float(money)*x), per_cent.values() ) )

print ("Возможная прибыль в банках", deposit)
print(" Максимальная сумма, которую вы можете заработать — ", max(deposit) )  
