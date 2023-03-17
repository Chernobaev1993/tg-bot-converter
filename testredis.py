import redis
import json

red = redis.Redis(
    host="redis-15203.c302.asia-northeast1-1.gce.cloud.redislabs.com",
    port=15203,
    password='95YmYY1II6xx40G2XBHCsGhW5CFEmA3J'
)

# # создаём словарь для записи
# dict1 = {'key1': 'value1', 'key2': 'value2'}
#
# # с помощью функции dumps() из модуля json превратим наш словарь в строчку
# red.set('dict1', json.dumps(dict1))
#
# # с помощью знакомой нам функции превращаем данные, полученные из кеша обратно в словарь
# converted_dict = json.loads(red.get('dict1'))
#
# # убеждаемся, что мы получили действительно словарь
# print(type(converted_dict))
#
# # ну и выводим его содержание
# print(converted_dict)

red.delete('dict1')
print(red.get('dict1'))
