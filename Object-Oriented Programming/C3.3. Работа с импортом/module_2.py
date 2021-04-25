import module_1 as m

r, a, b = int(input()), int(input()), int(input()),

if m.circle(r) > m.rectangle(a, b):
    print('круг больше прямоугольника')

else:
    print("прямоугольник больше круга")
