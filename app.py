import os

command = {"hide":['arg', {'-on':'h1','-off':'h2'}],
           "state":['arg', {'-r':'st1','-w':'st2'}],
           "archive":['arg', {'-on':'ar1','-off':'ar2'}],
           "show":['emp', 'sh1'],
           "switch":['nm', 'sw1'],
           "attr":['nm', 'at1']
           }

pt = os.path.dirname(os.path.abspath(__file__)) + '\\test_dir\\'

def commander(ch):
    match ch[0]:
        case 'h1':
            if os.path.isfile(pt + ch[1]):
                if 'H' not in os.popen('attrib ' + pt + ch[1]).read().split()[1]:
                    os.system('attrib +h ' + pt + ch[1])
                    print('Файл был скрыт!')
                else:
                    print('[Файл уже скрыт!]')
            else:
                print('[Такого файла нет!]')
        case 'h2':
            if os.path.isfile(pt + ch[1]):
                if 'H' in os.popen('attrib ' + pt + ch[1]).read().split()[1]:
                    os.system('attrib -h ' + pt + ch[1])
                    print('Файл был открыт!')
                else:
                    print('[Файл уже открыт!]')
            else:
                print('[Такого файла нет!]')
        case 'st1':
            if os.path.isfile(pt + ch[1]):
                os.system('attrib +r ' + pt + ch[1])
                print('Режим только чтения!')
            else:
                print('Такого файла нет!')
        case 'st2':
            if os.path.isfile(pt + ch[1]):
                os.system('attrib -r ' + pt + ch[1])
                print('Режим чтения и записи!')
            else:
                print('Такого файла нет!')
        case 'ar1':
            if os.path.isfile(pt + ch[1]):
                os.system('attrib +a ' + pt + ch[1])
                print('Готов к архивации!')
            else:
                print('Такого файла нет!')
        case 'ar2':
            if os.path.isfile(pt + ch[1]):
                os.system('attrib -a ' + pt + ch[1])
                print('Не готов к архивации!')
            else:
                print('Такого файла нет!')
        case 'sh1':
            os.system('dir ' + pt)
            print('Вывод содержимого каталога!')
        case 'sw1':
            print('Переключение текущего каталога')
        case 'at1':
            if os.path.isfile(pt + ch[1]):
                os.system('attrib ' + pt + ch[1])
                print('Вывод всех атрибутов файла!')
            else:
                print('Такого файла нет!')            

while True:
    st = input('Введите команду -> ')
    ls = st.split(' ')
    if ls[0] in command.keys():
        if len(ls) == 3:
            if command[ls[0]][0] == 'arg':
                if ls[1] in command[ls[0]][1].keys():
                    commander([command[ls[0]][1][ls[1]], ls[2]])
            else:
                print("NO!")
        elif len(ls) == 2:
            if command[ls[0]][0] == 'nm':
                commander([command[ls[0]][1], ls[1]])
            else:
                print("NO!")
        elif len(ls) == 1:
            if command[ls[0]][0] == 'emp':
                commander([command[ls[0]][1]])
            else:
                print("NO!")
        else:
            print("NO!")
    else:
        print('Такой команды нет!')

