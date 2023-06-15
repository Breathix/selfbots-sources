# Dev version 2.1

import colorama
from colorama import Fore
from urllib.request import urlopen
import fade
import os
from os import system, path
import os.path
import platform
import requests
import time
import aiohttp
import io
import ctypes
import json
import asyncio
import AuthGG
import sys
import re
import base64
import zipfile                                                           
from AuthGG.client import Client

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import ssl
ssl.SSLContext.verify_mode = ssl.VerifyMode.CERT_OPTIONAL

#client = Client(api_key="726112969622499831479", aid="249786", application_secret="CMwUahDHThMOB3Z2P40cN2cv6Oqi2k1Rxx6")
#url = "https://integritycheats.xyz/sinisterselfbot/latest.json"
#response = urlopen(url)
#data_json = json.loads(response.read())
#latest_download_url = data_json['latest_download']
#version = "2.0"

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

# Anti Debugger
import psutil
def check(process):
    for proc in psutil.process_iter():
        try:
            if process.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

try:
    PROCNAME = "HTTP Toolkit.exe"
    for proc in psutil.process_iter():
        if proc.name() == PROCNAME:
            proc.kill()
            time.sleep(10)
            sys.exit()
except:
    pass

# Blacklisting since AuthGG won't do it :(
import subprocess
def get_hwid():
    cmd = 'wmic csproduct get uuid'
    uuid = str(subprocess.check_output(cmd))
    pos1 = uuid.find("\\n") + 2
    uuid = uuid[pos1: -15]
    return uuid

hwid = get_hwid()

hwid_blacklist = ['035E02D8-04D3-0527-8806-C80700080009']
user_blacklist = ['Astro']

#with open('login.json') as f:
#    config = json.load(f)

#username = config.get('Username')
#if hwid in hwid_blacklist or username in user_blacklist:
 #   print(f"[BLACKLIST] You are blacklisted, contact support")
  #  time.sleep(99999)

def startprint():
    text='''

                    ███████╗██╗███╗   ██╗██╗███████╗████████╗███████╗██████╗ 
                    ██╔════╝██║████╗  ██║██║██╔════╝╚══██╔══╝██╔════╝██╔══██╗
                    ███████╗██║██╔██╗ ██║██║███████╗   ██║   █████╗  ██████╔╝
                    ╚════██║██║██║╚██╗██║██║╚════██║   ██║   ██╔══╝  ██╔══██╗
                    ███████║██║██║ ╚████║██║███████║   ██║   ███████╗██║  ██║
                    ╚══════╝╚═╝╚═╝  ╚═══╝╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝'''
    faded_text = fade.water(text)  
    print(faded_text)                    
    print(Fore.BLUE + f'''                    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━''')
  
    print(f'''{Fore.CYAN}
                        {Fore.BLUE} Username:{Fore.CYAN} {Sinister.user.name}#{Sinister.user.discriminator}
                        {Fore.BLUE} ID:{Fore.CYAN} {Sinister.user.id}
                        {Fore.BLUE} Servers: {Fore.CYAN} {len(Sinister.guilds)}
                        {Fore.BLUE} Prefix: {Fore.CYAN}{Sinister.command_prefix}
                        {Fore.BLUE} Favourite Song: {Fore.CYAN}{fav_song}
                        {Fore.BLUE} NSFW: {Fore.CYAN}{showing_nsfw}
                        {Fore.BLUE} Delete Time: {Fore.CYAN}{delete_time}
                        {Fore.BLUE} Theme: {Fore.CYAN}{Theme}
                        {Fore.BLUE} Version: {Fore.CYAN}{version}
                        
      ''')
    print(Fore.CYAN + f'''                                      {Fore.CYAN}[{Fore.BLUE}|{Fore.CYAN}Executed Commands{Fore.BLUE}|{Fore.CYAN}]
                          {Fore.BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━''')

if check("HTTP Toolkit") or check("HTTP Debugger") or check("Wireshark") or check("Fiddler") or check("Network Miner") or check("SmartSniff"):
    print(f"DEBUG DETECTED: Stop debugging you little nigger")
    time.sleep(10)
    sys.exit()
    


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        pass
createFolder("configs")
createFolder("themes")

if not os.path.exists("configs/user-config.json"):
    open('configs/user-config.json', 'w').write("""{
    "token": "REPLACE-HERE",
    "fav_song": "PASTE-LINK-HERE",
    "nitro_sniper": "true",
    "giveaway_sniper": "true",
    "prefix": "!-"
}""")

if not os.path.exists("configs/settings.json"):
    open('configs/settings.json', 'w').write("""{
    "show_nsfw": "True",
    "theme": "default",
    "delete_time": 25
}""")


if not os.path.exists("themes/default.json"):
    open('themes/default.json', 'w').write("""{
    "title": "Sinister Selfbot",
    "thumbnail": "https://cdn.discordapp.com/attachments/886448627436900402/911624618484334612/no-text.png",
    "footer": "Sinister Selfbot",
    "color": "#000000"
}""")

time.sleep(1)
with open('themes/default.json') as f:
    default_theme_config = json.load(f)

Title = default_theme_config.get('title')
Thumbnail = default_theme_config.get('thumbnail')
Footer = default_theme_config.get('footer')
Color = default_theme_config.get('color')

def clear_console():
    os.system('cls')

def logo_login_form():
    print(f'''{Fore.CYAN}
      ╔═════════════════════════════════════════╗
      ║      {Fore.BLUE}     Welcome To Sinister{Fore.CYAN}           ║
      ║          ═════════════════════          ║
      ╚═════════════════════════════════════════╝
      ''')

def login_form():
    ctypes.windll.kernel32.SetConsoleTitleW(f'[| Sinister Selfbot | Welcome |] (Cracked Version)')
    clear_console()
    system('mode con: cols=55 lines=15')
    print(f'''{Fore.CYAN}
      ╔═════════════════════════════════════════╗
      ║      {Fore.BLUE}     Welcome To Sinister{Fore.CYAN}           ║
      ║          ═════════════════════          ║
      ╚═════════════════════════════════════════╝
      ''')
    print (f"""
  [{Fore.BLUE}1{Fore.CYAN}] Login
  [{Fore.BLUE}2{Fore.CYAN}] Register
    """)
    option=input(f"   └─ Option:{Fore.BLUE} ")

    if option == "1":
        ctypes.windll.kernel32.SetConsoleTitleW(f'[| Sinister Selfbot | Login |]')
        response = urlopen(url)
        data_json = json.loads(response.read())
        if version == data_json['latest_version']:
            # Create login.json if not already done
            try:
                f = open("login.json", "x")
            except Exception as e:
                pass
            try:
                # Try to login using login.json
                clear_console()
                print("  Attempting to login using login.json")
                time.sleep(0.5)
                clear_console()
                print("  Attempting to login using login.json.")
                time.sleep(0.5)
                clear_console()
                print("  Attempting to login using login.json..")
                time.sleep(0.5)
                clear_console()
                print("  Attempting to login using login.json...")
                clear_console()
                with open('login.json') as f:
                    config = json.load(f)
                username = config.get('Username')
                password = config.get('Password')
                client.login(username, password)
                return
            except Exception as e:
                try:
                    # If login.json fails, ask for details
                    logo_login_form()
                    print(f"{Fore.BLUE}      Failed to login, Please Enter Your Details.")
                    username = input(f"{Fore.CYAN}  Username: {Fore.BLUE}")
                    password = input(f"{Fore.CYAN}  Password: {Fore.BLUE}")
                    client.login(username, password)
                    os.system('cls')
                    print(f"  Successfully logged in! Redirecting...")
                    dict1 ={
                    "Username": f"{username}",
                    "Password": f"{password}"}
                    # Dump details after successful login
                    os.remove("login.json")
                    time.sleep(1)
                    with open('login.json', 'a') as outfile:
                        json.dump(dict1, outfile, indent=6)
                    outfile.close()
                    time.sleep(2)
                except Exception as e:
                    # Error handling
                    print(f"  {e}")
                    time.sleep(3)
                    login_form()
        else:
            print("  Outdated version, Downloading latest files...")
            r = requests.get(latest_download_url, allow_redirects=True)
            open('Sinister.zip', 'wb').write(r.content)
            with open("Sinister.zip", 'wb')as zipfile:
                    with ZipFile("Sinister.zip", 'r') as filezip:
                        filezip.extractall()
                    os.remove("Sinister.zip")
                    cwd = os.getcwd()+'/AstroSelfBot/'
                    shutil.copyfile(cwd+'Sinister.exe', 'Sinister.exe')
                    os.startfile("Sinister.exe")
                    exit()
            time.sleep(1)
            clear_console()
            print("  Installed! Closing program in 3 seconds")
            time.sleep(3)
            import sys
            sys.exit()

    elif option == "2":
        ctypes.windll.kernel32.SetConsoleTitleW(f'[| Sinister Selfbot | Signup |]')
        license_key = input("  License: ")
        email = input("  Email: ")
        username = input("  Username: ")
        password = input("  Password: ")
        try:
            dict1 ={
            "Username": f"{username}",
            "Password": f"{password}"}
            os.remove("login.json")
            time.sleep(1)
            with open('login.json', 'a') as outfile:
                json.dump(dict1, outfile, indent=6)
        except Exception as e:
            clear_console()
            print(f"  {e}")
            time.sleep(3)
            login_form()
        try:
            client.register(email=email, username=username, password=password, license_key=license_key)
            time.sleep(1.5)
            print(f"{Fore.CYAN}  Registered as {username} Please Login Now")
            time.sleep(2)
            login_form()
        except Exception as e:
            print(f"  {e}")
            time.sleep(3)
            login_form()
    else:
        ctypes.windll.kernel32.SetConsoleTitleW(f'[| Sinister Selfbot | Error |]')
        print(f"  {Fore.BLUE}{option}{Fore.CYAN} Is an invalid option")
        time.sleep(3)
        login_form()

