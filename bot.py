import discord

#  파일 r 모드로 열기
f = open('token.txt', 'r')

# readline() 함수 이용해서 한 라인씩 읽어오기
token = f.readline()
# print(token)


intents = discord.Intents.default()
bot = discord.Client(intents=intents)


@bot.event
async def on_ready():  # 봇 실행 시 실행되는 함수
    print(f'{bot.user} 에 로그인하였습니다!')


@bot.event
async def on_message(message):  # 채팅창에 메시지 입력시 실행되는 함수
    # 입력되는 메시지가
    # !hello 이면 안녕하세요라고 반응하고
    # !bye가 입력되는 잘가요라고 반응합니다.

    if message.content.startswith('!hello'):
        await message.channel.send('안녕하세요!')

    if message.content.startswith('!bye'):
        await message.reply('잘가요!')


# 봇 실행
bot.run(token)