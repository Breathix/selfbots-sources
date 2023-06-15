from asyncio.windows_events import NULL
from http.client import RESET_CONTENT
from sqlite3.dbapi2 import Timestamp, connect
import sys
import asyncio
import aiohttp
from discord.ext import commands, tasks
import re
from win10toast import ToastNotifier
import asyncio, threading
import json
from aiohttp.helpers import TimeoutHandle
from colorama import init
from requests.utils import CaseInsensitiveDict
from itertools import cycle
from discord import embeds, guild, message, user
from discord.enums import Theme
from colour import Color
from discord.ext import commands
import datetime
from selenium import webdriver
import time
from os import system
from random import choices, randint
from discord.ext import commands
from gtts import gTTS
import codecs, datetime, io, random, numpy, datetime
import re
import httpx
from colorama import Fore, init
import platform
import json
import time
import traceback
from discord.ext import tasks
from os import system
from random import randint
from discord.ext import commands
import re
import httpx
from colorama import Fore, init
import platform
import sys
import traceback
import youtube_dl
import platform
import subprocess
import re
import random
import asyncio
import json
import psutil
import time
import traceback
import sys
import urllib
import requests
import discord
import ctypes
from pypresence import Presence, presence
from discord.embeds import Embed
import requests, wmi
import asyncio
import random
from colorama import init
from discord.ext import commands
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from AuthGG.client import Client
from AuthGG.admin import AdminClient
from AuthGG.logging import Logging
from PIL import Image
import time
from colorama import Fore
from hashlib import sha512
import json, hmac, math, zlib
import colorsys
import sys
import os
config = json.load(open('config.json', 'rb'))

########### >> Defining
os.system("color")

########### >> Variables

########### >> Classes
class Colours:
    White = "\x1b[38;2;250;250;250m"
    Magenta = "\x1b[38;2;255;94;255m"

def new_splash():
    print(f"""                                           {Colours.White}Welcome to Cotra Selfbot
  {Colours.Magenta}╔════════════════════════╗    ╔══════════════════════════════════════════════╗    ╔════════════════════════╗              
 {Colours.Magenta}╔╝         {Colours.White}Rules          {Colours.Magenta}╚╗  ╔╝                                              ╚╗  ╔╝        {Colours.White}Profile         {Colours.Magenta}╚╗             
                            {Colours.Magenta}║  ║    ██████{Colours.White}{Colours.White}╗ {Colours.Magenta}██████{Colours.White}{Colours.White}╗ {Colours.Magenta}████████{Colours.White}{Colours.White}╗{Colours.Magenta}██████{Colours.White}{Colours.White}╗  {Colours.Magenta}█████{Colours.White}{Colours.White}╗    {Colours.Magenta}║  ║                                     
        {Colours.White}No exe {Colours.Magenta}Sharing      {Colours.Magenta}║  ║   ██{Colours.White}╔════╝{Colours.Magenta}██{Colours.White}╔═══{Colours.Magenta}██{Colours.White}╗╚══{Colours.Magenta}██{Colours.White}╔══╝{Colours.Magenta}██{Colours.White}╔══{Colours.Magenta}██{Colours.White}╗{Colours.Magenta}██{Colours.White}╔══{Colours.Magenta}██{Colours.White}╗   {Colours.Magenta}║  ║   Username: {Colours.White}{str(bot.user)}                                 
     {Colours.White}No {Colours.Magenta}tampering {Colours.White}allowed   {Colours.Magenta}╚══╝   {Colours.Magenta}██{Colours.White}║     {Colours.Magenta}██{Colours.White}║   {Colours.Magenta}██{Colours.White}║   {Colours.Magenta}██{Colours.White}║   {Colours.Magenta}██████{Colours.White}╔╝{Colours.Magenta}███████{Colours.White}║   {Colours.Magenta}╚══╝   Friends: {Colours.White}{len(bot.user.friends)}                                   
      {Colours.White}No {Colours.Magenta}account {Colours.White}sharing    {Colours.Magenta}{Colours.Magenta}╔══╗   {Colours.Magenta}{Colours.Magenta}██{Colours.White}║     {Colours.Magenta}{Colours.Magenta}██{Colours.White}║   {Colours.Magenta}{Colours.Magenta}██{Colours.White}║   {Colours.Magenta}{Colours.Magenta}██{Colours.White}║   {Colours.Magenta}{Colours.Magenta}██{Colours.White}╔══{Colours.Magenta}{Colours.Magenta}██{Colours.White}╗{Colours.Magenta}{Colours.Magenta}██{Colours.White}╔══{Colours.Magenta}{Colours.Magenta}██{Colours.White}║   {Colours.Magenta}{Colours.Magenta}╔══╗   Guilds: {Colours.White}{len(bot.guilds)}                                     
                            {Colours.Magenta}║  ║   ╚{Colours.Magenta}██████{Colours.White}╗╚{Colours.Magenta}██████{Colours.White}╔╝   {Colours.Magenta}██{Colours.White}║   {Colours.Magenta}██{Colours.White}║  {Colours.Magenta}██{Colours.White}║{Colours.Magenta}██{Colours.White}║  {Colours.Magenta}██{Colours.White}║   {Colours.Magenta}║  ║   Prefix: {Colours.White}{config['prefix']}                                  
    {Colours.Magenta}discord.gg/{Colours.White}j8VV2RzKs3   {Colours.Magenta}║  ║    {Colours.White}╚═════╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝   {Colours.Magenta}║  ║                                     
 {Colours.Magenta}╚╗                        ╔╝  ╚╗                                              ╔╝  ╚╗                        ╔╝             
  {Colours.Magenta}╚════════════════════════╝    ╚═════════════════════╗ ╔══════════════════════╝    ╚════════════════════════╝                         
                                                      {Colours.Magenta}║ ║  
                         {Colours.Magenta}╔════════════════════════════╝ ╚════════════════════════════╗
                        {Colours.Magenta}╔╝                          {Colours.White}Selfbot                          {Colours.Magenta}╚╗
                                                 
                                {Colours.Magenta}Nitro Sniper: {Colours.White}True           {Colours.Magenta}Giveaway Joiner: {Colours.White}True
                                {Colours.Magenta}Commands: {Colours.White}{len(bot.commands)}                {Colours.Magenta}Delete Timer: {Colours.White}{config['deletetime']} 
                                {Colours.Magenta}Theme: {Colours.White}{config['theme']['name']}              {Colours.Magenta}Version: {Colours.White}{version}
                        {Colours.Magenta}╚╗                                                           ╔╝
                        {Colours.Magenta} ╚═══════════════════════════════════════════════════════════╝
""")

prefix = config['prefix']
version = "4.8"
dev = "4.9"
ids = "584879487850643456", "701792352301350973"
cmds = "201"
bot = commands.Bot(command_prefix=prefix, self_bot=True)
toaster = ToastNotifier()
toaster.show_toast("Cotra Selfbot",
                   "Is now loading...",
                   icon_path="A.ico",
                   duration=10)

toaster.show_toast("Cotra Selfbot",
                   "Is now loaded. Please wait 5 seconds",
                   icon_path="A.ico",
                   duration=5,
                   threaded=True)
# Wait for threaded notification to finish
while toaster.notification_active(): time.sleep(0.1)
bot.remove_command('help')
def restart_bot(): 
  #os.execv(sys.executable, ['python'] + sys.argv)
  os.execv(sys.executable,sys.argv)

print(chr(27) + "[2J")

def Clear():
    os.system('cls')

def is_me(m):
    return m.author == bot.user

snipermode = 1
gsniper= 1

giveaway_ids =   ["294882584201003009","716967712844414996","796315281688494081","673918978178940951","396464677032427530"]

@bot.event
async def on_message(message):
    time = datetime.datetime.now().strftime("%H:%M")
    start = datetime.datetime.now()
    token = config.get('token')
    headers = {'Authorization': token}

    def GiveawayData():
        print(f"{Colours.Magenta}[blicky Sniper] Giveaway Bot Used: {message.author}" + Colours.White)
        print(f"{Colours.Magenta}[blicky Sniper] Server: {message.guild}" + Colours.White)
        print(f"{Colours.Magenta}[blicky Sniper] Channel: {message.channel}" + Colours.White)
        print(f"{Colours.Magenta}[blicky Sniper] Date: {datetime.datetime.now().strftime('%H:%M:%S %p')}" + Colours.White)
    
    def GiveawayData2():
        print(f"{Colours.Magenta}[blicky Skipped] Giveaway Bot Used: {message.author}" + Colours.White)
        print(f"{Colours.Magenta}[blicky Skipped] Server: {message.guild}" + Colours.White)
        print(f"{Colours.Magenta}[blicky Skipped] Channel: {message.channel}" + Colours.White)
        print(f"{Colours.Magenta}[blicky Skipped] Reason: ITS SUS CUTIE I SAVED YOU" + Colours.White)
        print(f"{Colours.Magenta}[blicky Skipped] Date: {datetime.datetime.now().strftime('%H:%M:%S %p')}" + Colours.White)

    def NitroData(delay, code):
        response = round(bot.latency * 1000)
        print(f"{Colours.Magenta}[Sniper] {Colours.Magenta}Nitro Code sent by: {Fore.WHITE}{message.author}" + Colours.White)
        print(f"{Colours.Magenta}[Sniper] {Colours.Magenta}Nitro Code: {Fore.WHITE}{code}" + Colours.White)
        print(f"{Colours.Magenta}[Sniper] {Colours.Magenta}Server: {Fore.WHITE}{message.guild}" + Colours.White)
        print(f"{Colours.Magenta}[Sniper] {Colours.Magenta}Channel: {Fore.WHITE}{message.channel}" + Colours.White)
        print(f"{Colours.Magenta}[Sniper] {Colours.Magenta}Status: {Fore.LIGHTGREEN_EX}REAL" + Colours.White)
        print(f"{Colours.Magenta}[Sniper] {Colours.Magenta}Snipe Time: {Fore.WHITE}{delay}" + Colours.White)
        print(f"{Colours.Magenta}[Sniper] {Colours.Magenta}API Delay: {Fore.WHITE}{response}ms" + Colours.White)

    def NitroData2(delay, code):
        response = round(bot.latency * 1000)
        print(f"{Colours.Magenta}[Sniper] {Colours.Magenta}Nitro Code sent by: {Fore.WHITE}{message.author}" + Colours.White)
        print(f"{Colours.Magenta}[Sniper] {Colours.Magenta}Nitro Code: {Fore.WHITE}{code}" + Colours.White)
        print(f"{Colours.Magenta}[Sniper] {Colours.Magenta}Server: {Fore.WHITE}{message.guild}" + Colours.White)
        print(f"{Colours.Magenta}[Sniper] {Colours.Magenta}Channel: {Fore.WHITE}{message.channel}" + Colours.White)
        print(f"{Colours.Magenta}[Sniper] {Colours.Magenta}Status: {Fore.LIGHTRED_EX}FAKE" + Colours.White)
        print(f"{Colours.Magenta}[Sniper] {Colours.Magenta}Snipe Time: {Fore.WHITE}{delay}" + Colours.White)
        print(f"{Colours.Magenta}[Sniper] {Colours.Magenta}API Delay: {Fore.WHITE}{response}ms" + Colours.White)

    def NitroData3(delay, code):
        response = round(bot.latency * 1000)
        print(f"{Colours.Magenta}[Sniper] {Colours.Magenta}Nitro Code sent by: {Fore.WHITE}{message.author}" + Colours.White)
        print(f"{Colours.Magenta}[Sniper] {Colours.Magenta}Nitro Code: {Fore.WHITE}{code}" + Colours.White)
        print(f"{Colours.Magenta}[Sniper] {Colours.Magenta}Server: {Fore.WHITE}{message.guild}" + Colours.White)
        print(f"{Colours.Magenta}[Sniper] {Colours.Magenta}Channel: {Fore.WHITE}{message.channel}" + Colours.White)
        print(f"{Colours.Magenta}[Sniper] {Colours.Magenta}Status: {Fore.YELLOW}ALREADY REDEEMED" + Colours.White)
        print(f"{Colours.Magenta}[Sniper] {Colours.Magenta}Snipe Time: {Fore.WHITE}{delay}" + Colours.White)
        print(f"{Colours.Magenta}[Sniper] {Colours.Magenta}API Delay: {Fore.WHITE}{response}ms" + Colours.White)

    if 'discord.gift/' in message.content:
        if snipermode == 1:
            start = datetime.datetime.now()
            code = re.search("discord.gift/(.*)", message.content).group(1)
            token = config.get('token')
            r = requests.post(f'https://discord.com/api/v9/entitlements/gift-codes/{code}/redeem',headers=headers).text
            delay = datetime.datetime.now() - start
            delay = f'{delay.seconds}.{delay.microseconds}'
            if 'This gift has been redeemed already.' in r:
                print(""f"\n[{time}] - {Fore.LIGHTBLUE_EX}NITRO SNIPER"+ Colours.White)
                NitroData3(delay, code)

            elif 'subscription_plan' in r:
                print(""f"\n[{time}] - {Fore.LIGHTBLUE_EX}NITRO SNIPER"+ Colours.White)
                NitroData(delay, code)

            elif 'Unknown Gift Code' in r:
                print(""f"\n[{time}] - {Fore.LIGHTBLUE_EX}NITRO SNIPER"+ Colours.White)
                NitroData2(delay, code)
            else:
                return

    if 'GIVEAWAY' in message.content:
        if gsniper == 1:
            if str(message.author.id) in giveaway_ids:
                embed = message.embeds[0].to_dict()
                prize = embed["author"]["name"]
                if "ban" in prize.lower() or "kick" in prize.lower() or "mute" in prize.lower() or "punish" in prize.lower() or "lol" in prize.lower() or "test" in prize.lower() or "fake" in prize.lower():
                    print(f"\n[{time}] - Giveaway Skipped")
                    GiveawayData2()
                else:
                    await asyncio.sleep(5)
                    await message.add_reaction("🎉")          
                    print(f"\n[{time}] - Giveaway Sniped And Entered")
                    GiveawayData()

    if f'Congratulations <@{bot.user.id}>' in message.content:
        if gsniper == 1:
            if str(message.author.id) in giveaway_ids:   
                print(f"\n[{time}] - Giveaway Has Been Won")
                GiveawayData()
        else:
            return

    await bot.process_commands(message)

@bot.event
async def on_connect():
    title = ctypes.windll.kernel32.SetConsoleTitleW(f"Cotra Selfbot | Version: [{version}]  | Commands: [{len(bot.commands)}] | Theme: {config['theme']['name']}") 
    time.sleep(1)
    title
    new_splash()


