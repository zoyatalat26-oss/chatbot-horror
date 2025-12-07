from crewai import Agent, Task, Crew, LLM
import os

# Free LLM (you can use any)
llm = LLM(model="groq/llama-3.1-8b-instant", api_key=os.getenv("GROQ_API_KEY"))

# Single Agent
story_agent = Agent(
    role="StoryTeller",
    goal="Tell a fun short story for kids.",
    backstory="A creative robot who loves bedtime stories.",
    llm=llm
)

# Single Task
story_task = Task(
    description="Create a 5-line funny story about a talking cat.",
    expected_output="A funny 5-line story about a talking cat.",
    agent=story_agent
)

# Single-Agent Crew
crew = Crew(
    agents=[story_agent],
    tasks=[story_task]
)

result = crew.kickoff()
print(result)

