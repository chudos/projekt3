"""
main.py: třetí projekt do Engeto Online Python Akademie

author: Adam Krejčí
email: adam.krejci.1915@gmail.com
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import sys
import csv

headers_to_find = ["sa2", "sa3", "sa5"]
header_map = {
    "sa2": "registered",
    "sa3": "envelopes",
    "sa5": "valid"
}

def get_municipality_links_and_data(main_url):
    response = requests.get(main_url)
    soup = BeautifulSoup(response.text, "html.parser")
    data = []
    for tr in soup.find_all("tr"):
        td_cislo = tr.find("td", class_="cislo")
        a = td_cislo.find("a", href=True) if td_cislo else None
        if a:
            url = urljoin(main_url, a["href"])
            code = a.get_text(strip=True)
            td_name = td_cislo.find_next_sibling("td")
            name = td_name.get_text(strip=True) if td_name else ""
            data.append({
                "url": url,
                "code": code,
                "name": name
            })
    return data

def scrapuj_vysledky_obce(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    values = {}
    for h in headers_to_find:
        td = soup.find("td", class_="cislo", headers=h)
        if td:
            values[h] = td.get_text(strip=True)
        else:
            values[h] = None

    party_results = []
    tables = soup.find_all("table", class_="table")
    for table in tables:
        trs = table.find_all("tr")
        for tr in trs[1:-1]:
            tds = tr.find_all("td")
            if len(tds) >= 3:
                nazev = tds[1].get_text(strip=True)
                hlasy = tds[2].get_text(strip=True)
                party_results.append({
                    "nazev": nazev,
                    "hlasy": hlasy
                })

    return values, party_results

def clean_value(value):
    if isinstance(value, str):
        return value.replace('\xa0', ' ').replace('¬†', ' ').strip()
    return value

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <input_url> <output_csv>")
        sys.exit(1)
    main_url = sys.argv[1]
    output_csv = sys.argv[2]

    municipality_data = get_municipality_links_and_data(main_url)
    all_rows = []
    party_order = []

    print(f"Downloading data from {main_url}")

    for item in municipality_data:
        url = item["url"]
        code = item["code"]
        name = item["name"]
        values, party_results = scrapuj_vysledky_obce(url)
        row = {
            "code": code,
            "name": name
        }
        for h in headers_to_find:
            row[header_map[h]] = values[h]
        for party in party_results:
            row[party["nazev"]] = party["hlasy"]
            if party["nazev"] not in party_order:
                party_order.append(party["nazev"])
        all_rows.append(row)

    summary_headers = ["code", "name"] + [header_map[h] for h in headers_to_find]
    headers = summary_headers + party_order

    print(f"Saving data to {output_csv}")

    with open(output_csv, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=headers, delimiter=';')
        writer.writeheader()
        for row in all_rows:
            cleaned_row = {key: clean_value(row.get(key, "")) for key in headers}
            writer.writerow(cleaned_row)

if __name__ == "__main__":
    main()