@bot.command()
async def nitrosnipermode(ctx):
        await ctx.message.delete()
        global snipermode
        if snipermode == 0:
            snipermode += 1        
        elif snipermode == 1:
            snipermode  -= 1

@bot.command()
async def blacklist(ctx):
    await ctx.message.delete()
    if ctx.message.author.id in ids:
        await ctx.send("Unfortunately, you have been blacklisted from the bot. If you wish to know why or appeal, join this server:")


@bot.command()
async def gsnipermode(ctx):
        await ctx.message.delete()
        global gsniper
        if gsniper == 0:
            gsniper += 1        
        elif gsniper == 1:
            gsniper -= 1

ritchy_pres = config['rpc']

if ritchy_pres == True:
    rpc = Presence("926564240259711107")
    rpc.connect()
    rpc.update(state="Using Cotra Selfbot",large_image="uwu",start=time.time(),large_text=f"Logged in as : GET FUCKING LEAKED YOU CUNT",buttons=[{"label": "Discord", "url": "https://discord.gg/6EzTsPnbbA"}],small_image="uwu",small_text=f"Version : [{version}]")


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

def rgb_to_hex(rgb):
        return '%02x%02x%02x' % rgb

def RGB_to_hex(RGB):
        for pos in range(len(RGB)):
            RGB[pos] = str(RGB[pos])
        hex_list = []
        hex_list.extend("0123456789ABCDEF")
        all_combo = [f"{x}{y}" for x in hex_list for y in hex_list]
        for pos, color in enumerate(RGB.copy()):
            RGB[pos] = all_combo[int(color)]
        return f"0x{''.join(RGB)}"



#/////// HELP ///////


@bot.command()
async def help(ctx, category=None):
    await ctx.message.delete()
    if category is None:
        msg = f"""
        ```ini
╔══════════════════════════════════════════════════════════════════════╗
     [Help Panel]   ║ Prefix: [{config['prefix']}] ║ Commands: [{len(bot.commands)}] ║ version: [{version}]     
║══════════════════════════════════════════════════════════════════════║
║   [{bot.command_prefix}]general »» Displays general commands                            ║
║   [{bot.command_prefix}]fun »» Displays fun commands (SOME RISKY)                       ║                         
║   [{bot.command_prefix}]memes »» Displays meme commands                                 ║
║   [{bot.command_prefix}]server »» Displays server commands                              ║
║   [{bot.command_prefix}]text »» Displays text commands                                  ║
║   [{bot.command_prefix}]images »» Displays image commands                               ║
║   [{bot.command_prefix}]token »» Displays token commands                                ║
║   [{bot.command_prefix}]nsfw »» Displays nsfw commands                                  ║
║   [{bot.command_prefix}]promo »» Displays promo commands                                ║
║   [{bot.command_prefix}]settings »» Displays settings commands                          ║
║══════════════════════════════════════════════════════════════════════║
   {config['theme']['title']} | {config['theme']['text']} | Delete time: {config['deletetime']}                         
╚══════════════════════════════════════════════════════════════════════╝
        ```
        """
        print(Colours.Magenta+"[Command] <>Help Panel<>"+Colours.White)
        await ctx.send(msg,delete_after=config['deletetime'])

#/////// GENERAL ///////

@bot.command()
async def general(ctx, category=None):
    await ctx.message.delete()
    if category is None:

        msg = f"""
        ```ini
╔═══════════════════════════════════════════════════════════════════════╗
     [General Panel]   ║ Prefix: [{config['prefix']}] ║ Commands: [{len(bot.commands)}] ║ version: [{version}]   
║═══════════════════════════════════════════════════════════════════════║
║   [{bot.command_prefix}]allcmds »» Displays all commands                                 ║
║   [{bot.command_prefix}]purge »» Displays fun commands (SOME RISKY)                      ║
║   [{bot.command_prefix}]userinfo »» Displays helpsection commands                        ║
║   [{bot.command_prefix}]first »» Displays meme commands                                  ║
║   [{bot.command_prefix}]yt »» Displays server commands                                   ║
║   [{bot.command_prefix}]dmdel »» deletes dms by amount                                   ║
║   [{bot.command_prefix}]dnd »» sets status dnd                                           ║
║   [{bot.command_prefix}]online »» sets status online                                     ║
║   [{bot.command_prefix}]idle »» sets status idle                                         ║
║   [{bot.command_prefix}]invisible »» sets status invisible                               ║
║═══════════════════════════════════════════════════════════════════════║
   {config['theme']['title']} | {config['theme']['text']} | Delete time: {config['deletetime']}                         
╚═══════════════════════════════════════════════════════════════════════╝
        ```
        """
        print(Colours.Magenta+"[Command] <>General Panel<>"+Colours.White)
        await ctx.send(msg,delete_after=config['deletetime'])




#/////// MEMES ///////

@bot.command()
async def memes(ctx, category=None):
    await ctx.message.delete()
    if category is None:

            msg = f"""
        ```ini
╔══════════════════════════════════════════════════════════════════════╗
     [Memes Panel]   ║ Prefix: [{config['prefix']}] ║ Commands: [{len(bot.commands)}] ║ version: [{version}]     
║══════════════════════════════════════════════════════════════════════║
║   [{bot.command_prefix}]blm »» Displays blm                                             ║
║   [{bot.command_prefix}]discum »» Displays Discum                                       ║
║   [{bot.command_prefix}]pp »» Displays users PP size                                    ║
║   [{bot.command_prefix}]meme »» Posts memes                                             ║
║   [{bot.command_prefix}]balls »» Posts my balls are cold                                ║
║   [{bot.command_prefix}]gay »» see how gay someone is                                   ║
║   [{bot.command_prefix}]gaypfp »» gay pfp user                                          ║
║   [{bot.command_prefix}]pixel »» pixel pfp user                                         ║
║   [{bot.command_prefix}]lolice »» lolice pfp user                                       ║
║   [{bot.command_prefix}]passed »» Mission passed pfp user                               ║
║   [{bot.command_prefix}]wanted »» wanted pfp user                                       ║
║   [{bot.command_prefix}]jail »» jail pfp user                                           ║
║   [{bot.command_prefix}]triggered »» triggered pfp user                                 ║
║   [{bot.command_prefix}]joke »» posts joke                                              ║
║   [{bot.command_prefix}]8ball »» Posts 8ball                                            ║    
║══════════════════════════════════════════════════════════════════════║
   {config['theme']['title']} | {config['theme']['text']} | Delete time: {config['deletetime']}                         
╚══════════════════════════════════════════════════════════════════════╝
        ```
        """
    print(Colours.Magenta+"[Command] <>Memes Panel<>"+Colours.White)
    await ctx.send(msg,delete_after=config['deletetime'])

#/////// FUN ///////

@bot.command()
async def fun(ctx):
    if not is_me(ctx.message):
        await ctx.message.delete()
        return

    msg = f"""
        ```ini
╔══════════════════════════════════════════════════════════════════════╗
     [Fun Panel]   ║ Prefix: [{config['prefix']}] ║ Commands: [{len(bot.commands)}] ║ version: [{version}]        
║══════════════════════════════════════════════════════════════════════║
║   [{bot.command_prefix}]killvc »» kills vc                                              ║
║   [{bot.command_prefix}]massgc »» mass adds user to gc                                  ║
║   [{bot.command_prefix}]animnick »» animates nickname                                   ║
║   [{bot.command_prefix}]rgbrole »» makes role rainbow                                   ║
║   [{bot.command_prefix}]gcleave »» leaves all gcs                                       ║
║   [{bot.command_prefix}]tts »» sends tts to message                                     ║
║   [{bot.command_prefix}]loopstatus »» loops status between online and offline           ║ 
║══════════════════════════════════════════════════════════════════════║
   {config['theme']['title']} | {config['theme']['text']} | Delete time: {config['deletetime']}                         
╚══════════════════════════════════════════════════════════════════════╝
        ```
        """
    print(Colours.Magenta+"[Command] <>Fun Panel<>"+Colours.White)
    await ctx.send(msg,delete_after=config['deletetime'])

#/////// NSFW ///////

@bot.command()
async def nsfw(ctx, category=None):
    await ctx.message.delete()
    if category is None:

        msg = f"""
        ```ini
╔══════════════════════════════════════════════════════════════════════╗
     [NSFW Panel]   ║ Prefix: [{config['prefix']}] ║ Commands: [{len(bot.commands)}] ║ version: [{version}]       
║══════════════════════════════════════════════════════════════════════║
║   [{bot.command_prefix}]pgif »» Posts porn gif                                          ║
║   [{bot.command_prefix}]niko »» niko :]                                                 ║
║   [{bot.command_prefix}]yiff »» posts lewdneko                                          ║
║   [{bot.command_prefix}]femboy »» posts femboy                                          ║
║   [{bot.command_prefix}]cum »» posts cum                                                ║
║   [{bot.command_prefix}]spank »» posts spank pics                                       ║
║   [{bot.command_prefix}]feet »» feet pics                                               ║
║   [{bot.command_prefix}]pokeporn »» posts pokemon porn                                  ║
║   [{bot.command_prefix}]r34 »» posts r34                                                ║
║   [{bot.command_prefix}]fortnite »» posts fortnite nsfw                                 ║
║   [{bot.command_prefix}]paizuri »» posts paizuri                                        ║
║   [{bot.command_prefix}]hthighs »» posts hentai thighs                                  ║
║   [{bot.command_prefix}]nsfw2 »» Posts NSFW Section 2                                   ║                                              
║══════════════════════════════════════════════════════════════════════║
   {config['theme']['title']} | {config['theme']['text']} | Delete time: {config['deletetime']}                         
╚══════════════════════════════════════════════════════════════════════╝
        ```
        """
    print(Colours.Magenta+"[Command] <>NSFW Panel<>"+Colours.White)
    await ctx.send(msg,delete_after=config['deletetime'])

@bot.command()
async def nsfw2(ctx):
    await ctx.message.delete()
    msg = f"""
    ```ini
╔══════════════════════════════════════════════════════════════════════╗
     [NSFW 2 Panel]   ║ Prefix: [{config['prefix']}] ║ Commands: [{len(bot.commands)}] ║ version: [{version}]       
║══════════════════════════════════════════════════════════════════════║
║   [{bot.command_prefix}]thighs »» posts thighs                                          ║
║   [{bot.command_prefix}]holo »» posts holo                                              ║
║   [{bot.command_prefix}]femdom »» posts femdom                                          ║
║   [{bot.command_prefix}]lewdkemo »» posts lewdkemo                                      ║
║   [{bot.command_prefix}]erokemo »» posts erokemo                                        ║
║   [{bot.command_prefix}]pwankg »» posts pwankg                                          ║
║   [{bot.command_prefix}]keta  »» posts keta                                             ║
║   [{bot.command_prefix}]lewdk »» posts lewdk                                            ║
║   [{bot.command_prefix}]eron »» posts eron                                              ║ 
║   [{bot.command_prefix}]eroyuri »» posts eyuri                                          ║
║   [{bot.command_prefix}]solo »» posts so                                                ║
║══════════════════════════════════════════════════════════════════════║
   {config['theme']['title']} | {config['theme']['text']} | Delete time: {config['deletetime']}                         
╚══════════════════════════════════════════════════════════════════════╝
        ```
        """
    print(Colours.Magenta+"[Command] <>NSFW 2  Panel<>"+Colours.White)
    await ctx.send(msg,delete_after=config['deletetime'])
#/////// Settings ///////

@bot.command()
async def settings(ctx, category=None):
    await ctx.message.delete()
    if category is None:


        msg = f"""
        ```ini
╔════════════════════════════════════════════════════════════════════════╗
     [Settings Panel]   ║ Prefix: [{config['prefix']}] ║ Commands: [{len(bot.commands)}] ║ version: [{version}]    
║════════════════════════════════════════════════════════════════════════║
║   [{bot.command_prefix}]restart »» Restarts the bot                                       ║
║   [{bot.command_prefix}]info »» shows info on the bot                                     ║
║   [{bot.command_prefix}]clearconsole »» clears console                                    ║
║   [{bot.command_prefix}]uptime »» displays uptime                                         ║
║   [{bot.command_prefix}]gsnipermode »» Toggles On/Off                                     ║
║   [{bot.command_prefix}]nitrosnipermode »» Toggles On/Off                                 ║
║   [{bot.command_prefix}]tts »» sends tts to message                                       ║
║════════════════════════════════════════════════════════════════════════║
   {config['theme']['title']} | {config['theme']['text']} | Delete time: {config['deletetime']}                        
╚════════════════════════════════════════════════════════════════════════╝
        ```
        """
    print(Colours.Magenta+"[Command] <>Settings Panel<>"+Colours.White)
    await ctx.send(msg,delete_after=config['deletetime'])


#/////// token commands ///////

@bot.command()
async def token(ctx, category=None):
    await ctx.message.delete()
    if category is None:


            msg = f"""
        ```ini
╔══════════════════════════════════════════════════════════════════════╗
     [Token Panel]   ║ Prefix: [{config['prefix']}] ║ Commands: [{len(bot.commands)}] ║ version: [{version}]       
║══════════════════════════════════════════════════════════════════════║
║   COMING SOON DW                                                     ║
║══════════════════════════════════════════════════════════════════════║
   {config['theme']['title']} | {config['theme']['text']} | Delete time: {config['deletetime']}                         
╚══════════════════════════════════════════════════════════════════════╝
        ```
        """
    print(Colours.Magenta+"[Command] <>token Panel<>"+Colours.White)
    await ctx.send(msg,delete_after=config['deletetime'])

#/////// Server commands ///////

@bot.command()
async def server(ctx, category=None):
    await ctx.message.delete()
    if category is None:


            msg = f"""
        ```ini
╔══════════════════════════════════════════════════════════════════════╗
     [Server Panel]   ║ Prefix: [{config['prefix']}] ║ Commands: [{len(bot.commands)}] ║ version: [{version}]      
║══════════════════════════════════════════════════════════════════════║
║   [{bot.command_prefix}]yoink »» clones a server                                        ║
║   [{bot.command_prefix}]invnick »» invisible nickname                                   ║
║   [{bot.command_prefix}]ban »» bans user                                                ║
║   [{bot.command_prefix}]police »» Police role                                           ║
║   [{bot.command_prefix}]unban »» unbans user                                            ║
║   [{bot.command_prefix}]kick »» kicks user                                              ║
║   [{bot.command_prefix}]nick »» changes nickname                                        ║ 
║══════════════════════════════════════════════════════════════════════║
   {config['theme']['title']} | {config['theme']['text']} | Delete time: {config['deletetime']}                        
╚══════════════════════════════════════════════════════════════════════╝
        ```
        """
    print(Colours.Magenta+"[Command] <>Server Panel<>"+Colours.White)
    await ctx.send(msg,delete_after=config['deletetime'])

