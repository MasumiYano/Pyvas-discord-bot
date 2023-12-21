from .command import Command
from canvas_api.client import CanvasAPIClient
from .utils import (user_id_not_recognized, discord_id_not_recognized)
from bot.json_handler import JsonHandler


class ShowCourseNowCommand(Command):
    async def execute(self, discord_id):
        user_id = JsonHandler.get_user_id(discord_id)
        if not JsonHandler.is_student_exists(user_id):
            return user_id_not_recognized()
        if not JsonHandler.does_disc_id_match(user_id, discord_id):
            return discord_id_not_recognized()

        response = CanvasAPIClient(user_id)

        return await response.get_course_current()
