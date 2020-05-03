a = input('Введите текст: ').split()
list2 = []
def func():
    for i in a:
        list2.append(i.strip(',.()!?\':'))
    newstring = len(''.join(list2))
    lenstring = ' '.join(list2)
    newstring, lenstring = lenstring, newstring
    lowercase = 0
    uppercase = 0
    for e in newstring:
        if e.islower():
            lowercase += 1
        elif e.isupper():
            uppercase +=1
    return (f'строчных букв: {round(lowercase / lenstring * 100, 2)} процентов, заглавных букв: {round(uppercase / lenstring *100, 2)} процентов')
print(func())