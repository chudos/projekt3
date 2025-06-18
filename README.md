# Municipality Election Results Scraper

This Python project downloads and saves municipal election results from a public website.  
It scrapes summary statistics and party results for each municipality, then saves everything into a CSV file—ready for analysis or use in Excel.

---

## Features

- Downloads a list of municipalities from a given URL
- For each municipality, scrapes:
  - Basic statistics (registered voters, envelopes, valid votes)
  - Number of votes for each party
- Saves all results into a single CSV file (UTF-8 with BOM for Excel compatibility)

---

## Requirements

- Python 3.7+
- See `requirements.txt` for dependencies:

requests==2.32.4
beautifulsoup4==4.13.4

Install dependencies with:

pip install -r requirements.txt

---

## Usage

Run the script from the command line:

python main.py <input_url> <output_csv>


- `<input_url>`: The URL of the main page listing all municipalities.
- `<output_csv>`: The filename for the output CSV file.

**Example:**

python main.py https://example.com/municipalities.html results.csv


---

## Output

- The script creates a CSV file with columns:
  - Municipality code
  - Municipality name
  - Registered voters
  - Envelopes
  - Valid votes
  - One column for each party (with the number of votes)

- The CSV is encoded as UTF-8 with BOM for compatibility with Microsoft Excel.

---

## Notes

- The script is designed for Czech municipal election result websites, but can be adapted for similar structures.
- If you encounter errors, check that the input URL is correct and that the website structure matches the script’s expectations.