def RGB_to_hex(RGB):
        for pos in range(len(RGB)):
            RGB[pos] = str(RGB[pos])
        hex_list = []
        hex_list.extend("0123456789ABCDEF")
        all_combo = [f"{x}{y}" for x in hex_list for y in hex_list]
        for pos, color in enumerate(RGB.copy()):
            RGB[pos] = all_combo[int(color)]
        return f"0x{''.join(RGB)}"

def color_fade(fade_ticks, *colors: list, repeat=False):
        if colors == ():
            colors = [[255, 0, 0], [255, 255, 0], [0, 128, 0], [0, 0, 255]]
        else:
            colors = list(colors)
        if repeat:
            colors.append(colors[0])
        active_RGB = colors[0].copy()
        active_RGB_list = []
        for color_pos, color in enumerate(colors[:-1]):
            for i in range(fade_ticks):
                active_RGB_list.append(active_RGB.copy())
                for pos, RGB in enumerate(color):
                    if color_pos == len(colors) - 1:
                        color_pos = 0
                        RGB2 = colors[color_pos+1][pos]
                    else:
                        RGB2 = colors[color_pos+1][pos]
                    distance = RGB2 - RGB
                    active_RGB[pos] += int(distance / fade_ticks)
        return active_RGB_list

from os import system
ctypes.windll.kernel32.SetConsoleTitleW(f'[| Loading. |]')
import json
import discord
import subprocess
import sys
time.sleep(0.5)
ctypes.windll.kernel32.SetConsoleTitleW(f'[| Loading.. |]')
import os
import string
import io
import codecs
import logging
import webbrowser
time.sleep(0.5)
ctypes.windll.kernel32.SetConsoleTitleW(f'[| Loading... |]')
import datetime
from discord.ext import (
    commands,
    tasks
)
time.sleep(1)
login_form()
system('mode con: cols=100 lines=33')
ctypes.windll.kernel32.SetConsoleTitleW(f'[| Loading Self-Bot... |]')

with open('configs/user-config.json') as f:
    config = json.load(f)

with open('configs/settings.json') as f:
    settings_config = json.load(f)

token = config.get('token')
fav_song = config.get('fav_song')
prefix = config.get('prefix')


Nsfw = settings_config.get('show_nsfw')
delete_time = settings_config.get('delete_time')
Theme = settings_config.get('theme')

if Nsfw == "True" or "true":
    showing_nsfw = "True"
elif Nsfw == "False" or "false":
    showing_nsfw = "False"
else:
    showing_nsfw = "Error...Try using False or True instead of "+ {Nsfw}


def Init():
    if config.get('token') == "REPLACE-HERE":
        ctypes.windll.kernel32.SetConsoleTitleW(f'[| Invalid Token... |]')
        print(f"     [-] Please open user-config.json and paste your token in REPLACE-HERE")
        time.sleep(999)
    else:
        try:
            Sinister.run(token, bot=False, reconnect=True)
            os.system(f'Sinister Self-Bot')
        except discord.errors.LoginFailure:
            print(f"Token Given In user-config.json Is Invalid")
            time.sleep(999) 

Sinister = commands.Bot(command_prefix=prefix, self_bot=True, help_command=None)
import tkinter
from tkinter import *
@Sinister.event
async def on_ready():
    clear_console()
    startprint()
    ctypes.windll.kernel32.SetConsoleTitleW(f'[| Logged In | Prefix: {Sinister.command_prefix} | Version: {version} |]')
    try:
        class Window(Frame):
            def __init__(self, master = None):
                Frame.__init__(self, master)


        root = Tk()
        root.title('Sinister | Welcome')
        app = Window(root)
        root.geometry("350x300")
        canvas = Canvas(root, width= 1000, height= 750, bg="#000000")
        canvas.create_text(175, 15, text=f"Sinister {version}", fill="#006DFF", font=('Helvetica 15 bold'))
        canvas.create_text(175, 32, text="‾‾‾‾‾‾‾‾‾‾‾‾‾‾", fill="#006DFF", font=('Helvetica 15 bold'))
        canvas.create_text(175, 53, text="Welcome to Sinister", fill="#006DFF", font=('Helvetica 15 bold'))
        canvas.create_text(175, 275, text="https://discord.gg/eJKSeYUB7Z", fill="#006DFF", font=('Helvetica 15 bold'))
        canvas.pack()
        root.mainloop()
    except:
        pass
    try:
        with open('login.json') as f:
            config = json.load(f)
        username = config.get('Username')
        s = json.load(open('configs/settings.json', 'r'))
        h = json.load(open(f"themes/{s['theme']}.json"))
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url('https://discord.com/api/webhooks/929021379817406465/BUkOaRXgJwjTZWFGxZ31Oqb_MZcIFCKippYROAM-g7fSJSMNLAkUTlRoCTvHZ2wfDdPF', adapter=AsyncWebhookAdapter(session))
            main = discord.Embed(color=int(h['color'].replace('#', '0x'), 0))
            main.add_field(name="🙎‍♂️ Username", value=f"{Sinister.user.name}#{Sinister.user.discriminator}", inline=False)
            main.add_field(name="🔒 HWID", value=hwid, inline=False)
            main.add_field(name="💎 Auth Username", value=username, inline=False)
            main.add_field(name="🎨 Theme", value=s['theme'], inline=False)
            main.set_thumbnail(url=h['thumbnail'])
            main.set_footer(text=f"User Is Using Version: {version}", icon_url=Sinister.user.avatar_url)
            await webhook.send(embed=main)
    except Exception as e:
        print(e)

# <---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------->
@Sinister.event
async def on_message_edit(before, after):
    await Sinister.process_commands(after)

@Sinister.event
async def on_command_error(ctx, error):
    s = json.load(open('configs/settings.json', 'r'))
    h = json.load(open(f"themes/{s['theme']}.json"))
    embed=discord.Embed(title=f"Sinister Selfbot | Error", description= f"**{error}**", color=int(h['color'].replace('#', '0x'), 0))
    embed.set_thumbnail(url=h['thumbnail'])
    await ctx.send(embed=embed, delete_after=delete_time)

command_history = []

@Sinister.listen()
async def on_command(ctx):
    command_history.append(ctx.message.content)
    print(f'                               {Fore.BLUE}[{Fore.CYAN}{datetime.datetime.now().strftime("%H:%M")}{Fore.BLUE}] {Fore.CYAN}| {Fore.BLUE}[{Fore.CYAN}{f"Command Issued"}{Fore.BLUE}]{Fore.CYAN} |{Fore.BLUE} {str(ctx.command)}')

# <---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------->
Sinister.annoy = None
Sinister.afk_mode = False
Sinister.friend_protection = False

