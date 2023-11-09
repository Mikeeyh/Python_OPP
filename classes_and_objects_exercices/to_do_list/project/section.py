from project.task import Task


class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"
        return f"Task is already in the section {self.name}"

    def complete_task(self, task_name):
        for task_given in self.tasks:
            if task_name == task_given.name:
                task.completed = True
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        removed_tasks = [task_current for task_current in self.tasks if task_current.completed]
        self.tasks = [task_current for task_current in self.tasks if not task_current.completed]
        return f"Cleared {len(removed_tasks)} tasks."

    def view_section(self):
        task_details = [t.details() for t in self.tasks]
        section_details = "\n".join(task_details)
        return f"Section {self.name}:\n{section_details}"


task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())
section = Section("Daily tasks")
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
print(section.clean_section())
print(section.view_section())
