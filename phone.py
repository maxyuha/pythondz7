def readfile(filename):
    return open(filename).read().split('\n')
 
def scan(data):
    for i in  data:
        print(i)
        
def search(data):
    flag = 1
    name = input('имя > ')
    for line in data:
        if name in line:
            flag = 0
            print(line)
    if flag: print('no name given')

def phone_add(data):
    name = input('введите контакт в формате ФИО НОМЕР')
    with open('phones.txt','a') as f_in:
      f_in.write(input(f'\n{name}\n'))

    
data = readfile('phones.txt') 
dict_command = {'1' :  scan, '2' : search, '3' : phone_add} 
 
print('''Команды для работы со справочником:
    Просмотр всех записей справочника - 1
    Поиск по справочнику - 2
    Добавить контакт - 3''')
 
while True:
    command = input('Команда: > ')
    if command in dict_command:
        dict_command[command](data)
    else:
        print('ошибка')
