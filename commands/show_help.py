from .command import Command


class ShowHelp(Command):
    async def execute(self, _):
        help_details = {
            "title": "Help ✅",
            "description": "Commands List",
            "fields": [
                {
                    "name": "`$substudent <user id>`",
                    "value": "Subscribe your user id to pyvas. To get user id, see [here link for readme.md].\n",
                    "inline": False
                },
                {
                    "name": "\n`$subcourse <course name> <course id>`",
                    "value": "Subscribe to the course that you want to keep track of the assignments. `course name` can be anything. To get course id, see [here link for readme.md]\n",
                    "inline": False
                },
                {
                    "name": "\n`$subhw <course name> <hw name> <hw id>`",
                    "value": "Subscribe to the hw (Homework). The `hw name` can be anything. To get hw id, see [here link for readme.md].\n",
                    "inline": False
                },
                {
                    "name": "\n`$showcourse`",
                    "value": "Show all the courses that you're enrolled.\n",
                    "inline": False
                },
                {
                    "name": "\n`$showcoursenow`",
                    "value": "Show all the courses for the quarter.\n",
                    "inline": False
                },
                {
                    "name": "\n`$showhwgrade <course name> <hw name>`",
                    "value": "Show the grade of your subscribed hw.\n",
                    "inline": False
                },
                {
                    "name": "\n`$showhwdue <course name> <hw name>`",
                    "value": "Show the due date for your subscribed hw.\n",
                    "inline": False
                }
            ],
            "color": 0x00ff00
        }

        return help_details
