import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = '-')

await client.change_presence(status=discord.Status.online)  # 온라인
# await client.change_presence(status=discord.Status.idle) #자리비움
# await client.change_presence(status=discord.Status.dnd) #다른용무
# await client.change_presence(status=discord.Status.offline) #오프라인

await client.change_presence(activity=discord.Game(name="게임 하는중"))
# await client.change_presence(activity=discord.Streaming(name="스트림 방송중", url='링크'))
# await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="노래 듣는중"))
# await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="영상 시청중"))

print("봇 이름:", client.user.name, "봇 아이디:", client.user.id, "봇 버전:", discord.__version__)

# 디스코드에는 현재 본인이 어떤 게임을 플레이하는지 보여주는 기능이 있습니다.
# 이 기능을 사용하여 봇의 상태를 간단하게 출력해줄 수 있습니다.


# 봇이 새로운 메시지를 수신했을때 동작되는 코드입니다.
@client.event
async def on_message(message):
    if message.author.bot:  # 만약 메시지를 보낸사람이 봇일 경우에는
        return None  # 동작하지 않고 무시합니다.

    id = message.author.id  # id라는 변수에는 메시지를 보낸사람의 ID를 담습니다.
    channel = message.channel  # channel이라는 변수에는 메시지를 받은 채널의 ID를 담습니다.

    if message.content == "!명령어":
        embed = discord.Embed(title="!명령어", description="아래의 명령어를 입력해보세요", color=0xff0000)
        embed.add_field(name="!행운", value="행운을 올려보세요", inline=False)
        embed.add_field(name="!가이드북", value="가이드북 주소를 올려드려요", inline=False)
        embed.add_field(name="!패치파일", value="두번째 패치파일 주소를 올려드려요", inline=False)
        embed.add_field(name="!천사날개 조합식", value="천사날개 조합식을 알려드려요", inline=False)
        embed.add_field(name="!알파윙 조합식", value="알파 윙 조합식을 알려드려요", inline=False)
        embed.add_field(name="!진알파 조합식", value="眞-알파 윙 조합식을 알려드려요", inline=False)
        embed.add_field(name="!케루빔 조합식", value="케루빔의 수호 날개 조합식을 알려드려요", inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith('!행운'):
        channel = message.channel
        await channel.send('오늘은 좋은걸 얻을거 같은 기분이예요!!')

    if message.content.startswith('!가이드북'):
        channel = message.channel
        await channel.send("https://cafe.naver.com/twguide/2?boardType=L")

    if message.content.startswith('!패치파일'):
       channel = message.channel
       await channel.send("https://drive.google.com/file/d/1eq2UkT6M_-imjFikJ6RRP72XFUy3kw5n/view?usp=sharing")

    if message.content.startswith('!알파윙 조합식'):
        channel = message.channel
        await channel.send("리틀 그레스 윙 3합\n에메랄드 20개\n천공의 깃털 20개")

    if message.content.startswith('!천사날개 조합식'):
        channel = message.channel
        await channel.send("리틀 플라티나 윙 3합\n에메랄드 20개\n천공의 깃털 20개")

    if message.content.startswith('!진알파 조합식'):
        channel = message.channel
        await channel.send("알파 윙 3합 1개\n흑해진보 40개\n쿠로이 깃털 1개")

    if message.content.startswith('!케루빔 조합식'):
         channel = message.channel
         await channel.send("천사날개 3합 1개\n흑해진보 40개\n쿠로이 깃털 1개")

    @app.command(name="청소", pass_context=True)
    async def _clear(ctx, *, amount=5):
        await ctx.channel.purge(limit=amount)

    # 서버에 멤버가 들어왔을 때 수행 될 이벤트
    async def on_member_join(self, member):
        channel = client.get_channel(808342847748440084)
        msg = "<@{}>님이 서버에 들어오셨어요. 환영합니다.".format(str(member.id))
        await find_first_channel(member.guild.text_channels).send(msg)
        return None

    # 사버에 멤버가 나갔을 때 수행 될 이벤트
    async def on_member_remove(self, member):
        channel = client.get_channel(808342847748440084)
        msg = "<@{}>님이 서버에서 나가거나 추방되었습니다.".format(str(member.id))
        await find_first_channel(member.guild.text_channels).send(msg)
        return None

    # 봇에 메시지가 오면 수행 될 액+션
    async def on_message(self, message):
        if message.author.bot:
            return None


client.run(os.environ['token'])
