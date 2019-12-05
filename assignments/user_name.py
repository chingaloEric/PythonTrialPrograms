users = ['Eric', 'Lisa', 'Miguel', 'Arthur', 'Antonela', 'Mirabelle']
new_users = ['Mpoki', 'Eric']
for name in new_users:
    if name in users:
        print(name + ' is Availble')
    else:
        print('Ooups! ' + name + ' not available')