f = open('text.txt', 'w', encoding='utf8')

f.write('This is a test str\n')
f.write('This is a new str\n')

f.close()  # обязательно нужно закрыть файл иначе он будет заблокирован ОС

f = open('text.txt', 'r', encoding='utf8')
print(f.read(30))  # указатель до 30-й позиции
print(f.read())  # считали остаток файла
f.seek(0)  # смещение указателя на начало файла - 0
print(f.readline())
print(f.readline())
f.close()

# добавление строк в файл
f = open('text.txt', 'w', encoding='utf8')
items = ['New string 1\n', 'New string 2\n']
f.writelines(items)
f.close()

f = open('text.txt', 'r', encoding='utf8')
print(f.readlines())
f.close()

f = open('text.txt', 'r', encoding='utf8')
for i in items:
    print(f.readline())
f.close()

with open('text.txt', 'r') as f:
    print(f.read())
#
f = open('input.txt', 'w', encoding='utf8')
n = ['text 1\n', 'text 2\n']
f.writelines(n)
f.close()

f, k = open('input.txt', 'r', encoding='utf8'), open('output.txt', 'w', encoding='utf8')

for i in f:
    k.writelines(i)
k.close()

f = open('numbers.txt', 'w', encoding='utf8')
items = [1, 2, 3, 4, 5, 6, 7, 8, 9]
j=[]
for i in items:
    new_items = str(i) +'\n'
    j.append(new_items)
items = j
for i in items:
    f.write(str(i))
f.close()

f = open('numbers.txt', 'r', encoding='utf8')
a = f.readlines()

res = int(min(a))+int(max(a))
print(res)

f = open('output.txt', 'w', encoding='utf8')
a = f.write(str(res))

#
with open('input.txt', 'r', encoding='utf8') as f:
    count = 0
    for i in f:
        if int(i.split('.')[-1]) < 3:
            count += 1
    print(count)

f = open('input.txt', 'r', encoding='utf8')
k = open('output.txt', 'w', encoding='utf8')
for i in reversed(f.readlines()):
    k.write(i)
    print(k)
f.close()

