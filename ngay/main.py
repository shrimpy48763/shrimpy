import os
import discord
import asyncio
from discord.ext import commands
from keep_alive import keep_alive
keep_alive()

bot = Bot(token=os.environ.get('token'))

token = os.getenv("NGAY_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='',intents=intents)

@bot.command()
async def 自我介紹(ctx):
    await ctx.send('I’m ngay 你係唔係想認識我 我有180 但我患有侏儒症 有腹肌 青澀害羞小男孩 私生活乾淨 熱愛提供資金援助 簡稱ATM 但擁有色盲了看不到這個有顏色美麗的世界 你…願…意…成為我眼中的色彩…嗎…')

@bot.command()
async def 個人信息(ctx):
    await ctx.send('這是我的個人信息 姓名:NGAY 身高:180 是個侏儒 體重:48763公斤 但我有厭食症 愛玩:candy crush 退坑原因:我有色盲 性別：認為自己是雙性人 有吸引力的直升機 只穿著內褲在街上奔跑 但沒有雞雞 我的性取向:內部性別的女人是郵件與一條大d也是ALIEN CUM 銀行號碼:603-114-514')

@bot.command()
async def 個人信息eng(ctx):
    await ctx.send('Hello, I am ngay like playing candy crush but I’m color blindness I just got cheated on by my girlfriend💔💔💔I am in urgent need of $48763 so I NEED UR HELP to pick up a new girl CUZ I’M A FUCKBOY Now as long as you v me 48763 when I pick up a new girlfriend  I will run away directly and be ungrateful and also add u to my backup list of girlfriends this is my bank number: 603-114-514 Remember to tell me after entering the number here my information name : NGAY hobbies: candy crush height : 180 but a dwarf weight : 48763kg but I have anorexia gender : i identify as intersex attractive helicopter who only wears underwear run on the street but with no d my sexual orientation : woman of internal gender is mail with a big MALE D ALSO ALIEN CXM')

@bot.command()
async def fuck(ctx):
    await ctx.send('嗯 我也想被fuck')

@bot.command()
async def FUCK(ctx):
    await ctx.send('嗯 我也想被fuck')

@bot.command()
async def kondo(ctx):
    await ctx.send('# Kondo is my waifu')


@bot.command()
async def ivy(ctx):
     await ctx.send('# 我老婆')

@bot.command()
async def  內部郵件(ctx):
    await ctx.send('# 還分手嗎？還分手嗎？說話說話說話說話說話說話說話說話說話 嗯？我愛你一輩子')

@bot.command()
async def 寶貝怎麼出牢房了(ctx):
    await ctx.send('對不起主人～我再也不敢了')

@bot.command() 
async def 滾出來(ctx):
    await ctx.send('嗯～好的主人')

@bot.command()
async def 滾回去(ctx):
    await ctx.send('嗯～好的主人')

@bot.command()
async def 操你媽(ctx):
    await ctx.send('嗯～好的主人操你媽操你媽操你媽操你媽操你媽操你媽操你媽操你媽操你媽操你媽操你媽操你媽操你媽操你媽操你媽操你媽操你媽操你媽操你媽操你媽操你媽操你媽操你媽操你媽操你媽操你媽操你媽操你媽操你媽操你媽操你媽操你媽操你操你媽操你媽操你媽操你媽操你媽操你媽操你媽操你媽操你媽操你媽操你媽操你媽操你媽操你媽操你媽操你媽操你媽操你操你媽操你媽操你媽操你媽操你媽操你媽操你媽操你媽操你媽操你媽操你媽操你媽操你媽操你媽操你媽操你媽 操我')

@bot.command()
async def RAP(ctx):
    await ctx.send('ＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰＲＡＰ')

@bot.command()
async def wat(ctx):
    await ctx.send('watsons')

@bot.command()
async def 藍色真皆(ctx):
    await ctx.send('可惜我的眼睛已經看不到這麼美麗的顏色了...')

@bot.command()
async def 好的總裁(ctx):
    await ctx.send('NGAY你的小秘書一枚呀～')

@bot.command()
async def 好的種菜(ctx):
    await ctx.send('要先種菜還是先吃我這類型的菜')

@bot.command()
async def 快v我(ctx):
    await ctx.send('你好我是ngay，我剛被女朋友飛了，我現在急需$48763來泡新的女人，現在只要你v我48763，等我泡到新女友，一定會直接跑路忘恩負義，也會把你加入我的後備女友名單，這是我的銀行號碼:603-114-514。入數後記得和我說一聲')

@bot.command()
async def 生日快樂(ctx):
    await ctx.send('今天是ngay的生日，轉發給五個群，你的果照就會自動被流出，我試過了是真的，而且還會被他背刺，但是今天真的是ngay的生日，ngay生日快樂，你信他會改過還是信我是內部郵件？你的內部郵件即將收到一個病毒GAY之毒 請謹慎點開訊息 你的性取向比較危 但是你的內部郵件彌補了這一部份 如果你去抑制一下你的戀愛腦 又會讓你的玻璃心無處安放 所以會建議你抑制之後 再做一個物理閹割手術')

bot.run(token)
