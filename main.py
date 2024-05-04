# Quick Search

import os
import discord
import urllib.parse
import discord.activity

from discord.ext import commands
from discord.ui import Button, View
from discord import Interaction

from web import keep_alive

# Setting
keep_alive()

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
TOKEN = os.environ['TOKEN']


@bot.event
async def on_ready():
    await bot.tree.sync()
    await bot.change_presence(activity=discord.activity.Game("Search"))
    print(f'{bot.user.name} is Online!')


# Command

@bot.tree.command(name='naver', description='네이버에서 검색')
async def naver(interaction: Interaction, query: str):
    query1 = urllib.parse.quote(query)
    url = f'https://search.naver.com/search.naver?query={query1}'

    btn1 = Button(label="검색 결과", url=url)

    view = View()
    view.add_item(btn1)

    await interaction.response.send_message(f"'{query}'의 검색결과", view=view)


@bot.tree.command(name='google', description='Search at google')
async def google(interaction: Interaction, query: str):
    query1 = urllib.parse.quote(query)
    url = f'https://www.google.com/search?q={query1}'

    btn1 = Button(label="Result", url=url)

    view = View()
    view.add_item(btn1)

    await interaction.response.send_message(f"Result for '{query}'", view=view)


@bot.tree.command(name='gmap', description='Search at google map')
async def gmap(interaction: Interaction, query: str):
    query1 = urllib.parse.quote(query)
    url = f'https://www.google.co.kr/maps/search/{query1}'

    btn1 = Button(label='Result', url=url)

    view = View()
    view.add_item(btn1)

    await interaction.response.send_message(f"Result for '{query}'", view=view)


@bot.tree.command(name='nmap', description='네이버 지도에서 검색')
async def nmap(interaction: Interaction, query: str):
    query1 = urllib.parse.quote(query)
    url = f'https://map.naver.com/p/search/{query1}'

    btn1 = Button(label="검색 결과", url=url)

    view = View()
    view.add_item(btn1)

    await interaction.response.send_message(f"'{query}'의 검색결과", view=view)

bot.run(TOKEN)
