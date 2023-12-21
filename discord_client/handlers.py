from commands.command_processor import CommandProcessor


async def handle_message(message, user_message, user_id):
    if message.content.startswith('$'):
        response = await CommandProcessor.process(user_message, user_id)
        return response
