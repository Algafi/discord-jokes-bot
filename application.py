import discord
import asyncio
import platform
import random
import mysql.connector
from discord.ext import commands


### OBTENCIO VARIABLES NECESSARIES DE LA BD ###

###------------------###


bot = commands.Bot(command_prefix='!', description='CHISTES!', pm_help=True)

@bot.event
async def on_ready():
	print('Logged in as '+bot.user.name+' (ID:'+bot.user.id+') | Connected to '+str(len(bot.servers))+' servers | Connected to '+str(len(set(bot.get_all_members())))+' users')
	print('--------')
	#await bot.say('¡Mrglglrglglglgl!')


@bot.command()
#Explica un acudit d'un tema si s'especifica
async def chiste(tema=None):

	db = mysql.connector.connect(host="XXXXXX.eu-west-2.rds.amazonaws.com",user="XXXXXX",password="XXXXXX",database="murloc")
	cursor = db.cursor(dictionary=True)
	cursor.execute("SELECT * FROM murloc.jokes JOIN (SELECT FLOOR(RAND()*(SELECT COUNT(ID) FROM murloc.jokes)+1) AS ID) AS Result USING (ID)")
	jokeRow = cursor.fetchone()

	await bot.say(jokeRow['Text'])

	cursor.close()
	db.close()

bot.run('yourToken')