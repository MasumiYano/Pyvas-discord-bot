# Importing from same package
from .command import Command
from .utils import user_id_not_recognized, discord_id_not_recognized

# Importing from outer package
from bot.json_handler import JsonHandler
from canvas_api.client import CanvasAPIClient


class ShowCourseCommand(Command):
    async def execute(self, discord_id):
        user_id = JsonHandler.get_user_id(discord_id)
        if not JsonHandler.is_student_exists(user_id):
            return user_id_not_recognized()

        if not JsonHandler.does_disc_id_match(user_id, discord_id):
            return discord_id_not_recognized()

        canvas_client = CanvasAPIClient(user_id)

        return await canvas_client.courses()
