[[tool]]
name = "schedule_event"
description = "Schedules an event in your calendar."
input_parameters = [
  { name = "task_description", type = "string", description = "The task or event to be scheduled." },
  { name = "time", type = "string", description = "The time when the event should be scheduled (e.g., '2pm today')." }
]

[[prompt]]
name = "schedule_todo_task"
description = "Schedules a task from the todo list into your calendar."
input_parameters = [
  { name = "task_description", type = "string", description = "The task to schedule." }
]
template = """
The user wants to schedule the task: '{task_description}'.
Suggest a good time for today and call the `schedule_event` tool to add it to the calendar.
"""