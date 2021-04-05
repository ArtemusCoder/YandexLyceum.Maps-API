import os
import sys
from io import BytesIO
import pygame
import requests

lon = input('Введите долготу: ')
lat = input('Введите широту: ')
while True:
    scale = input('Введите масштаб(0-17): ')
    if 0 <= int(scale) <= 17:
        break
    print('Неправильно!')

map_params = {
    "l": "map",
    "ll": "{},{}".format(lon, lat),
    'z': '{}'.format(scale)
}

map_api_server = "http://static-maps.yandex.ru/1.x/"
response = requests.get(map_api_server, params=map_params)

if not response:
    print("Ошибка выполнения запроса:")
    print(map_api_server)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)

pygame.init()
screen = pygame.display.set_mode((600, 450))
screen.blit(pygame.image.load(BytesIO(response.content)), (0, 0))
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
