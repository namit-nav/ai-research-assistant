from research.search import search_company
from research.web_scraper import scrape_page
from research.text_cleaner import clean_text
from research.news_collector import get_company_news
from agents.persona_manager import get_persona_prompt
from core.llm import ask_llm
from core.memory import add_to_memory
from core.prompts import research_prompt


def research_company(company):

    # Ask persona once
    persona = input("Choose persona (research_assistant / market_analyst / sales_strategist): ")
    persona_prompt = get_persona_prompt(persona)

    print("\nSearching for company information...\n")

    links = search_company(company)

    collected_text = ""

    for link in links:

        try:
            print("Scraping:", link)

            page_text = scrape_page(link)
            page_text = clean_text(page_text)

            collected_text += page_text[:2000]

        except:
            print("Failed to scrape:", link)

    # Collect news only once
    news_links = get_company_news(company)

    print("\nCollecting recent news...\n")

    for n in news_links:
        print("News:", n)

    prompt = research_prompt(persona_prompt, company, collected_text)

    result = ask_llm(prompt)

    return result


if __name__ == "__main__":

    company = input("Enter company name: ")

    report = research_company(company)
    add_to_memory("assistant", report)

    print("\nResearch Report:\n")

    print(report)