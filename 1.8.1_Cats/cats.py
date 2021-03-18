from Cat import Cat


cat_1 = Cat("Барон", "мальчик", 2)
cat_2 = Cat("Сэм", "мальчик", 2)

list_of_cats = [cat_1, cat_2]

for kitten in list_of_cats:
    print(f"Кличка кошки: {kitten.get_name()}")
    print(F"Пол: {kitten.get_gender()}")
    print(f"Возраст (лет): {kitten.get_age()}")