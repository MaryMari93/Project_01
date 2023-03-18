# Задача 1.1.

# Есть строка с перечислением песен

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.

# первый трек 
print(my_favorite_songs[:14] + my_favorite_songs[15:23])

# последний
print(my_favorite_songs[-13:])

# Второй 
print(my_favorite_songs[25:30] + my_favorite_songs[33:49])

# второй с конца
print(my_favorite_songs[-26:-15])