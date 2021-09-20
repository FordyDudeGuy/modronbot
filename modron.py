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
    await ctx.send('====================================\nHi there'+ ctx.message.author.mention +'!'+ "\nI am a Modron.\nMy sole purpose is to roll dice for you.\nPlease find a list of my commands below.\n\n_Commands_\n\n/d*x* where *x* is 2, 4, 6, 8, 10, 12 or 20 to roll a die with that many sides.\n/r *x*d*y* where *x* = no. of dice and *y* = dice sides\nIf you miss out *x*, I'll assume you just want the one. If you leave out *x*d*y*, I'll just  assume you just want a d20. You can also add a + for more dice to be rolled at the same time or for a modifier \n/adv (or just /a) - Rolls 2d20 for adv./disadv sorted in asc. order.\n====================================")    

# Roll a d4
@bot.command(pass_context=True, aliases=['D4']) 
async def d4(ctx):
    await ctx.send('====================================\nRolling a d4 for ' + ctx.message.author.mention + "  *Result:* " + '**' +  str(random.randint(1, 4))+ '**' +  "\n====================================")

# Roll a d6
@bot.command(pass_context=True, aliases=['D6']) 
async def d6(ctx):
    await ctx.send('====================================\nRolling a d6 for ' + ctx.message.author.mention + "  *Result:* " + '**' +  str(random.randint(1, 6))+ '**' +  "\n====================================")

# Roll a d8
@bot.command(pass_context=True, aliases=['D8']) 
async def d8(ctx):
    await ctx.send('====================================\nRolling a d8 for ' + ctx.message.author.mention + "  *Result:* " + '**' +  str(random.randint(1, 8))+ '**' +  "\n====================================")

# Roll a d10
@bot.command(pass_context=True, aliases=['D10']) 
async def d10(ctx):
    await ctx.send('====================================\nRolling a d10 for ' + ctx.message.author.mention + "  *Result:* " + '**' +  str(random.randint(1, 10))+ '**' +  "\n====================================")

# Roll a d12
@bot.command(pass_context=True, aliases=['D12']) 
async def d12(ctx):
    await ctx.send('====================================\nRolling a d12 for ' + ctx.message.author.mention + "  *Result:* " + '**' +  str(random.randint(1, 12))+ '**' +  "\n====================================") 

# Roll a d20
@bot.command(pass_context=True, aliases=['D20']) 
async def d20(ctx):
    await ctx.send('====================================\nRolling a d20 for ' + ctx.message.author.mention + "  *Result:* " + '**' + str(random.randint(1, 20))+ '**' +  "\n====================================")
    
# Roll 2d20s and sort them from lowest to highest.
@bot.command(pass_context=True, aliases=['a','A']) 
async def adv(ctx, *modifier,):
    result_list = [random.randint(1,20) for _ in range(2)]
    result_list.sort()
    joinedmodifier = ''.join(roll)

    if not modifier:
      await ctx.send('====================================\nRolling two d20s for ' + ctx.message.author.mention + "  *Results:* **" + str(result_list[0]) + '** and **' +  str(result_list[1]) + "**\n====================================")
      return

    if str(joinedModifier).find('+') != -1:
      positiveModifierNumber = str(modifier.replace('+',''))
      if positiveModifierNumber.isnumeric():
        result1 = int(result_list[0]) + int(positiveModifierNumber)
        result2 = int(result_list[1]) + int(positiveModifierNumber)
        await ctx.send('====================================\nRolling two d20s for ' + ctx.message.author.mention + "  *Results:* **" + str(result1) + '** and **' +  str(result2) + "**\n====================================")
        return
    

if positiveModifierNumber.isnumeric():

#Flip the table
@bot.command(pass_context=True, aliases=['f','F', 'FLIP'])
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
async def r(ctx, *roll,):
    #/r command takes a string argument that will be processed and used later.
    #initialise variables
    resultTotal = 0
    resultString = ''
    negativeOperator = '-'
    i = 0
    n = 0
    rollModifier = int(0)
    negativeRollModifier = int(0)
    
    #if no argument is given then just roll a d20.
    if not roll:
      await ctx.send('====================================\nRolling a d20 for ' + ctx.message.author.mention + "  *Result:* " + '**'+str(random.randint(1, 20))+'**'+"\n====================================")
      return
    
    # This converts the argument (which is a Tuple) to a string with no spaces. Then separates the string into a list of individual terms that were separated by a +. No negative integer support currently, figure that out later.
    joinedRoll= ''.join(roll)  
    rollList = joinedRoll.split('+')
    
   
    # While loop that for each term in the 'rollList' that will either add it to a total modifier if it is an integer or will split it and roll it if it is a xdy expression
    while i < len(rollList):
      
        if rollList[i].find(negativeOperator) != -1:
            subtractiveTerm = rollList[i].split('-')[1]
            if subtractiveTerm.isnumeric():
              negativeRollModifier = negativeRollModifier + subtractiveTerm
          

        elif rollList[i].isnumeric():
            rollModifier = int(rollModifier) + int(rollList[i])
            i = i + 1 

        else:
          try:
            numDice = rollList[i].split('d')[0]
            diceVal = rollList[i].split('d')[1]

            # If the number of dice is not specified defualt to one dice of given type. 
            if str(numDice) =='':
              numDice = int(1)

            #reset n then do another while loop to create results string.
            n = 0
            while n < int(numDice):
              diceResult = random.randint(1, int(diceVal))
              resultTotal = int(resultTotal) + int(diceResult)

              if resultString == '':
                resultString += str(diceResult)
                n = n + 1
                                     
              else:
                resultString += ', ' + str(diceResult)
                n = n + 1
              
            i = i + 1 
          
    #This exception should print and skip any terms that are not integers or xdy expressions               
          except Exception as e:      
            print (e)
            await ctx.send("I'm confused by the term '*" + rollList[i] + "*' so I'm skipping it.")
            i = i + 1 
    
    # Output: If the number of dice was more than 1 
    else:
        
        grandTotal = resultTotal + rollModifier - negativeRollModifier
        printedRoll= joinedRoll.replace("+", " + ")
        printedRoll= printedRoll.replace("-", " - ")
        if rollModifier > 1:
          await ctx.send("====================================\nRolling *" + printedRoll + "*  for %s" % (ctx.message.author.mention) + "\n*Result:* " + resultString + "\n*Subtotal:* " + str(resultTotal) + ' + ' + str(rollModifier) + '\n*Total:*  ' + "**" + str(grandTotal) + "**"+"\n====================================")
        else:
          await ctx.send("====================================\nRolling *" + printedRoll + "*  for %s" % (ctx.message.author.mention) + "\n*Result:* " + resultString + '\n*Total:*  ' + "**" + str(grandTotal) + "**"+"\n====================================")
        
        return 
                             
bot.run(Bot_Token)