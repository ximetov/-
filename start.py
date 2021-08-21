import requests
from datetime import *
import time
token = ''
 
while True:
    today = datetime.today()
    day = today.strftime('%d')
    month = today.strftime('%m')
    year = today.strftime('%Y')
    i = requests.get(f'https://api.vk.com/method/vkRun.setSteps?steps=80000&distance=50000&date={year}-{month}-{day}'
                     f'&v=5.124&access_token={tok}')
    print(i.text)
    print(f'{year}-{month}-{day}')
    time.sleep(86400)