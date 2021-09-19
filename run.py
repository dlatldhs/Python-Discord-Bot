TOKEN="디스코드 토큰"#디스코드 토큰(고유 값 번호)
api_key ="롤 api key code" #leauge of legends api input key 
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib import parse
import requests
import json 
import asyncio
import discord
from discord.ext import commands
from requests.models import Response
client=discord.Client() #코드를 줄이기 위해서 Client에 discord.Client를 넣어줌
@client.event #event 함수 
async def on_ready(): # if(bot==online) excute
    print(f'{client.user} online') 
    print(f'{client.user} 정상작동ing') 
    await client.change_presence(status=discord.Status.online,activity=discord.Game("League of legends")) #디스코드밑에 하고 있는거 표시해줌

@client.event #메세지 수정하면 알려주는 명령어들
async def on_message_edit(before,after):
    await before.channel.send(str(before.author)+"님이\n"+ before.content + "에서➜"+ after.content+"로 메세지를 수정하였습니다.")
    return

@client.event #메세지 삭제되면 감지하여 삭제된 메세지를 알려주는 것
async def on_message_delete(message):
    await message.channel.send("메세지 삭제 감지("+str(message.author)+"):"+message.content)
    return

@client.event#event 함수 
async def on_message(message): # discord message storage
    if message.author == client.user: 
        return 
    if message.content.startswith('ㅎㅇ'):
       await message.channel.send('반갑고')
    #if message.content.startswith("!대회"):
        #print(message.reply(bsObject.head.find("span",{"class":"filter_label__2fEDe"})))
    if message.content.startswith('!cham'):
       await message.channel.send('제작중')#weeeb crwoling 
       #input('검색하고 싶은 챔피언 이름 입력')
       #url = 'https://www.op.gg/champion/'+talon+'/statistics/mid/build'
       #print("크롤링이 성공적일 때 나오는 메세지")

    if message.content.startswith('917 몇살이냐?'):
       await message.channel.send('니 뱃살 ㅋ')

    if message.content.startswith('!player'):#leaguge of legends 전적검색 기능 구현 하기 
            Name = message.content[7:len(message.content)]
            Final_Name = Name.replace(" ","+")#입력 받을 때 공백이면 +로 인식해서 데이터 찾기
            URL = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/"+Final_Name
            res = requests.get(URL, headers ={"X-Riot-Token":api_key})
            if res.status_code == 200:#value == 200 이름이 있을 경우
                resobj = json.loads(res.text)
                URL = "https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/"+resobj["id"]
                res = requests.get(URL, headers={"X-Riot-Token": api_key})
                rankinfo = json.loads(res.text)#embed=discord.Embed(title=("소환사 이름: "+Final_Name)) 추가로 디스코드에 소환사 이름 넣고 싶을때
                for i in rankinfo:
                    if i["queueType"] == "RANKED_SOLO_5x5":
                        embed=discord.Embed(title=("솔로랭크"))
                        embed.set_footer(text=(f'티어: {i["tier"]} {i["rank"]}'+f'승: {i["wins"]}판, 패: {i["losses"]}판'))
                    else:
                        embed=discord.Embed(title=("자유랭크"))
                        embed.set_footer(text=(f'티어: {i["tier"]} {i["rank"]}'+f'승: {i["wins"]}판, 패: {i["losses"]}판'))
                    await message.channel.send(embed=embed)
            else:#value<200 이름이 없는 경우
                embed=discord.Embed(title="소환사가 이 세상에 존재하지 않습니다.")
                await message.channel.send(embed=embed)
client.run(TOKEN)
# web 웹 크롤링 기본 틀
#html = urlopen("https://game.naver.com/esports/schedule/lck") # 웹 크롤링 할 사이트
#bsObject = BeautifulSoup(html,"html.parser")
#print(bsObject.head.find("div",{"class":"champion-index-table__name"})) #웹 문서 전체가 출력됩니다.
#await message.reply 디스코드에 변수를 출력해주는 문법
#embed.set_footer(text="자유랭크:"+f'티어: {i["tier"]} {i["rank"]}'+f'승: {i["wins"]}판, 패: {i["losses"]}판')