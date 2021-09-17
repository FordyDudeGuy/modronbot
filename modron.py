# Import requirements.
import discord
import os
import random
from discord.ext import commands
from discord.ext.commands import Bot

#Initialise bot prefix and get token from secret value.
bot = Bot(command_prefix='/')
Bot_Token = os.environ['TOKEN']


# Load Success Message
@bot.event
async def on_ready():
	print(f'*** {bot.user} online. ***')

# Info command. 
@bot.command(pass_context=True, aliases=['i', 'I'])
async def info(ctx):
    await ctx.send('====================================\nHi there'+ ctx.message.author.mention +'!'+ "\nI am a Modron.\nMy sole purpose is to roll dice for you.\nPlease find a list of my commands below.\n\n_Commands_\n/d*x* where is 2, 4, 6 , 8, 10, 12 or 20 to roll a die with that many sides.\n/r *x*d*y* where *x* = no. of dice and *y* = dice sides\nIf you miss out *x*, I'll assume you just want the one. if you leave out *x*d*y*, I'll just  assume you just want a d20.\n/adv (or just /a) - Rolls 2d20 for adv./disadv sorted in asc. order.\n/flip (or just /f) - Flip the virtual table when the dice betray you.\n====================================")    

# Roll a d4
@bot.command(pass_context=True, aliases=['D4']) 
async def d4(ctx):
    await ctx.send('====================================\nRolling a d4 for ' + ctx.message.author.mention + "  **Result:** " + str(random.randint(1, 4))+ "\n====================================")

# Roll a d6
@bot.command(pass_context=True, aliases=['D6']) 
async def d6(ctx):
    await ctx.send('====================================\nRolling a d6 for ' + ctx.message.author.mention + "  **Result:** " + str(random.randint(1, 6))+ "\n====================================")

# Roll a d8
@bot.command(pass_context=True, aliases=['D8']) 
async def d8(ctx):
    await ctx.send('====================================\nRolling a d8 for ' + ctx.message.author.mention + "  **Result:** " + str(random.randint(1, 8))+ "\n====================================")

# Roll a d10
@bot.command(pass_context=True, aliases=['D10']) 
async def d10(ctx):
    await ctx.send('====================================\nRolling a d10 for ' + ctx.message.author.mention + "  **Result:** " + str(random.randint(1, 10))+ "\n====================================")

# Roll a d12
@bot.command(pass_context=True, aliases=['D12']) 
async def d12(ctx):
    await ctx.send('====================================\nRolling a d12 for ' + ctx.message.author.mention + "  **Result:** " + str(random.randint(1, 12))+ "\n====================================") 

# Roll a d20
@bot.command(pass_context=True, aliases=['D20']) 
async def d20(ctx):
    await ctx.send('====================================\nRolling a d20 for ' + ctx.message.author.mention + "  **Result:** " + str(random.randint(1, 20))+ "\n====================================")
    
# Roll 2d20s and sort them from lowest to highest.
@bot.command(pass_context=True, aliases=['a','A']) 
async def adv(ctx):
    result_list = [random.randint(1,20) for _ in range(2)]
    result_list.sort()
    await ctx.send('====================================\nRolling two d20s for ' + ctx.message.author.mention + "  **Results:** " + str(result_list[0]) + ' and '+ str(result_list[1]) + "\n====================================")

#Flip the table
@bot.command(pass_context=True, aliases=['f','F'])
@commands.cooldown(rate=1, per=20) 
async def flip(ctx):
    await ctx.send('====================================\n %s asked me to flip the table as they are mad. I passed my Strength check, so here goes... \n\n(╯°□°)╯︵ ┻━┻\n\n===================================='% ctx.message.author.name)

#If users try to use the flip command too soon after last time using it...
@flip.error
async def command_name_error(ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send("Sorry %s, I'm still unflipping the table from last time you asked me to flip it. Please try again in a moment." % ctx.message.author.name )
 
#General all-purpose Roll function 
@bot.command(pass_context=True, aliases=['roll', 'ROLL'])
async def r(ctx, roll : str = None):
    #/r command takes a string argument that will be used later.
    
    #initialise default values for result.
    resultTotal = 0
    resultString = ''
    
    #if no argument is given then just roll a d20.
    if roll is None:
      await ctx.send('====================================\nRolling a d20 for ' + ctx.message.author.mention + "  **Result:** " + str(random.randint(1, 20))+ "\n====================================")
      return

    spaceless_roll= roll.replace(" ", "")
    print(spaceless_roll)
    rollList = spaceless_roll.split('+') 
    i = 0
    rollModifier = 0
    while i < len(rollList):
      if rollList[i].isnumeric():
            rollModifier = rollModifier + int(rollList[i])
            print ('Roll modifier is now ', rollModifier)
            i = i + 1 
      else:

        try:
          numDice = rollList[i].split('d')[0]
          diceVal = rollList[i].split('d')[1]
          print ('Rolling ', numDice, 'of dice type d', diceVal)
          i = i + 1 
                       
        except Exception as e:      
          print (e)
          await ctx.send("I'm confused by that term so I'm skipping it.")
          i = i + 1 
         
      
        
        
        
        
        
        #Trying to roll more than 100 dice.
      #if int(numDice) > 100:
          #await ctx.send("Sorry %s, I don't have enough dice for that" % ctx.message.author.name)
          #return
        
        #Trying to roll dice with more than 100 faces. 
      #if int(diceVal) > 100:
          #await ctx.send("Sorry %s, a d100 is the largest dice type the Primus gave me." % ctx.message.author.name)
          #return                
        
        #rolls, limit = map(int, roll.split('d'))

      #for r in range(rolls):
            #number = random.randint(1, limit)
            #resultTotal = resultTotal + number
            
            #if resultString == '':
                #resultString += str(number)
            #else:
                #resultString += ', ' + str(number)
        
        # Output: If number of dice was specifically 1.
      #if numDice == '1':
            #await ctx.send("====================================\nRolling a d%s for %s" % (diceVal, ctx.message.author.mention)  + "\n**Result:** " + resultString + "\n====================================")
        
        # Output: If the number of dice was more than 1.
      #else:
            #await ctx.send("====================================\nRolling *%sd%s* for %s" % (numDice, diceVal, ctx.message.author.mention) + "\n**Result:** " + resultString + "\n**Total:** " + str(resultTotal)+ "\n====================================")

    

        
        
        
        

bot.run(Bot_Token)