def user_id_not_recognized() -> dict:
    user_error = {
        "title": "Error ⚠️",
        "description": "Oops, something is wrong...",
        "fields": [
            {
                "name": "User Error.",
                "value": "I didn't recognize that user id. You have to subscribe your user id first using `!substudent <user id>`. See [here link for readme.md].",
                "inline": False
            }
        ],
        "color": 0xFF0000
    }

    return user_error


def user_id_already_exist(user_id: str) -> dict:
    user_error = {
        "title": "Error ⚠️",
        "description": "Oops, something is wrong...",
        "fields": [
            {
                "name": "User Error.",
                "value": f"The {user_id} already exists in your database.",
                "inline": False
            }
        ],
        "color": 0xFF0000
    }

    return user_error


def discord_id_not_recognized() -> dict:
    password_error = {
        "title": "Error ⚠️",
        "description": "Oops, something is wrong...",
        "fields": [
            {
                "name": "Discord ID Error",
                "value": "You do not exist in my database. Make sure to subscribe you first!",
                "inline": False
            }
        ],
        "color": 0xff0000
    }

    return password_error


def course_not_recognized() -> dict:
    course_error = {
        "title": "Error ⚠️",
        "description": "Oops, something is wrong...",
        "fields": [
            {
                "name": "Course ID Error",
                "value": "I didn't recognize that course. Please subscribe your course id first using `!subcourse <course_name> <course_id>.`",
                "inline": False
            }
        ],
        "color": 0xff0000
    }

    return course_error


def course_already_exist(course_id: str) -> dict:
    course_error = {
        "title": "Error ⚠️",
        "description": "Oops, something is wrong...",
        "fields": [
            {
                "name": "Course ID Error",
                "value": f"Course {course_id} already exists in my database.",
                "inline": False
            }
        ],
        "color": 0xff0000
    }

    return course_error


def assignment_not_recognized() -> dict:
    assignment_error = {
        "title": "Error ⚠️",
        "description": "Oops, something is wrong...",
        "fields": [
            {
                "name": "HW Name Error",
                "value": "I didn't recognize that hw name. Make sure to subscribe the hw first using `!subhw <course name> <hw name> <hw id>`",
                "inline": False
            }
        ],
        "color": 0xff0000
    }

    return assignment_error


def assignment_already_exist(hw_name: str) -> dict:
    assignment_error = {
        "title": "Error ⚠️",
        "description": "Oops, something is wrong...",
        "fields": [
            {
                "name": "HW Name Error",
                "value": f"{hw_name} already exists in my database."
            }
        ],
        "color": 0xff0000
    }

    return assignment_error
