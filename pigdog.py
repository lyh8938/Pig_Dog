# -*- coding:utf-8 -*- 
# 가끔가다 애가 인코딩을 잘못 읽어서 오류를 냅니다. 그것을 대비하기 위해 'utf-8'으로 읽으라고 선언합니다.

import discord, asyncio # 디스코드 모듈과, 보조 모듈인 asyncio를 불러옵니다.

token = "NjkzMDkzOTQzODg1NDMwODM1.Xn4EzQ.HHX1IQ1pT6YB44yd6oggUCQnN2Q" # 아까 메모해 둔 토큰을 입력합니다
client = discord.Client() # discord.Client() 같은 긴 단어 대신 client를 사용하겠다는 선언입니다.

@client.event
async def on_ready(): # 봇이 준비가 되면 1회 실행되는 부분입니다.
  # 봇이 "반갑습니다"를 플레이 하게 됩니다.
  # 눈치 채셨을지 모르곘지만, discord.Status.online에서 online을 dnd로 바꾸면 "다른 용무 중", idle로 바꾸면 "자리 비움"으로 바뀝니다.
  await client.change_presence(status=discord.Status.online, activity=discord.Game("열심히 일"))
  print("저는 준비되었습니다.!") # I'm Ready! 문구를 출력합니다.
  print(client.user.name) # 봇의 이름을 출력합니다.
  print(client.user.id) # 봇의 Discord 고유 ID를 출력합니다.
  
@client.event
async def on_message(message): # 메시지가 들어 올 때마다 가동되는 구문입니다.
  if message.author.bot: # 채팅을 친 사람이 봇일 경우
    return None # 반응하지 않고 구문을 종료합니다.
  
  if message.content == "!명령어": 
    embed = discord.Embed(title="명령어 도움말", description=" ", color=0xFFE400) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
    embed.add_field(name="**방송 관련**", value="`!방송` `!방송국` `!유튜브`", inline=False)
    embed.add_field(name="**마인크래프트 관련**", value="`!마크시참`", inline=False)
    embed.add_field(name="**시참 관련**", value="`!내전규칙` `!내전시참`", inline=False)
    embed.add_field(name="**롤 관련**", value="`!패치노트` `!전적 <닉네임>` `!챔프 <챔프이름>` **닉네임 띄어쓰기X**", inline=False)
    embed.add_field(name="**추가중..**", value="추가중..", inline=False)
    embed.set_footer(text=" ") # 하단에 들어가는 조그마한 설명을 잡아줍니다
    await message.channel.send(" ", embed=embed) # embed와 메시지를 함께 보내고 싶으시면 이렇게 사용하시면 됩니다.


  if message.content == "!내전규칙": 
    embed = discord.Embed(title="**■■■■■■■■■■■내전규칙■■■■■■■■■■■**", description=" ", color=0xFF0000) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
    embed.add_field(name="**1 :**", value="> 내전중 도발성 **전챗 & 감정표현** 을 자제해주시기 바랍니다.", inline=False)
    embed.add_field(name="**2 :**", value="> 픽 도중 닷지는 불가합니다.** 모두가 인정하는 사유라면 허가합니다.**", inline=False)
    embed.add_field(name="**3 :**", value="> **고의적인 트롤** 또는 **자신만** 즐겁기위한 **즐겜픽** 은 하지마세요.", inline=False)
    embed.add_field(name="**4 :**", value="> 자신만의 **템트리**와 **아이템트리**는 팀원분들 **모두**가 OK하면 할수있습니다.", inline=False)
    embed.add_field(name="**5 :**", value="> 내전도중에 **탈주**할것같다면 미리 말을한후** 참여**를 하거나  **불참** 해주시기 바랍니다. ", inline=False)
    embed.add_field(name="**6 :**", value="> 내전 참여는 유튜브 **구독**과 방송 **추천&즐찾** 은 **필수** 입니다.", inline=False)
    embed.set_footer(text=" ") # 하단에 들어가는 조그마한 설명을 잡아줍니다
    await message.channel.send(" ", embed=embed) # embed와 메시지를 함께 보내고 싶으시면 이렇게 사용하시면 됩니다.


  if message.content == "!내전시참": 
    embed = discord.Embed(title="**■■■■■■■■■■■내전시참■■■■■■■■■■■**", description=" ", color=0xABF200) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
    embed.add_field(name="**1 :**", value="> 리그 오브 레전드    >    사용자 설정 참여하기", inline=False)
    embed.add_field(name="**2 :**", value="> 방제는 방송에서 확인", inline=False)
    embed.add_field(name="**3 :**", value="> 비번은 퀴즈를 풀어서 들어오면 된다!", inline=False)
    embed.add_field(name="**4 :**", value="> 하이패스를 하려면 별풍 5개를 하면된다", inline=False)
    embed.add_field(name="**5 :**", value="> 내전 참여는 유튜브 **구독**과 방송 **추천&즐찾** 은 **필수** 입니다.", inline=False)
    embed.set_footer(text=" ") # 하단에 들어가는 조그마한 설명을 잡아줍니다
    await message.channel.send(" ", embed=embed) # embed와 메시지를 함께 보내고 싶으시면 이렇게 사용하시면 됩니다.


  if message.content == "!마크시참": 
    embed = discord.Embed(title="**■■■■■■■■■■■마인크래프트■■■■■■■■■■■**", description=" ", color=0xBDBDBD) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
    embed.add_field(name="**서버주소 :**", value="> 돼지.서버.한국", inline=False)
    embed.add_field(name="**모드다운방법 :**", value="> http://bj.afreecatv.com/dmsdydcjs/post/54354650", inline=False)
    embed.set_footer(text=" ") # 하단에 들어가는 조그마한 설명을 잡아줍니다
    await message.channel.send(" ", embed=embed) # embed와 메시지를 함께 보내고 싶으시면 이렇게 사용하시면 됩니다.


  if message.content.endswith("!방송"):
      await message.channel.send("http://play.afreecatv.com/dmsdydcjs/null")

  if message.content.endswith("!방송국"):
      await message.channel.send("http://bj.afreecatv.com/dmsdydcjs")

  if message.content.endswith("!유튜브"):
      await message.channel.send("https://www.youtube.com/channel/UCIU8xJviKOiq4XlJ8mHC0FQ")

  if message.content.endswith("!패치노트"):
      await message.channel.send("https://kr.leagueoflegends.com/ko-kr/news/game-updates/")

  if message.content.startswith("!전적"):
      msg = message.content[4:]
      print(msg)
      msg1 = "https://www.op.gg/summoner/userName="
      msg2 = msg1+msg
      await message.channel.send(msg2)

  if message.content.startswith("!챔프"):
      msg = message.content[4:]
      print(msg)
      msg1 = "https://www.op.gg/champion/"
      msg3 = "/statistics"

      msg2 = msg1+msg+msg3
      await message.channel.send(msg2)


    
client.run(token) # 아까 넣어놓은 토큰 가져다가 봇을 실행하라는 부분입니다. 이 코드 없으면 구문이 아무리 완벽해도 실행되지 않습니다.