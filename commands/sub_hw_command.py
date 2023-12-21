# Importing form same package
from .command import Command
from .utils import (user_id_not_recognized,
                    course_not_recognized,
                    assignment_already_exist,
                    discord_id_not_recognized)

# Importing from outer package
from bot.json_handler import JsonHandler


class SubHWCommand(Command):
    async def execute(self, course_name, hw_name, hw_id, discord_id):
        user_id = JsonHandler.get_user_id(discord_id)
        if not JsonHandler.is_student_exists(user_id):
            return user_id_not_recognized()
        if not JsonHandler.does_disc_id_match(user_id, discord_id):
            return discord_id_not_recognized()
        if not JsonHandler.is_course_exists(user_id, course_name):
            return course_not_recognized()
        if JsonHandler.is_assignment_exists(user_id, course_name, hw_name):
            return assignment_already_exist(hw_name)

        JsonHandler.write_new_assignment(user_id, course_name, hw_name, hw_id)
        return f"Assignment {hw_name} with ID {hw_id} subscribed successfully for {user_id}"
