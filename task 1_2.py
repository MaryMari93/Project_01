# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

name_song = {}
name_song['Easy'] = 4.15
name_song['Beautiful Day'] = 4.04
name_song['New Salvation'] = 4.02
total_sum = 0
for my_favorite_songs in name_song:
    song_length = name_song[my_favorite_songs]
    print(my_favorite_songs, song_length)
    total_sum += song_length
    print('Три песни звучат',
total_sum, 'минут')


import random
print(random.sample(my_favorite_songs, k=3))

# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

song = {}
song['Beautiful Day'] = 4.04
song['In This World'] = 4.02
song['Waste a Moment'] = 3.03

sum_of_songs= (song['Beautiful Day'] + song['In This World'] + song['Waste a Moment'])
print('Три песни звучат',
sum_of_songs, 'минут')


from random import sample
name = list(dict.items(my_favorite_songs_dict))
results = sample(name, 3)
print(results)

# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random
# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 
