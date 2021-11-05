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
    await ctx.send('====================================\nHi there'+ ctx.message.author.mention +'!'+ "\nI am a Modron.\nMy sole purpose is to roll dice for you.\nPlease find a list of my commands below.\n\n_Commands_\n\n/r *x*d*y* where *x* = no. of dice and *y* = dice sides\nIf you miss out *x*, I'll assume you just want the one. If you leave out *x*d*y*, I'll just  assume you just want a d20. You can also add a + for more dice to be rolled at the same time or for a modifier \n/adv (or just /a) - Rolls 2d20 for adv./disadv sorted in asc. order.\n====================================")    

#statgen
@bot.command(pass_context=True, aliases=['stats']) 
async def statgen(ctx):
  statList = []
  i = 0

  while i < 6: 
    rollList = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
    droppedRoll = min(rollList)
    rollList.remove(min(rollList))
    totalAbilityScore = str(sum(rollList))
    statList.append(totalAbilityScore)
    i = i + 1
    
  else:
    await ctx.send('====================================\nRolling stats for ' + ctx.message.author.mention + "\n*Results:* **" + str(statList[0]) + ' ' + str(statList[1]) + ' ' +str(statList[2]) + ' ' +str(statList[3]) + ' ' + str(statList[4]) + ' ' + str(statList[5]) + "**\n====================================")  
    return 
    
#Roll
@bot.command(pass_context=True, aliases=['roll', 'ROLL', 'Roll'])
async def r(ctx, *roll,):
    #/r command takes a string argument that will be processed and used later.
    #initialise variables
    resultTotal = 0
    resultString = ''
    i = 0
    n = 0
    a = 0
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
      
        if rollList[i].find('-') = 1:
          
          try:
            beforeMinus = rollList[i].split('-')[0]
            afterMinus = rollList[i].split('-')[1]
            rollList.remove(rollList[i])
            rollList.append(beforeMinus)

        if rollList[i].isnumeric():
            rollModifier = int(rollModifier) + int(rollList[i])
            i = i + 1 

        else:
          try:
            numDice = rollList[i].split('d')[0]
            diceVal = rollList[i].split('d')[1]

            # If the number of dice is not specified default to one dice of given type. 
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
          
    #This exception will abort the command if any of the terms are not integers or xdy expressions               
          except Exception as e:      
            await ctx.send("Error. I didn't understand that command %s." % (ctx.message.author.mention))
            return
    
    # Output: If the number of dice was more than 1 
    else:
        
        grandTotal = resultTotal + rollModifier - int(beforeMinus)
        printedRoll= joinedRoll.replace("+", " + ")
        printedRoll= printedRoll.replace("-", " - ")
        if rollModifier > 1:
          await ctx.send("====================================\nRolling *" + printedRoll + "*  for %s" % (ctx.message.author.mention) + "\n*Result:* " + resultString + "\n*Subtotal:* " + str(resultTotal) + ' + ' + str(rollModifier) + '\n*Total:*  ' + "**" + str(grandTotal) + "**"+"\n====================================")
        else:
          await ctx.send("====================================\nRolling *" + printedRoll + "*  for %s" % (ctx.message.author.mention) + "\n*Result:* " + resultString + '\n*Total:*  ' + "**" + str(grandTotal) + "**"+"\n====================================")
        
        return 

# Adv./ Disadv.
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
    
    if joinedModifier.find('-') != -1:
      negativeModifierNumber = str(joinedModifier.replace('-',''))
      if negativeModifierNumber.isnumeric():
        result1 = int(result_list[0]) - int(negativeModifierNumber)
        result2 = int(result_list[1]) - int(negativeModifierNumber)
        await ctx.send('====================================\nRolling two d20s and subtracting '+ str(negativeModifierNumber) +' for ' + ctx.message.author.mention + "\n*Dice Rolls:* " + str(result_list[0]) +' and '+ str(result_list[1]) + "\n*Totals:* **" + str(result1) + '** and **' +  str(result2) + "**\n====================================")
        return        

#Command required for bot to function.                             
bot.run(Bot_Token)