import discord
import requests
import json
import os

def get_meme():
  response = requests.get('https://meme-api.com/gimme')
  json_data = json.loads(response.text)
  return json_data['url']

def get_gay_meme():
  response = requests.get('https://meme-api.com/gimme/gaymemesforgayppl')
  json_data = json.loads(response.text)
  return json_data['url']

class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))
  async def on_message(self, message):
    if message.author == self.user:
      return

    if message.content.startswith('$meme'):
      await message.channel.send(get_meme())
    
    if message.content.startswith('$gaymeme'):
      await message.channel.send(get_gay_meme())

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.getenv("DISCORD_BOT_TOKEN")) # Replace with your own token.