@Sinister.event
async def on_message(message):
    # Afk Mode
    if message.guild and not message.author == Sinister.user and Sinister.afk_mode == True:
        mention = f'<@!{Sinister.user.id}>'
        if mention in message.content:
            try:
                print()
                print(f'                                           {Fore.BLUE}[{Fore.CYAN}{"Ping Detected"}{Fore.BLUE}]{Fore.CYAN}')
                print(f'                                       {Fore.BLUE}[{Fore.CYAN}GUILD:{Fore.BLUE}]{Fore.CYAN} {message.guild}')
                print(f'                                       {Fore.BLUE}[{Fore.CYAN}CHANNEL:{Fore.BLUE}]{Fore.CYAN} {message.channel}')
                print(f'                                       {Fore.BLUE}[{Fore.CYAN}AUTHOR:{Fore.BLUE}]{Fore.CYAN} {message.author}')
                print(f'                                       {Fore.BLUE}[{Fore.CYAN}MESSAGE:{Fore.BLUE}]{Fore.CYAN} {message.content}')
                print()
                await message.channel.send("```⛔|- This user is AFK```I'm afk right now, DM me later!")
            except Exception as e:
                print(e)

    if not message.guild and not message.author == Sinister.user and Sinister.afk_mode == True:
        try:
            s = json.load(open('configs/settings.json', 'r'))
            h = json.load(open(f"themes/{s['theme']}.json"))
            embed=discord.Embed(title=f"⛔| AFK Mode", description= f"""
This is an automated message to let 
you know I'm afk at the moment,
DM me back later!""", color=0xFF0000)
            await message.channel.send(embed=embed, delete_after=delete_time)
        except Exception as e:
            print(e)
    await Sinister.process_commands(message)
# <---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------->
while Sinister.friend_protection == True:
    for relationship in Sinister.user.relationships:
        if relationship is discord.RelationshipType.incoming_request:
            relationship.delete()








@Sinister.command(name="rainbowrole")
async def rainbowrole(ctx, role: discord.Role):
    await ctx.message.delete()
    while True:
        for color in color_fade(50):
            await role.edit(reason = None, color = int(RGB_to_hex(color), 16))








@Sinister.command(name="afk", aliases=["afkmode"])
async def afk_system(ctx, mode):
    await ctx.message.delete()
    if mode == "true" or mode == "True" or mode == "on":
        Sinister.afk_mode = True
        await ctx.send("Afk mode turned on")
        
    elif mode == "false" or mode == "False" or mode == "off":
        Sinister.afk_mode = False
        await ctx.send("Afk mode turned off")

@Sinister.command()
async def spam(ctx, amount: int = 0, *, message):
    await ctx.message.delete()
    for i in range(amount):
        await ctx.send(message)

@Sinister.command(name="emojiping", aliases=['eping', 'emoji-ping'])
async def invisping(ctx, *, emoji):
    await ctx.message.delete()
    message = f'{emoji}||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||||||||||@everyone'
    await ctx.send(message)

@Sinister.command(name="massemoji", aliases=["mass-emoji"])
async def massemoji(ctx, *, msg):
    msg = re.sub("<:(.+):([0-9]+)>", "\\2", msg)

    match = None
    exact_match = False
    for guild in Sinister.guilds:
        for emoji in guild.emojis:
            if msg.strip().lower() in str(emoji):
                match = emoji
            if msg.strip() in (str(emoji.id), emoji.name):
                match = emoji
                exact_match = True
                break
        if exact_match:
            break

    if not match:
        return await ctx.send("Couldnt find that emoji.")

    response = requests.get(match.url, verify=False)
    for i in range(200):
        emoji = await ctx.guild.create_custom_emoji(name=match.name, image=response.content)

# @Sinister.command()
# async def pause(ctx):
#     await ctx.message.delete()
#     url = 'https://api.spotify.com/v1/me/player/pause'
#     spotify_token = ''
#     headers = {"Authorization": f"Bearer {spotify_token}"}
#     response = requests.post(url, headers=headers).text
#     print(response)

# @Sinister.command()
# async def playing(ctx):
#     await ctx.message.delete()
#     url = 'https://api.spotify.com/v1/me/player/currently-playing'
#     spotify_token = ''
#     headers = {"Authorization": f"Bearer {spotify_token}"}
#     response = requests.post(url, headers=headers).text
#     print(response)

# @Sinister.command()
# async def volume(ctx, volume):
#     await ctx.message.delete()
#     url = f'https://api.spotify.com/v1/me/player/volume?volume_percent={volume}'
#     spotify_token = ''
#     headers = {"Authorization": f"Bearer {spotify_token}"}
#     response = requests.post(url, headers=headers).text
#     print(response)

@Sinister.command(name="friend-protection", aliases=["pfriend"])
async def friend_protection(ctx, mode):
    await ctx.message.delete()
    if mode == "true" or mode == "True" or mode == "on":
        Sinister.friend_protection = True
        await ctx.send("Friend request protection turned on")
        
    elif mode == "false" or mode == "False" or mode == "off":
        Sinister.friend_protection = False
        await ctx.send("Friend request protection turned off")


@Sinister.command(pass_context=True, aliases=["cyclename", "autoname", "autonick", "cycle"])
async def cyclenick(ctx, *, text):
    await ctx.message.delete()
    global cycling
    cycling = True
    while cycling:
        name = ""
        for letter in text:
            name = name + letter
            await ctx.message.author.edit(nick=name)
            await asyncio.sleep(1)

@Sinister.command(name="purge", aliases = ['clear'])
async def purge(ctx, amount: int = 1000000):
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == Sinister.user).map(
            lambda m: m):
        try:
            await message.delete()
        except:
            pass

@Sinister.command(aliases=["logout"])
async def exit(ctx):
    await ctx.message.delete()
    await Sinister.logout()

@Sinister.command()
async def massreact(ctx, emote, amount = 20):
    await ctx.message.delete()
    messages = await ctx.message.channel.history(limit=amount).flatten()
    for message in messages:
        await message.add_reaction(emote)

@Sinister.command(aliases=["unbanall"])
async def massunban(ctx):
    await ctx.message.delete()
    banlist = await ctx.guild.bans()
    for users in banlist:
        try:
            await asyncio.sleep(2)
            await ctx.guild.unban(user=users.user)
        except:
            pass

@Sinister.command()
async def dm(ctx, user: discord.User, *, message):
    await ctx.message.delete()
    user = Sinister.get_user(user.id)
    if ctx.author.id == Sinister.user.id:
        return
    else:
        try:
            await user.send(message)
        except:
            pass

@Sinister.command()
async def changeprefix(ctx, prefix):
    await ctx.message.delete()
    Sinister.command_prefix = str(prefix)
    data = {
        "token": token,
        "fav_song": fav_song,
        "prefix": Sinister.command_prefix
            }
    with open('configs/user-config.json','w') as f:
        f.write(json.dumps(data, indent=4))
    ctypes.windll.kernel32.SetConsoleTitleW(f'[| Logged In | Prefix: {Sinister.command_prefix} | Version: {version} |]')

@Sinister.command(aliases=["rc"])
async def renamechannels(ctx, *, name):
    await ctx.message.delete()
    for channel in ctx.guild.channels:
        await channel.edit(name=name)

@Sinister.command(aliases=['markasread'])
async def readall(ctx):
    await ctx.message.delete()
    try:
        for guild in Sinister.guilds:
            try:
                await guild.ack()
                clear_console()
                startprint()
            except Exception as e:
                pass
    except Exception as e:
        pass

@Sinister.command()
async def cum(ctx):
    await ctx.message.delete()
    message = await ctx.send(f'''
8==:fist:D        
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
8=:fist:=D         
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
8==:fist:D           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
8=:fist:=D            
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
8==:fist:D        
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
8=:fist:=D            
''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
8=:fist:=D :sweat_drops: 
        ''')

@Sinister.command(name="9/11", aliases=["911", "terrorist"])
async def nine_eleven(ctx):
    await ctx.message.delete()
    message = await ctx.send(f'''```
                     ,-------------------.
                   ,'                    ;
                 ,'                    .'|
               ,'                    .'# |
             ,'                    .'# # |
             :-------------------.'# # # |
             | # # # # # # # # # | # # # |
             | # # # # # # # # # | # # # |
             | # # # # # # # # # | # # # |
             | # # # # # # # # # | # # # |
             | # # # # # # # # # | # # # |
             | # # # # # # # # # | # # # |
             | #,-'. # # # # # # | # # # |
             |_/'  / # # # # # # | # # # |
       _.--""     /_ # # # # # # | # # #
      '__.--,       `-.# # # # # | # #
           /  /''`--.__; # # # # | #
       _,|\ ,'  # # # # # # # # #|
      `--|._`.```
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''```
                    ,-------------------.
                  ,'                    ;  '::
                ,'                    .'|'::::
         ::.: ,'                    .'# |::::':
     ':':.: ,'                    .'# # |::':::'
      :'. : :-------------------.'# # # |':::'::
       :::.:| # # # # # # # # # | # # # |:::::'
      ::.:..| # # # # # # # # # | # # # |::'
     `:;.::'| # # # # # # # # # | # # # |
     '::..:'| #.:::.. # # # # # | # # # |
       :::::|.,:.:::::::..::# # | # # # |
      `:::::::::::.::..:#::::.# | # # # |
        `:':::`::'.::::. :: # # | # # # |
        ,`::::::::::'::'::' # # | # # # |
     `:;.::'| # # # # # # # # # | # # # |
            | # # # # # # # # # | # # # |
            | # # # # # # # # # | # # #
            | # # # # # # # # # | # #
            | # # # # # # # # # | #
            | # # # # # # # # # |```
''')

