# Vandivort Bot by LuckyThe4thJr

import discord
from discord.ext import commands

TOKEN = 'TOKEN'

  #<-----Basic Setup----->

client = commands.Bot(command_prefix = 'v/')
client.remove_command('help')
status = ['Prefix "v/"', 'at Hotel Vandivort', 'v/help']

async def change_status():
  await client.wait_unitl_ready()
  msgs = cycle(status)
  
  while not client.is_closed:
  current_status = next(msgs)
  await client.change_presence(game=discord.Game(name=current_status))
  await asyncio.sleep(10)

@client.event
async def on_ready():
  await client.change_presence(game=discord.Game(name='Hotel Vandivort'))
  print('Bot online!')

@client.event
async def on_message(message):
  print('A user has sent a message.')
  await client.process_commands(message)

@client.event
async def on_member_join(member):
  role = discord.utils.get(member.server.roles, name="Vandivort Member")
  await client.add_roles(member, role)

  #<-----Welcome/Goodbye Message----->
  
@client.event
async def on_member_join(member):
  print ("Recognised that a member called " + member.name + " joined")
  await client.send_message(member, "Welcome to the Offical Hotel Vandivort Discord server!")
  print ("Sent message to " + member.name)
  
@client.event
async def on_message_leave(member):
  print ("Recognised that a member " + memver.name + " left")
  await client.send_message(member, "Goodbye, we well miss you here at the Offical Hotel Vandivort Discord server.")
  print ("Sent message to " + member.name)
 
  #<-----Basic Commands----->

@client.command()
async def ping():
  await client.say('Pong!')
  
@client.command()
async def echo(ctx, *, msg):
  await client.delete_message(ctx.message)
  await bot.say(msg)
  
@client.event
async def on_message(message):
    if message.content.startswith(myname + '!btcprice'):
        print('[command]: btcprice ')
        btc_price_usd, btc_price_rub = get_btc_price()
        msg = 'USD: ' + str(btc_price_usd) + ' | RUB: ' + str(btc_price_rub)
        await client.send_message(message.author, msg)
  
  #<-----Moderation----->
  
@client.command(pass_context = True)
async def kick(ctx, member: discord.User):
  await client.kick(member)
  await client.delete_message(ctx.message)
  
@client.command(pass_context = True)
async def ban(ctx, member: discord.User):
  await client.ban(member)
  await client.delete_message(ctx.message)
  
  @client.command(pass_context = True)
  async def mute(ctx, member, discord.User):
    rMute = discord.utils.get(ctx.message.server.roles, name ='Muted'
    await client.add_roles(member, rMute)
  
  @client.command(pass_content=True)
async def purge(ctx, amount=10):
  channel = ctx.message.channel
  messages = []
  
  async for message in client.logs_form(channel, limit=int(amount) + 1):
    messages.append(message)
    msg_ammount += 1
    
  await client.delete_message(messages)
  await client.say('{} messages deleted.'.format(msg_ammount))
  
  #<-----Embeds----->
  
@client.command(pass_context=True)
async def help(ctx):
  author = ctx.message.author
  
  embed = discord.Embed(
    colour = discord.Colour.orange()
  )
  
  embed.set_author(name='All Commands Help')
  embed.add_field(name='!help', value='Shows you all the commands!', inline=False)
  embed.add_field(name='!ping', value='Returns Pong!', inline=False)
  embed.add_field(name='!clear <amount>', value='Clears chat messages.', inline=False)
  embed.add_field(name='!echo', value='Repeats the message you sent after the command.', inline=False)

@client.command()
async def displayembed():
  embed = discord.Embed(
    title = 'Title',
    description = 'This is a description',
    colour = discord.Colour.gold()
  )
  
  embed.set_footer(text='This is a footer')
  embed.set_image(url='https://t4.rbxcdn.com/4ad833f22d57fed3fda9e6d5c9f7b052')
  embed.set_thumbnail(url='')
  embed.add_field(name='Field Name', value='Field Value',inline=False)
  
  await client.say(embed=embed)
  
  #<-----Ending Code----->

client.loop.create_task(change_status())
client.run(TOKEN)
