import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time
import undetected_chromedriver as uc

def main():
    # Configuration
    CSV_PATH = 'input.csv'

    # Read the CSV
    df = pd.read_csv(CSV_PATH)
    addresses = df['Wallet addresses'].tolist()

    # Setup the driver
    driver = uc.Chrome(headless=False,use_subprocess=False)
    WebDriverWait(driver, 10)

    barred_links = [
        "facebook.com",
        "instagram.com",
        "reddit.com",
        "linkedin.com",
        "snapchat.com",
        "tumblr.com",
        "pinterest.com",
        "tiktok.com",
        "threads.net",
        "flickr.com"
    ]

    # Define the function
    def get_social_links(eth_address):
        url = f"https://opensea.io/{eth_address}"
        print(f"Getting the url of : {url}")
        driver.get(url)
        time.sleep(12)
        
        links_elements = driver.find_elements(By.XPATH, "//a[@class='sc-634df830-0 ccOkzW']")
        twitter_link = None
        website_link = None

        for link_element in links_elements:
            link = link_element.get_attribute('href')
            
            if not link:  # If link is None or an empty string, skip this iteration
                continue
            # Check if link is in barred_links and skip to the next iteration if it is
            if any(barred_site in link for barred_site in barred_links):
                continue

            if "twitter.com" in link:
                twitter_link = link
            else:
                website_link = link
                
        print(f"twitter_link : {twitter_link}, website_link: {website_link}")
        print()

        return twitter_link, website_link

    # Process each address
    results = []

    for address in addresses:
        twitter, website = get_social_links(address)
        results.append({
            'Wallet addresses': address,
            'Twitter': twitter or '',
            'Website': website or ''
        })

    driver.close()

    # Write results to a new CSV
    output_df = pd.DataFrame(results)
    output_df.to_csv('output.csv', index=False)


if __name__ == '__main__':
    main()