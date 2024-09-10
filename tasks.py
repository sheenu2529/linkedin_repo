from textwrap import dedent
from crewai import Task

class Tasks:
    def scraper_task(self, agent, position, primary_skills):
        return Task(
            description=dedent(
                f"""
                Log into LinkedIn and scrape candidate details based on the position '{position}' and primary skills '{primary_skills}' from the LinkedIn search page. Extract relevant information and save it in a Markdown (.md) file in the specified output directory.
                """
            ),
            expected_output=dedent(
                f"""
                1. Log into LinkedIn using the provided credentials.
                2. Navigate to the LinkedIn search page with the position '{position}' and primary skills '{primary_skills}'.
                3. Save the formatted data for each candidate in a separate Markdown (.md) file in the specified output directory.
                4. Extract and save the following key profile details:
                   - Name
                   - Headline
                   - Email
                   - Country
                   - City
                   - Experience
                   - Education
                   - Skills
                5. Ensure proper error handling and respect LinkedIn's usage policies and rate limits.
                """
            ),
            agent=agent,
            # tools=[linkedin_scraper],
        )
