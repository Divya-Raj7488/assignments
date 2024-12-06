from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time

# Dictionary for month mapping
month_key = {
    "january": "01",
    "february": "02",
    "march": "03",
    "april": "04",
    "may": "05",
    "june": "06",
    "july": "07",
    "august": "08",
    "september": "09",
    "october": "10",
    "november": "11",
    "december": "12",
}


def scrape_data():
    driver = webdriver.Chrome()
    driver.get("https://nailib.com/ia-sample")
    time.sleep(2)
    html_text = driver.page_source
    soup = BeautifulSoup(html_text, "lxml")
    all_ias = soup.find_all("a", {"class": "sample_sample__fWsLe"})

    scraped_data = []
    entryCount = 0;

    for ia in all_ias:
        try:
            title_tag = ia.find("h3", class_="sample_sample__right__heading__TxYVC")
            title = title_tag.text.strip() if title_tag else "No title found"
            description_tag = ia.find(
                "div", class_="sample_sample__right__paragraph__QNi7I"
            )
            description = (
                description_tag.p.text.strip()
                if description_tag and description_tag.p
                else "No description found"
            )
            assessment_id = ia.get("id")
            details_link = ia.get("href")
            full_details_link = (
                f"https://nailib.com{details_link}" if details_link else "No link found"
            )
            details = []
            if full_details_link != "No link found":
                details_html = requests.get(full_details_link).text
                details_soup = BeautifulSoup(details_html, "lxml")
                details_div = details_soup.find(
                    "section",
                    class_="file_sample__body__container__middle__section__toc__Z6dIA",
                )
                if details_div:
                    details_list = details_div.find_all("ul")
                    details = [ul.text.strip() for ul in details_list]
            stat_Info = ia.find_all(
                "div", class_="sample_sample__right__stat__item__E0oPZ"
            )
            subject = (
                stat_Info[0].text.strip() if len(stat_Info) > 0 else "No subject found"
            )
            word_count = (
                stat_Info[4].text.strip()
                if len(stat_Info) > 4
                else "No word count found"
            )
            read_time = (
                stat_Info[3].text.strip()
                if len(stat_Info) > 3
                else "No read time found"
            )
            if len(stat_Info) >= 8:
                publish_month = stat_Info[6].text.strip()
                publish_year = stat_Info[7].text.strip()
            else:
                publish_month = "NA"
                publish_year = "NA"
            document = {
                "assessment_id": assessment_id,
                "title": title,
                "description": description,
                "subject": subject,
                "word_count": int(word_count) if word_count.isdigit() else 0,
                "read_time": read_time,
                "publication_date": (
                    f"{publish_year}/{month_key[publish_month.lower()]}/00"
                    if publish_month != "NA"
                    else "NA"
                ),
                "details": details,
            }
            scraped_data.append(document)
            entryCount+= 1
            print(f"scraping...{entryCount}")
        except Exception as e:
            print(f"Error processing entry: {e}")

    driver.quit()
    return scraped_data
