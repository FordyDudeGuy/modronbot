# Import requirements and initialise bot prefix and get token from secret value.
import discord
import os
import random
from discord.ext import commands
from discord.ext.commands import Bot
import re
bot = Bot(command_prefix='!')
Bot_Token = os.environ['TOKEN']

# Load Success Message
@bot.event
async def on_ready():
	print(f'*** {bot.user} online. ***')

#statgen
@bot.command(pass_context=True, aliases=['stats']) 
async def statgen(ctx):
  statList = []
  i = 0

  while i < 6: 
    rollList = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
    rollList.remove(min(rollList))
    totalAbilityScore = str(sum(rollList))
    statList.append(totalAbilityScore)
    i = i + 1
    
  else:
    await ctx.send('==========================\nRolling stats for ' + ctx.message.author.mention + "\n*Results:* **" + str(statList[0]) + ' ' + str(statList[1]) + ' ' +str(statList[2]) + ' ' +str(statList[3]) + ' ' + str(statList[4]) + ' ' + str(statList[5]) + "**\n==========================")  
    return 
    
#roll command
@bot.command(pass_context=True, aliases=['roll', 'ROLL', 'Roll'])
async def r(ctx, *roll,):
 
  #if no argument is given then just roll a d20.
    if not roll:
      await ctx.send('==========================\n*Rolling a d20 for ' + ctx.message.author.mention + "*\n**Dice Roll: " + str(random.randint(1, 20))+'**'+"\n==========================")
      return

  #initialise variables
    resultTotal = 0
    resultNTotal = 0
    resultString = ''
    i = 0
    n = 0
    rollModifier = int(0)
    rollNModifier = int(0)
    positiveList = []
    negativeList= []

  # This converts the argument (which is a Tuple) to a string with no spaces. Then separates the string into a list of individual terms that were separated by a + or a -. 
      
    joinedRoll= ''.join(roll)  
    rollList = re.findall('[-+]?\w+', joinedRoll.replace(' ', ''))
    
  # While loop that splits terms into positive list and negative list.
    
    while i < len(rollList):
      if "-" in str(rollList[i]):
        negativeList.append(rollList[i])
      elif "-" not in str(rollList[i]):
        positiveList.append(rollList[i])
      i = i + 1 
    
  #Positive term resolution
    i = 0
    while i < len(positiveList):
      positiveList[i] = positiveList[i].replace ("+", "")
      if "d" not in positiveList[i]:
        rollModifier = rollModifier + int(positiveList[i])
        i = i + 1
      else:
        try:
          numDice = positiveList[i].split('d')[0]
          diceVal = positiveList[i].split('d')[1]

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
                  
        except Exception:      
            await ctx.send("Error. I didn't understand that command %s." % (ctx.message.author.mention))
            return
        i = i + 1
         
  #negative term resolution
    i = 0
    while i < len(negativeList):
      negativeList[i] = negativeList[i].replace("-","")
      if "d" not in negativeList[i]:
        rollNModifier = rollNModifier + int(negativeList[i])
        i = i + 1
      else:
        try:
          numDice = negativeList[i].split('d')[0]
          diceVal = negativeList[i].split('d')[1]

  # If the number of dice is not specified default to one dice of given type. 
          if str(numDice) =='':
            numDice = int(1)
            
  #reset n then do another while loop to create results string.
          n = 0
          while n < int(numDice):
            diceResult = random.randint(1, int(diceVal))
            resultNTotal = int(resultNTotal) + int(diceResult)
            
            if resultString == '':
              resultString += str(diceResult)
              n = n + 1
                                     
            else:
              resultString += ', -' + str(diceResult)
              n = n + 1
          
        
        except Exception:      
            await ctx.send("Error. I didn't understand that command %s." % (ctx.message.author.mention))
            return
      i = i + 1
      
  # Output
    print (resultNTotal)
    grandTotal = resultTotal + rollModifier  - rollNModifier - resultNTotal
    printedRoll= joinedRoll.replace("+", " + ")
    printedRoll= printedRoll.replace("-", " - ")
    rollNModifier = str(rollNModifier).replace("-", "")
    await ctx.send("==========================\n*Rolling: " + printedRoll + "*  for %s" % (ctx.message.author.mention) + "\nDice Rolls: " + resultString + "\n**Total:**  " + "**" + str(grandTotal) + "**" + "\n==========================")
    return
                   
#adv./disadv. command
@bot.command(pass_context=True, aliases=['a','A']) 
async def adv(ctx, *modifier,):
    result_list = [random.randint(1,20) for _ in range(2)] 
    joinedModifier = ''.join(modifier)
    
    if not modifier:
      await ctx.send('==========================\n*Rolling two d20s for* ' + ctx.message.author.mention + "\n**Dice Rolls: " + str(result_list[0]) + '** and **' +  str(result_list[1]) + "**\n==========================")
      return

    if joinedModifier.find('+') != -1:
      positiveModifierNumber = str(joinedModifier.replace('+',''))
      if positiveModifierNumber.isnumeric():
        result1 = int(result_list[0]) + int(positiveModifierNumber)
        result2 = int(result_list[1]) + int(positiveModifierNumber)
        await ctx.send('==========================\n*Rolling two d20s and adding '+ str(positiveModifierNumber) +'* for ' + ctx.message.author.mention + "\nDice Rolls: " + str(result_list[0]) +' and '+ str(result_list[1]) + "\n**Totals:** **" + str(result1) + '** and **' +  str(result2) + "**\n==========================")
        return
    
    if joinedModifier.find('-') != -1:
      negativeModifierNumber = str(joinedModifier.replace('-',''))
      if negativeModifierNumber.isnumeric():
        result1 = int(result_list[0]) - int(negativeModifierNumber)
        result2 = int(result_list[1]) - int(negativeModifierNumber)
        await ctx.send('==========================\n*Rolling two d20s and subtracting '+ str(negativeModifierNumber) +'* for ' + ctx.message.author.mention + "\nDice Rolls: " + str(result_list[0]) +' and '+ str(result_list[1]) + "\n**Totals:** **" + str(result1) + '** and **' +  str(result2) + "**\n==========================")
        return        

#Command required for bot to function.                             
bot.run(Bot_Token)