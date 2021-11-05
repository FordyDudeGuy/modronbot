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
async def d4(ctx, *modifier):
  joinedModifier = ''.join(modifier)
  roll = random.randint(1, 4)
  if not modifier:
    await ctx.send('====================================\nRolling a d4 for ' + ctx.message.author.mention + "  *Result:* " + '**' + str(roll) + '**' +  "\n====================================")
    return

  elif joinedModifier.find('+') != -1:
      positiveModifierNumber = str(joinedModifier.replace('+',''))
      if positiveModifierNumber.isnumeric():
         total = roll + int(positiveModifierNumber)
         await ctx.send('====================================\nRolling a d4 and adding ' + str(positiveModifierNumber) + ' for ' + ctx.message.author.mention + " \n*Roll:* " + str(roll) + "\n*Result:* **" + str(total) + "**\n====================================")
         return
      else: 
        await ctx.send("I'm sorry, I didn't understand the term " + joinedModifier + ". Please try again.")
  
  elif joinedModifier.find('-') != -1:
      negativeModifierNumber = str(joinedModifier.replace('-',''))
      if negativeModifierNumber.isnumeric():
         
         total = roll - int(negativeModifierNumber)
         await ctx.send('====================================\nRolling a d4 and subtracting ' + str(negativeModifierNumber) + ' for ' + ctx.message.author.mention + " \n*Roll:* " + str(roll) + "\n*Result:* **" + str(total) + "**\n====================================")
         return
      else: 
        await ctx.send("I'm sorry, I didn't understand the term " + joinedModifier + ". Please try again.")

# Roll stats
@bot.command(pass_context=True, aliases=['']) 
async def stat(ctx):
    rollList = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
    rollList.sort()
    rawRolls = str(rollList)
    droppedRoll = min(rollList)
    rollList.remove(min(rollList))
    totalAbilityScore = str(sum(rollList))
    await ctx.send('====================================\nRolling a stat for ' + ctx.message.author.mention + "  *Result:* " + '**' + str(rawRolls)+ '**' + '\nDropping the **' + str(droppedRoll) + '** and totalling the rest = ' + '**' + str(totalAbilityScore) + '**' + "\n====================================")
    return

#full statgen
@bot.command(pass_context=True, aliases=['']) 
async def statgen(ctx):
  statList = []
  i = 0 
  while i < 7: 
    rollList = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
    rawRolls = str(rollList)
    droppedRoll = min(rollList)
    rollList.remove(min(rollList))
    totalAbilityScore = str(sum(rollList))
    statList.append(totalAbilityScore)
    i = i + 1
    return
  
  else:
    await ctx.send('====================================\nRolling stats for ' + ctx.message.author.mention + "  *\nResults:* **" + str(statList) + "\n====================================")
    return
  

# Roll a d6
@bot.command(pass_context=True, aliases=['D6']) 
async def d6(ctx, *modifier):
  joinedModifier = ''.join(modifier)
  roll = random.randint(1, 6)
  if not modifier:
    await ctx.send('====================================\nRolling a d6 for ' + ctx.message.author.mention + "  *Result:* " + '**' + str(roll) + '**' +  "\n====================================")
    return

  elif joinedModifier.find('+') != -1:
      positiveModifierNumber = str(joinedModifier.replace('+',''))
      if positiveModifierNumber.isnumeric():
         total = roll + int(positiveModifierNumber)
         await ctx.send('====================================\nRolling a d6 and adding ' + str(positiveModifierNumber) + ' for ' + ctx.message.author.mention + " \n*Roll:* " + str(roll) + "\n*Result:* **" + str(total) + "**\n====================================")
         return
      else: 
        await ctx.send("I'm sorry, I didn't understand the term " + joinedModifier + ". Please try again.")
  
  elif joinedModifier.find('-') != -1:
      negativeModifierNumber = str(joinedModifier.replace('-',''))
      if negativeModifierNumber.isnumeric():
         
         total = roll - int(negativeModifierNumber)
         await ctx.send('====================================\nRolling a d6 and subtracting ' + str(negativeModifierNumber) + ' for ' + ctx.message.author.mention + " \n*Roll:* " + str(roll) + "\n*Result:* **" + str(total) + "**\n====================================")
         return
      else: 
        await ctx.send("I'm sorry, I didn't understand the term " + joinedModifier + ". Please try again.")