#/////// Text commands ///////

@bot.command()
async def text(ctx, category=None):
    await ctx.message.delete()
    if category is None:



            msg = f"""
        ```ini
╔══════════════════════════════════════════════════════════════════════╗
     [Text Panel]   ║ Prefix: [{config['prefix']}] ║ Commands: [{len(bot.commands)}] ║ version: [{version}]      
║══════════════════════════════════════════════════════════════════════║
║   [{bot.command_prefix}]spam »» Spams message                                           ║
║   [{bot.command_prefix}]ascii »» ascii to text                                          ║
║   [{bot.command_prefix}]rv »» reverses text                                             ║
║   [{bot.command_prefix}]encrypt »» encrypts message with cotra                          ║
║   [{bot.command_prefix}]decrypt »» decrypts message with cotra                          ║
║   [{bot.command_prefix}]gp »» ghost pings user                                          ║
║   [{bot.command_prefix}]shrek »» what are ye doin in ma swamp                           ║
║   [{bot.command_prefix}]boldunderline »» bold underline                                 ║
║   [{bot.command_prefix}]underline »» underlines message                                 ║
║   [{bot.command_prefix}]bolditalic »» bold italics message                              ║
║   [{bot.command_prefix}]bold »» bolds message                                           ║
║   [{bot.command_prefix}]lenny »» posts lenny face                                       ║
║   [{bot.command_prefix}]emojify »» emojifys message                                     ║
║   [{bot.command_prefix}]spoiler »» spoilers message                                     ║ 
║══════════════════════════════════════════════════════════════════════║
   {config['theme']['title']} | {config['theme']['text']} | Delete time: {config['deletetime']}                         
╚══════════════════════════════════════════════════════════════════════╝
        ```
        """
    print(Colours.Magenta+"[Command] <>Text Panel<>"+Colours.White)       
    await ctx.send(msg,delete_after=config['deletetime'])

#/////// images ///////

@bot.command()
async def images(ctx, category=None):
    await ctx.message.delete()
    if category is None:
            msg = f"""
        ```ini
╔══════════════════════════════════════════════════════════════════════╗
     [Images Panel]   ║ Prefix: [{config['prefix']}] ║ Commands: [{len(bot.commands)}] ║ version: [{version}]      
║══════════════════════════════════════════════════════════════════════║
║   [{bot.command_prefix}]rick »» rick rolls user                                         ║
║   [{bot.command_prefix}]neko »» posts neko                                              ║
║   [{bot.command_prefix}]foximg »» posts a cute fox                                      ║
║   [{bot.command_prefix}]pat »» pats user                                                ║
║   [{bot.command_prefix}]kiss »» kisses user                                             ║
║   [{bot.command_prefix}]hug »» hugs user                                                ║     
║   [{bot.command_prefix}]furry »» Posts furry image                                      ║
║   [{bot.command_prefix}]wallpaper »» Posts wallpaper                                    ║
║   [{bot.command_prefix}]cuddle »» Cuddles user                                          ║
║   [{bot.command_prefix}]gasm »» gasm                                                    ║
║   [{bot.command_prefix}]feed »» Feeds user                                              ║
║   [{bot.command_prefix}]poke »» Pokes user                                              ║
║   [{bot.command_prefix}]images2 »» Posts Image section                                  ║
║══════════════════════════════════════════════════════════════════════║
   {config['theme']['title']} | {config['theme']['text']} | Delete time: {config['deletetime']}                        
╚══════════════════════════════════════════════════════════════════════╝
        ```
        """
    await ctx.send(msg,delete_after=config['deletetime'])
    print(Colours.Magenta+"[Command] <>Images Panel<>"+Colours.White)

@bot.command()
async def images2(ctx):
    await ctx.message.delete()
    msg = f"""
        ```ini
╔════════════════════════════════════════════════════════════════════════╗
     [Images 2 Panel]   ║ Prefix: [{config['prefix']}] ║ Commands: [{len(bot.commands)}] ║ version: [{version}]      
║════════════════════════════════════════════════════════════════════════║
║   [{bot.command_prefix}]tickle »» Tickles user                                            ║
║   [{bot.command_prefix}]baka »» bakas user                                                ║
║   [{bot.command_prefix}]play »» sends cute play img                                       ║ 
║   [{bot.command_prefix}]warcrimes »» commits warcrimes                                    ║
║   [{bot.command_prefix}]trampoline »» bouncy bouncy                                       ║
║   [{bot.command_prefix}]ducking »» ducks cutely                                           ║
║   [{bot.command_prefix}]trump »» sends trump tweet                                        ║
║   [{bot.command_prefix}]ph »» fake pornhub comment                                        ║
║   [{bot.command_prefix}]stickbug »» stickbugs user                                        ║
║   [{bot.command_prefix}]gah »» omg                                                        ║
║   [{bot.command_prefix}]coffeee »» steamy coffee                                          ║
║   [{bot.command_prefix}]waifu »» waifu uwu                                                ║
║════════════════════════════════════════════════════════════════════════║
   {config['theme']['title']} | {config['theme']['text']} | Delete time: {config['deletetime']}                        
╚════════════════════════════════════════════════════════════════════════╝
        ```
        """
    await ctx.send(msg,delete_after=config['deletetime'])
    print(Colours.Magenta+"[Command] <>Images 2 Panel<>"+Colours.White)

#/////// Promotions ///////

@bot.command()
async def promo(ctx, category=None):
    await ctx.message.delete()
    if category is None:

            msg = f"""
        ```ini
╔════════════════════════════════════════════════════════════════════════╗
     [Promotions Panel] ║ Prefix: [{config['prefix']}] ║ Commands: [{len(bot.commands)}] ║ version: [{version}]     
║════════════════════════════════════════════════════════════════════════║
║   [{bot.command_prefix}]Ragnarok »» Official Reseller                                     ║
║   [{bot.command_prefix}]mysite »» webite                                                  ║
║   [{bot.command_prefix}]cactus »» Official Reseller                                       ║
║   [{bot.command_prefix}]buy »» BUY COTRA NOW                                              ║
║   [{bot.command_prefix}]complex »» Official Reseller                                      ║
║   [{bot.command_prefix}]flop »» Official Reseller                                         ║
║   [{bot.command_prefix}]pathetic »» Official Reseller                                     ║
║   [{bot.command_prefix}]troop »» Official Reseller                                        ║ 
║════════════════════════════════════════════════════════════════════════║
   {config['theme']['title']} | {config['theme']['text']} | Delete time: {config['deletetime']}                        
╚════════════════════════════════════════════════════════════════════════╝
        ```
        """
    print(Colours.Magenta+"[Command] <>Images Panel<>"+Colours.White)
    await ctx.send(msg,delete_after=config['deletetime'])

#/////// Commands below ///////

# async def killvc(ctx,channelid,times):
#     if not is_me(ctx.message):
#         return
#     await ctx.message.delete()
#     for x in range(int(times)):
#         url = "https://canary.discord.com/api/v9/channels/"+str(channelid)+"/call"
#         headers = {"Authorization": config["token"],"Content-Type": "application/json",
#             "Accept": "*/*",
#             "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}


#         regeion = ['europe', 'hongkong', 'india', 'russia', 'brazil', 'japan', 'singapore', 'southafrica', 'sydney', 'us-central', 'us-east', 'us-west', 'us-south']
#         data = {"region":random.choice(regeion)}

#         pp = requests.patch(url=url, headers=headers, json=data)

@bot.command()
async def joke(ctx):
    await ctx.message.delete()
    headers = requests.structures.CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"
    url = "https://icanhazdadjoke.com/"
    response = requests.get(url, headers=headers)
    stuff = json.loads(response.text)
    joke = stuff["joke"]

    msg = f"""
```ini
[Joke]
{joke}
```
    """

    await ctx.send(msg,delete_after=config['deletetime'])

@bot.command()
async def killvc(ctx,times):
    if not is_me(ctx.message):
        return
    await ctx.message.delete()
    for ch in bot.private_channels:
         channelid = ch.id
    for x in range(int(times)):
        url = "https://canary.discord.com/api/v9/channels/"+str(channelid)+"/call"
        headers = {"Authorization": config["token"],"Content-Type": "application/json",
            "Accept": "*/*",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}


        regeion = ['europe', 'hongkong', 'india', 'russia', 'brazil', 'japan', 'singapore', 'southafrica', 'sydney', 'us-central', 'us-east', 'us-west', 'us-south']
        data = {"region":random.choice(regeion)}

        pp = requests.patch(url=url, headers=headers, json=data)


rainboo = 0
@bot.command()
async def rgbrole(ctx, *, role: discord.Role):
    await ctx.message.delete()
    global rainboo
    oldcolour = role.color
    red = Color("#ff3d3d")
    pink = Color("#f54287")
    rainbow = list(red.range_to(pink, 50))
    if rainboo == 0:
        rainboo +=1
    elif rainboo == 1:
        rainboo -=1
    while rainboo == 1:
        for x in rainbow:
            colour = f'{x}'
            await role.edit(color=int(colour.replace('#', '0x'), 0))
    await role.edit(color=oldcolour)

@bot.command(name="police")
async def policerole(ctx, role: discord.Role):
        print(Colours.Magenta+"[Command] <>Police Role<>"+Colours.White)
        await ctx.message.delete()
        cols = [0xff0002,0x001eff]
        color = random.choice(cols)
        while True:
                await role.edit(reason = None, color = random.choice(cols))
                await asyncio.sleep(1.5)

@bot.command(name="pcinfo", aliases=["pcstats","pcspecs","pcspec"])
async def pcinfo(ctx):
        computer = wmi.WMI()
        await ctx.message.delete()
        os_info = computer.Win32_OperatingSystem()[0]
        os_name = os_info.Name.encode('utf-8').split(b'|')[0]

        msg = f"""
```ini
[PC Specs]
WIN {str(os_name).replace("'", "").replace("b", "", 1)}
CPU {computer.Win32_Processor()[0].Name}
RAM {str(round(psutil.virtual_memory().total / (1024.0 **3)))} GB
GPU {computer.Win32_VideoController()[0].Name}
```
        """
        await ctx.send(msg,delete_after=config['deletetime'])



@bot.command(pass_context=True)
async def meme(ctx):
        await ctx.message.delete()

        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
                res = await r.json()

        msg = f"""
```ini
[Meme]
Enjoy spicy memes 
```
    """

        await ctx.send(msg,delete_after=config['deletetime'])
        await ctx.send(res['data']['children'] [random.randint(0, 25)]['data']['url'],delete_after=config['deletetime'])


@bot.command()
async def staring(ctx):
    await ctx.message.delete()

    msg = f"""
```ini
[Staring]
Staring at u uwu 
```
    """

    await ctx.send(msg,delete_after=config['deletetime'])
    await ctx.send("https://cdn.discordapp.com/attachments/917896528927019012/932138950804537404/unknown.png")


@bot.command()
async def dmdel(ctx, ammount=None):
    try:
        limit = int(ammount)
    except:
        limit=None
    await ctx.message.delete()
    for  m in await ctx.channel.history(limit=limit).flatten():
        try:
            await m.delete()
        except:
            pass

@bot.command()
async def dele(ctx, ammount=None):
    try:
        limit = int(ammount)
    except:
        limit=None
    await ctx.message.delete()
    for  m in await ctx.channel.history(limit=limit).flatten():
        try:
            await m.delete()
        except:
            pass

@bot.command(pass_context=True)
async def femboy(ctx):
    await ctx.message.delete()
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/FemBoys/new.json?sort=hot') as r:
            res = await r.json()

        msg = f"""
```ini
[Femboy uwu]
Enjoy the femboy cutie uwu 
```
    """

        await ctx.send(msg,delete_after=config['deletetime'])
        await ctx.send(res['data']['children'] [random.randint(0, 25)]['data']['url'],delete_after=config['deletetime'])

@bot.command(pass_context=True)
async def anime(ctx):
    await ctx.message.delete()

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/anime/new.json?sort=hot') as r:
            res = await r.json()
        msg = f"""
```ini
[anime]
Enjoy spicy anime 
```
    """

        await ctx.send(msg,delete_after=config['deletetime'])
        await ctx.send(res['data']['children'] [random.randint(0, 25)]['data']['url'],delete_after=config['deletetime'])


@bot.command(pass_context=True)
async def r34(ctx):
    await ctx.message.delete()
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/rule34/new.json?sort=hot') as r:
            res = await r.json()
        msg = f"""
```ini
[R34]
Enjoy r34 memes 
```
    """

        await ctx.send(msg,delete_after=config['deletetime'])
        await ctx.send(res['data']['children'] [random.randint(0, 25)]['data']['url'],delete_after=config['deletetime'])

@bot.command(pass_context=True)
async def gyiff(ctx):
    await ctx.message.delete()

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/gfur/new.json?sort=hot') as r:
            res = await r.json()
        msg = f"""
```ini
[gyiff]
Enjoy Gay yiff 
```
    """

        await ctx.send(msg,delete_after=config['deletetime'])
        await ctx.send(res['data']['children'] [random.randint(0, 25)]['data']['url'],delete_after=config['deletetime'])

@bot.command(pass_context=True)
async def fortnite(ctx):
    await ctx.message.delete()
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/FortniteNSFW/new.json?sort=top') as r:
            res = await r.json()
        msg = f"""
```ini
[Fortnite]
Enjoy fortnite porn 
```
    """

        await ctx.send(msg,delete_after=config['deletetime'])
        await ctx.send(res['data']['children'] [random.randint(0, 25)]['data']['url'],delete_after=config['deletetime'])



@bot.command(pass_context=True)
async def pokeporn(ctx):
    await ctx.message.delete()
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/pokeporn/new.json?sort=hot') as r:
            res = await r.json()
        msg = f"""
```ini
[pokeporn]
Enjoy pokemon porn 
```
    """

        await ctx.send(msg,delete_after=config['deletetime'])
        await ctx.send(res['data']['children'] [random.randint(0, 25)]['data']['url'],delete_after=config['deletetime'])

@bot.command(pass_context=True)
async def yiff(ctx):
    await ctx.message.delete()
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/yiff/new.json?sort=top') as r:
            res = await r.json()
        msg = f"""
```ini
[yiff]
Enjoy yiff uwu 
```
    """

        await ctx.send(msg,delete_after=config['deletetime'])
        await ctx.send(res['data']['children'] [random.randint(0, 25)]['data']['url'],delete_after=config['deletetime'])

