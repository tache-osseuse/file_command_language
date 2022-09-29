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
    global pt
    match ch[0]:
        case 'h1':
            if os.path.isfile(pt + ch[1]):
                st = os.popen('attrib ' + pt + ch[1]).read().split()
                if len(st) == 3 and 'H' not in st[1]:
                    os.system('attrib +h ' + pt + ch[1])
                    print('Файл был скрыт!')
                elif len(st) == 2 and 'H' not in st[0]:
                    os.system('attrib +h ' + pt + ch[1])
                    print('Файл был скрыт!')
                else:
                    print('[Файл уже скрыт!]')
            else:
                print('[Такого файла нет!]')
        case 'h2':
            if os.path.isfile(pt + ch[1]):
                st = os.popen('attrib ' + pt + ch[1]).read().split()
                if len(st) == 3 and 'H' in st[1]:
                    os.system('attrib -h ' + pt + ch[1])
                    print('Файл был открыт!')
                elif len(st) == 2 and 'H' in st[0]:
                    os.system('attrib -h ' + pt + ch[1])
                    print('Файл был открыт!')
                else:
                    print('[Файл уже открыт!]')
            else:
                print('[Такого файла нет!]')
        case 'st1':
            if os.path.isfile(pt + ch[1]):
                st = os.popen('attrib ' + pt + ch[1]).read().split()
                print(st)
                if len(st) == 3 and 'H' not in st[1]:
                    if 'R' not in st[1]:
                        os.system('attrib +r ' + pt + ch[1])
                        print('Был установлен режим только чтения!')
                    else:
                        print('[Режим только для чтения уже установлен!]')
                elif len(st) == 2 and 'H' not in st[0]:
                    if 'R' not in st[0]:
                        os.system('attrib +r ' + pt + ch[1])
                        print('Был установлен режим только чтения!')
                    else:
                        print('[Режим только для чтения уже установлен!]')
                elif len(st) == 1:
                    os.system('attrib +r ' + pt + ch[1])
                    print('Был установлен режим только чтения!')
                else:
                    print('|Файл скрыт!|')
            else:
                print('[Такого файла нет!]')
        case 'st2':
            if os.path.isfile(pt + ch[1]):
                st = os.popen('attrib ' + pt + ch[1]).read().split()
                print(st)
                if len(st) == 3 and 'H' not in st[1]:
                    if 'R' in st[1]:
                        os.system('attrib -r ' + pt + ch[1])
                        print('Был установлен режим чтения и записи!')
                    else:
                        print('[Режим только для чтения и записи уже установлен!]')
                elif len(st) == 2 and 'H' not in st[0]:
                    if 'R' in st[0]:
                        os.system('attrib -r ' + pt + ch[1])
                        print('Был установлен режим чтения и записи!')
                    else:
                        print('[Режим только для чтения и записи уже установлен!]')
                elif len(st) == 1:
                    print('[Режим только для чтения и записи уже установлен!]')
                else:
                    print('[Файл скрыт!]')
            else:
                print('[Такого файла нет!]')
        case 'ar1':
            if os.path.isfile(pt + ch[1]):
                st = os.popen('attrib ' + pt + ch[1]).read().split()
                if len(st) == 3:
                    print('[Файл уже готов к архивации!]')
                elif len(st) == 2:
                    if 'H' not in st[0]:
                        os.system('attrib +a ' + pt + ch[1])
                        print('Готов к архивации!')
                    else:
                        print('[Файл скрыт!]')
                elif len(st) == 1:
                    os.system('attrib +a ' + pt + ch[1])
                    print('Готов к архивации!')
                else:
                    print('[Файл уже готов к архивации!]')
            else:
                print('[Такого файла нет!]')
        case 'ar2':
            if os.path.isfile(pt + ch[1]):
                st = os.popen('attrib ' + pt + ch[1]).read().split()
                if len(st) == 3:
                    if 'H' not in st[1]:
                        os.system('attrib -a ' + pt + ch[1])
                        print('Не готов к архивации!')
                    else:
                        print('[Файл скрыт!]')
                elif len(st) == 2:
                    if 'H' not in st[0]:
                        os.system('attrib -a ' + pt + ch[1])
                        print('Не готов к архивации!')
                    else:
                        print('[Файл скрыт!]')
                else:
                    print('[Файл уже не готов к архивации!]')
            else:
                print('[Такого файла нет!]')
        case 'sh1':
            st = os.popen('dir /b /a-d ' + pt).read().split()
            for el in st:
                print(el, end=' ')
            print()
        case 'sw1':
            if os.path.exists(ch[1]):
                pt = ch[1]
            else:
                print('[Такой директории нет!]')
        case 'at1':
            if os.path.isfile(pt + ch[1]):
                lst = os.popen('attrib ' + pt + ch[1]).read().split()
                if len(lst) == 1:
                    print('|Файл не готов к архивации, доступен в режиме чтения и записи, файл открыт|')
                elif len(lst) == 2 and lst[0] == 'A':
                    print('|Файл готов к архивации, доступен в режиме чтения и записи, файл открыт|')
                elif len(lst) == 2 and lst[0] == 'R':
                    print('|Файл не готов к архивации, доступен только в режиме чтения, файл открыт|')
                elif len(lst) == 2 and lst[0] == 'H':
                    print('|Файл не готов к архивации, доступен в режиме чтения и записи, файл скрыт|')
                elif len(lst) == 2 and lst[0] == 'HR':
                    print('|Файл не готов к архивации, доступен только в режиме чтения, файл скрыт|')
                elif len(lst) == 3 and lst[1] == 'R':
                    print('|Файл готов к архивации, доступен только в режиме чтения, файл открыт|')
                elif len(lst) == 3 and lst[1] == 'H':
                    print('|Файл готов к архивации, доступен в режиме чтения и записи, файл скрыт|')
                elif len(lst) == 3 and lst[1] == 'HR':
                    print('|Файл готов к архивации, доступен только в режиме чтения, файл скрыт|')
            else:
                print('Такого файла нет!')            

while True:
    st = input('=> ')
    ls = st.split(' ')
    if ls[0] in command.keys():
        if len(ls) == 3:
            if command[ls[0]][0] == 'arg':
                if ls[1] in command[ls[0]][1].keys():
                    commander([command[ls[0]][1][ls[1]], ls[2]])
            else:
                print("[Такой команды нет!]")
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

