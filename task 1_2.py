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

# Ну да, можно такое решение применить. 
# Правда сначала не понял зачем добовлять новые ключ значения в словарь, потом осознал что пункт B)

# Вот еще варианты + пункт D
# ###################### Решение ######################

# Импорты
from random import sample, choices
from datetime import timedelta
from math import modf

# Пункт А
time = my_favorite_songs[0][1] + my_favorite_songs[2][1] + my_favorite_songs[4][1]
print(f'Пункт А: Три песни звучат {time} минут.')

# Пункт С(А)
time = 0
for song in sample(my_favorite_songs, 3):
    time += song[1]

print(f'Пункт C(A): Три песни звучат {round(time, 2)}')

# Пункт D(А)
total_time = timedelta()
for song in sample(my_favorite_songs, 3):
    s, m = modf(song[1])
    total_time += timedelta(minutes=int(m), seconds=int(s * 100))

print(f'Пункт D(A): Три песни звучат {total_time}')


# Пункт B
time = my_favorite_songs_dict['Waste a Moment'] + my_favorite_songs_dict['Staying\' Alive'] + my_favorite_songs_dict['Easy']
print(f'Пункт B: Три песни звучат {time} минут.')

# Пункт C(B)
time = 0
for song in sample(tuple(my_favorite_songs_dict), 3):
    time += my_favorite_songs_dict[song]

print(f'Пункт C(B): Три песни звучат {round(time, 2)}')

# Пункт D(А)
total_time = timedelta()
for song in sample(tuple(my_favorite_songs_dict), 3):
    s, m = modf(my_favorite_songs_dict[song])
    total_time += timedelta(minutes=int(m), seconds=int(s * 100))

print(f'Пункт D(B): Три песни звучат {total_time}')