# Roll a d8
@bot.command(pass_context=True, aliases=['D8']) 
async def d8(ctx, *modifier):
  joinedModifier = ''.join(modifier)
  roll = random.randint(1, 8)
  if not modifier:
    await ctx.send('====================================\nRolling a d8 for ' + ctx.message.author.mention + "  *Result:* " + '**' + str(roll) + '**' +  "\n====================================")
    return

  elif joinedModifier.find('+') != -1:
      positiveModifierNumber = str(joinedModifier.replace('+',''))
      if positiveModifierNumber.isnumeric():
         total = roll + int(positiveModifierNumber)
         await ctx.send('====================================\nRolling a d8 and adding ' + str(positiveModifierNumber) + ' for ' + ctx.message.author.mention + " \n*Roll:* " + str(roll) + "\n*Result:* **" + str(total) + "**\n====================================")
         return
      else: 
        await ctx.send("I'm sorry, I didn't understand the term " + joinedModifier + ". Please try again.")
  
  elif joinedModifier.find('-') != -1:
      negativeModifierNumber = str(joinedModifier.replace('-',''))
      if negativeModifierNumber.isnumeric():
         
         total = roll - int(negativeModifierNumber)
         await ctx.send('====================================\nRolling a d8 and subtracting ' + str(negativeModifierNumber) + ' for ' + ctx.message.author.mention + " \n*Roll:* " + str(roll) + "\n*Result:* **" + str(total) + "**\n====================================")
         return
      else: 
        await ctx.send("I'm sorry, I didn't understand the term " + joinedModifier + ". Please try again.")


# Roll a d10
@bot.command(pass_context=True, aliases=['D10']) 
async def d10(ctx, *modifier):
  joinedModifier = ''.join(modifier)
  roll = random.randint(1, 10)
  if not modifier:
    await ctx.send('====================================\nRolling a d10 for ' + ctx.message.author.mention + "  *Result:* " + '**' + str(roll) + '**' +  "\n====================================")
    return

  elif joinedModifier.find('+') != -1:
      positiveModifierNumber = str(joinedModifier.replace('+',''))
      if positiveModifierNumber.isnumeric():
         total = roll + int(positiveModifierNumber)
         await ctx.send('====================================\nRolling a d10 and adding ' + str(positiveModifierNumber) + ' for ' + ctx.message.author.mention + " \n*Roll:* " + str(roll) + "\n*Result:* **" + str(total) + "**\n====================================")
         return
      else: 
        await ctx.send("I'm sorry, I didn't understand the term " + joinedModifier + ". Please try again.")
  
  elif joinedModifier.find('-') != -1:
      negativeModifierNumber = str(joinedModifier.replace('-',''))
      if negativeModifierNumber.isnumeric():
         
         total = roll - int(negativeModifierNumber)
         await ctx.send('====================================\nRolling a d10 and subtracting ' + str(negativeModifierNumber) + ' for ' + ctx.message.author.mention + " \n*Roll:* " + str(roll) + "\n*Result:* **" + str(total) + "**\n====================================")
         return
      else: 
        await ctx.send("I'm sorry, I didn't understand the term " + joinedModifier + ". Please try again.")


# Roll a d12
@bot.command(pass_context=True, aliases=['D12']) 
async def d12(ctx, *modifier):
  joinedModifier = ''.join(modifier)
  roll = random.randint(1, 12)
  if not modifier:
    await ctx.send('====================================\nRolling a d12 for ' + ctx.message.author.mention + "  *Result:* " + '**' + str(roll) + '**' +  "\n====================================")
    return

  elif joinedModifier.find('+') != -1:
      positiveModifierNumber = str(joinedModifier.replace('+',''))
      if positiveModifierNumber.isnumeric():
         total = roll + int(positiveModifierNumber)
         await ctx.send('====================================\nRolling a d12 and adding ' + str(positiveModifierNumber) + ' for ' + ctx.message.author.mention + " \n*Roll:* " + str(roll) + "\n*Result:* **" + str(total) + "**\n====================================")
         return
      else: 
        await ctx.send("I'm sorry, I didn't understand the term " + joinedModifier + ". Please try again.")
  
  elif joinedModifier.find('-') != -1:
      negativeModifierNumber = str(joinedModifier.replace('-',''))
      if negativeModifierNumber.isnumeric():
         
         total = roll - int(negativeModifierNumber)
         await ctx.send('====================================\nRolling a d12 and subtracting ' + str(negativeModifierNumber) + ' for ' + ctx.message.author.mention + " \n*Roll:* " + str(roll) + "\n*Result:* **" + str(total) + "**\n====================================")
         return
      else: 
        await ctx.send("I'm sorry, I didn't understand the term " + joinedModifier + ". Please try again.")


