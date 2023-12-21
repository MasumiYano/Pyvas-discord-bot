# from config import TOKEN
import discord
from .handlers import handle_message


async def send_message(message, user_message, is_private, user_id):
    try:
        # response = await handle_message(message, user_message)
        # await message.author.send(response) if is_private else await message.channel.send(response)
        response = await handle_message(message, user_message, user_id)

        if isinstance(response, dict) and 'title' in response:
            embed = discord.Embed(
                title=response['title'],
                description=response.get('description', ""),
                color=response.get("color", 0x00ff00)
            )
            for field in response.get("fields", []):
                embed.add_field(name=field['name'], value=field['value'], inline=field.get('inline', False))
            await message.channel.send(embed=embed)
        else:
            await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print("Error occurred")
        print(e)


class DiscordClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} is now running!')

    async def on_message(self, message):
        if message.author == self.user:
            return
        user_id = message.author.id
        await send_message(message, message.content, False, user_id)
