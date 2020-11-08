import discord
import threading
import time
import datetime
import asyncio
from UsersReminders import UsersReminders
#from discord.ext import commands

test = []
client = discord.Client()
commandSymbol = '!'
default_channel = 774675797033091075
index = 0


async def time_check():
    await client.wait_until_ready()
    #print("working")
    while True:
        await asyncio.sleep(40)
        #print("working")
        now = datetime.datetime.now()
        for x in test:
            for i in x.dates[datetime.datetime.today().weekday()]:
                if now.hour == i.hour and now.minute == i.minute:
                    #print(now.hour == i.hour)
                    await client.get_channel(default_channel).send("{} time for class".format(x.messageauthor.mention))

def contains(test, messageauthor):
    for x in test:    
        if x.messageauthor == messageauthor:
            return True
    return False

def day(date): #!add monday 14
    day = date[date.find(' ') + 1: date.find(' ', 5)]
    day = day.upper()

    if day == "MONDAY":
        return 0
    if day == "TUESDAY":
        return 1
    if day == "WEDNESDAY":
        return 2
    if day == "THURSDAY":
        return 3
    if day == "FRIDAY":
        return 4
    if day == "SATURDAY":
        return 5
    if day == "SUNDAY":
        return 6
    
    return -1

def hour(date):
    print(date[date.find(' ', 5) + 1 : ])
    hour = date[date.find(' ', 5) + 1 : date.find(':')]
    hour = int(hour)
    if hour > 23:
        hour = 23
    
    if hour < 0:
        hour = 0

    return hour

def minute(date):
    minute = date[date.find(':') + 1 :]
    minute = int(minute)

    if minute > 59:
        minute = 59
    
    if minute < 0:
        minute = 0

    return minute
    


# thread = threading.Thread(target = check_time, args = ())
# thread.start()

@client.event
async def on_ready():
    print('Bot is ready.')
    

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(commandSymbol + "channelid"):
        default_channel = int(message.content[11: len(message.content)]) #client.get_channel()
        print(message.content[11: len(message.content)])
        await message.channel.send('Channel set to: ' + str(default_channel))
    
    if message.content.startswith(commandSymbol + 'ping'):
        await message.channel.send('Pinging {}'.format(message.author.mention))

    if message.content.startswith(commandSymbol + 'add'):
        if (day(message.content) == -1):
            await message.channel.send("Invalid day, please try again\n $add day hour(24hr):minute")
        elif not contains(test, message.author):
            
            test.append(UsersReminders(message.author))
            test[len(test) - 1].add(day(message.content), hour(message.content), minute(message.content))

            await message.channel.send("{} reminder added".format(message.author.mention))
        elif contains(test, message.author):

            test[len(test) - 1].add(day(message.content), hour(message.content), minute(message.content))
            await message.channel.send("{} reminder added".format(message.author.mention))
        



    
client.loop.create_task(time_check())
client.run('Nzc0Njc1NjcwOTgyODUyNjE4.X6bO8A.7kUnwBU7Z3QPz9KfJeSLVNDjoE0')