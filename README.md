# Project Manager

This is a simple Python project manager that allows you to add and remove projects from a list. Each project has a name, description, technologies used, and a flag indicating whether a Large Language Model (LLM) was involved in its development.

## Features

- **Add a Project**: Add a new project to the list with details such as name, description, technologies used, and whether an LLM was involved.
- **Remove a Project**: Remove a project from the list by specifying its name.
- **Prevent Duplicates**: Ensures that no two projects with the same name can be added.
- **Display Projects**: View all projects in the list with their details.

## Usage

### Adding a Project

To add a project, use the `add_project` function. It takes the following parameters:
- `name`: The name of the project (must be unique).
- `description`: A brief description of the project.
- `technologies_used`: A list of technologies used in the project.
- `involved_llm`: A boolean flag indicating whether an LLM was used (default is `False`).

Example:
```python
add_project(
    name="Chatbot Assistant",
    description="A virtual assistant powered by an LLM to answer queries.",
    technologies_used=["Python", "OpenAI API", "Flask"],
    involved_llm=True
)