@bot.command(pass_context=True)
async def furry(ctx):
    await ctx.message.delete()
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/furry/new.json?sort=hot') as r:
            res = await r.json()
        msg = f"""
```ini
[furry]
Enjoy furry uwu 
```
    """

        await ctx.send(msg,delete_after=config['deletetime'])
        await ctx.send(res['data']['children'] [random.randint(0, 25)]['data']['url'],delete_after=config['deletetime'])


@bot.command()
async def themeinfo(ctx):
    await ctx.message.delete()
    print(Colours.Magenta+"[Command] <>Posted Theme info<>"+Colours.White)
    msg = f"""
    ```ini
    ╔═══════════════════════════════════════════╗
    ║               [THEME INFO]                ║
    ║═══════════════════════════════════════════║
      Theme name: {config['theme']['name']}       
      Theme header: {config['theme']['title']}    
      Delete time: {config['deletetime']}          
      Panel text: {config['theme']['text']}                    
    ╚═══════════════════════════════════════════╝
    ```
    """

    await ctx.send(msg,delete_after=config['deletetime'])

format = "%a, %d %b %Y | %H:%M:%S %ZGMT"

@bot.command()
@commands.guild_only()
async def sinfo(ctx):
    await ctx.message.delete()
    text_channels = len(ctx.guild.text_channels)
    voice_channels = len(ctx.guild.voice_channels)
    categories = len(ctx.guild.categories)
    channels = text_channels + voice_channels
    msg = f"""
    ```ini
    ╔═════════════════════════════════════════════╗
                    [{ctx.guild.name}'s Info]             
    ║═════════════════════════════════════════════║
       ID: [{ctx.guild.id}]                  
       Owner: [{ctx.guild.owner}]                       
       Creation: {ctx.guild.created_at.strftime(format)} 
       Members: {ctx.guild.member_count}                                
       Channels: {channels} Channels {text_channels} Text, {voice_channels} Voice, {categories}   
       Verification: {str(ctx.guild.verification_level).upper()}                        
    ╚═════════════════════════════════════════════╝
    ```
    """

    await ctx.send(msg,delete_after=config['deletetime'])
    print(Colours.Magenta+"[Command] <>ServerInfo<>"+Colours.White)


@bot.command()
async def uptime(ctx):
    await ctx.message.delete()
    uptime = datetime.datetime.utcnow() - start_time
    uptime = str(uptime).split('.')[0]
    msg = f"""
```ini
[Cotra UI has been Online:]
{f''+uptime+''} 
```
    """

    await ctx.send(msg,delete_after=config['deletetime'])
start_time = datetime.datetime.utcnow()



@bot.command()
async def foximg(ctx):
    await ctx.message.delete()
    r = requests.get('https://randomfox.ca/floof/').json()
    msg = f"""
    ```ini
[foximg]
Enjoy fox img 
```
    """

    await ctx.send(msg,delete_after=config['deletetime'])
    await ctx.send(r['image'],delete_after=config['deletetime'])


@bot.command()
async def gcleave(ctx):
    await ctx.message.delete()
    for channel in bot.private_channels:
        if isinstance(channel, discord.GroupChannel):
            await channel.leave()



@bot.command(name="pgif",)
async def pgif(ctx):
        await ctx.message.delete()
        request = requests.get(f'https://nekobot.xyz/api/image?type=pgif')
        res = request.json()
        msg = f"""
```ini
[pgif]
Enjoy porn gif 
```
    """

        await ctx.send(msg,delete_after=config['deletetime'])
        await ctx.send(res['message'])

@bot.command(name="coffee",)
async def coffee(ctx):
        await ctx.message.delete()
        request = requests.get(f'https://nekobot.xyz/api/image?type=coffee')
        res = request.json()
        msg = f"""
```ini
[Coffee]
Enjoy Coffee 
```
    """

        await ctx.send(msg,delete_after=config['deletetime'])
        await ctx.send(res['message'])
        print(Colours.Magenta+"[Command] <>coffee<>"+Colours.White)

@bot.command(name="paizuri",)
async def paizuri(ctx):
        await ctx.message.delete()
        request = requests.get(f'https://nekobot.xyz/api/image?type=paizuri')
        res = request.json()
        msg = f"""
```ini
[paizuri]
Enjoy paizuri  
```
    """

        await ctx.send(msg,delete_after=config['deletetime'])
        await ctx.send(res['message'])
        print(Colours.Magenta+"[Command] <>paizuri<>"+Colours.White)

@bot.command(name="hthighs",)
async def hthighs(ctx):
        await ctx.message.delete()
        request = requests.get(f'https://nekobot.xyz/api/image?type=hthigh')
        res = request.json()
        msg = f"""
```ini
[hthighs]
Enjoy hentai thighs  
```
    """

        await ctx.send(msg,delete_after=config['deletetime'])
        await ctx.send(res['message'])
        print(Colours.Magenta+"[Command] <>hthighs<>"+Colours.White)

@bot.command(name="thighs",)
async def thighs(ctx):
        await ctx.message.delete()
        request = requests.get(f'https://nekobot.xyz/api/image?type=thigh')
        res = request.json()
        msg = f"""
```ini
[thighs]
Enjoythighs  
```
    """

        await ctx.send(msg,delete_after=config['deletetime'])
        await ctx.send(res['message'])

        print(Colours.Magenta+"[Command] <>thighs<>"+Colours.White)

@bot.command(name="gah",)
async def gah(ctx):
        await ctx.message.delete()
        request = requests.get(f'https://nekobot.xyz/api/image?type=gah')
        res = request.json()
        msg = f"""
```ini
[gah]
Gahh!!  
```
    """

        await ctx.send(msg,delete_after=config['deletetime'])
        await ctx.send(res['message'])
        print(Colours.Magenta+"[Command] <>gah<>"+Colours.White)

@bot.command(name="holo",)
async def holo(ctx):
        await ctx.message.delete()
        request = requests.get(f'https://nekobot.xyz/api/image?type=holo')
        res = request.json()
        msg = f"""
```ini
[holo]
Enjoy holo  
```
    """

        await ctx.send(msg,delete_after=config['deletetime'])
        await ctx.send(res['message'])
        print(Colours.Magenta+"[Command] <>holo<>"+Colours.White)

