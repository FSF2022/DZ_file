import os
file_name = 'schet.txt'

bill = 0
history = []
""" if os.path.exists(file_name):
    with open(file_name,'r', encoding = 'utf-8') as f:
        result = f.read()
        print(result) """

def buy(bill):
    pay = int(input('Введите сумму покупки'))
    if pay > bill:
      print('Недостаточно суммы на счете')
    else:
      bill -= pay
      name = input('Введите название покупки')
      history.append((name,pay))
    return bill

while True:
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')
    print(f'Ваш счет {bill}')
    choice = input('Выберите пункт меню')
    if choice == '1':
        pay = int(input('Введите сумму пополнения'))
        bill += pay
    elif choice == '2':
        bill = buy(bill)
    elif choice == '3':
        print(history)
    elif choice == '4':
        with open(file_name,'a',encoding = 'utf-8') as f:
              for name,pay in history:
                  f.write(f'{name,pay}\n')
        break
    else:
        print('Неверный пункт меню')




