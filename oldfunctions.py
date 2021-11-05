
# Roll a d4
# @bot.command(pass_context=True, aliases=['D4']) 
# async def d4(ctx, *modifier):
#   joinedModifier = ''.join(modifier)
#   roll = random.randint(1, 4)
#   if not modifier:
#     await ctx.send('====================================\nRolling a d4 for ' + ctx.message.author.mention + "  *Result:* " + '**' + str(roll) + '**' +  "\n====================================")
#     return

#   elif joinedModifier.find('+') != -1:
#       positiveModifierNumber = str(joinedModifier.replace('+',''))
#       if positiveModifierNumber.isnumeric():
#          total = roll + int(positiveModifierNumber)
#          await ctx.send('====================================\nRolling a d4 and adding ' + str(positiveModifierNumber) + ' for ' + ctx.message.author.mention + " \n*Roll:* " + str(roll) + "\n*Result:* **" + str(total) + "**\n====================================")
#          return
#       else: 
#         await ctx.send("I'm sorry, I didn't understand the term " + joinedModifier + ". Please try again.")
  
#   elif joinedModifier.find('-') != -1:
#       negativeModifierNumber = str(joinedModifier.replace('-',''))
#       if negativeModifierNumber.isnumeric():
         
#          total = roll - int(negativeModifierNumber)
#          await ctx.send('====================================\nRolling a d4 and subtracting ' + str(negativeModifierNumber) + ' for ' + ctx.message.author.mention + " \n*Roll:* " + str(roll) + "\n*Result:* **" + str(total) + "**\n====================================")
#          return
#       else: 
#         await ctx.send("I'm sorry, I didn't understand the term " + joinedModifier + ". Please try again.")

# # Roll a d6
# @bot.command(pass_context=True, aliases=['D6']) 
# async def d6(ctx, *modifier):
#   joinedModifier = ''.join(modifier)
#   roll = random.randint(1, 6)
#   if not modifier:
#     await ctx.send('====================================\nRolling a d6 for ' + ctx.message.author.mention + "  *Result:* " + '**' + str(roll) + '**' +  "\n====================================")
#     return

#   elif joinedModifier.find('+') != -1:
#       positiveModifierNumber = str(joinedModifier.replace('+',''))
#       if positiveModifierNumber.isnumeric():
#          total = roll + int(positiveModifierNumber)
#          await ctx.send('====================================\nRolling a d6 and adding ' + str(positiveModifierNumber) + ' for ' + ctx.message.author.mention + " \n*Roll:* " + str(roll) + "\n*Result:* **" + str(total) + "**\n====================================")
#          return
#       else: 
#         await ctx.send("I'm sorry, I didn't understand the term " + joinedModifier + ". Please try again.")
  
#   elif joinedModifier.find('-') != -1:
#       negativeModifierNumber = str(joinedModifier.replace('-',''))
#       if negativeModifierNumber.isnumeric():
         
#          total = roll - int(negativeModifierNumber)
#          await ctx.send('====================================\nRolling a d6 and subtracting ' + str(negativeModifierNumber) + ' for ' + ctx.message.author.mention + " \n*Roll:* " + str(roll) + "\n*Result:* **" + str(total) + "**\n====================================")
#          return
#       else: 
#         await ctx.send("I'm sorry, I didn't understand the term " + joinedModifier + ". Please try again.")

# # Roll a d8
# @bot.command(pass_context=True, aliases=['D8']) 
# async def d8(ctx, *modifier):
#   joinedModifier = ''.join(modifier)
#   roll = random.randint(1, 8)
#   if not modifier:
#     await ctx.send('====================================\nRolling a d8 for ' + ctx.message.author.mention + "  *Result:* " + '**' + str(roll) + '**' +  "\n====================================")
#     return

#   elif joinedModifier.find('+') != -1:
#       positiveModifierNumber = str(joinedModifier.replace('+',''))
#       if positiveModifierNumber.isnumeric():
#          total = roll + int(positiveModifierNumber)
#          await ctx.send('====================================\nRolling a d8 and adding ' + str(positiveModifierNumber) + ' for ' + ctx.message.author.mention + " \n*Roll:* " + str(roll) + "\n*Result:* **" + str(total) + "**\n====================================")
#          return
#       else: 
#         await ctx.send("I'm sorry, I didn't understand the term " + joinedModifier + ". Please try again.")
  
#   elif joinedModifier.find('-') != -1:
#       negativeModifierNumber = str(joinedModifier.replace('-',''))
#       if negativeModifierNumber.isnumeric():
         
#          total = roll - int(negativeModifierNumber)
#          await ctx.send('====================================\nRolling a d8 and subtracting ' + str(negativeModifierNumber) + ' for ' + ctx.message.author.mention + " \n*Roll:* " + str(roll) + "\n*Result:* **" + str(total) + "**\n====================================")
#          return
#       else: 
#         await ctx.send("I'm sorry, I didn't understand the term " + joinedModifier + ". Please try again.")

# # Roll a d10
# @bot.command(pass_context=True, aliases=['D10']) 
# async def d10(ctx, *modifier):
#   joinedModifier = ''.join(modifier)
#   roll = random.randint(1, 10)
#   if not modifier:
#     await ctx.send('====================================\nRolling a d10 for ' + ctx.message.author.mention + "  *Result:* " + '**' + str(roll) + '**' +  "\n====================================")
#     return

