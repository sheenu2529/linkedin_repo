import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def scrape_website(url, topic):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract all text content from the website
        text_content = soup.get_text()

        # Filter the text content based on the topic
        relevant_content = [line for line in text_content.split('\n') if topic.lower() in line.lower()]

        return '\n'.join(relevant_content)
    except requests.exceptions.RequestException as e:
        print(f"Error scraping website: {e}")
        return ""

def main():
    input_url = input("Enter the website URL: ")
    input_topic = input("Enter the topic to search for: ")
    scraped_content = scrape_website(input_url, input_topic)
    print(scraped_content)

if __name__ == "__main__":
    main()