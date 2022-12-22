#!/usr/bin/python3.8
################### import #####################
import random
import os
import json
import base64
import http
import time
import os
import string
import sys
import colorama
import discord_webhook
import discord.ext
import discord
import requests
from discord.ext import commands
import time
import requests

##################### from ####################
from concurrent.futures import thread
from pathlib import Path

from discord_webhook import *
from sys import *
from colorama import *
from requests import *

############### Settings ########################


with open('config.json') as f:
    config = json.load(f)

token = config.get('token_bot')

colorama.init(autoreset=True)
platform = sys.platform

if platform == "linux" or platform == "linux2":

    osuserLW = "clear"
else:
    osuserLW = "cls"


os.system(osuserLW)
logofront = (f"""
    {Fore.RED}             ┌─┐┌┬┐┬ ┬┌─┐{Fore.MAGENTA}   ┌┬┐┌─┐┌─┐┬  
    {Fore.RED}             │ │ │ ├─┤│ │{Fore.MAGENTA}    │ │ ││ ││  
    {Fore.RED}             └─┘ ┴ ┴ ┴└─┘{Fore.MAGENTA}    ┴ └─┘└─┘┴─┘
    {Fore.RED}
    

                   #made by brute x ezekiel
""")
choice = f"""

    {Fore.RED}[{Fore.MAGENTA}1{Fore.RED}] Discord Bot DMALL (need to be verified or will use 3sec timeout){Fore.RED}
    {Fore.RED}[{Fore.MAGENTA}2{Fore.RED}] Webhook Deleter{Fore.RED}
    {Fore.RED}[{Fore.MAGENTA}3{Fore.RED}] Webhook Spammer (4 webhooks (random pfp's & random names)){Fore.RED}
    {Fore.RED}[{Fore.BLUE}99{Fore.RED}] exit{Fore.RED}
"""
def menu_main():
    print(logofront)
    print(choice)
    choice_func = input(f"{Fore.RED}[{Fore.MAGENTA}++{Fore.RED}] {Fore.MAGENTA} >>")

    if choice_func == "1":
        bot_verified = input(f"{Fore.RED} Bot Verified ?? (y/n) >>")
        discord_dmall_bot(bot_verified) # call func
    elif choice_func == "2":
        user_wb = input(f"{Fore.RED}Webhook >>")
        user_wb_fucker(user_wb)
    elif choice_func == "3":
        webhook_rota = []
        for x in range(4):
            wb = input(f"{Fore.RED}Webhook {x}>>")
            webhook_rota.append(wb)
        message = input(f"{Fore.RED}Message >>")
        while True:
            for i in range(4):
                webhook = DiscordWebhook(url=webhook_rota[i], content=message)
                response = webhook.execute()


def discord_bot_verif(bot_verified):
    if bot_verified == 'y':
        ratelimit_bot = False
    else:
        ratelimit_bot = True
    return ratelimit_bot



def discord_dmall_bot(bot_verified):
        intents = discord.Intents.all()
        client = commands.Bot(command_prefix='!', intents=intents)
        @client.event
        async def on_ready():
            print("!dmall <message>")
            await client.change_presence(
            status=discord.Status.do_not_disturb,
            activity=discord.Game(name='Using otho x)'))



        @client.command()
        async def dmall(ctx, arg):
            await ctx.send("**DMALL Started !**")
            member_guild = ctx.guild.members
            for member in member_guild:
                try:
                    await member.send(arg)
                    if discord_bot_verif(bot_verified) == True:
                        pass
                    else:
                        time.sleep(3) #le timeout pour eviter le ban (0)
                except:
                    pass

        client.run(token)
        

def user_wb_fucker(user_wb):
    for i in range(15):
        webhook = DiscordWebhook(url=user_wb, content="@everyone You GOT Fucked By Otho byebye discord.gg/pension")
        response = webhook.execute()
    requests.delete(user_wb)
    print(f"{Fore.RED}Webhook Spammed & Deleted !")
    time.sleep(4)
    menu_main()


        
menu_main()