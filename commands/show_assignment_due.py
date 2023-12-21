# Importing from same package
from .command import Command
from .utils import (user_id_not_recognized,
                    discord_id_not_recognized,
                    course_not_recognized,
                    assignment_not_recognized)

# Importing from outer package
from bot.json_handler import JsonHandler
from canvas_api.client import CanvasAPIClient


class ShowAssignmentDue(Command):
    async def execute(self, course_name: str, hw_name: str, discord_id):
        user_id = JsonHandler.get_user_id(discord_id)
        if not JsonHandler.is_student_exists(user_id):
            return user_id_not_recognized()
        if not JsonHandler.does_disc_id_match(user_id, inc_discord_id=discord_id):
            return discord_id_not_recognized()
        if not JsonHandler.is_course_exists(user_id, course_name):
            return course_not_recognized()
        if not JsonHandler.is_assignment_exists(user_id, course_name, hw_name):
            return assignment_not_recognized()

        canvas = CanvasAPIClient(user_id)

        return await canvas.assignment_due_dates(course_name, hw_name)
