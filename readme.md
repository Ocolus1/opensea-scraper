# OpenSea Scraper Documentation

This script allows for scraping OpenSea profiles to obtain associated social media links of Ethereum wallet owners. Specifically, it looks for Twitter and any other website links linked to the profile, while excluding certain social media platforms.

## Dependencies

- `pandas`
- `selenium`
- `undetected_chromedriver`

## How It Works

1. Reads Ethereum wallet addresses from an input CSV file (`input.csv`).
2. Uses the Chrome web driver to open each Ethereum profile on OpenSea.
3. Scans the page for social media links.
4. Saves the discovered Twitter and other website links to an `output.csv` file.

### Configuration

- `CSV_PATH`: Path to the input CSV file containing Ethereum wallet addresses. The addresses should be listed under the column name `Wallet addresses`.

### Excluded Platforms

The script is configured to ignore links from the following platforms:

- Facebook
- Instagram
- Reddit
- LinkedIn
- Snapchat
- Tumblr
- Pinterest
- TikTok
- Threads.net
- Flickr

## Functions

### `get_social_links(eth_address)`

**Purpose:** Extracts social media links (Twitter and a generic website link) from the OpenSea profile of a given Ethereum address.

**Parameters:**

- `eth_address`: The Ethereum address string for which the OpenSea profile is to be scanned.

**Returns:** A tuple containing the discovered Twitter link (if any) and another website link (if any). If no link is found for a category, the value will be `None`.

## Execution

To run the script, execute it as a standard Python script:

```bash
python main.py
```

After execution, you can find the extracted links in `output.csv`.

## Notes

- The script uses the `undetected_chromedriver` to bypass bot detection techniques. If you encounter issues, you might need to update or modify the setup.
- A delay of 12 seconds is added after navigating to each OpenSea profile. This delay ensures the page loads fully and all elements are accessible. Adjust this delay as necessary based on your network speed and OpenSea's response time.
