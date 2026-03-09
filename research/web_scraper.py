import requests
from bs4 import BeautifulSoup


def scrape_page(url):

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")

    paragraphs = soup.find_all("p")

    text = ""

    for p in paragraphs:
        text += p.get_text() + "\n"

    return text


if __name__ == "__main__":

    url = "https://en.wikipedia.org/wiki/Nvidia"

    content = scrape_page(url)

    print(content[:2000])