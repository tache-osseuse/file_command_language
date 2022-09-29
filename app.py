import os

command = {"hide":['arg', {'-on':'h1','-off':'h2'}],
           "state":['arg', {'-r':'st1','-w':'st2'}],
           "archive":['arg', {'-on':'ar1','-off':'ar2'}],
           "show":['emp', 'sh1'],
           "switch":['nm', 'sw1'],
           "attr":['nm', 'at1']
           }

pt = os.path.dirname(os.path.abspath(__file__)) + '\\test_dir\\'

def maker(ch, st):
    global pt
    match ch[0]:
        case 'h1':
            if len(st) == 3 and 'H' not in st[1]:
                os.system('attrib +h ' + pt + ch[1])
                print(ch[1] + ' -> Файл был скрыт!')
            elif len(st) == 2 and 'H' not in st[0]:
                os.system('attrib +h ' + pt + ch[1])
                print(ch[1] + ' -> Файл был скрыт!')
            elif len(st) == 1:
                os.system('attrib +h ' + pt + ch[1])
                print(ch[1] + ' -> Файл был скрыт!')
            else:
                print(ch[1] + ' [Файл уже скрыт!]')
        case 'h2':
            if len(st) == 3 and 'H' in st[1]:
                os.system('attrib -h ' + pt + ch[1])
                print(ch[1] + ' -> Файл был открыт!')
            elif len(st) == 2 and 'H' in st[0]:
                os.system('attrib -h ' + pt + ch[1])
                print(ch[1] + ' -> Файл был открыт!')
            else:
                print(ch[1] + ' [Файл уже открыт!]')
        case 'st1':
            if len(st) == 3 and 'R' not in st[1]:
                os.system('attrib -h ' + pt + ch[1])
                os.system('attrib +r ' + pt + ch[1])
                os.system('attrib +h ' + pt + ch[1])
                print(ch[1] + ' -> Был установлен режим только чтения!')
            elif len(st) == 2 and 'R' not in st[0]:
                if 'H' in st[0]:
                    os.system('attrib -h ' + pt + ch[1])
                    os.system('attrib +r ' + pt + ch[1])
                    os.system('attrib +h ' + pt + ch[1])
                    print(ch[1] + ' -> Был установлен режим только чтения!')
                else:
                    os.system('attrib +r ' + pt + ch[1])
                    print(ch[1] + ' -> Был установлен режим только чтения!')
            elif len(st) == 1:
                os.system('attrib +r ' + pt + ch[1])
                print(ch[1] + ' -> Был установлен режим только чтения!')
            else:
                print(ch[1] + ' [Режим только чтения уже установлен!]')
        case 'st2':
            if len(st) == 3 and 'R' in st[1]:
                if 'H' in st[1]:
                    os.system('attrib -h ' + pt + ch[1])
                    os.system('attrib -r ' + pt + ch[1])
                    os.system('attrib +h ' + pt + ch[1])
                    print(ch[1] + ' -> Был установлен режим чтения и записи!')
                else:
                    os.system('attrib -r ' + pt + ch[1])
                    print(ch[1] + ' -> Был установлен режим чтения и записи!')
            elif len(st) == 2 and 'R' in st[0]:
                if 'H' in st[0]:
                    os.system('attrib -h ' + pt + ch[1])
                    os.system('attrib -r ' + pt + ch[1])
                    os.system('attrib +h ' + pt + ch[1])
                    print(ch[1] + ' -> Был установлен режим чтения и записи!')
                else:
                    os.system('attrib -r ' + pt + ch[1])
                    print(ch[1] + ' -> Был установлен режим чтения и записи!')
            else:
                print(ch[1] + ' [Режим только для чтения и записи уже установлен!]')
        case 'ar1':
            if len(st) == 3:
                print(ch[1] + ' [Файл уже готов к архивации!]')
            elif len(st) == 2 and 'A' not in st[0]:
                if 'H' in st[0]:
                    os.system('attrib -h ' + pt + ch[1])
                    os.system('attrib +a ' + pt + ch[1])
                    os.system('attrib +h ' + pt + ch[1])
                    print(ch[1] + ' -> Готов к архивации!')
                else:
                    os.system('attrib +a ' + pt + ch[1])
                    print(ch[1] + ' -> Готов к архивации!')
            elif len(st) == 1:
                os.system('attrib +a ' + pt + ch[1])
                print(ch[1] + ' -> Готов к архивации!')
            else:
                print(ch[1] + ' [Файл уже готов к архивации!]')
        case 'ar2':
            if len(st) == 3 and 'A' in st[0]:
                if 'H' not in st[1]:
                    os.system('attrib -a ' + pt + ch[1])
                    print(ch[1] + ' -> Не готов к архивации!')
                else:
                    os.system('attrib -h ' + pt + ch[1])
                    os.system('attrib -a ' + pt + ch[1])
                    os.system('attrib +h ' + pt + ch[1])
                    print(ch[1] + ' -> Не готов к архивации!')
            elif len(st) == 2 and 'A' in st[0]:
                os.system('attrib -a ' + pt + ch[1])
                print(ch[1] + ' -> Не готов к архивации!')
            else:
                print(ch[1] + ' [Файл уже не готов к архивации!]')
        case 'sh1':
            stp = os.popen('dir /b /a-d ' + pt).read().split()
            for el in stp:
                print(el, end=' ')
            print()
        case 'sw1':
            if os.path.exists(st):
                pt = st
            else:
                print('[Такой директории нет!]')
        case 'at1':
            if os.path.isfile(pt + ch[1]):
                lst = os.popen('attrib ' + pt + ch[1]).read().split()
                print(ch[1], end=" -> ")
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


def commander(ch):
    global pt
    if len(ch) > 1:
        if ch[0] != 'sw1':
            for el in ch[1]:
                if os.path.isfile(pt + el):
                    st = os.popen('attrib ' + pt + el).read().split()
                    maker([ch[0], el], st)
                else:
                    print('[Такого файла нет!]')
        else:
            maker(ch, ch[1][0])
    else:
        maker(ch, [])
    
while True:
    st = input('=> ')
    ls = st.split(' ')
    if ls[0] in command.keys():
        if len(ls) > 2:
            if command[ls[0]][0] == 'arg':
                if ls[1] in command[ls[0]][1].keys():
                    commander([command[ls[0]][1][ls[1]], [el for el in ls[2:]]])
                else:
                    print('[Такого флага нет!]')
            elif command[ls[0]][0] == 'nm':
                commander([command[ls[0]][1], [el for el in ls[1:]]])
            else:
                print("[Такой команды нет!]")
        elif len(ls) == 2:
            if command[ls[0]][0] == 'nm':
                commander([command[ls[0]][1], [ls[1]]])
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

