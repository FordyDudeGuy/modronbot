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
async def adv(ctx):
    result_list = [random.randint(1,20) for _ in range(2)]
    result_list.sort()
    await ctx.send('====================================\nRolling two d20s for ' + ctx.message.author.mention + "  *Results:* " + '**' +str(result_list[0]) + '**' + + ' and '+ '**' +  str(result_list[1]) + '**' + "\n====================================")

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
    
    # This converts the argument (which is a Tuple) to a string with no spaces. 
    joinedRoll= ''.join(roll)  
    print(joinedRoll, ' <-- joinedRoll')

    # This separates the string into a list of individual terms that were separated by a +. No negative integer support currently, figure that out later.
    rollList = joinedRoll.split('+') 
    print (rollList, ' <-- Roll List')
    
    
    # While loop that for each term in the 'rollList' that will either add it to a total modifier if it is an integer or will split it and roll it if it is a xdy expression
    while i < len(rollList):
      
        if rollList[i].isnumeric():
            rollModifier = int(rollModifier) + int(rollList[i])
            i = i + 1 
            #print ('this term is numeric so added to RollModifier now: ', rollModifier)
        
        else:
          print('Term is not numeric so will try to split. ')
          try:
            numDice = rollList[i].split('d')[0]
            diceVal = rollList[i].split('d')[1]
            print ('Rolling ', numDice, 'of dice type d', diceVal)
            
            #reset n
            n = 0

            while n < int(numDice):
              diceResult = random.randint(1, int(diceVal))
              resultTotal = int(resultTotal) + int(diceResult)
              n = n + 1

              print (resultTotal, ' <-- Current Result Total')
              print ('Rolling a d', diceVal, '=', diceResult)
              
                        
              if resultString == '':
                resultString += str(diceResult)
                n = n + 1
                
                print (resultString)
                            
              else:
                resultString += ', ' + str(diceResult)
                n = n + 1
                
                print (resultString, '<-- Current Result String')
                
                

            #rolls, limit = map(int, roll.split('d'))

            #for r in range(rolls):
              #number = random.randint(1, diceVal)
             # resultTotal = resultTotal + number
              #print (resultTotal, ' <-- Current Result Total')
            
              #if resultString == '':
                #resultString += str(number)
                #print (resultString)
              #else:
                #resultString += ', ' + str(number)
                #print (resultString, '<-- Current Result String')
            
            i = i + 1 
          

    #This exception should print and skip any terms that are not integers or xdy expressions               
          except Exception as e:      
            print (e)
            await ctx.send("I'm confused by the term '*" + rollList[i] + "*' so I'm skipping it.")
            await ctx.send(e)
            i = i + 1 
    
    # Output: If the number of dice was more than 1 
    else:
        grandTotal = int(resultTotal) + int(rollModifier)
        await ctx.send("====================================\nRolling *%sd%s* for %s" % (numDice, diceVal, ctx.message.author.mention) + "\n**Result:** " + int(resultString) + "\n*Roll Total:* " + int(resultTotal) + int(rollModifier) + '\n *Total*'+ int(grandTotal) + "\n====================================")
        return
         
      #Trying to roll more than 100 dice.
      #if int(numDice) > 100:
          #await ctx.send("Sorry %s, I don't have enough dice for that" % ctx.message.author.name)
          #return
        
      #Trying to roll dice with more than 100 faces. 
      #if int(diceVal) > 100:
          #await ctx.send("Sorry %s, a d100 is the largest dice type the Primus gave me." % ctx.message.author.name)
          #return                
              
      # Output: If number of dice was specifically 1.
      #if numDice == '1':
            #await ctx.send("====================================\nRolling a d%s for %s" % (diceVal, ctx.message.author.mention)  + "\n**Result:** " + resultString + "\n====================================")
  
bot.run(Bot_Token)