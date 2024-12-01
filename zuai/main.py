from scraper.scraper import scrape_data
from scraper.schema_validator import validate_assessment
from scraper.mongodb_handler import upsert_valid_data

def main():
    print("Starting data scraping...")
    scraped_data = scrape_data()
    print(f"Scraped {len(scraped_data)} records.")
    print("Validating and upserting data...")
    upsert_valid_data(scraped_data)
    print("Process complete.")

if __name__ == "__main__":
    main()

