import requests

id = 1

while True:
        try:
                p = requests.get(f'https://vk.com/sticker/1-{id}-128')
                out = open(f'sticker_{id}.png', "wb")
                out.write(p.content)
                out.close()
                id+=1
                print(f'sticker_{id} - успешно')
        except Exception as e:
                print(f'sticker_{id} error: {e}')
                break