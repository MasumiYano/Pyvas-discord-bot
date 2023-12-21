import json


class JsonHandler:
    FILE_PATH = "/Users/lukiee/Desktop/newDesktop/Coding/pyvas/student_info.json"

    @staticmethod
    def read_json():
        try:
            with open(JsonHandler.FILE_PATH, 'r') as file:
                return json.load(file)
        except FileNotFoundError as e:
            print(f"Error {e}")
            return {}

    @staticmethod
    def write_json(data):
        with open(JsonHandler.FILE_PATH, 'w') as file:
            json.dump(data, file, indent=2)

    @staticmethod
    def is_student_exists(user_id):
        data = JsonHandler.read_json()
        return str(user_id) in data

    @staticmethod
    def is_course_exists(user_id, course_name):
        data = JsonHandler.read_json()
        return str(user_id) in data and course_name in data[str(user_id)]

    @staticmethod
    def is_assignment_exists(user_id, course_name, assignment_name):
        data = JsonHandler.read_json()
        return (
                str(user_id) in data and
                course_name in data[str(user_id)] and
                "assignments" in data[str(user_id)][course_name] and
                assignment_name in data[str(user_id)][course_name]["assignments"]
        )

    @staticmethod
    def does_disc_id_match(user_id, inc_discord_id):
        data = JsonHandler.read_json()
        discord_id = data.get(str(user_id), {}).get("discord_id")
        return discord_id == inc_discord_id

    @staticmethod
    def get_user_id(inc_discord_id):
        data = JsonHandler.read_json()
        for user_id, user_data in data.items():
            if user_data.get("discord_id") == inc_discord_id:
                return user_id
        return None

    @staticmethod
    def get_course_id(user_id, course_name):
        data = JsonHandler.read_json()
        return data.get(str(user_id), {}).get(course_name, {}).get("id")

    @staticmethod
    def get_assignment_id(user_id, course_name, assignment_name):
        data = JsonHandler.read_json()
        return data.get(str(user_id), {}).get(course_name, {}).get("assignments", {}).get(assignment_name)

    @staticmethod
    def write_new_user_id(user_id, inc_discord_id):
        data = JsonHandler.read_json()
        if str(user_id) not in data:
            data[str(user_id)] = {"discord_id": inc_discord_id}
            JsonHandler.write_json(data)

    @staticmethod
    def write_new_course(user_id, course_name, course_id):
        data = JsonHandler.read_json()
        if str(user_id) in data:
            data[str(user_id)][course_name] = {"id": course_id, "assignments": {}}
            JsonHandler.write_json(data)

    @staticmethod
    def write_new_assignment(user_id, course_name, assignment_name, assignment_id):
        data = JsonHandler.read_json()
        if str(user_id) in data and course_name in data[str(user_id)]:
            data[str(user_id)][course_name]["assignments"][assignment_name] = assignment_id
            JsonHandler.write_json(data)
