# Project 3 – Election Results Scraper

## Project Description

This project is designed to automatically download and process election results from the Czech election website [volby.cz](https://volby.cz/). Based on an input URL, the script goes through all municipalities within a given district or region and saves the election results into a CSV file.

The project uses HTML parsing, the `requests` library for downloading data from the web, and `BeautifulSoup` for parsing the HTML. The output is a structured `.csv` file suitable for further analysis.

## Requirements

- Python 3.7+
- Libraries:
  - `requests`
  - `beautifulsoup4`

Install the required libraries using:

```bash
pip install requests beautifulsoup4
```

## How to Run the Script

```bash
python projekt3.py <INPUT_URL> <OUTPUT_FILE.csv>
```

### Example:

```bash
python main.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=1&xnumnuts=1100" vysledky_praha.csv
```

## Output

The resulting CSV file contains the following information for each municipality:

- Municipality code (`code`)
- Municipality name (`name`)
- Number of registered voters (`registered`)
- Number of issued envelopes (`envelopes`)
- Number of valid votes (`valid`)
- Vote counts for each political party

## Code Structure

- `main.py` – main script that downloads, processes, and saves the data
- Key functions:
  - `get_municipality_links_and_data` – retrieves links and names of all municipalities
  - `scrapuj_vysledky_obce` – scrapes results for a specific municipality
  - `clean_value` – removes unwanted characters from text data
  - `main` – main execution logic

## Notes

- The script is intended for one-time scraping of a specific election results page.
- The output file uses `utf-8-sig` encoding and semicolon (`;`) as the delimiter, which ensures compatibility with Excel.
