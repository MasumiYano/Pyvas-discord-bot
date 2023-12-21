# Importing from same package
from .command import Command
from .utils import user_id_already_exist

# Importing from outer package
from bot.json_handler import JsonHandler


class SubStudentCommand(Command):
    async def execute(self, user_id, discord_id):
        if JsonHandler.is_student_exists(user_id):
            return user_id_already_exist(user_id)
        JsonHandler.write_new_user_id(user_id, discord_id)
        return f'User {user_id} is now subscribed!!'