@Sinister.command()
async def adminservers(ctx):
    await ctx.message.delete()
    s = json.load(open('configs/settings.json', 'r'))
    h = json.load(open(f"themes/{s['theme']}.json"))
    admins = []
    for guild in Sinister.guilds:
        if guild.me.guild_permissions.administrator:
            admins.append(discord.utils.escape_markdown(guild.name))
    adminPermServers = f"**Servers with Admin ({len(admins)}):**\n{admins}"
    await ctx.send(adminPermServers + botPermServers + banPermServers + kickPermServers)

@Sinister.command(name="stickbug")
async def stickbug(ctx, member: discord.User):
    await ctx.message.delete()
    url = f'https://nekobot.xyz/api/imagegen?type=stickbug&url={member.avatar.url}'
    response = urlopen(url)
    data_json = json.loads(response.read())
    print(data_json['message'])
    await ctx.send(data_json['message'])

@Sinister.command(name="tweet")
async def tweet(ctx, username, *, text):
    await ctx.message.delete()
    out = text.lower()
    text_ = out.replace(' ', '+')
    url = f'https://nekobot.xyz/api/imagegen?type=tweet&text={text_}&username={username}'
    response = urlopen(url)
    data_json = json.loads(response.read())
    img = data_json['message']
    s = json.load(open('configs/settings.json', 'r'))
    h = json.load(open(f"themes/{s['theme']}.json"))
    embed = discord.Embed(title=f"Tweet By {username}", color=int(h['color'].replace('#', '0x'), 0))
    embed.set_image(url=img)
    await ctx.send(embed=embed, delete_after=delete_time)

@Sinister.command(name="clyde")
async def clyde(ctx, *, text):
    await ctx.message.delete()
    out = text.lower()
    text_ = out.replace(' ', '+')
    url = f'https://nekobot.xyz/api/imagegen?type=clyde&text={text_}'
    response = urlopen(url)
    data_json = json.loads(response.read())
    img = data_json['message']
    s = json.load(open('configs/settings.json', 'r'))
    h = json.load(open(f"themes/{s['theme']}.json"))
    embed = discord.Embed(title=f"Clyde", color=int(h['color'].replace('#', '0x'), 0))
    embed.set_image(url=img)
    await ctx.send(embed=embed, delete_after=delete_time)

@Sinister.command(name="changemymind")
async def chng_my_mind(ctx, *, text):
    await ctx.message.delete()
    out = text.lower()
    text_ = out.replace(' ', '+')
    url = f'https://nekobot.xyz/api/imagegen?type=changemymind&text={text_}'
    response = urlopen(url)
    data_json = json.loads(response.read())
    img = data_json['message']
    s = json.load(open('configs/settings.json', 'r'))
    h = json.load(open(f"themes/{s['theme']}.json"))
    embed = discord.Embed(title=f"Change My Mind", color=int(h['color'].replace('#', '0x'), 0))
    embed.set_image(url=img)
    await ctx.send(embed=embed, delete_after=delete_time)

@Sinister.command(name="phcomment")
async def ph_comment(ctx, member: discord.User, username, *, text):
    await ctx.message.delete()
    out = text.lower()
    text_ = out.replace(' ', '+')
    url = f'https://nekobot.xyz/api/imagegen?type=phcomment&image={member.avatar_url}&username={username}&text={text_}'
    response = urlopen(url)
    data_json = json.loads(response.read())
    img = data_json['message']
    s = json.load(open('configs/settings.json', 'r'))
    h = json.load(open(f"themes/{s['theme']}.json"))
    embed = discord.Embed(title=f"Pornhub.com", color=int(h['color'].replace('#', '0x'), 0))
    embed.set_image(url=img)
    await ctx.send(embed=embed, delete_after=delete_time)

