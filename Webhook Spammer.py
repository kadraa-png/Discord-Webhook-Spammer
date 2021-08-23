import discord_webhook
from discord_webhook import DiscordWebhook

a=input('Enter webhook you want to spam on:\n')
b=input('What message do you want to spam?:\n')
c=input('How many times do you want webhook to spam?:\n')
d=input('What do you want webhook to be called?:\n')
e=int(c)

for i in range(e):
    webhook = DiscordWebhook(url=a, username=d,content=b)
    ae=webhook.execute()
    print('Sent')

