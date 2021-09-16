import discord
import os
import random
from discord.ext import commands
from discord.ext.commands import Bot


bot = Bot(command_prefix='/')
Bot_Token = os.environ['TOKEN']



@bot.event
async def on_ready():
	print(f'*** Established telepathic link to Mechanus as {bot.user} ***')

@bot.command(pass_context=True) 
async def info(ctx):
    await ctx.send('====================================\nHi'+ ctx.message.author.mention + '\n\nI am a Modron.\nMy sole purpose is to roll dice for you.\nPlease find a list of my commands below.\n_Commands_\n/r - Rolls a d20.\n/a - Rolls 2d20 for adv./disadv.\n/d X*d*Y* - for damage rolls.\n     where*X* = no.of dice and *Y* = dice sides\n*/b* to add a break for clarity.\n*/flip* - Flip the virtual table.\n====================================')    #await ctx.message.delete() 

@bot.command(pass_context=True) 
async def b(ctx):
    await ctx.send("====================================\n\n*" + ctx.message.author.mention + " wants a break for clarity.*\n\n====================================")
    #await ctx.message.delete()
	
@bot.command(pass_context=True) 
async def r(ctx):
    await ctx.send('====================================\nRolling a d20 for ' + ctx.message.author.mention + "  **Result:** " + str(random.randint(1, 20))+ "\n====================================")
    #await ctx.message.delete()

@bot.command(pass_context=True) 
async def roll(ctx):
    await ctx.send('====================================\nRolling a d20 for ' + ctx.message.author.mention + "  **Result:** " + str(random.randint(1, 20))+ "\n====================================")
    #await ctx.message.delete()      

@bot.command(pass_context=True) 
async def a(ctx):
    
    result_list = [random.randint(1,20) for _ in range(2)]
    result_list.sort()
    await ctx.send('====================================\nRolling two d20s for ' + ctx.message.author.mention + "  **Results:** " + str(result_list[0]) + ' and '+ str(result_list[1]) + "\n====================================")
    #await ctx.message.delete()

@bot.command(pass_context=True) 
async def flip(ctx):
    await ctx.send('====================================\n' + ctx.message.author.mention + ' asked me to flip the table as they are mad. I passed my Strength check, so here goes... \n\n(╯°□°)╯︵ ┻━┻\n\n====================================')
    #await ctx.message.delete()

@bot.command(pass_context=True)
async def d(ctx, roll : str):
    """Rolls a dice using #d# format.
    e.g .r 3d6"""
    
    resultTotal = 0
    resultString = ''
    try:
        try: 
            numDice = roll.split('d')[0]
            diceVal = roll.split('d')[1]
        
         except Exception as e:
            print(e)
            await ctx.send("BZZT. ERROR. Format has to be in #d# %s." % ctx.message.author.name)
            return

        if int(numDice) > 50:
            await ctx.send("I cant roll that many dice %s. I am only a Monodrone." % ctx.message.author.name)
            return

        if int(diceVal) > 100:
            await ctx.send("Sorry %s, a d100 is the largest dice type the Primus gave me." % ctx.message.author.name)
            return

        if str(numDice) == '':
            numDice= int(1)
          
        await ctx.send("====================================\nRolling %s d%s for %s" % (numDice, diceVal, ctx.message.author.mention))
        rolls, limit = map(int, roll.split('d'))

        for r in range(rolls):
            number = random.randint(1, limit)
            resultTotal = resultTotal + number
            
            if resultString == '':
                resultString += str(number)
            else:
                resultString += ', ' + str(number)
        
        if numDice == '1':
            await ctx.send(ctx.message.author.mention + " **Result:** " + resultString + "\n====================================")
        
        else:
            await ctx.send(ctx.message.author.mention + " **Result:** " + resultString + "\n**Total:** " + str(resultTotal)+ "\n====================================")

    except Exception as e:
        print(e)
        await ctx.send("ERROR. Format has to be in *x*d*y*, " + ctx.message.author.mention)
        return
    #await ctx.message.delete()
        
bot.run(Bot_Token)
