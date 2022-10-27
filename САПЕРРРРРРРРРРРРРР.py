from random import choice
from colorama import Fore
from pyfiglet import figlet_format

print(Fore.LIGHTCYAN_EX + figlet_format('MINESWEEPER', font='smslant').rstrip())
print(Fore.RED + figlet_format('by  R31VU', font='smslant'))
coordinates_list, bombs_list = list(), list()
size_y, size_x, number_of_bombs = int(
    input(f'{Fore.GREEN}> {Fore.RESET}Введите {Fore.GREEN}высоту{Fore.RESET} поля: ')), int(input(
    f'{Fore.GREEN}> {Fore.RESET}Введите {Fore.GREEN}ширину{Fore.RESET} поля: ')), int(
    input(f'{Fore.RED}> {Fore.RESET}Введите количество {Fore.RED}бомб{Fore.RESET}: '))
symbol_of_bomb = f'{Fore.RED}X{Fore.RESET}'
for y in range(size_y):
    for x in range(size_x):
        coordinates_list.append((y, x))
matrix = [[0 for _ in range(size_x)] for __ in range(size_y)]
for i in range(number_of_bombs):
    bomb_coord = choice(coordinates_list)
    coordinates_list.remove(bomb_coord)
    bombs_list.append(bomb_coord)
for elem in bombs_list:
    matrix[elem[0]][elem[1]] = symbol_of_bomb
for coordinate in bombs_list:
    y, x = coordinate
    counter = 0
    if y != 0 and matrix[y - 1][x] != symbol_of_bomb:
        matrix[y - 1][x] += 1
    if x != 0 and matrix[y][x - 1] != symbol_of_bomb:
        matrix[y][x - 1] += 1
    if y + 1 != size_y and matrix[y + 1][x] != symbol_of_bomb:
        matrix[y + 1][x] += 1
    if x + 1 != size_x and matrix[y][x + 1] != symbol_of_bomb:
        matrix[y][x + 1] += 1
    if x + 1 != size_x and y + 1 != size_y and matrix[y + 1][x + 1] != symbol_of_bomb:
        matrix[y + 1][x + 1] += 1
    if x != 0 and y != 0 and matrix[y - 1][x - 1] != symbol_of_bomb:
        matrix[y - 1][x - 1] += 1
    if x != 0 and y + 1 != size_y and matrix[y + 1][x - 1] != symbol_of_bomb:
        matrix[y + 1][x - 1] += 1
    if x + 1 != size_x and y != 0 and matrix[y - 1][x + 1] != symbol_of_bomb:
        matrix[y - 1][x + 1] += 1
print(f'\n{Fore.GREEN}> {Fore.RESET}Результат {Fore.RESET}генерации: \n')
print(f'\n{"    " * size_x}\n'.join(
    [f'  {Fore.LIGHTCYAN_EX}' + f'{Fore.RESET}     {Fore.LIGHTCYAN_EX}'.join([str(elem) for elem in __]) for __ in
     matrix]))
