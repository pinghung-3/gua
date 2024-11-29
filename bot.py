# test 登錄
import discord
import time
from discord.ext import commands, tasks
from discord import app_commands

TOK = "MTMwMjYxNDcwNjk2MzM0OTUxNA.GeqIBk.Xuol8O_Y8VSVF724B-vQIcuePQxNdCAvC-fh4w"
# client是跟discord連接，intents是要求機器人的權限
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!",
                   intents=intents,
                   application_id="1302614706963349514")


@bot.event
async def on_ready():
    slash = await bot.tree.sync()
    print(f"目前登入身份 --> {bot.user}")
    print(f"載入 {len(slash)} 個斜線指令")


@tasks.loop(minutes=5)  # 每 5 分鐘檢查一次
async def check_connection():
    if bot.is_closed():  # 如果機器人掉線
        await bot.start("YOUR_BOT_TOKEN")  # 使用 Token 重啟機器人


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    text = message.content
    author_id = message.author.id
    if ("范翔皓" in text):
        await message.channel.send("<@" + str(author_id) + "> 你是范翔皓")
        await message.channel.send("<@" + str(author_id) + "> 你是范翔皓")
        await message.channel.send("<@" + str(author_id) + "> 你是范翔皓")
        await message.add_reaction("<:you:1302605122815393862>")
    print("from: " + message.author.name + "  message: " + text)

'''
@bot.event
async def on_reaction_add(reaction, user):
    # 確保是來自特定消息並且有勾勾符號 (✅)
    if reaction.message.id == TARGET_MESSAGE_ID and reaction.emoji == "✅":
        # 取得伺服器
        guild = reaction.message.guild
        # 找到身分組
        role = discord.utils.get(guild.roles, name=ROLE_NAME)
        if role:
            # 給予用戶身分組
            member = guild.get_member(user.id)
            if member:
                await member.add_roles(role)
                print(f"Added {role.name} to {user.name}")
            else:
                print(f"User {user.name} not found!")
        else:
            print(f"Role {ROLE_NAME} not found!")

'''
@bot.tree.command(name='改名稱', description="改名稱")
@app_commands.describe(member="要改誰", nickname="要改成甚麼")
async def message_bomb(interaction: discord.Interaction, member: discord.User,
                       nickname: str):
    try:
        # 更改成員暱稱
        if (member.name != "hung100liu"):
            await member.edit(nick=nickname)
            await interaction.response.send_message(
                f"{member.display_name} 的暱稱已更改為 {nickname}！")
        else:
            await interaction.response.send_message(f"你不能改 o((>ω< ))o")
    except discord.Forbidden:
        await interaction.response.send_message("我沒有權限更改此成員的暱稱。")
    except:
        await interaction.response.send_message("更改暱稱時發生錯誤。")

'''
@bot.tree.command(name='身分組', description="加身分組",)
@app_commands.describe(message="訊息",name="身分組名稱")
async def rename(interaction: discord.Interaction, message:str, name:str):
    TARGET_MESSAGE_ID = 
'''
bot.run(TOK)
'''
'''
