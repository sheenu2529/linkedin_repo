from crewai import Crew
from tasks import Tasks
from agents import Agents
from langchain_groq import ChatGroq

my_llm = ChatGroq(
    api_key="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",
    model="llama3-8b-8192",
)

tasks = Tasks()
agents = Agents()

position = input("Enter the job position: "),
primary_skills=input("Enter the primary skills: "),


scraper_agent = agents.scraper_agent()
scraper_task = tasks.scraper_task(scraper_agent, position, primary_skills)

crew = Crew(
    agents=[scraper_agent],
    tasks=[scraper_task],
    verbose=2,
)

result = crew.kickoff()
print(result)