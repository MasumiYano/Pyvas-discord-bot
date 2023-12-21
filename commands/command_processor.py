from .sub_substudent_command import SubStudentCommand
from .sub_course_command import SubCourseCommand
from .sub_hw_command import SubHWCommand
from .show_course_command import ShowCourseCommand
from .show_course_now import ShowCourseNowCommand
from .show_assignment_grade_command import ShowAssignmentGrade
from .show_assignment_due import ShowAssignmentDue
from .show_help import ShowHelp


class CommandProcessor:
    @staticmethod
    def process(command_string: str, discord_id):
        command_parts = command_string.split()
        command_name = command_parts[0]
        args = command_parts[1:]

        match command_name:
            case '$substudent':
                command = SubStudentCommand()
            case '$subcourse':
                command = SubCourseCommand()
            case '$showcoursenow':
                command = ShowCourseNowCommand()
            case '$subhw':
                command = SubHWCommand()
            case '$showcourse':
                command = ShowCourseCommand()
            case '$showhwgrade':
                command = ShowAssignmentGrade()
            case '$showhwdue':
                command = ShowAssignmentDue()
            case '$help':
                command = ShowHelp()
            case _:
                return

        return command.execute(*args, discord_id)
