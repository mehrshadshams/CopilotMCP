[[tool]]
name = "add_task"
description = "Adds a new task to your todo list."
input_parameters = [
  { name = "task_description", type = "string", description = "The task to add to your todo list." }
]

[[prompt]]
name = "plan_daily_tasks"
description = "Plans the day by breaking down a user goal into actionable tasks."
input_parameters = [
  { name = "user_goal", type = "string", description = "The user's goal for the day." }
]
template = """
Based on the user's goal: '{user_goal}', generate 2-3 specific, actionable tasks that would help the user achieve it.
For each task, call the `add_task` tool with a helpful task description.
"""