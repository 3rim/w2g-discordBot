import discord
import requests
# config file with API_KEYS
import config

intents = discord.Intents.all()
# needed for message.content
intents.message_content = True
# you need your own w2g API_KEY ;)
watch2gether_API_KEY = config.W2G_API_KEY


class MyClient(discord.Client):
    # login
    async def on_ready(self):
        print(f"Bot {self.user} logged peep bop")

    # read messages
    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        if message.author == client.user:
            return

        if message.content.startswith('$watch'):
            link = create_w2gether()
            await message.channel.send(link)


def create_w2gether():
    url = 'https://api.w2g.tv/rooms/create.json'
    payload = {
        "w2g_api_key": watch2gether_API_KEY,
        "share": "https://www.youtube.com/watch?v=u2qyVsUrNN8",
        "bg_color": "#000000",
        "bg_opacity": "50"
    }
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    r = requests.post(url, json=payload, headers=headers)
    print(r.json())
    json_response = r.json()

    link = ": Here is your room! \n https://w2g.tv/rooms/" + json_response['streamkey']
    return link


client = MyClient(intents=intents)
# you need your own discord bot API_KEY ;)
client.run(config.DISCOR_BOT_KEY)
