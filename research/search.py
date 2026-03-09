import requests
from bs4 import BeautifulSoup
import urllib.parse


def search_company(company):

    query = company + " company"

    url = f"https://duckduckgo.com/html/?q={query}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")

    links = []

    results = soup.find_all("a", class_="result__a")

    for r in results:

        link = r.get("href")

        if "uddg=" in link:

            real_url = link.split("uddg=")[1]
            real_url = urllib.parse.unquote(real_url)

            links.append(real_url)

    return links[:5]


if __name__ == "__main__":

    company = "Nvidia"

    results = search_company(company)

    for r in results:
        print(r)