from GuestsList import NewGuests

personnel_collection={}
collection = []
a = "N"
while True:
    if a == "N" or a == "n":
        full_name = input('Введите имя: ')
        city = input('Введите город: ')
        status = input('Введите роль сотрудника: ')
        print('Нажмите "Y", если хотите завершить заполнение списка, '
              '"N", если хотите продолжить заполнение')
        personnel_collection['full_name'] = full_name
        personnel_collection['city'] = city
        personnel_collection['status'] = status

        collection.append(personnel_collection.copy()) # !
        a = input()
        continue
    elif a == "Y" or a == "y":
        break

for guest in collection:
    guest_person = NewGuests()
    guest_person.init_from_dict(guest)
    print(f'{guest_person.full_name},', f'г.{guest_person.city},', f'статус "{guest_person.status}"')