@bot.command()
async def femdom(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/femdom")
    res = r.json()
    msg = f"""
```ini
[femdom]
Enjoy femdom uwu  
```
    """

    await ctx.send(msg,delete_after=config['deletetime'])
    await ctx.send(res['url'],delete_after=config['deletetime'])
    print(Colours.Magenta+"[Command] <>femdom<>"+Colours.White)

@bot.command()
async def lewdkemo(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/lewdkemo")
    res = r.json()
    msg = f"""
```ini
[lewdkemo]
Enjoy lewdkemo uwu  
```
    """

    await ctx.send(msg,delete_after=config['deletetime'])
    await ctx.send(res['url'],delete_after=config['deletetime'])
    print(Colours.Magenta+"[Command] <>lewdkemo<>"+Colours.White)

@bot.command()
async def erokemo(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/erokemo")
    res = r.json()
    msg = f"""
```ini
[erokemo]
Enjoy erokemo uwu  
```
    """

    await ctx.send(msg,delete_after=config['deletetime'])
    await ctx.send(res['url'],delete_after=config['deletetime'])
    print(Colours.Magenta+"[Command] <>erokemo<>"+Colours.White)

@bot.command()
async def pwankg(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/pwankg")
    res = r.json()
    msg = f"""
```ini
[pwankg]
Enjoy pwankg uwu  
```
    """

    await ctx.send(msg,delete_after=config['deletetime'])
    await ctx.send(res['url'],delete_after=config['deletetime'])
    print(Colours.Magenta+"[Command] <>pwankg<>"+Colours.White)

@bot.command()
async def keta(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/keta")
    res = r.json()
    msg = f"""
```ini
[keta]
Enjoy keta uwu  
```
    """

    await ctx.send(msg,delete_after=config['deletetime'])
    await ctx.send(res['url'],delete_after=config['deletetime'])
    print(Colours.Magenta+"[Command] <>keta<>"+Colours.White)

@bot.command()
async def lewdk(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/lewdk")
    res = r.json()
    msg = f"""
```ini
[lewdk]
Enjoy lewdk uwu  
```
    """

    await ctx.send(msg,delete_after=config['deletetime'])
    await ctx.send(res['url'],delete_after=config['deletetime'])
    print(Colours.Magenta+"[Command] <>lewdk<>"+Colours.White)

@bot.command()
async def waifu(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/waifu")
    res = r.json()
    msg = f"""
```ini
[waifu]
Enjoy waifu uwu  
```
    """

    await ctx.send(msg,delete_after=config['deletetime'])
    await ctx.send(res['url'],delete_after=config['deletetime'])
    print(Colours.Magenta+"[Command] <>waifu<>"+Colours.White)

@bot.command()
async def eron(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/eron")
    res = r.json()
    msg = f"""
```ini
[eron]
Enjoy eron uwu  
```
    """

    await ctx.send(msg,delete_after=config['deletetime'])
    await ctx.send(res['url'],delete_after=config['deletetime'])
    print(Colours.Magenta+"[Command] <>eron<>"+Colours.White)

@bot.command()
async def eroyuri(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/eroyuri")
    res = r.json()
    msg = f"""
```ini
[eroyuri]
Enjoy eroyuri uwu  
```
    """

    await ctx.send(msg,delete_after=config['deletetime'])
    await ctx.send(res['url'],delete_after=config['deletetime'])
    print(Colours.Magenta+"[Command] <>eroyuri<>"+Colours.White)

@bot.command()
async def solo(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/solo")
    res = r.json()
    msg = f"""
```ini
[solo]
Enjoy solo uwu  
```
    """

    await ctx.send(msg,delete_after=config['deletetime'])
    await ctx.send(res['url'],delete_after=config['deletetime'])
    print(Colours.Magenta+"[Command] <>solo<>"+Colours.White)

@bot.command()
async def massgc(ctx,userid1,times):
    if not is_me(ctx.message):
        return
    await ctx.message.delete()
    for x in range(int(times)):
            
        headers = {
            'authority': 'discord.com',
            'content-length': '0',
            'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjIwMDAiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLUdCIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTA0Mjc2LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
            'x-context-properties': 'eyJsb2NhdGlvbiI6IkFkZCBGcmllbmRzIHRvIERNIn0=',
            'authorization': config["token"],
            'x-debug-options': 'bugReporterEnabled',
            'accept-language': 'en-US',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36',
            'accept': '*/*',
            'origin': 'https://discord.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://discord.com/channels/@me/895409258785550406',
            'cookie': '__dcfduid=0f52e1903dce11eca260a166ca1ce2a2; __sdcfduid=0f52e1913dce11eca260a166ca1ce2a26685cf1817e5918f525ccb544c7b38dd469403cf86d6082435cd8cbb46d620ef; __stripe_mid=b0aea78a-f66f-4067-b204-0a7ee4db6acaf58e16',
        }

        response = requests.put(f'https://discord.com/api/v9/channels/{str(ctx.channel.id)}/recipients/{userid1}', headers=headers)
        
        #print(response.text)
        createdserver = response.json()
        for x in createdserver["recipients"]:
            if userid1 != x["id"]:
                cotra=x["id"]

        headers = {
            'authority': 'discord.com',
            'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjIwMDAiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLUdCIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTA0Mjc2LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
            'authorization': config['token'],
            'x-debug-options': 'bugReporterEnabled',
            'accept-language': 'en-US',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36',
            'accept': '*/*',
            'origin': 'https://discord.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://discord.com/channels/@me/908312413412155404',
            'cookie': '__dcfduid=0f52e1903dce11eca260a166ca1ce2a2; __sdcfduid=0f52e1913dce11eca260a166ca1ce2a26685cf1817e5918f525ccb544c7b38dd469403cf86d6082435cd8cbb46d620ef; __stripe_mid=b0aea78a-f66f-4067-b204-0a7ee4db6acaf58e16',
        }

        response = requests.delete(f'https://discord.com/api/v9/channels/{str(createdserver["id"])}/recipients/{cotra}', headers=headers)
        #print(cotra)
        #print(response.text)
        choices = ["haha lol","bitchnigga","fatty","https://www.cotra.xyz","U suck","die bitch","CotraUI Selfbot","You smell","fuck you","Get Creampied","https://www.pornhub.com/gay"]
        headers = {
            'authority': 'discord.com',
            'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjIwMDAiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLUdCIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTA0Mjc2LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
            'authorization': config['token'],
            'x-debug-options': 'bugReporterEnabled',
            'accept-language': 'en-US',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36',
            'content-type': 'application/json',
            'accept': '*/*',
            'origin': 'https://discord.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://discord.com/channels/@me/908317396379525160',
            'cookie': '__dcfduid=0f52e1903dce11eca260a166ca1ce2a2; __sdcfduid=0f52e1913dce11eca260a166ca1ce2a26685cf1817e5918f525ccb544c7b38dd469403cf86d6082435cd8cbb46d620ef; __stripe_mid=b0aea78a-f66f-4067-b204-0a7ee4db6acaf58e16',
        }
        xyz = random.choice(choices)
        data = '{"name":"'+xyz+'"}'

        response = requests.patch(f'https://discord.com/api/v9/channels/{str(createdserver["id"])}', headers=headers, data=data)

        headers = {
            'authority': 'discord.com',
            'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjIwMDAiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLUdCIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTA0Mjc2LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
            'authorization': config['token'],
            'x-debug-options': 'bugReporterEnabled',
            'accept-language': 'en-US',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36',
            'accept': '*/*',
            'origin': 'https://discord.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://discord.com/channels/@me',
            'cookie': '__dcfduid=0f52e1903dce11eca260a166ca1ce2a2; __sdcfduid=0f52e1913dce11eca260a166ca1ce2a26685cf1817e5918f525ccb544c7b38dd469403cf86d6082435cd8cbb46d620ef; __stripe_mid=b0aea78a-f66f-4067-b204-0a7ee4db6acaf58e16',
        }

        response = requests.delete(f'https://discord.com/api/v9/channels/{str(createdserver["id"])}', headers=headers)
       # print(response.text)

# (pass_context)= True
# async def rainbowrole(ctx,*,rolename):
#     if not is_me(ctx.message): #i like lines
#         return
#     await ctx.message.delete()
#     print("<>rainbowrole<>")
    
#     role = discord.utils.get(ctx.message.guild.roles,name=rolename)
#     colors = ["16711685","15105570","16771840","2067276","3447003","10181046","15277667"]
#     num1 = 0
#     while True:


#         headers = {
#             'authority': 'discord.com',
#             'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjIwMDAiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLUdCIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTA0Mjc2LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
#             'authorization': config['token'],
#             'x-debug-options': 'bugReporterEnabled',
#             'accept-language': 'en-US',
#             'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36',
#             'content-type': 'application/json',
#             'accept': '*/*',
#             'origin': 'https://discord.com',
#             'sec-fetch-site': 'same-origin',
#             'sec-fetch-mode': 'cors',
#             'sec-fetch-dest': 'empty',
#             'referer': 'https://discord.com/channels/889840534754054145/907218560248610836',
#             'cookie': '__dcfduid=0f52e1903dce11eca260a166ca1ce2a2; __sdcfduid=0f52e1913dce11eca260a166ca1ce2a26685cf1817e5918f525ccb544c7b38dd469403cf86d6082435cd8cbb46d620ef; __stripe_mid=b0aea78a-f66f-4067-b204-0a7ee4db6acaf58e16',
#         }

#         data = '{"name":"'+rolename+'","permissions":"1071728021057","color":'+str(random.choice(colors))+',"hoist":false,"mentionable":false,"icon":null,"unicode_emoji":null}'

#         response = requests.patch(f'https://discord.com/api/v9/guilds/{str(ctx.message.guild.id)}/roles/{str(role.id)}', headers=headers, data=data)
#         await asyncio.sleep(1.5)
#         #if num1 + 1000 > 16777215:
#             #num1 = 0
#         #num1 += 1000
#         #print(response.text)
#         if "retry_after" in response.text:
#             kk=response.json()
#             print(f"hit retry limit waiting {str(kk['retry_after'])} second(s)")
#             await asyncio.sleep(int(kk["retry_after"]))

@bot.command()
async def mysite(ctx,):
    await ctx.message.delete()
    msg = f"""
```ini
[CotraUI Website]  
```
    """

    await ctx.send(msg,delete_after=config['deletetime'])
    await ctx.send("https://www.cotra.xyz")
    print(Colours.Magenta+"[Command] <>MySite<>"+Colours.White)

@bot.command()
async def balls(ctx):
    await ctx.message.delete()
    msg = f"""
```ini
[My balls are cold]
uwu :3  
```
    """

    await ctx.send(msg,delete_after=config['deletetime'])
    await ctx.send("https://media.discordapp.net/attachments/824953552324788273/908661319488634910/image0-5-2.gif",delete_after=config['deletetime'])



@bot.command()
async def nitroking(ctx):
    await ctx.message.delete()
    msg = f"""
```ini
[96 BOOSTS IN A DAY]
Nitro King  
```
    """

    await ctx.send(msg,delete_after=config['deletetime'])
    await ctx.send("https://images-ext-1.discordapp.net/external/Ma42_cB-hgi9YnQKzK5iELhamXlDktUk-7-U9JtGXWo/https/cdn.upload.systems/uploads/GM5MIAlZ.png?width=393&height=671",delete_after=config['deletetime'])
    print(Colours.Magenta+"[Command] <>NitroPosted<>"+Colours.White)

@bot.command()
async def neko(ctx):
    if not is_me(ctx.message):
        return
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/neko")
    res = r.json()
    msg = f"""
```ini
[neko]
Enjoy neko uwu  
```
    """

    await ctx.send(msg,delete_after=config['deletetime'])
    await ctx.send(res['url'],delete_after=config['deletetime'])
    print(Colours.Magenta+"[Command] <>neko<>"+Colours.White)

@bot.command()
async def emptymessage(ctx):
    await ctx.message.delete()
    await ctx.send("_ _")

@bot.command()
async def first(ctx):
    await ctx.message.delete()
    channel = ctx.channel
    first_message = (await channel.history(limit = 1, oldest_first = True).flatten())[0]
    msg = f"""
```ini
[First message]
First message: {first_message.content}
Click the url below to go to the first msg
```
    """

    await ctx.send(msg,delete_after=config['deletetime'])
    await ctx.send(f"{first_message.jump_url}")                                        


@bot.command()
async def animnick(ctx,*,names):
    print(Colours.Magenta+"[Command] <>animnick started<>"+Colours.White)
    if not is_me(ctx.message):
        return
    await ctx.message.delete()
    names=names.split(" ")
    while True:
    


        headers = {
        'authority': 'discord.com',
        'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjIwMDAiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLUdCIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTA0NTk3LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
        'x-fingerprint': '908477669916692491.kcb2l619Luz24fNTGCkHM-OklWM',
        'authorization': config['token'],
        'x-debug-options': 'bugReporterEnabled',
        'accept-language': 'en-US',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36',
        'content-type': 'application/json',
        'accept': '*/*',
        'origin': 'https://discord.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://discord.com/channels/907501014914060329/907501015341858824',
        'cookie': '__dcfduid=0f52e1903dce11eca260a166ca1ce2a2; __sdcfduid=0f52e1913dce11eca260a166ca1ce2a26685cf1817e5918f525ccb544c7b38dd469403cf86d6082435cd8cbb46d620ef; __stripe_mid=b0aea78a-f66f-4067-b204-0a7ee4db6acaf58e16',
    }
        for x in names:
            data = '{"nick":"'+x+'"}'

            response = requests.patch(f'https://discord.com/api/v9/guilds/{str(ctx.guild.id)}/members/@me', headers=headers, data=data)
            await asyncio.sleep(12)
            if "retry_after" in response.text:
                kk=response.json()
                print(f"hit retry limit waiting {str(kk['retry_after'])} second(s)")
                await asyncio.sleep(int(kk["retry_after"]))


@animnick.error
async def animnick_error(ctx,error):
    await ctx.message.delete()
    msg = f"""
    ```css
    ╔═══════════════════════════════════╗
              [Critical ERROR]         
    ║═══════════════════════════════════║

      How to use: [{bot.command_prefix}]animnick (text 1) (text 2)
      Details: It changes nickname rapidly
      Use: [In servers only]

    ╚═══════════════════════════════════╝
    ```
    """

    await ctx.send(msg,delete_after=config['deletetime'])
    print(Fore.RED+f"[SYSTEM] Animnick error!"+Fore.RESET)



@bot.event
async def on_command_error(ctx, error:commands.CommandError):
        if isinstance(error, commands.CommandNotFound):
            await ctx.message.delete()
            cmd = ctx.message.content.split()[0]
            cmd = cmd.lstrip(prefix)
        msg = f"""
    ```css
    ╔═══════════════════════════════════╗
              [Critical ERROR]         
    ║═══════════════════════════════════║
      The command {cmd} Does not exist  
    ╚═══════════════════════════════════╝
    ```
    """

        await ctx.send(msg,delete_after=config['deletetime'])
        print(Fore.RED+f"[SYSTEM] The Command {cmd} Does not exist"+Fore.RESET)

@yiff.error
async def yiff_error(ctx,error):
    await ctx.message.delete()
    msg = f"""
    ```css
    ╔═══════════════════════════════════╗
              [Critical ERROR]         
    ║═══════════════════════════════════║

             Something broke lol

    ╚═══════════════════════════════════╝
    ```
    """

    await ctx.send(msg,delete_after=config['deletetime'])
    print(Fore.RED+f"[SYSTEM] yiff error!"+Fore.RESET)

@furry.error
async def furry_error(ctx,error):
    await ctx.message.delete()
    msg = f"""
    ```css
    ╔═══════════════════════════════════╗
              [Critical ERROR]         
    ║═══════════════════════════════════║

             Something broke lol

    ╚═══════════════════════════════════╝
    ```
    """

    await ctx.send(msg,delete_after=config['deletetime'])
    print(Fore.RED+f"[SYSTEM] yiff error!"+Fore.RESET)


@femboy.error
async def femboy_error(ctx,error):
    await ctx.message.delete()
    msg = f"""
    ```css
    ╔═══════════════════════════════════╗
              [Critical ERROR]         
    ║═══════════════════════════════════║

             Something broke lol

    ╚═══════════════════════════════════╝
    ```
    """

    await ctx.send(msg,delete_after=config['deletetime'])
    print(Fore.RED+f"[SYSTEM] yiff error!"+Fore.RESET)

@rgbrole.error
async def rgbrole_error(ctx,error):
    await ctx.message.delete()
    msg = f"""
    ```css
    ╔═══════════════════════════════════╗
              [Critical ERROR]         
    ║═══════════════════════════════════║

      How to use: [{bot.command_prefix}]rgbrole (@role)
      Details: It changes role color rainbow
      Use: [In servers only]

    ╚═══════════════════════════════════╝
    ```
    """

    await ctx.send(msg,delete_after=config['deletetime'])
    print(Fore.RED+f"[SYSTEM] rgbrole error!"+Fore.RESET)

@sinfo.error
async def sinfo_error(ctx,error):
    await ctx.message.delete()
    msg = f"""
    ```css
    ╔═══════════════════════════════════╗
              [Critical ERROR]         
    ║═══════════════════════════════════║

      [YOU CAN ONLY DO THIS IN SERVERS]

    ╚═══════════════════════════════════╝
    ```
    """

    await ctx.send(msg,delete_after=config['deletetime'])
    print(Fore.RED+f"[SYSTEM] sinfo error!"+Fore.RESET)

@massgc.error
async def massgc_error(ctx,error):
    await ctx.message.delete()
    msg = f"""
    ```css
    ╔═══════════════════════════════════╗
              [Critical ERROR]         
    ║═══════════════════════════════════║

      How to use: [{bot.command_prefix}]massgc (victim ID)
      Details: You must send the command in friends dms to work

    ╚═══════════════════════════════════╝
    ```
    """

    await ctx.send(msg,delete_after=config['deletetime'])
    print(Fore.RED+f"[SYSTEM] massgc error!"+Fore.RESET)

@bot.command(name="restart", aliases=["shutdown","botgobrrr","goaway"])
async def restart(ctx):
    await ctx.message.delete()
    if not is_me(ctx.message):
        return
    msg = f"""
    ```ini
    ╔═══════════════════════════════════╗
                [RESTARTING]         
    ║═══════════════════════════════════║

      COTRA IS RESTARTING PLEASE WAIT...

    ╚═══════════════════════════════════╝
    ```
    """

    await ctx.send(msg,delete_after=config['deletetime'])
    print(Colours.Magenta+"[Command] <>restarting<>"+Colours.White)
    restart_bot()


@bot.command(aliases=['youtube','yt'])
async def _youtube(ctx, *, search):
    await ctx.message.delete()
    author=ctx.message.author
    guild=ctx.guild
    query_string = urllib.parse.urlencode({'search_query': search})
    html_content = urllib.request.urlopen('http://www.youtube.com/results?' + query_string)
    search_content= html_content.read().decode()
    search_results = re.findall(r'\/watch\?v=\w+', search_content)
    #print(search_results)
    await ctx.send(f'{author.mention} result:\n https://www.youtube.com' + search_results[0])



@bot.command('tts')
async def tts(ctx, *, text):
    await ctx.message.delete()
    myobj = gTTS(text=text, lang='en', slow=False)
    myobj.save(f"{os.getcwd()}/tts.mp3")
    await ctx.send(file=discord.File(f'{os.getcwd()}/tts.mp3'))
    await asyncio.sleep(5)
    os.remove(f'{os.getcwd()}/tts.mp3')



@bot.command()
async def ban(ctx, *, user: discord.Member):
    await ctx.message.delete()
    await user.ban()
    msg = f"""
    ```ini
    ╔═══════════════════════════════════╗
                  [BANNED]         
    ║═══════════════════════════════════║

      Done. {user.name} has been banned

    ╚═══════════════════════════════════╝
    ```
    """

    await ctx.send(msg,delete_after=config['deletetime'])


@bot.command(name='unban')
async def _unban(ctx, id: int):
    user = await bot.fetch_user(id)
    await ctx.guild.unban(user)
    await ctx.message.delete()
    msg = f"""
    ```ini
    ╔═══════════════════════════════════╗
                  [UNBANNED]         
    ║═══════════════════════════════════║

      Done. {user.name} has been unbanned

    ╚═══════════════════════════════════╝
    ```
    """

    await ctx.send(msg,delete_after=config['deletetime'])

@bot.command()
async def kick(ctx,*, user: discord.Member):
   await ctx.message.delete()
   await user.kick()
   msg = f"""
    ```ini
    ╔═══════════════════════════════════╗
                  [KICKED]         
    ║═══════════════════════════════════║

      Done. {user.name} has been KICKED

    ╚═══════════════════════════════════╝
    ```
    """

   await ctx.send(msg,delete_after=config['deletetime'])

@bot.command()
async def pp(ctx, member = None):
    await ctx.message.delete()
    if member == None:
        member = ctx.author
    else:
        member = ctx.message.mentions[0]
    size = random.randint(1, 15)
    dong = ""
    for _i in range(0, size):
        dong += "="
        msg = f"""
```ini
[Penis size]
The User {member.display_name}'s dick size is 8{dong}D 😳
```
    """

    await ctx.send(msg,delete_after=config['deletetime'])     



@bot.command()
async def yoink(ctx): 
    await ctx.message.delete()
    wow = await bot.create_guild(f'{ctx.guild.name}')
    await asyncio.sleep(4)
    for g in bot.guilds:
        if f'backup-{ctx.guild.name}' in g.name:
            for c in g.channels:
                await c.delete()
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}")
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}")
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(f"{chann}")
    for role in ctx.guild.roles[::-1]:
        if role.name != "@everyone":
            try:
                await wow.create_role(name=role.name, color=role.color, permissions=role.permissions, hoist=role.hoist, mentionable=role.mentionable)
            except:
                break

@bot.command()
async def niko(ctx):
    await ctx.message.delete()
    if not is_me(ctx.message):
        return
    msg = f"""
```ini
[Niko]
Simply the best command
```
    """

    await ctx.send(msg,delete_after=config['deletetime'])
    await ctx.send("https://cdn.discordapp.com/attachments/867153594142687302/872394286564540486/5bd354ffd5f3baf0e9fa45d2f25b5a78a04c3100.mp4",delete_after=config['deletetime']) 


@bot.command()
async def info(ctx,):
    await ctx.message.delete()
    totalcommands = len(bot.commands)
    if not is_me(ctx.message):
        return

    msg = f"""
    ```ini
    ╔═══════════════════════════════════╗
    ║         [Cotra UI Info]           ║
    ║═══════════════════════════════════║
    ║        Made by [cotra#0001]       ║
    ║═══════════════════════════════════║ 
      Total commands: {totalcommands}               
      Prefix: [{bot.command_prefix}]                         
      Version: [{version}]                      
      Theme: {config['theme']['name']}                     
    ║                                   ║
    ╚═══════════════════════════════════╝
    ```
    """
    await ctx.send(msg,delete_after=config['deletetime'])


@bot.command()
async def encrypt(ctx, *, text: str):
    await ctx.message.delete()
    to_morse = { 
        "a" : "ɗรٱคร",
        "b" : "ɗรٱค",
        "c" : "รɗﻉ",
        "d" : "Շร๔є",
        "e" : "ፕነዕቿ",
        "f" : "丂d乇",
        "g" : "Շรɗﻉ",
        "h" : "ዪዐጌረዐሸሠሁነቿፕ5",
        "i" : "ዪዐጌረዐሸሠሁነቿፕ",
        "j" : "ዪዐጌረዐሸሠሁነቿ",
        "k" : "ዪዐጌረዐሸሠሁነ",
        "l" : "ዪዐጌረዐሸሠሁነቿ5",
        "m" : "ዪዐጌረዐሸሠሁዐ",
        "n" : "ዪዐጌረዐሸሠሁ",
        "o" : "ዪዐጌረዐሁነቿፕ5",
        "p" : "ዪዐጌረሸሠሁነቿፕ5",
        "q" : "ዪዐረዐሸሠሁነቿፕ5",
        "r" : "ዪዐጌረዐሸሠሁነቿ?5",
        "s" : "ዪዐጌረዐሠሁነቿፕ5",
        "t" : "ዐጌረዐሸሠሁነቿፕ5",
        "u" : "ҀФГЯД",
        "v" : "ҀФГЯ",
        "w" : "ҀФr",
        "x" : "ҀФГ",
        "y" : "ℜ𝔄",
        "z" : "ｷ乇ｲg",
        "1" : ".คŦгเςค",
        "2" : ".. ልቻዪጎርል",
        "3" : "ₐfᵣᵢcₐ",
        "4" : "丂 乃o尺刀",
        "5" : "ﾶﾘ ﾶoﾶ",
        "6" : "🇲🇾 🇲🇴🇲",
        "7" : "cﾑ",
        "8" : "Ў",
        "9" : "𝓶𝓸𝓶",
        "0" : "-----",
        "-" : "ልዪፕዐር",
        "." : "ↄoTᴙA",
        "?" : "£$R%T:$£PT",
        "!" : "𝐜𝐨𝐭𝐫𝐚",
        "/" : "???????",
        "£" : "ȼøŧɍȺ",
        "$" : "ᶜᵒᵗʳᵃ",
        "," : "ዪልኗክልዪዐጕ",
        "_" : " ",
        ":" : "???!??!sped!?!?!",
        "#" : "???!??!cotra!?!?!"
    }
    cipher = ''
    for letter in text:
        if letter != ' ':
            cipher += to_morse[letter.lower()] + ' '
        else:
            cipher += ' '
    encrypted = (cipher)
    msg = f"""
```ini
[ENCRYPTED!!]
Below will be your encrypted message (NO ONE CAN CRACK THIS APART FROM COTRA USERS)
Encrypted [{cipher}]
    ```
    """
    await ctx.send(msg,delete_after=config['deletetime'])


@bot.command()
async def decrypt(ctx, *, text: str):
    await ctx.message.delete()
    to_morse = { 
        "a" : "ɗรٱคร",
        "b" : "ɗรٱค",
        "c" : "รɗﻉ",
        "d" : "Շร๔є",
        "e" : "ፕነዕቿ",
        "f" : "丂d乇",
        "g" : "Շรɗﻉ",
        "h" : "ዪዐጌረዐሸሠሁነቿፕ5",
        "i" : "ዪዐጌረዐሸሠሁነቿፕ",
        "j" : "ዪዐጌረዐሸሠሁነቿ",
        "k" : "ዪዐጌረዐሸሠሁነ",
        "l" : "ዪዐጌረዐሸሠሁነቿ5",
        "m" : "ዪዐጌረዐሸሠሁዐ",
        "n" : "ዪዐጌረዐሸሠሁ",
        "o" : "ዪዐጌረዐሁነቿፕ5",
        "p" : "ዪዐጌረሸሠሁነቿፕ5",
        "q" : "ዪዐረዐሸሠሁነቿፕ5",
        "r" : "ዪዐጌረዐሸሠሁነቿ?5",
        "s" : "ዪዐጌረዐሠሁነቿፕ5",
        "t" : "ዐጌረዐሸሠሁነቿፕ5",
        "u" : "ҀФГЯД",
        "v" : "ҀФГЯ",
        "w" : "ҀФr",
        "x" : "ҀФГ",
        "y" : "ℜ𝔄",
        "z" : "ｷ乇ｲg",
        "1" : ".คŦгเςค",
        "2" : ".. ልቻዪጎርል",
        "3" : "ₐfᵣᵢcₐ",
        "4" : "丂 乃o尺刀",
        "5" : "ﾶﾘ ﾶoﾶ",
        "6" : "🇲🇾 🇲🇴🇲",
        "7" : "cﾑ",
        "8" : "Ў",
        "9" : "𝓶𝓸𝓶",
        "0" : "-----",
        "-" : "ልዪፕዐር",
        "." : "ↄoTᴙA",
        "?" : "£$R%T:$£PT",
        "!" : "𝐜𝐨𝐭𝐫𝐚",
        "/" : "???????",
        "£" : "ȼøŧɍȺ",
        "$" : "ᶜᵒᵗʳᵃ",
        "," : "ዪልኗክልዪዐጕ",
        "_" : " ",
        ":" : "???!??!sped!?!?!",
        "#" : "???!??!cotra!?!?!"
    }
    text += ' '
    decipher = ''
    cipher = ''
    for letter in text:
        if letter != ' ':
            i = 0
            cipher += letter
        else:
            i += 1 
            if i == 2:
                decipher += ' '
            else:
                decipher += list(to_morse.keys())[list(to_morse.values()).index(cipher)]
                cipher = ''
    decrypted = (decipher)
    msg = f"""
```ini
[DECRYPTED!!]
Below will be your decrypted message
Decrypted: [{decrypted}]  do [{bot.command_prefix}]encrypt to encrypt a message
    ```
    """
    await ctx.send(msg,delete_after=config['deletetime'])

@bot.command()
async def gp(ctx, member=None):
    await ctx.message.delete()
    if member == None:
        member = ctx.author
    else:
        member = ctx.message.mentions[0]

@bot.command()
async def discum(ctx,):
    await ctx.message.delete()
    if not is_me(ctx.message):
        return
    msg = f"""
```ini
[discum]
discum sucks massive cock
    ```
    """
    await ctx.send(msg,delete_after=config['deletetime'])
    await ctx.send("https://cdn.discordapp.com/attachments/900114227862323210/913448547574251621/poop-emoji-png-transparent-background-image-free-png-templates-poop-emoji-transparent-1000_824.png")


@bot.command()
async def blm(ctx):
    await ctx.message.delete()
    if not is_me(ctx.message):
        return
    msg = f"""
```ini
[BLM!!!]
JUST KIDDING BITCH ASS NIGGA
    ```
    """
    await ctx.send(msg,delete_after=config['deletetime'])
    await ctx.send("https://cdn.discordapp.com/attachments/900098205738475551/913912873019924540/aprilfoolsdaymsn.jpg")

@bot.command()
async def allcmds(ctx):
    await ctx.message.delete()
    await ctx.send(f"{prefix}general", delete_after=0.1)
    await asyncio.sleep(2)
    await ctx.send(f"{prefix}fun", delete_after=0.1)
    await asyncio.sleep(2)
    await ctx.send(f"{prefix}memes", delete_after=0.1)
    await asyncio.sleep(2)
    await ctx.send(f"{prefix}images", delete_after=0.1)
    await asyncio.sleep(2)
    await ctx.send(f"{prefix}images2", delete_after=0.1)
    await asyncio.sleep(2)
    await ctx.send(f"{prefix}nsfw", delete_after=0.1)
    await asyncio.sleep(2)
    await ctx.send(f"{prefix}nsfw2", delete_after=0.1)
    await asyncio.sleep(2)
    await ctx.send(f"{prefix}server", delete_after=0.1)
    await asyncio.sleep(2)
    await ctx.send(f"{prefix}text", delete_after=0.1)
    await asyncio.sleep(2)
    await ctx.send(f"{prefix}token", delete_after=0.1)
    await asyncio.sleep(2)
    await ctx.send(f"{prefix}promo", delete_after=0.1)
    await asyncio.sleep(2)
    await ctx.send(f"{prefix}settings", delete_after=0.1)

@bot.command()
async def spam(ctx, *, message, amount: int):
    await ctx.message.delete()    
    for _i in range(amount):
        await ctx.send(message)


@bot.command()
async def cactus(ctx):
    if not is_me(ctx.message):
        await ctx.message.delete()
        return
    msg = f"""
    ```ini
    ╔═══════════════════════════════════╗
              [Cactus Reselling]         
    ║═══════════════════════════════════║
           Official Reseller of COTRA
         
         https://CactusReselling.com
         
         https://discord.gg/XKAS4kpCwg

    ╚═══════════════════════════════════╝
    ```
    """

    await ctx.send(msg,delete_after=config['deletetime'])
    print(Colours.Magenta+"[Command] <>Cactus posted<>"+Colours.White)


@bot.command()
async def troop(ctx):
    if not is_me(ctx.message):
        await ctx.message.delete()
        return
    msg = f"""
    ```ini
    ╔═══════════════════════════════════╗
                [Troop keys]         
    ║═══════════════════════════════════║
          Official Reseller of COTRA
         
            https://troopkeys.cf/
         
         https://discord.gg/ts38Bbth

    ╚═══════════════════════════════════╝
    ```
    """

    await ctx.send(msg,delete_after=config['deletetime'])
    print(Colours.Magenta+"[Command] <>troop posted<>"+Colours.White)


@bot.command()
async def pathetic(ctx):
    if not is_me(ctx.message):
        await ctx.message.delete()
        return
    msg = f"""
    ```ini
    ╔═══════════════════════════════════╗
                 [Pathetic]         
    ║═══════════════════════════════════║
          Official Reseller of COTRA
         
            https://lamahook.xyz/
         
         https://discord.gg/QxrAEmatJ3

    ╚═══════════════════════════════════╝
    ```
    """

    await ctx.send(msg,delete_after=config['deletetime'])
    print(Colours.Magenta+"[Command] <>pathetic posted<>"+Colours.White)

@bot.command()
async def complex(ctx):
    await ctx.message.delete()
    msg = f"""
    ```ini
    ╔═══════════════════════════════════╗
             [Complex Services]         
    ║═══════════════════════════════════║
          Official Reseller of COTRA
         
         https://discord.gg/RXTf4f7bTc

    ╚═══════════════════════════════════╝
    ```
    """

    await ctx.send(msg,delete_after=config['deletetime'])
    print(Colours.Magenta+"[Command] <>complex posted<>"+Colours.White)

@bot.command()
async def flop(ctx):
    await ctx.message.delete()
    msg = f"""
    ```ini
    ╔═══════════════════════════════════╗
                    [FLOP]         
    ║═══════════════════════════════════║
          Official Reseller of COTRA
         
         https://discord.gg/4GzYd6AuGk

    ╚═══════════════════════════════════╝
    ```
    """

    await ctx.send(msg,delete_after=config['deletetime'])
    print(Colours.Magenta+"[Command] <>flop posted<>"+Colours.White)

@bot.command(name="ascii",  aliases=["asci","asc"])
async def ascii(ctx, *, text: str):
        if text is None:
            return
        else:
            r = requests.get(f'https://artii.herokuapp.com/make?text={urllib.parse.quote(text)}')
            rr = r.text
            try:
                await ctx.send(f'```{rr}```')
            except discord.HTTPException:
                return
            await ctx.message.delete()
def avatarUrl(id, avatar):
            url = ""
            if not str(avatar).startswith("http"):
                if str(avatar).startswith("a_"):
                    url =  f"https://cdn.discordapp.com/avatars/{id}/{avatar}.gif?size=1024"
                else:
                    url =  f"https://cdn.discordapp.com/avatars/{id}/{avatar}.png?size=1024"
@bot.command()
async def userinfo(ctx, member=None):
    await ctx.message.delete()
    if member == None:
        member = ctx.author
    else:
        member = ctx.message.mentions[0]
    msg = f"""
    ```ini
    ╔═══════════════════════════════════╗
    ║             [USERINFO]            ║
    ║═══════════════════════════════════║
      Username: {member.display_name}                 
    ║ ID: {member.id}            ║
    ║ Tag: [#{member.discriminator}]                      ║   
    ║ Creation date: {member.created_at.strftime('%d/%m/%Y')}         ║
      Is bot: {member.bot}                     
    ╚═══════════════════════════════════╝
    ```
    """

    await ctx.send(msg,delete_after=config['deletetime'])
    print(Colours.Magenta+"[Command] <>userinfo posted<>"+Colours.White)

@bot.command(name="rv", description="Reverses the text", usage="Reverse <text>")
async def reverse(ctx, *, text: str):
    await ctx.message.delete()
    await ctx.send(''.join(reversed(text)))


@bot.command()
async def nshout(ctx):
    msg = f"""
    ```ini
    [Nshout]
    Nshout is a femboy uwu
    ```
    """

    await ctx.send(msg,delete_after=config['deletetime'])
    await ctx.send("https://cdn.discordapp.com/attachments/927495636570488856/929860390534385714/d2a5e5addccd1c9082b127fd0dca67e3.gif")


@bot.command()
async def stickbug(ctx, member=None):
    if member==None:
        member = ctx.message.author
    else:
        member = ctx.message.mentions[0]
        member = await bot.fetch_user(int(member.id))
    await ctx.message.delete()
    url = member.avatar_url_as(format="png")
    response = requests.get(f"https://nekobot.xyz/api/imagegen?type=stickbug&url={url}")
    stuff = json.loads(response.text)
    await ctx.send(stuff["message"])

@bot.command()
async def warcrimes(ctx):
    await ctx.message.delete()
    msg = f"""
    ```ini
    [warcrimes]
    I pwomise i didnt!
    ```
    """

    await ctx.send(msg,delete_after=config['deletetime'])
    await ctx.send("https://media.discordapp.net/attachments/927495636570488856/927557846827151370/klee-genshin-impact-klee.gif")

@bot.command()
async def ducking(ctx):
    await ctx.message.delete()
    msg = f"""
    ```ini
    [ducking]
    dwuck dwuck uwu
    ```
    """

    await ctx.send(msg,delete_after=config['deletetime'])
    await ctx.send("https://media.discordapp.net/attachments/916823128351588382/916824513021353984/fakeduck_p.gif",delete_after=config['deletetime'])


@bot.command()
async def gay(ctx, member=None):
    await ctx.message.delete()
    if member==None:
        member=ctx.author
    else:
        member = ctx.message.mentions[0]
        member = await bot.fetch_user(int(member.id))
        msg = f"""
    ```ini
    [How gay?]
    {member.display_name} is {random.randint(0,100)}% gay
    ```
    """
    await ctx.send(msg,delete_after=config['deletetime'])

@bot.command()
async def trampoline(ctx):
    await ctx.message.delete()
    msg = f"""
    ```ini
    [trampoline]
    Bwoing Bwoing uwu
    ```
    """

    await ctx.send(msg,delete_after=config['deletetime'])
    await ctx.send("https://cdn.discordapp.com/attachments/927312578022092880/928423819025203290/god-i-love-trampolining-katieverse.gif")

@bot.command()
async def play(ctx):
    await ctx.message.delete()
    msg = f"""
    ```ini
    [play]
    Pwease Pway with me
    ```
    """

    await ctx.send(msg,delete_after=config['deletetime'])
    await ctx.send("https://media.discordapp.net/attachments/927495636570488856/927557571802447922/klee-genshin-impact.gif")
    print(Colours.Magenta+"[Command] <>play<>"+Colours.White)

@bot.command()
async def ohno(ctx):
    await ctx.message.delete()
    msg = f"""
    ```ini
    [play]
    oh no horny is back
    ```
    """

    await ctx.send(msg,delete_after=config['deletetime'])
    await ctx.send("https://cdn.discordapp.com/attachments/927312578022092880/928387835382349894/863823606831120426.png")
    print(Colours.Magenta+"[Command] <>ohno<>"+Colours.White)

@bot.command()
async def spfp(ctx):
    await ctx.message.delete()
    f = ctx.guild
    await ctx.send(f.icon_url)

@bot.command()
async def trump(ctx, *, msg):
    await ctx.message.delete()
    response = requests.get(f"https://nekobot.xyz/api/imagegen?type=trumptweet&text={msg}")
    stuff = json.loads(response.text)
    msg = f"""
    ```ini
[Trump]
The man the myth the legend
    ```
    """
    await ctx.send(msg,delete_after=config['deletetime'])
    await ctx.send(stuff['message'])
    print(Colours.Magenta+"[Command] <>Trump has tweeted<>"+Colours.White)

@bot.command() 
async def loopstatus(ctx): # b'\xfc' 
    await ctx.message.delete()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Content-Type': 'application/json',
        'Authorization': config["token"],
    }
    request = requests.Session()
    payload = {
        'theme': "darkmode",
        'locale': "en-GB",
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
        'status': "online"
    } 
    while True:
        try:
            request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload)
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Colours.White)
        else:
            break
    statuses = cycle(["online", "invisible"])
    while True:
        setting = {
            'status': next(statuses)
        }

        while True:
            try:
                request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=setting, timeout=10)
            except Exception as e:
                print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Colours.White)
            else:
                break 
            return

@bot.command()
async def ph(ctx, member=None, *, msg):
    if member==None:
        member = ctx.message.author
    else:
        member = ctx.message.mentions[0]
        member = await bot.fetch_user(int(member.id))
    await ctx.message.delete()
    url = member.avatar_url_as(format="png")
    response = requests.get(f"https://nekobot.xyz/api/imagegen?type=phcomment&image={url}&username={member.display_name}&text={msg}")
    stuff = json.loads(response.text)
    msg = f"""
```ini
[ph]
Caught red handed cunt
```
    """

    await ctx.send(msg,delete_after=config['deletetime'])
    await ctx.send(stuff['message'])
    print(Colours.Magenta+"[Command] <>searching the interwebs<>"+Colours.White)



@bot.command()
async def gaypfp(ctx, member=None):
    await ctx.message.delete()
    if member==None:
        member = ctx.message.author
    else:
        member = ctx.message.mentions[0]
        member = await bot.fetch_user(int(member.id))
    async with aiohttp.ClientSession() as trigSession:
        async with trigSession.get(f'https://some-random-api.ml/canvas/gay?avatar={member.avatar_url_as(format="png", size=1024)}') as trigImg:
            imageData = io.BytesIO(await trigImg.read()) 
            
            await trigSession.close()
            
            await ctx.send(file=discord.File(imageData, 'CotraUI.gif'))

@bot.command()
async def trap(ctx, member=None):
    await ctx.message.delete()
    if member==None:
        member = ctx.message.author
    else:
        member = ctx.message.mentions[0]
        member = await bot.fetch_user(int(member.id))
    async with aiohttp.ClientSession() as trigSession:
        async with trigSession.get(f'https://nekobot.xyz/api/image?type=trap?avatar={member.avatar_url_as(format="png", size=1024)}') as trigImg:
            imageData = io.BytesIO(await trigImg.read()) 
            
            await trigSession.close()
            
            await ctx.send(file=discord.File(imageData, 'CotraUI.gif'))

@bot.command()
async def triggered(ctx, member=None):
    await ctx.message.delete()
    if member==None:
        member = ctx.message.author
    else:
        member = ctx.message.mentions[0]
        member = await bot.fetch_user(int(member.id))
    async with aiohttp.ClientSession() as trigSession:
        async with trigSession.get(f'https://some-random-api.ml/canvas/triggered?avatar={member.avatar_url_as(format="png", size=1024)}') as trigImg:
            imageData = io.BytesIO(await trigImg.read()) 
            
            await trigSession.close()
            
            await ctx.send(file=discord.File(imageData, 'CotraUI.gif'))

@bot.command()
async def passed(ctx, member=None):
    await ctx.message.delete()
    if member==None:
        member = ctx.message.author
    else:
        member = ctx.message.mentions[0]
        member = await bot.fetch_user(int(member.id))
    async with aiohttp.ClientSession() as trigSession:
        async with trigSession.get(f'https://some-random-api.ml/canvas/passed?avatar={member.avatar_url_as(format="png", size=1024)}') as trigImg:
            imageData = io.BytesIO(await trigImg.read()) 
            
            await trigSession.close()
            
            await ctx.send(file=discord.File(imageData, 'CotraUI.gif'))

@bot.command()
async def jail(ctx, member=None):
    await ctx.message.delete()
    if member==None:
        member = ctx.message.author
    else:
        member = ctx.message.mentions[0]
        member = await bot.fetch_user(int(member.id))
    async with aiohttp.ClientSession() as trigSession:
        async with trigSession.get(f'https://some-random-api.ml/canvas/jail?avatar={member.avatar_url_as(format="png", size=1024)}') as trigImg:
            imageData = io.BytesIO(await trigImg.read()) 
            
            await trigSession.close()
            
            await ctx.send(file=discord.File(imageData, 'CotraUI.gif'))

@bot.command()
async def wasted(ctx, member=None):
    await ctx.message.delete()
    if member==None:
        member = ctx.message.author
    else:
        member = ctx.message.mentions[0]
        member = await bot.fetch_user(int(member.id))
        
    async with aiohttp.ClientSession() as trigSession:
        async with trigSession.get(f'https://some-random-api.ml/canvas/wasted?avatar={member.avatar_url_as(format="png", size=1024)}') as trigImg:
            imageData = io.BytesIO(await trigImg.read()) 
            
            await trigSession.close()
            
            await ctx.send(file=discord.File(imageData, 'CotraUI.gif'))

@bot.command()
async def lolice(ctx, member=None):
    await ctx.message.delete()
    if member==None:
        member = ctx.message.author
    else:
        member = ctx.message.mentions[0]
        member = await bot.fetch_user(int(member.id))
    async with aiohttp.ClientSession() as trigSession:
        async with trigSession.get(f'https://some-random-api.ml/canvas/lolice?avatar={member.avatar_url_as(format="png", size=1024)}') as trigImg:
            imageData = io.BytesIO(await trigImg.read()) 
            
            await trigSession.close()
            
            await ctx.send(file=discord.File(imageData, 'CotraUI.gif'))

@bot.command()
async def horny(ctx, member=None):
    await ctx.message.delete()
    if member==None:
        member = ctx.message.author
    else:
        member = ctx.message.mentions[0]
        member = await bot.fetch_user(int(member.id))
    async with aiohttp.ClientSession() as trigSession:
        async with trigSession.get(f'https://some-random-api.ml/canvas/horny?avatar={member.avatar_url_as(format="png", size=1024)}') as trigImg:
            imageData = io.BytesIO(await trigImg.read()) 
            
            await trigSession.close()
            
            await ctx.send(file=discord.File(imageData, 'CotraUI.gif'))

@bot.command()
async def pixel(ctx, member=None):
    await ctx.message.delete()
    if member==None:
        member = ctx.message.author
    else:
        member = ctx.message.mentions[0]
        member = await bot.fetch_user(int(member.id))
    async with aiohttp.ClientSession() as trigSession:
        async with trigSession.get(f'https://some-random-api.ml/canvas/pixelate?avatar={member.avatar_url_as(format="png", size=1024)}') as trigImg:
            imageData = io.BytesIO(await trigImg.read()) 
            
            await trigSession.close()
            
            await ctx.send(file=discord.File(imageData, 'CotraUI.gif'))

@bot.command()
async def clyde(ctx,*, msg):
    await ctx.message.delete()
    response = requests.get(f"https://nekobot.xyz/api/imagegen?type=clyde&text={msg}")
    stuff = json.loads(response.text)
    msg = f"""
```ini
[clyde]
Discord error help clyde plz
```
    """

    await ctx.send(msg,delete_after=config['deletetime'])
    await ctx.send(stuff['message'])
    print(Colours.Magenta+"[Command] <>searching the interwebs<>"+Colours.White)

@bot.command()
async def status(ctx,*, msg):
    await ctx.message.delete()

    url = "https://discordapp.com/api/v9/users/@me/settings"

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"
    headers["Authorization"] = config["token"]

    data = {
        "custom_status": {
            "text": f"{msg}"
        }
    }

    requests.patch(url, headers=headers, json=data)


@bot.command()
async def cs(ctx):
    await ctx.message.delete()
    msg = f"""
```ini
[CSGO]
csgo real life uwua
```
    """

    await ctx.send(msg,delete_after=config['deletetime'])
    await ctx.send("https://cdn.discordapp.com/attachments/927312578022092880/928388235590271026/914413812378112040.png")
    print(Colours.Magenta+"[Command] <>UwU<>"+Colours.White)


@bot.command()
async def helloworld(ctx):
    await ctx.message.delete()
    


@bot.command()
async def cum(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/cum")
    res = r.json()
    msg = f"""
```ini
[cum]
Yummy cummy in my tummy uwu
```
    """

    await ctx.send(msg,delete_after=config['deletetime'])
    await ctx.send(res['url'],delete_after=config['deletetime'])
    print(Colours.Magenta+"[Command] <>cum<>"+Colours.White)

@bot.command(pass_context=True)
async def purge(ctx, limit: int):
        await ctx.channel.purge(limit=limit)
        msg = f"""
```css
[PURGE]
You have Purged: {limit} Messages by {ctx.author}
```
    """

        await ctx.send(msg,delete_after=config['deletetime'])

@bot.command()
async def invnick(ctx):
    await ctx.message.delete()
    try:
            name = ' ឵឵ ឵឵ ឵឵ ឵឵‎'
            await ctx.author.edit(nick=name)

    except Exception:
            return

@bot.command()
async def rick(ctx, member=None):
    await ctx.message.delete()
    if member == None:
        member = ctx.author
    else:
        member = ctx.message.mentions[0]
    msg = f"""
```ini
[rick]
YOU GOT RICK ROLLED {member.display_name}
```
    """

    await ctx.send(msg,delete_after=config['deletetime'])
    await ctx.send("https://cdn.discordapp.com/attachments/907863077712703508/915238064811544686/rickroll-rick.gif")
    print(Colours.Magenta+"[Command] <>Rickroll posted<>"+Colours.White)


@bot.command()
async def clearconsole(ctx):
    await ctx.message.delete()
    Clear()
    new_splash()

@bot.command()
async def aboutme(ctx, *, text):
    await ctx.message.delete()

    url = "https://discord.com/api/v9/users/@me"

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"
    headers["Authorization"] = config["token"]

    data = {
        "bio": text
    }

    requests.patch(url, headers=headers, json=data)

@bot.command()
async def pat(ctx, member=None):
    await ctx.message.delete()
    if member == None:
        member = ctx.author
    else:
        member = ctx.message.mentions[0]
    r = requests.get("https://nekos.life/api/v2/img/pat")
    res = r.json()
    msg = f"""
```ini
[pat]
pats :3
```
    """

    await ctx.send(msg,delete_after=config['deletetime'])
    await ctx.send(res['url'],delete_after=config['deletetime'])
    print(Colours.Magenta+"[Command] <>Pat<>"+Colours.White)

@bot.command()
async def buy(ctx):
    await ctx.message.delete()
    msg = f"""
    ```ini
    ╔══════════════════════════════════════════╗
    ║               [BUY INFO]                 ║
    ║══════════════════════════════════════════║
    ║ Website: https://www.cotra.xyz           ║              
    ║ Discord: https://discord.gg/cotraui      ║  
    ║ Owner: [cotra#0001 | 584879487850643456] ║   
    ║                                          ║
    ║ Create a ticket to buy in [#buy]         ║ 
    ╚══════════════════════════════════════════╝
    ```
    """

    await ctx.send(msg,delete_after=config['deletetime'])
    print(Colours.Magenta+"[Command] <>BUY<>"+Colours.WHITE)

@bot.command()
async def lewdneko(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/nsfw_neko_gif")
    res = r.json()
    msg = f"""
```ini
[lewdneko]
cum cum :3
```
    """

    await ctx.send(msg,delete_after=config['deletetime'])
    await ctx.send(res['url'],delete_after=config['deletetime'])
    print(Colours.Magenta+"[Command] <>lewdneko<>"+Colours.White)



# @bot.command()
# async def hideinvite(ctx, url, *, message: str='Hi'):
#         await ctx.message.delete()
#         await ctx.send(f'‎{message}||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||‎‎||‎||‎‎||‎‎||‎‎||‎‎||{url}')

# @bot.command()
# async def hidelink(ctx, url, spoofed_url):
#     await ctx.message.delete()
#     await ctx.send(f'‎<{spoofed_url}>||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||‎‎||‎||‎‎||‎‎||‎‎||‎‎||{url}')

@bot.command()
async def kiss(ctx, member=None):
    await ctx.message.delete()
    if member == None:
        member = ctx.author
    else:
        member = ctx.message.mentions[0]
    r = requests.get("https://nekos.life/api/v2/img/kiss")
    res = r.json()
    msg = f"""
```ini
[kiss]
kisses {member.display_name}
```
    """

    await ctx.send(msg,delete_after=config['deletetime'])
    await ctx.send(res['url'],delete_after=config['deletetime'])
    print(Colours.Magenta+"[Command] <>kiss<>"+Colours.White)

@bot.command()
async def hug(ctx, member=None):
    await ctx.message.delete()
    if member == None:
        member = ctx.author
    else:
        member = ctx.message.mentions[0]
    r = requests.get("https://nekos.life/api/v2/img/hug")
    res = r.json()
    msg = f"""
```ini
[hugs]
hugs {member.display_name}
```
    """

    await ctx.send(msg,delete_after=config['deletetime'])
    await ctx.send(res['url'],delete_after=config['deletetime'])
    print(Colours.Magenta+"[Command] <>hug<>"+Colours.White)


@bot.command()
async def spank(ctx, member=None):
    await ctx.message.delete()
    if member == None:
        member = ctx.author
    else:
        member = ctx.message.mentions[0]
    r = requests.get("https://nekos.life/api/v2/img/spank")
    res = r.json()
    msg = f"""
```ini
[spank]
spanks {member.display_name}
```
    """

    await ctx.send(msg,delete_after=config['deletetime'])
    await ctx.send(res['url'],delete_after=config['deletetime'])
    print(Colours.Magenta+"[Command] <>Spank<>"+Colours.White)



@bot.command()
async def feed(ctx, member=None):
    await ctx.message.delete()
    if member == None:
        member = ctx.author
    else:
        member = ctx.message.mentions[0]
    r = requests.get("https://nekos.life/api/v2/img/feed")
    res = r.json()
    msg = f"""
```ini
[feed]
feeds {member.display_name}
```
    """

    await ctx.send(msg,delete_after=config['deletetime'])
    await ctx.send(res['url'],delete_after=config['deletetime'])
    print(Colours.Magenta+"[Command] <>feed<>"+Colours.White)

@bot.command()
async def slap(ctx, member=None):
    await ctx.message.delete()
    if member == None:
        member = ctx.author
    else:
        member = ctx.message.mentions[0]
    r = requests.get("https://nekos.life/api/v2/img/slap")
    res = r.json()
    msg = f"""
```ini
[slap]
slaps {member.display_name}
```
    """

    await ctx.send(msg,delete_after=config['deletetime'])
    await ctx.send(res['url'],delete_after=config['deletetime'])
    print(Colours.Magenta+"[Command] <>slap<>"+Colours.White)


@bot.command()
async def poke(ctx, member=None):
    await ctx.message.delete()
    if member == None:
        member = ctx.author
    else:
        member = ctx.message.mentions[0]
    r = requests.get("https://nekos.life/api/v2/img/poke")
    res = r.json()
    msg = f"""
```ini
[poke]
pokes {member.display_name}
```
    """

    await ctx.send(msg,delete_after=config['deletetime'])
    await ctx.send(res['url'],delete_after=config['deletetime'])
    print(Colours.Magenta+"[Command] <>poke<>"+Colours.White)

@bot.command()
async def tickle(ctx, member=None):
    await ctx.message.delete()
    if member == None:
        member = ctx.author
    else:
        member = ctx.message.mentions[0]
    r = requests.get("https://nekos.life/api/v2/img/tickle")
    res = r.json()
    msg = f"""
```ini
[tickle]
tickle's {member.display_name}
```
    """

    await ctx.send(msg,delete_after=config['deletetime'])
    await ctx.send(res['url'],delete_after=config['deletetime'])
    print(Colours.Magenta+"[Command] <>tickle<>"+Colours.White)

@bot.command()
async def gasm(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/gasm")
    res = r.json()
    msg = f"""
```ini
[gasm]
gasm uwu
```
    """

    await ctx.send(msg,delete_after=config['deletetime'])
    await ctx.send(res['url'],delete_after=config['deletetime'])
    print(Colours.Magenta+"[Command] <>gasm<>"+Colours.White)

@bot.command()
async def cuddle(ctx, member=None):
    await ctx.message.delete()
    if member == None:
        member = ctx.author
    else:
        member = ctx.message.mentions[0]
    r = requests.get("https://nekos.life/api/v2/img/cuddle")
    res = r.json()
    msg = f"""
```ini
[cuddle]
cuddles {member.display_name}
```
    """

    await ctx.send(msg,delete_after=config['deletetime'])
    await ctx.send(res['url'],delete_after=config['deletetime'])
    print(Colours.Magenta+"[Command] <>cuddle<>"+Colours.White)

@bot.command()
async def baka(ctx, member=None):
    await ctx.message.delete()
    if member == None:
        member = ctx.author
    else:
        member = ctx.message.mentions[0]
    r = requests.get("https://nekos.life/api/v2/img/baka")
    res = r.json()
    msg = f"""
```ini
[baka]
baka {member.display_name}
```
    """

    await ctx.send(msg,delete_after=config['deletetime'])
    await ctx.send(res['url'],delete_after=config['deletetime'])
    print(Colours.Magenta+"[Command] <>baka<>"+Colours.White)

@bot.command()
async def feet(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/feet")
    res = r.json()
    msg = f"""
```ini
[feet]
feetsy uwu
```
    """

    await ctx.send(msg,delete_after=config['deletetime'])
    await ctx.send(res['url'],delete_after=config['deletetime'])
    print(Colours.Magenta+"[Command] <>feet<>"+Colours.White)

@bot.command()
async def wallpaper(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/wallpaper")
    res = r.json()
    msg = f"""
    ```ini
[Wallpaper]
Enjoy some lovely wallpapers uwu
```
    """

    await ctx.send(msg,delete_after=config['deletetime'])
    await ctx.send(res['url'],delete_after=config['deletetime'])
    print(Colours.Magenta+"[Command] <>Wallpaper<>"+Colours.White)


@bot.command()
async def dnd(ctx):
    await ctx.message.delete()

    url = "https://discordapp.com/api/v9/users/@me/settings"

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"
    headers["Authorization"] = config["token"]

    data = {
        "status": "dnd"
    }

    requests.patch(url, headers=headers, json=data)

@bot.command()
async def online(ctx):
    await ctx.message.delete()

    url = "https://discordapp.com/api/v9/users/@me/settings"

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"
    headers["Authorization"] = config["token"]

    data = {
        "status": "online"
    }

    requests.patch(url, headers=headers, json=data)

@bot.command()
async def idle(ctx):
    await ctx.message.delete()

    url = "https://discordapp.com/api/v9/users/@me/settings"

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"
    headers["Authorization"] = config["token"]

    data = {
        "status": "idle"
    }

    requests.patch(url, headers=headers, json=data)

@bot.command()
async def invisible(ctx):
    await ctx.message.delete()

    url = "https://discordapp.com/api/v9/users/@me/settings"

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"
    headers["Authorization"] = config["token"]

    data = {
        "status": "invisible"
    }

    requests.patch(url, headers=headers, json=data)

@bot.command()
async def lightmode(ctx):
    await ctx.message.delete()

    url = "https://discordapp.com/api/v9/users/@me/settings"

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"
    headers["Authorization"] = config["token"]

    data = {
        "theme": "light"
    }

    requests.patch(url, headers=headers, json=data)

@bot.command()
async def test345(ctx):
    await ctx.send("fuc", delete_after=config['deletetime'])



@bot.command()
async def darkmode(ctx):
    await ctx.message.delete()

    url = "https://discordapp.com/api/v9/users/@me/settings"

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"
    headers["Authorization"] = config["token"]

    data = {
        "theme": "dark"
    }

    requests.patch(url, headers=headers, json=data)

@bot.command()
async def uwu(ctx):
    await ctx.message.delete()
    print("uwu")

@bot.command()
async def easteregg(ctx):
    await ctx.message.delete()
    print("you found the easter egg")

@bot.command()
async def shrek(ctx): ## Thanks yeet pizza :) 
    await ctx.message.delete()
    msg = f"""
```ini
[shrek]
what are ye doin in ma swamp!!
```
    """

    await ctx.send(msg,delete_after=config['deletetime'])
    await ctx.send(value,delete_after=config['deletetime'])
value=("""⢀⡴⠑⡄⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠸⡇⠀⠿⡀⠀⠀⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠑⢄⣠⠾⠁⣀⣄⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⣿⣿⠭⢤⣴⣦⣤⣹⠀⠀⠀⢀⢴⣶⣆ 
⠀⠀⢀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿⢂⠔⢚⡿⢿⣿⣦⣴⣾⠁⠸⣼⡿ 
⠀⢀⡞⠁⠙⠻⠿⠟⠉⠀⠛⢹⣿⣿⣿⣿⣿⣌⢤⣼⣿⣾⣿⡟⠉⠀⠀⠀⠀⠀ 
⠀⣾⣷⣶⠇⠀⠀⣤⣄⣀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
⠀⠉⠈⠉⠀⠀⢦⡈⢻⣿⣿⣿⣶⣶⣶⣶⣤⣽⡹⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠉⠲⣽⡻⢿⣿⣿⣿⣿⣿⣿⣷⣜⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣶⣮⣭⣽⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⠿⠿⠿⠛⠉""")

@bot.command()
async def lenny(ctx):
    await ctx.message.delete()
    await ctx.send("( ͡° ͜ʖ ͡°)")

@bot.command()
async def bold(ctx, *, msg):
    await ctx.message.delete()
    await ctx.send(f"**{msg}**")

@bot.command()
async def italic(ctx, *, msg):
    await ctx.message.delete()
    await ctx.send(f"*{msg}*")

@bot.command()
async def bolditalic(ctx, *, msg):
    await ctx.message.delete()
    await ctx.send(f"***{msg}***")

@bot.command()
async def underline(ctx, *, msg):
    await ctx.message.delete()
    await ctx.send(f"__{msg}__")

@bot.command()
async def boldunderline(ctx, *, msg):
    await ctx.message.delete()
    await ctx.send(f"__**{msg}**__")

@bot.command()
async def spoiler(ctx, *, msg):
    await ctx.message.delete()
    await ctx.send(f"||**{msg}**||")

@bot.command()
async def emojify(ctx, *, msg):
    dict = {
        "a": ":regional_indicator_a:",
        "b": ":regional_indicator_b:",
        "c": ":regional_indicator_c:",
        "d": ":regional_indicator_d:",
        "e": ":regional_indicator_e:",
        "f": ":regional_indicator_f:",
        "g": ":regional_indicator_g:",
        "h": ":regional_indicator_h:",
        "i": ":regional_indicator_i:",
        "j": ":regional_indicator_j:",
        "k": ":regional_indicator_k:",
        "l": ":regional_indicator_l:",
        "m": ":regional_indicator_m:",
        "n": ":regional_indicator_n:",
        "o": ":regional_indicator_o:",
        "p": ":regional_indicator_p:",
        "q": ":regional_indicator_q:",
        "r": ":regional_indicator_r:",
        "s": ":regional_indicator_s:",
        "t": ":regional_indicator_t:",
        "u": ":regional_indicator_u:",
        "v": ":regional_indicator_v:",
        "w": ":regional_indicator_w:",
        "x": ":regional_indicator_x:",
        "y": ":regional_indicator_y:",
        "z": ":regional_indicator_z:",
        " ": "    "
    }
    f = ""
    await ctx.message.delete()
    for let in msg:
        for letter in dict:
            if let == letter:
                f += dict.get(letter)
    
    await ctx.send(f)

@bot.command(pass_context=True)
async def nick(ctx,member: discord.Member, *, nick):
    await ctx.message.delete()
    if member == None:
        member = ctx.author
    else:
        member = ctx.message.mentions[0]
        await member.edit(nick=nick)
    msg = f"""
```ini
[Nick]
Nickname changed successfully for {member.display_name}
```
    """

    await ctx.send(msg,delete_after=config['deletetime'])

@bot.command()
async def spamchannel(ctx, ammount: int=None, *, name=None):
    await ctx.message.delete()
    if name == None:
        return await ctx.send("Specify a name")
    if ammount == None:
        return await ctx.send("Specify a ammount")
    f = 0
    while f < ammount:
        await ctx.guild.create_text_channel(name)
        f += 1

@bot.command(name="8ball")
async def _8ball(ctx, *, question=None):
    if question==None:
        return await ctx.send("You didnt say a question")
    await ctx.message.delete()
    answers = ["It is certain.", "It is decidedly so.", "Without a doubt", "Yes definitely.", "You may rely on it.","As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy try again.","Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.","Don\'t count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]    
    msg = f"""
```ini
[8BALL]
Question: {question} 

Answer: {random.choice(answers)}
```
    """

    await ctx.send(msg,delete_after=config['deletetime'])

@bot.command()
async def simp(ctx, member=None):
    await ctx.message.delete()
    if member==None:
        member=ctx.author
    else:
        member = ctx.message.mentions[0]
        member = await bot.fetch_user(int(member.id))
    msg = f"""
```ini
[cute]
The User {member.display_name} is {random.randint(0,100)}% a simp
```
    """

    await ctx.send(msg,delete_after=config['deletetime'])


@bot.command()
async def cute(ctx, member=None):
    await ctx.message.delete()
    if member==None:
        member=ctx.author
    else:
        member = ctx.message.mentions[0]
        member = await bot.fetch_user(int(member.id))
    msg = f"""
```ini
[cute]
The User {member.display_name} is {random.randint(0,100)}% cute
```
    """

    await ctx.send(msg,delete_after=config['deletetime'])


@tasks.loop(seconds=15)
async def clock(text):
    hour = datetime.datetime.now().strftime("%H")
    hour = int(hour)
    minute = datetime.datetime.now().strftime("%M")
    minute = int(minute)
    if hour >= 12:
        time = f"{hour-12}:{minute}PM"
    else:
        time = f"{hour}:{minute}AM"
    data = {"custom_status": {"text": f"{time} {text}", "emoji_name": "🕰️"}}
    url = "https://discordapp.com/api/v9/users/@me/settings"

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"
    headers["Authorization"] = config["token"]
    requests.patch(url, headers=headers, json=data)

@bot.command()
async def clockon(ctx, *, text: str=None):
    await ctx.message.delete()
    if not text==None:
        clock.start(text)
    else:
        clock.start("")

@bot.command()
async def clockoff(ctx):
    await ctx.message.delete()
    clock.stop()
    url = "https://discordapp.com/api/v9/users/@me/settings"

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"
    headers["Authorization"] = config["token"]

    data = {
        "custom_status": NULL
    }

    requests.patch(url, headers=headers, json=data)



# bot run #
    
# bot.run(config["token"], bot=False)
def Init():
    with open('config.json', encoding="utf-8") as f:
        config = json.load(f)
    token = config.get('token')
    try:
        bot.run(token, bot=False, reconnect=True)
    except discord.errors.LoginFailure:
        input(f"{Fore.RED}[SYSTEM] TOKEN IS INVALID CHECK CONFIG"+Colours.White)
        sys.exit
        python = sys.executable
        os.execl(python, python, * sys.argv)
Init()