from crewai import Agent
from langchain_groq import ChatGroq
from tools.linkedin import linkedin_scraper


class Agents:
    def __init__(self):
        self.llm = ChatGroq(
            api_key="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",
            model="llama3-8b-8192",
        )

    def scraper_agent(self):
        return Agent(
            role="LinkedIn Data Scraper",
            goal="Extract detailed candidate information from LinkedIn based on specified position and primary skills, and save the data in a structured Markdown format.",
            backstory="I am an AI agent specialized in LinkedIn data extraction. My primary function is to log into LinkedIn, search for candidates based on given position and primary skills, and extract comprehensive information about each candidate. I am designed to scrape all the  LinkedIn's data.",
            llm=self.llm,
            verbose=True,
            tools=[linkedin_scraper],
        )
