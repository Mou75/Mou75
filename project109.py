# Initialize an empty project list
project109 = []

# Function to add a project
def add_project(name, description, technologies_used, involved_llm=False):
    project = {
        "name": name,
        "description": description,
        "technologies": technologies_used,
        "used_llm": involved_llm
    }
    project109.append(project)
    print(f"Project '{name}' added successfully!")

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
