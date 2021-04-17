import redis
import json

# подключаемся к серверу Redis
red = redis.Redis(
    host='redis-12698.c259.us-central1-2.gce.cloud.redislabs.com',
    port=12698,
    password='94vA5sAmoXRKhZ7rsokTRiiCXgGwKzeW'
)

# записываем строки в кеш сервера Redis
# Option_1
red.set('var1', 'value1')
print(red.get('var1'))

# Option_2
red.set('Tatarstan', 'Kazan')
print(red.get('Tatarstan'))

# Получаем значение из кеша по ключу
red['Russia'] = 'Moscow'
print(red.get('Russia'))  # ответ будет: b'Moscow'

# создаём словарь
dict1 = {'key1': 'value1', 'key2': 'value2'}

# превратим словарь в строку
red.set('dict1', json.dumps(dict1))  # с помощью функции dumps() из модуля json превратим наш словарь в строчку

# получаем данные
print(red.get('dict1'))

# превращаем данные в словарь
print(json.loads(red.get('dict1')))  # с помощью функции loads() из модуля json превратим строку в словарь

# удаление данных
red.delete('dict1')
print(red.get('dict1'))

# удалить все ключи
for key in red.keys():
    red.delete(key)