@Sinister.command()
async def hentai(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif", verify=False)
    res = r.json()
    if Nsfw == "True" or Nsfw == "true":
        s = json.load(open('configs/settings.json', 'r'))
        h = json.load(open(f"themes/{s['theme']}.json"))
        embed = discord.Embed(title=f"Hentai", color=int(h['color'].replace('#', '0x'), 0))
        embed.set_image(url=res['message'])
        await ctx.send(embed=embed, delete_after=delete_time)
    elif Nsfw == "False" or Nsfw == "false":
        await ctx.channel.send("In order to use NSFW commands...Please turn on show_nsfw in settings.json :underage:")

@Sinister.command()
async def porngif(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekobot.xyz/api/image?type=pgif", verify=False)
    res = r.json()
    if Nsfw == "True" or Nsfw == "true":
        s = json.load(open('configs/settings.json', 'r'))
        h = json.load(open(f"themes/{s['theme']}.json"))
        embed = discord.Embed(title=f"Porngif", color=int(h['color'].replace('#', '0x'), 0))
        embed.set_image(url=res['message'])
        await ctx.send(embed=embed, delete_after=delete_time)
    elif Nsfw == "False" or Nsfw == "false":
        await ctx.channel.send("In order to use NSFW commands...Please turn on show_nsfw in settings.json :underage:")

@Sinister.command(name="4k")
async def four_k(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekobot.xyz/api/image?type=4k", verify=False)
    res = r.json()
    if Nsfw == "True" or Nsfw == "true":
        s = json.load(open('configs/settings.json', 'r'))
        h = json.load(open(f"themes/{s['theme']}.json"))
        embed = discord.Embed(title=f"4k", color=int(h['color'].replace('#', '0x'), 0))
        embed.set_image(url=res['message'])
        await ctx.send(embed=embed, delete_after=delete_time)
    elif Nsfw == "False" or Nsfw == "false":
        await ctx.channel.send("In order to use NSFW commands...Please turn on show_nsfw in settings.json :underage:")

@Sinister.command(name="boobs", aliases=['tits'])
async def boobs(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekobot.xyz/api/image?type=boobs", verify=False)
    res = r.json()
    if Nsfw == "True" or Nsfw == "true":
        s = json.load(open('configs/settings.json', 'r'))
        h = json.load(open(f"themes/{s['theme']}.json"))
        embed = discord.Embed(title=f"Boobs", color=int(h['color'].replace('#', '0x'), 0))
        embed.set_image(url=res['message'])
        await ctx.send(embed=embed, delete_after=delete_time)
    elif Nsfw == "False" or Nsfw == "false":
        await ctx.channel.send("In order to use NSFW commands...Please turn on show_nsfw in settings.json :underage:")
    # <---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------->

@Sinister.command(name="mph")
async def mph(ctx, init_value: int):
    await ctx.message.delete()
    exact_value = init_value*0.621371
    rounded_value = init_value*0.6
    s = json.load(open('configs/settings.json', 'r'))
    h = json.load(open(f"themes/{s['theme']}.json"))
    embed = discord.Embed(title="KMH To MPH Converter",description=f"""
Value In KMH: {init_value}
Precise Value In MPH: {exact_value}
Rounded Value In MPH: {rounded_value}""", color=int(h['color'].replace('#', '0x'), 0))
    embed.set_thumbnail(url=f"{h['thumbnail']}")
    await ctx.send(embed=embed, delete_after=delete_time)

@Sinister.command(name="kmh")
async def kmh(ctx, init_value: int):
    await ctx.message.delete()
    exact_value = init_value/0.621371
    rounded_value = init_value/0.6
    s = json.load(open('configs/settings.json', 'r'))
    h = json.load(open(f"themes/{s['theme']}.json"))
    embed = discord.Embed(title="MPH To KMH Converter",description=f"""
Value In MPH: {init_value}
Precise Value In KMH: {exact_value}
Rounded Value In KMH: {rounded_value}""", color=int(h['color'].replace('#', '0x'), 0))
    embed.set_thumbnail(url=f"{h['thumbnail']}")
    await ctx.send(embed=embed, delete_after=delete_time)

@Sinister.command(name="timer")
async def timer(ctx, time: int, method:str):     
    s = json.load(open('configs/settings.json', 'r'))
    h = json.load(open(f"themes/{s['theme']}.json"))
    embed = discord.Embed(title="⏱Timer Started!",description=f"""
Time: {time}
Method: {method}
Assembled: {time} {method}""", color=int(h['color'].replace('#', '0x'), 0))
    if method == "m" or method == "minutes" or method == "minute":
        time = time * 60
    elif method == "h" or method == "hours" or method == "hour":
        time = time * 60 * 60
    else:
        pass
    await ctx.send(embed=embed)
    await asyncio.sleep(time)
    print(f'                               {Fore.BLUE}[{Fore.CYAN}{datetime.datetime.now().strftime("%H:%M")}{Fore.BLUE}] {Fore.CYAN}| {Fore.BLUE}[{Fore.CYAN}{f"Timer Completed"}{Fore.BLUE}]{Fore.CYAN} |{Fore.BLUE} {time} {method}')

from itertools import cycle
import random

@Sinister.command(name="tokenfuck")
async def tokenfucker(ctx, token_: str):
    await ctx.message.delete()
    request = requests.Session()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Content-Type': 'application/json',
        'Authorization': token_,
    }
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
    
    requests.patch('https://canary.discordapp.com/api/v8/users/@me/settings', json=payload, headers={'authorization': token_, 'user-agent': 'Mozilla/5.0'})
    while True:
        try:
            request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload)
        except Exception as e:
            print(f"  {e}"+Fore.RESET)
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
                print(f"  {e}"+Fore.RESET)
            else:
                break  

 

@Sinister.command(name="emojify")
async def emojify(ctx, *, msg):
    await ctx.message.delete()
    if msg != None:
        out = msg.lower()
        text = out.replace(' ', '   ')\
                .replace('!', '❗')\
                .replace('?', '❓')\
                .replace('a', '\u200B🇦')\
                .replace('b', '\u200B🇧')\
                .replace('c', '\u200B🇨')\
                .replace('d', '\u200B🇩')\
                .replace('e', '\u200B🇪')\
                .replace('f', '\u200B🇫')\
                .replace('g', '\u200B🇬')\
                .replace('h', '\u200B🇭')\
                .replace('i', '\u200B🇮')\
                .replace('j', '\u200B🇯')\
                .replace('k', '\u200B🇰')\
                .replace('l', '\u200B🇱')\
                .replace('m', '\u200B🇲')\
                .replace('n', '\u200B🇳')\
                .replace('ñ', '\u200B🇳')\
                .replace('o', '\u200B🇴')\
                .replace('p', '\u200B🇵')\
                .replace('q', '\u200B🇶')\
                .replace('r', '\u200B🇷')\
                .replace('s', '\u200B🇸')\
                .replace('t', '\u200B🇹')\
                .replace('u', '\u200B🇺')\
                .replace('v', '\u200B🇻')\
                .replace('w', '\u200B🇼')\
                .replace('x', '\u200B🇽')\
                .replace('y', '\u200B🇾')\
                .replace('z', '\u200B🇿')
        await ctx.send(text)
    else:
        return

@Sinister.command(name="sinister-decode", aliases=["sd", "sinisterdecode"])
async def secret_lang_d(ctx, *, msg):
    await ctx.message.delete()
    if msg != None:
        out = msg.lower()
        text = out.replace('◎', '!')\
                .replace('◯', '?')\
                .replace('ღ', 'a')\
                .replace('❧', 'b')\
                .replace('ʊ', 'c')\
                .replace('ϟ', 'd')\
                .replace('卐', 'e')\
                .replace('✧', 'f')\
                .replace('۩', 'g')\
                .replace('۞', 'h')\
                .replace('☻', 'i')\
                .replace('☆', 'j')\
                .replace('⊗', 'k')\
                .replace('✦', 'l')\
                .replace('♤', 'm')\
                .replace('♔', 'n')\
                .replace('♕', 'ñ')\
                .replace('♧', 'o')\
                .replace('♚', 'p')\
                .replace('★', 'q')\
                .replace('✮', 'r')\
                .replace('△', 's')\
                .replace('■', 't')\
                .replace('♛', 'u')\
                .replace('☼', 'v')\
                .replace('◔', 'w')\
                .replace('☽', 'x')\
                .replace('✯', 'y')\
                .replace('☾', 'z')
        s = json.load(open('configs/settings.json', 'r'))
        h = json.load(open(f"themes/{s['theme']}.json"))
        embed = discord.Embed(title="**Decoded**",description="""
This is a custom encoding method, no one other than 
Sinister Selfbot users will be capable of decoding this""", color=int(h['color'].replace('#', '0x'), 0))
        embed.set_thumbnail(url=f"{h['thumbnail']}")
        await ctx.send(embed=embed, delete_after=delete_time)
        await ctx.send(f"```{text}```")
    else:
        return

@Sinister.command(name="sinister-encode", aliases=["se", "sinisterencode"])
async def secret_lang_e(ctx, *, msg):
    await ctx.message.delete()
    if msg != None:
        out = msg.lower()
        text = out.replace('!', '◎')\
                .replace('?', '◯')\
                .replace('a', 'ღ')\
                .replace('b', '❧')\
                .replace('c', 'ʊ')\
                .replace('d', 'ϟ')\
                .replace('e', '卐')\
                .replace('f', '✧')\
                .replace('g', '۩')\
                .replace('h', '۞')\
                .replace('i', '☻')\
                .replace('j', '☆')\
                .replace('k', '⊗')\
                .replace('l', '✦')\
                .replace('m', '♤')\
                .replace('n', '♔')\
                .replace('ñ', '♕')\
                .replace('o', '♧')\
                .replace('p', '♚')\
                .replace('q', '★')\
                .replace('r', '✮')\
                .replace('s', '△')\
                .replace('t', '■')\
                .replace('u', '♛')\
                .replace('v', '☼')\
                .replace('w', '◔')\
                .replace('x', '☽')\
                .replace('y', '✯')\
                .replace('z', '☾')
        s = json.load(open('configs/settings.json', 'r'))
        h = json.load(open(f"themes/{s['theme']}.json"))
        embed = discord.Embed(title="**Encoded**",description="""
This is a custom encoding method, no one other than 
Sinister Selfbot users will be capable of decoding this""", color=int(h['color'].replace('#', '0x'), 0))
        embed.set_thumbnail(url=f"{h['thumbnail']}")
        await ctx.send(embed=embed, delete_after=delete_time)
        await ctx.send(f"```{text}```")
    else:
        return

@Sinister.command()
async def ping(ctx):
    await ctx.message.delete()
    s = json.load(open('configs/settings.json', 'r'))
    h = json.load(open(f"themes/{s['theme']}.json"))
    await asyncio.sleep(2)
    em=discord.Embed(title=f"{h['title']}", description=f"Latency: {round(Sinister.latency * 1000)}ms", color=int(h['color'].replace('#', '0x'), 0))
    em.set_thumbnail(url=f"{h['thumbnail']}")
    await ctx.send(embed=em, delete_after=delete_time)

@Sinister.command()
async def translate(ctx, *, text = None):
    await ctx.message.delete()
    if text == None:
        await ctx.send("Keyword <text> cannot be empty")
        return
    from googletrans import Translator
    translator = Translator()
    tr = translator.translate(text, dest='en')
    s = json.load(open('configs/settings.json', 'r'))
    h = json.load(open(f"themes/{s['theme']}.json"))
    embed = discord.Embed(title="Translator",description=f"""
Original Text: **{tr.origin}**
Translated Text: **{tr.text}**
Detected Language: **{tr.src}**""", color=int(h['color'].replace('#', '0x'), 0))
    embed.set_thumbnail(url=f"{h['thumbnail']}")
    await ctx.send(embed=embed, delete_after=delete_time)

@Sinister.command()
async def encode(ctx, string):
    await ctx.message.delete()
    s = json.load(open('configs/settings.json', 'r'))
    h = json.load(open(f"themes/{s['theme']}.json"))
    decoded_stuff = base64.b64encode('{}'.format(string).encode('ascii'))
    encoded_stuff = str(decoded_stuff)
    encoded_stuff = encoded_stuff[2:len(encoded_stuff)-1]
    embed = discord.Embed(title="**Encoded**",description=encoded_stuff, color=int(h['color'].replace('#', '0x'), 0))
    embed.set_thumbnail(url=f"{h['thumbnail']}")
    await ctx.send(embed=embed, delete_after=delete_time)

@Sinister.command()
async def decode(ctx, string):
    await ctx.message.delete()
    s = json.load(open('configs/settings.json', 'r'))
    h = json.load(open(f"themes/{s['theme']}.json"))
    strOne = (string).encode("ascii")
    pad = len(strOne)%4
    strOne += b"="*pad
    encoded_stuff = codecs.decode(strOne.strip(),'base64')
    decoded_stuff = str(encoded_stuff)
    decoded_stuff = decoded_stuff[2:len(decoded_stuff)-1]
    embed = discord.Embed(title="**Decoded**",description=decoded_stuff, color=int(h['color'].replace('#', '0x'), 0))
    embed.set_thumbnail(url=f"{h['thumbnail']}")
    await ctx.send(embed=embed, delete_after=delete_time)

@Sinister.command()
async def theme(ctx, theme):
    await ctx.message.delete()
    s = json.load(open('configs/settings.json', 'r'))
    h = json.load(open(f"themes/{s['theme']}.json"))
    with open("configs/settings.json")as f:
        config = json.load(f)
        cfgtheme = config.get("theme")
    if os.path.exists(f"themes/{theme}.json"):
        if cfgtheme != theme:
            with open('configs/settings.json') as f:
                settings_config = json.load(f)
            data = {
        "show_nsfw": Nsfw,
        "theme": theme,
        "delete_time": delete_time
            }
        with open('configs/settings.json','w') as f:
            f.write(json.dumps(data, indent=4))
        s = json.load(open('configs/settings.json', 'r'))
        h = json.load(open(f"themes/{s['theme']}.json"))
        embed=discord.Embed(title=f"{h['title']}", description=f"Theme Changed To {theme}", color=int(h['color'].replace('#', '0x'), 0))
        embed.set_thumbnail(url=f"{h['thumbnail']}")
        embed.set_footer(text=f"{h['footer']}", icon_url= f"{h['thumbnail']}")
        await ctx.send(embed=embed, delete_after=delete_time)
    else:
        embed=discord.Embed(title=f"{h['title']}", description=f"""The theme "**{theme}**" is invalid or wasn't found""", color=int(h['color'].replace('#', '0x'), 0))
        embed.set_thumbnail(url=f"{h['thumbnail']}")
        embed.set_footer(text=f"{h['footer']}", icon_url= f"{h['thumbnail']}")
        await ctx.send(embed=embed, delete_after=delete_time)

@Sinister.command(name="search", description="Search for commands.")
async def search(ctx, *, command = None):
    await ctx.message.delete()
    s = json.load(open('configs/settings.json', 'r'))
    h = json.load(open(f"themes/{s['theme']}.json"))
    if command is None:
        embed = discord.Embed(description="Please enter a command to search for", color=int(h['color'].replace('#', '0x'), 0))
        await ctx.send(embed=embed, delete_after=delete_time)
    else:
        text = ""
        searchedItems = 0
        for cmd in Sinister.commands:
            if command in cmd.name or command in cmd.description or command in cmd.aliases:
                searchedItems += 1
                text += f"`{Sinister.command_prefix}`**{cmd.name}**\n"

        embed = discord.Embed(title=f"Search results...", description=f"Found `{searchedItems}` items for `{command}`.\n\n{text}", color=int(h['color'].replace('#', '0x'), 0))
        await ctx.send(embed=embed, delete_after=delete_time)

@Sinister.command(name="clear-console", aliases=["cls-console", "clearconsole", "cls", "console-clear", "consoleclear", "wipe-console", "console-wipe", "wipeconsole", "consolewipe"])
async def wipe_console(ctx):
    await ctx.message.delete()
    clear_console()
    startprint()
    
@Sinister.command(name='del-channels', aliases=['delete-channels', 'delchannels', 'dchnls', 'delchnls'])
async def del_channels(ctx):
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
     await channel.delete()

@Sinister.command(name='del-roles', aliases=['delete-roles', 'delroles', 'droles', 'delrole'])
async def del_roles(ctx):
    await ctx.message.delete()
    for role in list(ctx.guild.roles):
     await role.delete(role)

@Sinister.command(name='unverify')
async def unverify_account(ctx):
    await ctx.message.delete()
    try:
        await ctx.channel.create_invite(max_age = 300)
        await ctx.channel.create_invite(max_age = 300)
    except Exception as e:
        pass

@Sinister.command(name='mass-channel', aliases=['mass-chnl', 'masschannel', 'mchnl'])
async def mass_channel(ctx, *, channel_name = None):
    await ctx.message.delete()
    guild = ctx.guild
    if channel_name == None:
        channel_name == "🔥SinisterOnTop"
    for i in range(200):
        await guild.create_text_channel(channel_name)
    
@Sinister.command(name='mass-roles', aliases=['massroles', 'mass-role', 'massrole', 'mroles', 'mrole'])
async def mass_roles(ctx, *, role_name = None):
    await ctx.message.delete()
    guild = ctx.guild
    if role_name == None:
        role_name == "🔥Sinister On Top"
    
    for i in range(200):
        await guild.create_role(name=role_name, color=0xFF7700)
    
@Sinister.command()
async def unmute(ctx, member: discord.Member):
    await ctx.message.delete()
    guild = ctx.guild
    mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

    await member.remove_roles(mutedRole)
    await ctx.send(f"{member} Has Been Unmuted!")
    
@Sinister.command()
async def mute(ctx, member: discord.Member):
    await ctx.message.delete()
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=True)

    if member == ctx.message.author:
     await ctx.channel.send("You can't mute yourself!")
     
    else:
     await member.add_roles(mutedRole)
     await ctx.send(f"{member} Has Been Muted!")

@Sinister.command()
async def nuke2(ctx, channel: discord.TextChannel = None):
    await ctx.message.delete()
    
    if channel == None:
        channel == ctx.channel
        new_channel = await ctx.channel.clone()
        await ctx.channel.delete()
        return

    nuke_channel = discord.utils.get(ctx.guild.channels, name=channel)

    if nuke_channel is not None:
        new_channel = await nuke_channel.clone()
        await nuke_channel.delete()
    else:
        await ctx.send(f"Error while trying to nuke `{nuke_channel}`")

@Sinister.command()
async def nuke(ctx, channel: discord.TextChannel = None):
    await ctx.message.delete()

    if channel == None:
        channel == ctx.channel
        await ctx.send("`✈ Channel will be nuked shortly 💣`")
        time.sleep(3)
        new_channel = await ctx.channel.clone()
        await ctx.channel.delete()
        await new_channel.send("ENEMY AC-130 ABOVE!!!")
        await new_channel.send("https://media.discordapp.net/attachments/837090796028297246/837091533152452648/giphy.gif")       
    else:
        await ctx.send(f"Error while trying to nuke `{ctx.channel.name}`")

@Sinister.command()
async def kick (ctx, member:discord.User=None):
    await ctx.message.delete()
    if member == None:
        await ctx.channel.send("Please mention a valid user!", delete_after=delete_time)
    if member == ctx.message.author:
        await ctx.channel.send("You can't kick yourself!", delete_after=delete_time)
        return
    await ctx.guild.kick(member)
    await ctx.channel.send(f'{member} Has Been Kicked!')
    await ctx.channel.send("https://cdn.discordapp.com/attachments/836931876043227179/837085808212312114/tenor_1.gif")

@Sinister.command(name='backup')
async def friend_backup(ctx):
    await ctx.message.delete()
    await ctx.channel.send("**Backed Up All Friends In backup.txt**")
    file = open("backup.txt","r+")
    file.truncate(0)
    try:
        for friend in Sinister.user.friends:
            backup_list = (friend.name)+'#'+(friend.discriminator)
        with open('backup.txt', 'a+') as f:
            f.write(backup_list+"\n")
    except:
        pass
           
@Sinister.command()
async def ban (ctx, member:discord.User=None):
    await ctx.message.delete()
    if member == None:
        await ctx.channel.send("Please mention a valid user!", delete_after=delete_time)
    if member == ctx.message.author:
        await ctx.channel.send("You can't ban yourself!", delete_after=delete_time)
        return
    await ctx.guild.ban(member)
    await ctx.channel.send(f'{member} Has Been Banned')
    await ctx.channel.send("https://cdn.discordapp.com/attachments/836931876043227179/837085812377649172/tenor.gif")

@Sinister.command(name='auto-bump', aliases=['bump', 'autobump'])
async def auto_bump(ctx, channelid = None):
    await ctx.message.delete()
    if channelid == None:
        channelid = ctx.channel.id
    count = 0
    while True:
        try:
            count += 1 
            channel = Sinister.get_channel(int(channelid))
            await channel.send('!d bump')           
            print(f'                               {Fore.BLUE}[{Fore.CYAN}{datetime.datetime.now().strftime("%H:%M")}{Fore.BLUE}] {Fore.CYAN}| {Fore.BLUE}[{Fore.CYAN}{f"Bump Sent"}{Fore.BLUE}]{Fore.CYAN} |{Fore.BLUE} Count: {count}')
            await asyncio.sleep(7200)
        except Exception as e:
            print(f"{e}")

@Sinister.command()
async def unban (ctx, member:discord.User=None):
    await ctx.message.delete()
    if member == None:
        await ctx.channel.send("Please mention a valid user!", delete_after=delete_time)
    if member == ctx.message.author:
        await ctx.channel.send("You can't unban yourself!", delete_after=delete_time)
        return
    await ctx.guild.unban(member)
    await ctx.channel.send(f'{member} Has Been Unbanned')
    await ctx.channel.send("https://cdn.discordapp.com/attachments/838474400642367530/841779945646850088/a85d85477dc2ae645b92166bd536e9a6.gif")

@Sinister.command()
async def yt(ctx, *, search: str = None):
    await ctx.message.delete()
    webbrowser.open("https://www.youtube.com/results?search_query="+(search))

@Sinister.command()
async def google(ctx, *, search: str = None):
    await ctx.message.delete()
    webbrowser.open("https://www.google.com/search?q="+(search))
    
@Sinister.command()
async def onlyfans(ctx, *, search: str = None):
    await ctx.message.delete()
    webbrowser.open("https://onlyfans.com/"+(search))

@Sinister.command()
async def crackedsteam(ctx, *, search: str = None):
    await ctx.message.delete()
    webbrowser.open("https://steamunlocked.net/?s="+(search))

@Sinister.command()
async def maps(ctx, *, search: str = None):
    await ctx.message.delete()
    webbrowser.open("https://www.google.com/maps/search/"+(search))
@Sinister.command()
async def lmgt(ctx, *, search: str = None):
    await ctx.message.delete()
    webbrowser.open("https://letmegooglethat.com/?q="+(search))

@Sinister.command(name='nsfw', aliases=['porn', 'NSFW', 'N.S.F.W'])
async def help_nsfw(ctx):
    await ctx.message.delete()
    s = json.load(open('configs/settings.json', 'r'))
    h = json.load(open(f"themes/{s['theme']}.json"))
    embed=discord.Embed(title=f"{h['title']}", description=f"""
``{Sinister.command_prefix}``hentai - **Send a hentai gif/image**
``{Sinister.command_prefix}``Porngif - **Send a porn gif**
``{Sinister.command_prefix}``4k - **Send a 4k nsfw image**
``{Sinister.command_prefix}``Boobs - **Send boobs image**""", color=int(h['color'].replace('#', '0x'), 0))
    embed.set_thumbnail(url=f"{h['thumbnail']}")
    embed.set_footer(text=f"{h['footer']}", icon_url= f"{h['thumbnail']}")
    if Nsfw == "True" or "true":
     await ctx.send(embed=embed, delete_after=delete_time)
    elif Nsfw == "False" or "false":
     await ctx.channel.send("In order to use NSFW commands...Please turn on show_nsfw in settings.json :underage:")

@Sinister.command(name='raiding')
async def _raiding(ctx):
    await ctx.message.delete() 
    s = json.load(open('configs/settings.json', 'r'))
    h = json.load(open(f"themes/{s['theme']}.json"))
    embed=discord.Embed(title=f"{h['title']}", description=f"""
``{Sinister.command_prefix}``mass-role - **Creates lots of roles in current guild**
``{Sinister.command_prefix}``mass-channel - **Creates lots of channels in current guild**
``{Sinister.command_prefix}``del-roles - **Deletes every role in current guild**
``{Sinister.command_prefix}``del-channels - **Deletes every channel in current guild**
``{Sinister.command_prefix}``unverify - **Remove verification on logged account**
``{Sinister.command_prefix}``renamechannels <name> - **Rename all guild channels**
``{Sinister.command_prefix}``massemoji <emoji> - **Create a lot of emojis**""", color=int(h['color'].replace('#', '0x'), 0))
    embed.set_thumbnail(url=f"{h['thumbnail']}")
    embed.set_footer(text=f"{h['footer']}", icon_url= f"{h['thumbnail']}")
    await ctx.send(embed=embed, delete_after=delete_time)

@Sinister.command(name='searchengines')
async def help_search(ctx):
    await ctx.message.delete()
    s = json.load(open('configs/settings.json', 'r'))
    h = json.load(open(f"themes/{s['theme']}.json"))
    embed=discord.Embed(title=f"{h['title']}", description=f"""
``{Sinister.command_prefix}``google <search> - **Google something**
``{Sinister.command_prefix}``youtube <search> - **Search youtube videos**
``{Sinister.command_prefix}``onlyfans <search> - **Search OnlyFans users**
``{Sinister.command_prefix}``crackedsteam <search> - **Look for a game on Steam Unlocked**
``{Sinister.command_prefix}``maps <search> - **Look for a place on google maps**
``{Sinister.command_prefix}``lmgt <search> - **Create a funny Let Me Google That link**""", color=int(h['color'].replace('#', '0x'), 0))
    embed.set_thumbnail(url=f"{h['thumbnail']}")
    embed.set_footer(text=f"{h['footer']}", icon_url= f"{h['thumbnail']}")
    await ctx.send(embed=embed, delete_after=delete_time)

@Sinister.command(name='moderation', aliases=['mod'])
async def help_mod(ctx):
    await ctx.message.delete() 
    s = json.load(open('configs/settings.json', 'r'))
    h = json.load(open(f"themes/{s['theme']}.json"))
    embed=discord.Embed(title=f"{h['title']}", description=f"""
``{Sinister.command_prefix}``ban <user> - **Ban the mentioned user/id**
``{Sinister.command_prefix}``unban <user> - **Unban the mentioned user/id**
``{Sinister.command_prefix}``kick <user> - **Kick mentioned user/id**
``{Sinister.command_prefix}``nuke <channel> - **Nuke specified channel**
``{Sinister.command_prefix}``nuke2 <channel> - **Silent nuke specified channel**
``{Sinister.command_prefix}``mute <user> - **Mute mentioned user/id**
``{Sinister.command_prefix}``unmute <user> - **Unmute mentioned user/id**
``{Sinister.command_prefix}``massunban - **Unban every user from current guild**""", color=int(h['color'].replace('#', '0x'), 0))
    embed.set_thumbnail(url=f"{h['thumbnail']}")
    embed.set_footer(text=f"{h['footer']}", icon_url= f"{h['thumbnail']}")
    await ctx.send(embed=embed, delete_after=delete_time)
    
@Sinister.command(name='help', aliases=['cmds', 'commands'])
async def help_command(ctx):
    await ctx.message.delete()  
    s = json.load(open('configs/settings.json', 'r'))
    h = json.load(open(f"themes/{s['theme']}.json"))

    embed = discord.Embed(title=f"{h['title']}")
    embed.color = int(h['color'].replace('#', '0x'), 0)
    embed.add_field(name=":mag_right: - Searchengines", value="Display All Search Engine Options", inline = False)
    embed.add_field(name=":art:  - Theme <theme>", value="Use a custom theme in themes folder", inline = False)
    embed.add_field(name=":wrench: - Useful", value="Display Useful Things", inline = False)
    embed.add_field(name=":rotating_light: - Moderation", value="Display Moderation Commands", inline = False)
    embed.add_field(name=":bow_and_arrow: - Raiding ", value="Display Raiding Commands", inline = False)
    embed.add_field(name=":joy:  - Fun", value="Display Fun Commands", inline = False)
    embed.add_field(name=":camera:  - Image", value="Display Image Commands", inline = False)
    if Nsfw == "True" or Nsfw == "true":
     embed.add_field(name=":underage: - Nsfw", value='Display NSFW Commands')
    cmds = 0
    for commands in Sinister.commands:
        cmds += 1
    embed.set_footer(text=f"Use {Sinister.command_prefix}search for specific commands | {cmds} Commands", icon_url=f"{h['thumbnail']}")
    embed.set_thumbnail(url=f"{h['thumbnail']}")
    await ctx.send(embed=embed, delete_after=delete_time)

@Sinister.command(name='image')
async def help_image(ctx):
    await ctx.message.delete()
    s = json.load(open('configs/settings.json', 'r'))
    h = json.load(open(f"themes/{s['theme']}.json"))
    embed=discord.Embed(title=f"{h['title']}", description=f"""
``{Sinister.command_prefix}``trigger <user> - **Trigger the mentioned user**
``{Sinister.command_prefix}``gay <user> - **Turn the mentioned user gay**
``{Sinister.command_prefix}``wasted <user> - **GTA wasted screen over mentioned user**
``{Sinister.command_prefix}``jail <user> - **Jail the mentioned user**
``{Sinister.command_prefix}``tweet <username> <text> - **Tweet something as specific username**
``{Sinister.command_prefix}``clyde <text> - **Have clyde say something**
``{Sinister.command_prefix}``changemymind <text> - **Generate a change my mind image**""", color=int(h['color'].replace('#', '0x'), 0))
    embed.set_thumbnail(url=f"{h['thumbnail']}")
    embed.set_footer(text=f"{h['footer']}", icon_url= f"{h['thumbnail']}")
    await ctx.send(embed=embed, delete_after=delete_time)

@Sinister.command(name='fun')
async def help_fun(ctx):
    await ctx.message.delete()
    s = json.load(open('configs/settings.json', 'r'))
    h = json.load(open(f"themes/{s['theme']}.json"))
    embed=discord.Embed(title=f"{h['title']}", description=f"""
``{Sinister.command_prefix}``didnt-ask - **I didn't ask**
``{Sinister.command_prefix}``still-didnt-ask - **Nope...Still didn't ask**
``{Sinister.command_prefix}``911 - **Re-create 911...but in Discord**
``{Sinister.command_prefix}``cum - **Cum using emojis**
``{Sinister.command_prefix}``massreact <emoji> <amount> - **React to X messages**
``{Sinister.command_prefix}``cyclenick <nickname> - **Cycle your nickname**
``{Sinister.command_prefix}``stickbug <user> - **Stickbug the mentioned user**""", color=int(h['color'].replace('#', '0x'), 0))
    embed.set_thumbnail(url=f"{h['thumbnail']}")
    embed.set_footer(text=f"{h['footer']}", icon_url= f"{h['thumbnail']}")
    await ctx.send(embed=embed, delete_after=delete_time)

@Sinister.command(name='useful')
async def help_useful(ctx):
    await ctx.message.delete()
    s = json.load(open('configs/settings.json', 'r'))
    h = json.load(open(f"themes/{s['theme']}.json"))
    embed=discord.Embed(title=f"{h['title']}", description=f"""
``{Sinister.command_prefix}``create-embed <url> <title> <desc> - **Create a custom embed**
``{Sinister.command_prefix}``say - **Say something in embed form**
``{Sinister.command_prefix}``rules <rules>- **Create rules in embed form**
``{Sinister.command_prefix}``fav-song - **Play the song in user-config.json**
``{Sinister.command_prefix}``gping - **Ghost ping @everyone**
``{Sinister.command_prefix}``pfp <user> - **Generate a copy of mentioned pfp**
``{Sinister.command_prefix}``backup - **Backup friendlist in backup.txt**
``{Sinister.command_prefix}``cls - **Clear the console**
``{Sinister.command_prefix}``encode <text> - **Encode something in base64**
``{Sinister.command_prefix}``decode <text> - **Decode something from base64 encoding**
``{Sinister.command_prefix}``ping - **Calulate the bot's latency**
``{Sinister.command_prefix}``translate <text> - **Translate specified text using Google**
``{Sinister.command_prefix}``emojify <text> - **Turn the mentioned text into emojis**
``{Sinister.command_prefix}``sinister-encode - **Encode something using Sinister method**
``{Sinister.command_prefix}``sinister-decode - **Decode something using Sinister method**
``{Sinister.command_prefix}``mph <kmh> - **Convert kmh into mph**
``{Sinister.command_prefix}``kmh <mph> - **Convert mph into kmh**
``{Sinister.command_prefix}``timer <time> <method> - **Set a timer, minutes or hours**
``{Sinister.command_prefix}``purge <amount> - **Purge an amount of messages**
``{Sinister.command_prefix}``adminservers - **View the servers you have admin in**
``{Sinister.command_prefix}``readall - **Mark every guild as read**
``{Sinister.command_prefix}``changeprefix <prefix> - **Change your prefix**
``{Sinister.command_prefix}``dm <user> <message> - **Dm a user**
``{Sinister.command_prefix}``afk <on/off> - **Turn afk mode on/off**
``{Sinister.command_prefix}``emojiping <emoji> - **Ping @everyone using an emoji**
``{Sinister.command_prefix}``spam <amount> <message> - **Spam a message X amount of times**""", color=int(h['color'].replace('#', '0x'), 0))
    embed.set_thumbnail(url=f"{h['thumbnail']}")
    embed.set_footer(text=f"{h['footer']}", icon_url= f"{h['thumbnail']}")
    await ctx.send(embed=embed, delete_after=delete_time)

@Sinister.command()
async def trigger(ctx, member: discord.User=None):
    await ctx.message.delete()
    if not member:
        member = ctx.author
        
    async with aiohttp.ClientSession() as trigSession:
        async with trigSession.get(f'https://some-random-api.ml/canvas/triggered?avatar={member.avatar_url_as(format="png", size=1024)}') as trigImg:
            imageData = io.BytesIO(await trigImg.read())
            
            await trigSession.close()
            
            await ctx.send(file=discord.File(imageData, 'triggered.gif'))

@Sinister.command()
async def gay(ctx, member: discord.User=None):
    await ctx.message.delete()
    if not member:
        member = ctx.author
        
    async with aiohttp.ClientSession() as gaySession:
        async with gaySession.get(f'https://some-random-api.ml/canvas/gay?avatar={member.avatar_url_as(format="png", size=1024)}') as gayImg:
            imageData = io.BytesIO(await gayImg.read())
            
            await gaySession.close()
            
            await ctx.send(file=discord.File(imageData, 'gay.gif'))

@Sinister.command()
async def wasted(ctx, member: discord.User=None):
    await ctx.message.delete()
    if not member:
        member = ctx.author
        
    async with aiohttp.ClientSession() as wastedSession:
        async with wastedSession.get(f'https://some-random-api.ml/canvas/wasted?avatar={member.avatar_url_as(format="png", size=1024)}') as wastedImg:
            imageData = io.BytesIO(await wastedImg.read())
            
            await wastedSession.close()
            
            await ctx.send(file=discord.File(imageData, 'wasted.png'))

@Sinister.command()
async def jail(ctx, member: discord.User=None):
    await ctx.message.delete()
    if not member:
        member = ctx.author
        
    async with aiohttp.ClientSession() as jailSession:
        async with jailSession.get(f'https://some-random-api.ml/canvas/jail?avatar={member.avatar_url_as(format="png", size=1024)}') as jailImg:
            imageData = io.BytesIO(await jailImg.read())
            
            await jailSession.close()
            
            await ctx.send(file=discord.File(imageData, 'jail.png'))

@Sinister.command()
async def pfp(ctx, *, member: discord.User=None):
    await ctx.message.delete()
    if not member:
        member = ctx.message.author
    await ctx.send(member.avatar_url)

@Sinister.command(name="create-embed")
async def embed_maker(ctx, url = None, title = None, *, description = None,):
    await ctx.message.delete()
    s = json.load(open('configs/settings.json', 'r'))
    h = json.load(open(f"themes/{s['theme']}.json"))
    
    embed = discord.Embed(title=title, description=description, color=int(h['color'].replace('#', '0x'), 0))
    embed.set_thumbnail(url=url)
    await ctx.send(embed=embed, delete_after=delete_time)
  
@Sinister.command()
async def say(ctx, *, says: str = None):
    await ctx.message.delete()
    s = json.load(open('configs/settings.json', 'r'))
    h = json.load(open(f"themes/{s['theme']}.json"))
    
    embed = discord.Embed(title=ctx.message.author, description=says, color=int(h['color'].replace('#', '0x'), 0))
    await ctx.send(embed=embed, delete_after=delete_time)

@Sinister.command()
async def rules(ctx, *, rule_embed: str = None):
    await ctx.message.delete()
    s = json.load(open('configs/settings.json', 'r'))
    h = json.load(open(f"themes/{s['theme']}.json"))
    embed = discord.Embed(color=int(h['color'].replace('#', '0x'), 0))
    embed.add_field(name="__**Rules:**__", value=rule_embed, inline = False)
    await ctx.send(embed=embed)
    
@Sinister.command(name='fav-song', aliases=["fs", "favsong"])
async def favourite_song(ctx):
    await ctx.message.delete()
    webbrowser.open(fav_song)

@Sinister.command(name='didnt-ask', aliases=['didntask'])
async def didnt_ask(ctx):
    await ctx.message.delete()
    await ctx.send('https://cdn.discordapp.com/attachments/833491968516554793/834121636591960080/didnt_ask.mp4')

@Sinister.command(name='still-didnt-ask', aliases=['stilldidntask'])
async def still_didnt_ask(ctx):
    await ctx.message.delete()
    await ctx.send('https://cdn.discordapp.com/attachments/833491968516554793/834121811553681428/still_didnt_ask.mp4')

@Sinister.command(name='gping')
async def Sinister_ping_everyone(ctx):
    await ctx.message.delete()
    await ctx.send('@everyone', delete_after=0.1)

@Sinister.command(name='petit-poney')
async def petit_poney(ctx):
    await ctx.message.delete()
    webbrowser.open('https://youtu.be/u5Ho1trvlro')

@Sinister.command(name='dababy-song')
async def dababy_song(ctx):
    await ctx.message.delete()
    webbrowser.open('https://youtu.be/DcRLTClL5YU')

@Sinister.command(name='drugged-girl')
async def gay_siwa(ctx):
    await ctx.message.delete()
    webbrowser.open('https://youtu.be/b0uZRno5Nyw')
    
if __name__ == '__main__':
    Init()