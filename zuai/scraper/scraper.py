import requests
from bs4 import BeautifulSoup


def scrape_data():
    url = "https://example.com/assessments"  # Replace with the actual URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    data_list = []
    # Example scraping logic
    for item in soup.select(".assessment-item"):
        data = {
            "assessment_id": item["data-id"],
            "title": item.select_one(".title").get_text(strip=True),
            "description": item.select_one(".description").get_text(strip=True),
            "subject": item.select_one(".subject").get_text(strip=True),
            "word_count": int(item.select_one(".word-count").get_text(strip=True)),
            "read_time": item.select_one(".read-time").get_text(strip=True),
            "publication_date": "2024/12/00",  # Example static data
            "details": {
                "author": item.select_one(".author").get_text(strip=True),
                "difficulty_level": item.select_one(".difficulty").get_text(strip=True),
                "keywords": [
                    k.get_text(strip=True) for k in item.select(".keywords li")
                ],
            },
        }
        data_list.append(data)

    return data_list
