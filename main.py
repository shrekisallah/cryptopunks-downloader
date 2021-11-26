import requests
import os


def number(u):
    if u < 10:
        return '000' + f'{u}'
    elif u < 100:
        return '00' + f'{u}'
    elif u < 1000:
        return '0' + f'{u}'
    else:
        return u


i = 0
for x in range(10000):
    a = number(i)
    url = f'https://www.larvalabs.com/public/images/cryptopunks/punk{a}.png'
    r = requests.get(url=url)
    if r.status_code == 200:
        with open(f'punks/punk{a}.png', 'wb') as f:
            f.write(r.content)
        os.system('clear')
        print(f'Saved punk {i}')
    else:
        print(r.status_code)
    i += 1
