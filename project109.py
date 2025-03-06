# Initialize an empty project list
project109 = []

# Function to add a project
def add_project(name, description, technologies_used, involved_llm=False):
    # Check if a project with the same name already exists
    if any(project["name"] == name for project in project109):
        print(f"Project '{name}' already exists!")
        return
    
    project = {
        "name": name,
        "description": description,
        "technologies": technologies_used,
        "used_llm": involved_llm
    }
    project109.append(project)
    print(f"Project '{name}' added successfully!")

# Function to remove a project by name
def remove_project(name):
    global project109
    # Find the project by name
    project_to_remove = None
    for project in project109:
        if project["name"] == name:
            project_to_remove = project
            break
    
    if project_to_remove:
        project109 = [project for project in project109 if project["name"] != name]
        print(f"Project '{name}' removed successfully!")
    else:
        print(f"Project '{name}' not found!")

# Example Usage
add_project(
    name="Chatbot Assistant",
    description="A virtual assistant powered by an LLM to answer queries.",
    technologies_used=["Python", "OpenAI API", "Flask"],
    involved_llm=True
)

add_project(
    name="Weather App",
    description="A simple app to fetch real-time weather data.",
    technologies_used=["JavaScript", "HTML", "CSS"],
    involved_llm=False
)

# Display project109
print("\nproject109:")
for project in project109:
    print(f"- {project['name']} (LLM used: {project['used_llm']})")

# Remove a project
remove_project("Weather App")

# Display project109 after removal
print("\nproject109 after removal:")
for project in project109:
    print(f"- {project['name']} (LLM used: {project['used_llm']})")
