import discord


class MyClient(discord.Client):
    #Einloggen
    async def on_ready(self):
        print("Ich habe mich ")

    #Wenn Nachricht gepostet wird
    async def on_message(self, message):
        print("Nachricht von " + message.author + " enthalt " + message.content)
client = MyClient()
client.run()