import discord
from discord.ext import commands
from discord.commands import SlashCommandGroup, Option
import requests
import dotenv
import os

dotenv.load_dotenv()
bot = discord.Bot()
dapi = str(os.getenv("DISCORD_TOKEN"))


@bot.slash_command(name="characters", description="Get info about Squid Game characters")
async def characters(ctx: discord.ApplicationContext, season: 
                     discord.Option(int, "Select a season", choices=["1", "2"]),
                     number: discord.Option(int, "Select a Player Number", min_value=1, max_value=456)):
    await ctx.defer()
    tru = f"{number:03}"
    url = f"https://stainlesteel.github.io/squid-game-api/s{season}/characters/{tru}.json"
    resp = requests.get(url)
    json = resp.json()
    ans = "\n".join([f"{key} : {value}" for key, value in json.items()])
    await ctx.respond(ans)
    print("Message sent! (Characters)")

@bot.slash_command(name="episodes", description="Get info about Squid Game episodes")
async def episodes(ctx: discord.ApplicationContext, season: 
                     discord.Option(int, "Select a season", choices=["1", "2", "3"]),
                     num: discord.Option(int, "Select an episode number [001, 003, 007, .etc]", max_value=9)):
        await ctx.defer()
        tru = f"{num:03}"
        if season == 3:
          season = None
          url = f"https://stainlesteel.github.io/squid-game-api/s2/episodes-s3/{tru}.json"
        else:  
          url = f"https://stainlesteel.github.io/squid-game-api/s{season}/episodes/{tru}.json"
        resp = requests.get(url)
        debug = repr(resp.text)
        jso = resp.json()
        ans = "\n".join([f"{key} : {value}" for key, value in jso.items()])
        await ctx.respond(ans)
        print("Message sent! (Episodes)")
try:
  bot.run(dapi)
  print("Works! If there is an issue, check logs and try to fix it, if you can't open an issue on GitHub.")
except discord.errors.LoginFailure:
  print("[Python3] LoginFailure. You have not set a discord api token as an env variable.")
