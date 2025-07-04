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
python main.py <INPUT_URL> <OUTPUT_FILE.csv>
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
 
## Script progress

```bash
Downloading data from https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=1&xnumnuts=1100
Saving data to vysledky_praha.csv
```

## Example of data output

```bash
code;name;registered;envelopes;valid,...
500054;Praha 1;21 556;14 167;14 145;2 770;9;13;657;12;1;774;392;514;41;6;241;14;44;5;0;12;2 783;1 654;1;7;954;3;133;11;2;617;34
500224;Praha 10;79 964;52 277;52 238;8 137;40;34;3 175;50;17;2 334;2 485;1 212;230;15;1 050;35;67;9;8;30;6 497;10 856;37;53;2 398;12;477;69;53;2 998;162
```

## Notes

- The script is intended for one-time scraping of a specific election results page.
- The output file uses `utf-8-sig` encoding and semicolon (`;`) as the delimiter, which ensures compatibility with Excel.
