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
    await ctx.send('====================================\nHi'+ ctx.message.author.mention + '\n\nI am a Modron.\nMy sole purpose is to roll dice for you.\nPlease find a list of my commands below.\n_Commands_\n/r - Rolls a d20.\n/a - Rolls 2d20 for adv./disadv.\n/d X*d*Y* - for damage rolls.\n     where*X* = no.of dice and *Y* = dice sides\n*/b to add a break for clarity.\n*/flip* - Flip the virtual table.\n====================================')    #await ctx.message.delete() 

@bot.command(pass_context=True) 
async def b(ctx):
    await ctx.send("====================================\n\n*" ctx.message.author.mention + " wants a break for clarity.* **Organisation above all, beep boop.**\n\n====================================")
    await ctx.message.delete()
	
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
    await ctx.send('====================================\nRolling two d20s for ' + ctx.message.author.mention + "  **Result:** " + str(random.randint(1, 20)) + ' and '+ str(random.randint(1, 20)) + "\n====================================")
    #await ctx.message.delete()

@bot.command(pass_context=True) 
async def adv(ctx):
    await ctx.send('====================================\nRolling two d20s for ' + ctx.message.author.mention + "  **Result:** " + str(random.randint(1, 20)) + ' and '+ str(random.randint(1, 20)) + "\n====================================")
    #await ctx.message.delete()

@bot.command(pass_context=True) 
async def flip(ctx):
    await ctx.send('====================================\n' + ctx.message.author.mention + ' asked me to flip the table as they are mad. I passed my Strength check, so here goes... \n\n(╯°□°)╯︵ ┻━┻\n\n====================================')
    await ctx.message.delete()

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

        if int(numDice) > 100:
            await ctx.send("I cant roll that many dice %s. I am only a Monodrone.:robot:" % ctx.message.author.name)
            return

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
        return
    #await ctx.message.delete()
        
bot.run(Bot_Token)
