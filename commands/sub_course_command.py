# Importing from same pacakge
from .command import Command

# Importing from outer package
from bot.json_handler import JsonHandler
from commands.utils import (user_id_not_recognized, course_already_exist, discord_id_not_recognized)


class SubCourseCommand(Command):
    async def execute(self, course_name, course_id, discord_id):
        user_id = JsonHandler.get_user_id(discord_id)
        if not JsonHandler.is_student_exists(user_id):
            return user_id_not_recognized()
        if not JsonHandler.does_disc_id_match(user_id, discord_id):
            return discord_id_not_recognized()
        if JsonHandler.is_course_exists(user_id, course_id):
            return course_already_exist(course_id)

        JsonHandler.write_new_course(user_id, course_name, course_id)
        return f"Course {course_name} with ID {course_id} subscribed successfully!!"
