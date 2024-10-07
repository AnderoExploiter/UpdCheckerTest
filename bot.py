import discord
from discord.ext import commands
import random
import asyncio

TOKEN = ""

# Create Intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.voice_states = True  # Required to track voice state changes

# Initialize bot with intents
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="On Developing"))
    print(f'Bot is ready as {bot.user}')

@bot.command()
@commands.has_permissions(manage_roles=True)
async def mute_voice(ctx, member: discord.Member, *, reason=None):
    """Mutes a member in a voice channel."""
    if member.voice:
        await member.edit(mute=True, reason=reason)
        await ctx.send(f'{member.mention} has been muted in voice channel. Reason: {reason}')
    else:
        await ctx.send(f'{member.mention} is not in a voice channel.')

@bot.command()
@commands.has_permissions(manage_roles=True)
async def unmute_voice(ctx, member: discord.Member, *, reason=None):
    """Unmutes a member in a voice channel."""
    if member.voice:
        await member.edit(mute=False, reason=reason)
        await ctx.send(f'{member.mention} has been unmuted in voice channel. Reason: {reason}')
    else:
        await ctx.send(f'{member.mention} is not in a voice channel.')

@bot.command()
@commands.has_permissions(manage_guild=True)  # Проверка на наличие разрешений
async def set_status(ctx, *, status: str):
    """Устанавливает статус бота."""
    await bot.change_presence(activity=discord.Game(name=status))
    await ctx.send(f'Статус бота изменен на: {status}')


@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member.mention} has been banned. Reason: {reason}')

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member.mention} has been kicked. Reason: {reason}')

@bot.command()
@commands.has_permissions(manage_roles=True)
async def mute(ctx, member: discord.Member, duration: int, *, reason=None):
    guild = ctx.guild
    mute_role = discord.utils.get(guild.roles, name="Muted")

    if not mute_role:
        mute_role = await guild.create_role(name="Muted")
        for channel in guild.channels:
            await channel.set_permissions(mute_role, speak=False, send_messages=False)

    await member.add_roles(mute_role, reason=reason)
    await ctx.send(f'{member.mention} has been muted for {duration} seconds. Reason: {reason}')

    await asyncio.sleep(duration)
    await member.remove_roles(mute_role)
    await ctx.send(f'{member.mention} has been unmuted.')

@bot.command()
async def createchannel(ctx, channel_name: str, duration: int):
    guild = ctx.guild
    channel = await guild.create_text_channel(channel_name)

    await ctx.send(f'Channel {channel.mention} created for {duration} seconds.')

    await asyncio.sleep(duration)

    await channel.delete()
    await ctx.send(f'Channel {channel.mention} has been deleted.')

@bot.command()
async def pm(ctx, member: discord.Member, *, message: str):
    await member.send(message)

@bot.command()
async def pingo(ctx):
    await ctx.send('Pongo!')

@bot.command()
async def info(ctx):
    embed = discord.Embed(
        title="Info",
        description="This is description",
        color=discord.Color.blue()
    )
    embed.add_field(name="Fact 1", value="I'm created by Tim", inline=False)
    embed.add_field(name="Fact 2", value="I'm running on Replit", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def ping(ctx):
    members = ctx.guild.members
    members = [member for member in members if not member.bot]

    if members:
        random_member = random.choice(members)
        await ctx.send(f'Pinging {random_member.mention}!')
    else:
        await ctx.send('There are no members to ping.')

@bot.command()
async def ping5(ctx):
    members = ctx.guild.members
    members = [member for member in members if not member.bot]

    if members:
        for _ in range(5):
            random_member = random.choice(members)
            await ctx.send(f'Pinging {random_member.mention}!')
    else:
        await ctx.send('There are no members to ping.')

@bot.command()
async def банан(ctx):
    await ctx.send('🍌')

@bot.command()
async def огурец(ctx):
    await ctx.send('🥒')

@bot.command()
async def томат(ctx):
    await ctx.send('🍅')

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx):
    deleted = await ctx.channel.purge()
    await ctx.send(f'Deleted {len(deleted)} messages.', delete_after=5)

@bot.command()
async def developers(ctx):
    """Displays the list of developers of the bot."""
    embed = discord.Embed(
        title="Bot Developers",
        description="Here are the developers of this bot:",
        color=discord.Color.blue()
    )

    # List of developers
    developers_list = [
        "Tim - [Discord Profile](https://discord.com/users/1223228213040386220)",  # Replace with actual Discord profile link
        "SrFox - [Discord Profile](https://discord.com/users/1131022025843023882)",  # Replace with actual Discord profile link
    ]

    # Adding each developer to the embed
    for developer in developers_list:
        embed.add_field(name="Developer", value=developer, inline=False)

    await ctx.send(embed=embed)


@bot.command()
async def cmds(ctx):
    embed = discord.Embed(
        title="Command List",
        description="Here are the available commands:",
        color=discord.Color.green()
    )
    embed.add_field(name="!createchannel <name> <time>", value="Creates a temporary channel.", inline=False)
    embed.add_field(name="!pingo", value="Replies with 'Pongo!'", inline=False)
    embed.add_field(name="!info", value="Shows bot information.", inline=False)
    embed.add_field(name="!ping", value="Pings a random member.", inline=False)
    embed.add_field(name="!ping5", value="Pings 5 random members.", inline=False)
    embed.add_field(name="!банан", value="Sends banana emoji.", inline=False)
    embed.add_field(name="!огурец", value="Sends cucumber emoji.", inline=False)
    embed.add_field(name="!томат", value="Sends tomato emoji.", inline=False)
    embed.add_field(name="!clear", value="Clears all messages in the channel.", inline=False)
    embed.add_field(name="!pm <user> <message>", value="Pings a user and sends them a message.", inline=False)
    embed.add_field(name="!ban <user> <reason>", value="Bans a user.", inline=False)
    embed.add_field(name="!kick <user> <reason>", value="Kicks a user.", inline=False)
    embed.add_field(name="!mute_voice <user> <reason>", value="Mutes a user in a voice channel.", inline=False)
    embed.add_field(name="!unmute_voice <user> <reason>", value="Unmutes a user in a voice channel.", inline=False)
    embed.add_field(name="!mute <user> <duration> <reason>", value="Mutes a user.", inline=False)
    embed.add_field(name="!developers", value="Showing developer of this bot", inline=False)

    await ctx.send(embed=embed)

# Run the bot
bot.run(TOKEN)
