# Import from same package
from .config import CANVAS_URL

# Import from library
from datetime import datetime
import httpx
import pytz
from timezonefinder import TimezoneFinder


def display_assignment_dues(hw_name, due_at):
    user_timezone = get_user_timezone(47.7411, -120.7401) #your latitude and longitude.
    raw_due = datetime.strptime(due_at, "%Y-%m-%dT%H:%M:%SZ")
    due_local_time = raw_due.replace(tzinfo=pytz.utc).astimezone(user_timezone)
    formatted_due = format_datetime(due_local_time)
    return f'{hw_name} is due at {formatted_due}!'


def display_course(courses: list[object]) -> str:
    return '\n'.join(str(course_name) for course_name in courses)


def format_datetime(dt, format="%Y %b %d %H:%M:%S"):
    return dt.strftime(format)


def get_error_code(error_code):
    return f'Oops! Something went wrong... Error code: {error_code}'


async def get_possible_grade(assignment_id, course_id, headers):
    """
    This is a helper method for get_assignment_grade.
    This method gets maximum points possible for given assignment.
    :param headers: headers for the api request
    :param course_id: course id to get the grade from.
    :param assignment_id: Integer representation of assignment id.
    :return int_point: Returns the integer value of the possible point.
    """
    endpoint = f"{CANVAS_URL}/api/v1/courses/{course_id}/assignments"
    async with httpx.AsyncClient() as client:
        response = await client.get(endpoint, headers=headers)

        if not is_valid_response(response.status_code):
            return None

        assignment = next((item for item in response.json() if item.get('id') == int(assignment_id)), None)

        if assignment:
            try:
                return int(float(assignment['points_possible']))
            except ValueError:
                pass
        return None


def get_user_timezone(latitude, longitude):
    tf = TimezoneFinder()
    user_timezone = tf.timezone_at(lng=longitude, lat=latitude)
    return pytz.timezone(user_timezone)


def is_valid_response(stats_code):
    return stats_code == 200
