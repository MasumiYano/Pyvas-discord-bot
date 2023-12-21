from config import TOKEN
from discord_client.client import DiscordClient
import discord


def run_discord_bot():
    intents = discord.Intents.default()
    intents.message_content = True

    client = DiscordClient(intents=intents)
    client.run(TOKEN)


if __name__ == "__main__":
    run_discord_bot()