#   elif joinedModifier.find('+') != -1:
#       positiveModifierNumber = str(joinedModifier.replace('+',''))
#       if positiveModifierNumber.isnumeric():
#          total = roll + int(positiveModifierNumber)
#          await ctx.send('====================================\nRolling a d10 and adding ' + str(positiveModifierNumber) + ' for ' + ctx.message.author.mention + " \n*Roll:* " + str(roll) + "\n*Result:* **" + str(total) + "**\n====================================")
#          return
#       else: 
#         await ctx.send("I'm sorry, I didn't understand the term " + joinedModifier + ". Please try again.")
  
#   elif joinedModifier.find('-') != -1:
#       negativeModifierNumber = str(joinedModifier.replace('-',''))
#       if negativeModifierNumber.isnumeric():
#          total = roll - int(negativeModifierNumber)
#          await ctx.send('====================================\nRolling a d10 and subtracting ' + str(negativeModifierNumber) + ' for ' + ctx.message.author.mention + " \n*Roll:* " + str(roll) + "\n*Result:* **" + str(total) + "**\n====================================")
#          return
#       else: 
#         await ctx.send("I'm sorry, I didn't understand the term " + joinedModifier + ". Please try again.")

# # Roll a d12
# @bot.command(pass_context=True, aliases=['D12']) 
# async def d12(ctx, *modifier):
#   joinedModifier = ''.join(modifier)
#   roll = random.randint(1, 12)
#   if not modifier:
#     await ctx.send('====================================\nRolling a d12 for ' + ctx.message.author.mention + "  *Result:* " + '**' + str(roll) + '**' +  "\n====================================")
#     return

#   elif joinedModifier.find('+') != -1:
#       positiveModifierNumber = str(joinedModifier.replace('+',''))
#       if positiveModifierNumber.isnumeric():
#          total = roll + int(positiveModifierNumber)
#          await ctx.send('====================================\nRolling a d12 and adding ' + str(positiveModifierNumber) + ' for ' + ctx.message.author.mention + " \n*Roll:* " + str(roll) + "\n*Result:* **" + str(total) + "**\n====================================")
#          return
#       else: 
#         await ctx.send("I'm sorry, I didn't understand the term " + joinedModifier + ". Please try again.")
  
#   elif joinedModifier.find('-') != -1:
#       negativeModifierNumber = str(joinedModifier.replace('-',''))
#       if negativeModifierNumber.isnumeric():
         
#          total = roll - int(negativeModifierNumber)
#          await ctx.send('====================================\nRolling a d12 and subtracting ' + str(negativeModifierNumber) + ' for ' + ctx.message.author.mention + " \n*Roll:* " + str(roll) + "\n*Result:* **" + str(total) + "**\n====================================")
#          return
#       else: 
#         await ctx.send("I'm sorry, I didn't understand the term " + joinedModifier + ". Please try again.")


# # Roll a d20
# @bot.command(pass_context=True, aliases=['D20']) 
# async def d20(ctx, *modifier):
#   joinedModifier = ''.join(modifier)
#   roll = random.randint(1, 20)
#   if not modifier:
#     await ctx.send('====================================\nRolling a d20 for ' + ctx.message.author.mention + "  *Result:* " + '**' + str(roll) + '**' +  "\n====================================")
#     return

#   elif joinedModifier.find('+') != -1:
#       positiveModifierNumber = str(joinedModifier.replace('+',''))
#       if positiveModifierNumber.isnumeric():
#          total = roll + int(positiveModifierNumber)
#          await ctx.send('====================================\nRolling a d20 and adding ' + str(positiveModifierNumber) + ' for ' + ctx.message.author.mention + " \n*Roll:* " + str(roll) + "\n*Result:* **" + str(total) + "**\n====================================")
#          return
#       else: 
#         await ctx.send("I'm sorry, I didn't understand the term " + joinedModifier + ". Please try again.")
  
#   elif joinedModifier.find('-') != -1:
#       negativeModifierNumber = str(joinedModifier.replace('-',''))
#       if negativeModifierNumber.isnumeric():
         
#          total = roll - int(negativeModifierNumber)
#          await ctx.send('====================================\nRolling a d20 and subtracting ' + str(negativeModifierNumber) + ' for ' + ctx.message.author.mention + " \n*Roll:* " + str(roll) + "\n*Result:* **" + str(total) + "**\n====================================")
#          return
#       else: 
#         await ctx.send("I'm sorry, I didn't understand the term " + joinedModifier + ". Please try again.")

#Flip the table
# @bot.command(pass_context=True, aliases=['f','F', 'FLIP'])
# @commands.cooldown(rate=1, per=20) 
# async def flip(ctx):
#     await ctx.send('====================================\n %s asked me to flip the table as they are mad. I passed my Strength check, so here goes... \n\n(╯°□°)╯︵ ┻━┻\n\n===================================='% ctx.message.author.name)

# #If users try to use the flip command too soon after last time using it...
# @flip.error
# async def command_name_error(ctx, error):
#         if isinstance(error, commands.CommandOnCooldown):
#             await ctx.send("Sorry %s, I'm still unflipping the table from last time you asked me to flip it. Please try again in a moment." % ctx.message.author.name )