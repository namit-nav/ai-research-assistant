from research.search import search_company
from research.web_scraper import scrape_page
from research.text_cleaner import clean_text
from research.news_collector import get_company_news
from agents.persona_manager import get_persona_prompt
from core.llm import ask_llm
from core.memory import add_to_memory
from core.prompts import research_prompt
from concurrent.futures import ThreadPoolExecutor


# Scrape + clean helper
def scrape_and_clean(link):
    try:
        page_text = scrape_page(link)
        page_text = clean_text(page_text)
        return page_text[:1200]  # limit per page
    except Exception:
        return ""


def research_company(company, persona="research_assistant"):

    print("\nGenerating report...\n")

    # Persona prompt
    persona_prompt = get_persona_prompt(persona)

    # Search links
    links = search_company(company)

    # Remove duplicates
    links = list(set(links))

    # Parallel scraping
    collected_text = ""

    with ThreadPoolExecutor(max_workers=5) as executor:
        results = executor.map(scrape_and_clean, links)

    for text in results:
        collected_text += text

        # Limit total size (important for performance)
        if len(collected_text) > 10000:
            break

    # Collect news (simple integration)
    news_links = get_company_news(company)

    news_text = "\nRecent News Sources:\n"
    for n in news_links[:5]:
        news_text += n + "\n"

    collected_text += news_text

    # Generate prompt
    prompt = research_prompt(persona_prompt, company, collected_text)

    # LLM call
    result = ask_llm(prompt)

    # Store memory
    add_to_memory("user", company)
    add_to_memory("assistant", result)

    return result


if __name__ == "__main__":

    company = input("Enter company name: ")
    persona = input("Choose persona (research_assistant / market_analyst / sales_strategist): ")

    report = research_company(company, persona)

    print("\nResearch Report:\n")
    print(report)