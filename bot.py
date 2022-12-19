import discord
import asyncio
import os
from discord.ext import commands

TOKEN = os.environ['TOKEN']
FREFIX = os.environ['FREFIX']

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!", intents=intents)
client = discord.Client(intents=intents)


# 봇이 구동되었을 때 동작되는 코드
@client.event
async def on_ready():
    print("로그인 된 봇:")  # 화면에 봇의 아이디, 닉네임이 출력되는 코드
    print(client.user.name)
    print(client.user.id)
    print("===========")


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online)
    game = discord.Game("시작하는 중...")
    await client.change_presence(status=discord.Status.online, activity=game)
    while True:
        game = discord.Game("난 뚜뚜킹이야!!")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(3)

# 디스코드에는 현재 본인이 어떤 게임을 플레이하는지 보여주는 기능이 있습니다.
# 이 기능을 사용하여 봇의 상태를 간단하게 출력해줄 수 있습니다.

    @bot.event
    async def on_member_join(member):
        channel = bot.get_channel(808342847748440084)
        await channel.send(f"{member} 님이 서버에 오셨어요.")

    @bot.event
    async def on_member_remove(member):
        channel = bot.get_channel(808342847748440084)
        await channel.send(f"{member} 님이 서버에서 나가셨어요.")

# 봇이 새로운 메시지를 수신했을때 동작되는 코드입니다.
@client.event
async def on_message(message):
    if message.author.bot:  # 만약 메시지를 보낸사람이 봇일 경우에는
        return None  # 동작하지 않고 무시합니다.

    id = message.author.id  # id라는 변수에는 메시지를 보낸사람의 ID를 담습니다.
    channel = message.channel  # channel이라는 변수에는 메시지를 받은 채널의 ID를 담습니다.

    if message.content == "!명령어":
        embed = discord.Embed(title="!명령어", description="아래의 명령어를 입력해보세요!", color=0xff0000)
        embed.add_field(name="!행운", value="행운을 올려보세요", inline=False)
        embed.add_field(name="!가이드북", value="가이드북 주소를 알려드려요!", inline=False)
        embed.add_field(name="!패치파일", value="패치파일 주소를 알려드려요!", inline=False)
        embed.add_field(name="!천사날개 조합식", value="천사날개 조합식을 알려드려요!", inline=False)
        embed.add_field(name="!알파윙 조합식", value="알파 윙 조합식을 알려드려요!", inline=False)
        embed.add_field(name="!진알파 조합식", value="眞-알파 윙 조합식을 알려드려요!", inline=False)
        embed.add_field(name="!케루빔 조합식", value="케루빔의 수호 날개 조합식을 알려드려요!", inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith('!행운'):
        channel = message.channel
        await channel.send(message.author.name +'님 오늘은 좋은걸 얻을거 같아요!!')

    if message.content.startswith('!가이드북'):
        channel = message.channel
        await channel.send("https://cafe.naver.com/twguide/2?boardType=L")

    if message.content.startswith('!패치파일'):
       channel = message.channel
       await channel.send("https://drive.google.com/file/d/1wN9usx5rJm0fIXcba2cXDIyJMqrjFFib/view?usp=sharing")

    if message.content.startswith('!알파윙 조합식'):
        channel = message.channel
        await channel.send("```리틀 그레스 윙 3합\n에메랄드 20개\n천공의 깃털 20개```")

    if message.content.startswith('!천사날개 조합식'):
        channel = message.channel
        await channel.send("```리틀 플라티나 윙 3합\n에메랄드 20개\n천공의 깃털 20개```")

    if message.content.startswith('!진알파 조합식'):
        channel = message.channel
        await channel.send("```알파 윙 3합 1개\n흑해진보 40개\n쿠로이 깃털 1개```")

    if message.content.startswith('!케루빔 조합식'):
         channel = message.channel
         await channel.send("```천사날개 3합 1개\n흑해진보 40개\n쿠로이 깃털 1개```")
      
client.run(TOKEN)
