import string
from random import *
#need to add transliterate package
from transliterate import translit
#here is the path to the file from which the data is taken (full name)
    #in my case the path looks like this
with open('C:\\Users\\79505\\Desktop\\Файл_ФИО.txt', 'r', encoding='utf-8') as file:
    upp = [i for i in string.ascii_uppercase if i not in 'OI']
    low = [i for i in string.ascii_lowercase if i not in 'ol']
    num = [i for i in string.digits[2:]]
    sym = "_?!@#$%"
    symbols = set()
    # m- password length (in this case 8)
    n, m = 1, 8
    while len(symbols) != 56:
        excluded = [73, 79, 91, 92, 93, 94, 95, 96, 108, 111]
        symbol = randint(65, 122)
        symbols.add(str(randint(2, 9)))
        if symbol in excluded:
            continue
        else:
            symbols.add(chr(symbol))
    #here is the file where the login-password is saved...
    with open('C:\\Users\\79505\\Desktop\\лог_пор.txt', 'w', encoding='utf-8') as file_1:
        ru_text = [line.strip().lower() for line in file.readlines()]
        ru_id = []
        for i in ru_text:
            name_id = i.split()
            ru_id.append(name_id[0]+'_'+name_id[1][0]+name_id[2][0])
        for string in ru_id:
            en_txt = translit(string, language_code='ru', reversed=True)
            count = 0
            while count != n:
                output = '' + choice(num) + choice(low) + choice(upp) + choice(sym)
                while len(output) != m:
                    output += (choice(''.join(symbols)))
                count += 1
            file_1.write("".join(c for c in en_txt if c.isalpha() or c=='_')+'; password:'+''.join(sample(output, m))+'\n')