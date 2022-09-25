command = {"hide":['arg', {'-on':'h1','-off':'h2'}],
           "state":['arg', {'-r':'st1','-w':'st2'}],
           "archive":['arg', {'-on':'ar1','-off':'ar2'}],
           "show":['emp', 'sh1'],
           "switch":['nm', 'sw1'],
           "attr":['nm', 'at1']
           }

path = ''

def commander(ch):
    match ch:
        case 'h1':
            print('Сделать файл скрытым!')
        case 'h2':
            print('Сделать файл открытым!')
        case 'st1':
            print('Режим только чтения!')
        case 'st2':
            print('Режим чтения и записи!')
        case 'ar1':
            print('Готов к архивации!')
        case 'ar2':
            print('Не готов к архивации!')
        case 'sh1':
            print('Вывод содержимого каталога!')
        case 'sw1':
            print('Переключение текущего каталога')
        case 'at1':
            print('Вывод всех атрибутов файла!')

while True:
    st = input('Введите команду -> ')
    ls = st.split(' ')
    if ls[0] in command.keys():
        if len(ls) == 3:
            if command[ls[0]][0] == 'arg':
                if ls[1] in command[ls[0]][1].keys():
                    #проверка на путь
                    commander(command[ls[0]][1][ls[1]])
            else:
                print("NO!")
        elif len(ls) == 2:
            if command[ls[0]][0] == 'nm':
                #проверка на путь 
                commander(command[ls[0]][1])
            else:
                print("NO!")
        elif len(ls) == 1:
            if command[ls[0]][0] == 'emp':
                commander(command[ls[0]][1])
            else:
                print("NO!")
        else:
            print("NO!")
    else:
        print('Такой команды нет!')