# Roll a d20
@bot.command(pass_context=True, aliases=['D20']) 
async def d20(ctx, *modifier):
  joinedModifier = ''.join(modifier)
  roll = random.randint(1, 20)
  if not modifier:
    await ctx.send('====================================\nRolling a d20 for ' + ctx.message.author.mention + "  *Result:* " + '**' + str(roll) + '**' +  "\n====================================")
    return

  elif joinedModifier.find('+') != -1:
      positiveModifierNumber = str(joinedModifier.replace('+',''))
      if positiveModifierNumber.isnumeric():
         total = roll + int(positiveModifierNumber)
         await ctx.send('====================================\nRolling a d20 and adding ' + str(positiveModifierNumber) + ' for ' + ctx.message.author.mention + " \n*Roll:* " + str(roll) + "\n*Result:* **" + str(total) + "**\n====================================")
         return
      else: 
        await ctx.send("I'm sorry, I didn't understand the term " + joinedModifier + ". Please try again.")
  
  elif joinedModifier.find('-') != -1:
      negativeModifierNumber = str(joinedModifier.replace('-',''))
      if negativeModifierNumber.isnumeric():
         
         total = roll - int(negativeModifierNumber)
         await ctx.send('====================================\nRolling a d20 and subtracting ' + str(negativeModifierNumber) + ' for ' + ctx.message.author.mention + " \n*Roll:* " + str(roll) + "\n*Result:* **" + str(total) + "**\n====================================")
         return
      else: 
        await ctx.send("I'm sorry, I didn't understand the term " + joinedModifier + ". Please try again.")
 



# Advantage/Disadvantage: Roll 2d20s and sort them from lowest to highest.
@bot.command(pass_context=True, aliases=['a','A']) 
async def adv(ctx, *modifier,):
    result_list = [random.randint(1,20) for _ in range(2)]
    result_list.sort()
    joinedModifier = ''.join(modifier)
    
    if not modifier:
      await ctx.send('====================================\nRolling two d20s for ' + ctx.message.author.mention + "  *Results:* **" + str(result_list[0]) + '** and **' +  str(result_list[1]) + "**\n====================================")
      return

    if joinedModifier.find('+') != -1:
      positiveModifierNumber = str(joinedModifier.replace('+',''))
      if positiveModifierNumber.isnumeric():
        result1 = int(result_list[0]) + int(positiveModifierNumber)
        result2 = int(result_list[1]) + int(positiveModifierNumber)
        await ctx.send('====================================\nRolling two d20s and adding '+ str(positiveModifierNumber) +' for ' + ctx.message.author.mention + "\n*Dice Rolls:* " + str(result_list[0]) +' and '+ str(result_list[1]) + "\n*Totals:* **" + str(result1) + '** and **' +  str(result2) + "**\n====================================")
        return


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
    i = 0
    n = 0
    rollModifier = int(0)
    
    #if no argument is given then just roll a d20.
    if not roll:
      await ctx.send('====================================\nRolling a d20 for ' + ctx.message.author.mention + "  *Result:* " + '**'+str(random.randint(1, 20))+'**'+"\n====================================")
      return
    
    # This converts the argument (which is a Tuple) to a string with no spaces. Then separates the string into a list of individual terms that were separated by a +. No negative integer support currently, figure that out later.
    joinedRoll= ''.join(roll)  
    rollList = joinedRoll.split('+') 
   
    # While loop that for each term in the 'rollList' that will either add it to a total modifier if it is an integer or will split it and roll it if it is a xdy expression
    while i < len(rollList):
      
        if rollList[i].isnumeric():
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
        
        grandTotal = resultTotal + rollModifier
        printedRoll= joinedRoll.replace("+", " + ")
        if rollModifier > 1:
          await ctx.send("====================================\nRolling *" + printedRoll + "*  for %s" % (ctx.message.author.mention) + "\n*Result:* " + resultString + "\n*Subtotal:* " + str(resultTotal) + ' + ' + str(rollModifier) + '\n*Total:*  ' + "**" + str(grandTotal) + "**"+"\n====================================")
        else:
          await ctx.send("====================================\nRolling *" + printedRoll + "*  for %s" % (ctx.message.author.mention) + "\n*Result:* " + resultString + '\n*Total:*  ' + "**" + str(grandTotal) + "**"+"\n====================================")
        
        return 

#Command required for bot to function.                             
bot.run(Bot_Token)