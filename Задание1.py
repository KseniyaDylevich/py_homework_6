n = input('введите номер дня недели: ')
is_weekends = lambda x: 'да' if x in ['6', '7'] else 'нет' if x in ['1', '2', '3', '4', '5'] else  'такого дня недели не существует'
print(is_weekends(n))