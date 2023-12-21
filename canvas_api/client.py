# Importing from config file
from .config import CANVAS_URL, TOKEN

# Importing from utils file
from .utils import (display_course,
                    display_assignment_dues,
                    is_valid_response,
                    get_error_code,
                    get_possible_grade)

from bot.json_handler import JsonHandler

# Importing from requests library
import httpx


class CanvasAPIClient:
    """
    A class for interfacing with Canvas LMS REST API to retrieve assignment data, including grades and descriptions.

    To learn more about Canvas LMS - REST API, refer to the official documentation from Instructure
    :ref https://canvas.instructure.com/doc/api/index.html:

    Attributes:
        class_name (str): Name of the class that we will retrieve the data from.
        assignment_name (str): Name of the assignment that we wil retrieve the data from.
    """

    def __init__(self, user_id):
        """
        Asynchronous initialization of the assignment class.
        :param class_name: String representation of the class name.
        :param assignment_name: String representation of the assignment name.
        """
        self.user_id = user_id
        self.headers = {"Authorization": f"Bearer {TOKEN}"}

    async def courses(self) -> str:
        endpoint = f'{CANVAS_URL}/api/v1/courses'
        async with httpx.AsyncClient() as client:
            response = await client.get(endpoint, headers=self.headers)

            if not is_valid_response(response.status_code):
                return get_error_code(response.status_code)

            course_names = [course['name'] for course in response.json()]

            return display_course(course_names)

    async def assignment_grade(self, course_name: str, assignment_name: str) -> str:
        """
        Asynchronous function to get the particular assignment's grade
        :return : The string that indicates your score, the possible max score, and the percentage of your score
        """
        course_id = JsonHandler.get_course_id(self.user_id, course_name)
        ass_id = JsonHandler.get_assignment_id(self.user_id, course_name, assignment_name)
        endpoint = f'{CANVAS_URL}/api/v1/courses/{course_id}/assignments/{ass_id}/submissions/{self.user_id}'
        async with httpx.AsyncClient() as client:
            response = await client.get(endpoint, headers=self.headers)
            score_possible = await get_possible_grade(ass_id, course_id, self.headers)

            if not is_valid_response(response.status_code):
                return get_error_code(response.status_code)

            try:
                user_score = int(response.json().get("score"))
                percentage = (user_score / score_possible) * 100
                return f'Your grade was {user_score} out of {score_possible} ({percentage:.2f}%)!'
            except TypeError:
                return "Oops! It looks like your submission has not been graded!"
            except ZeroDivisionError:
                return "Zero division error."

    async def assignment_due_dates(self, course_name: str, hw_name: str):
        course_id = JsonHandler.get_course_id(user_id=self.user_id, course_name=course_name)
        assignment_id = JsonHandler.get_assignment_id(user_id=self.user_id, course_name=course_name,
                                                      assignment_name=hw_name)
        endpoint = f'{CANVAS_URL}/api/v1/courses/{course_id}/assignments/{assignment_id}'
        async with httpx.AsyncClient() as client:
            response = await client.get(endpoint, headers=self.headers)

            if is_valid_response(response.status_code):
                name = response.json().get('name')
                due = response.json().get('due_at')
                return display_assignment_dues(name, due)
            else:
                return get_error_code(response.status_code)
