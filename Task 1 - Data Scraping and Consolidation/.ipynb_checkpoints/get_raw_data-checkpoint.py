import os
import requests
from bs4 import BeautifulSoup

# Define base URL and data directory
base_url = "https://soilhealth.dac.gov.in/piechart"
data_dir = "data"

def create_directory(path):
  """Creates directory if it doesn't exist"""
  if not os.path.exists(path):
    os.makedirs(path)
def get_soup(url):
  requests.packages.urllib3.disable_warnings()
#   url = f"{base_url}/{state}/{table_type}"
  response = requests.get(url, verify=False)
  return BeautifulSoup(response.content, "html.parser")

def get_data(state, table_type):
  """Downloads data for a specific state and table"""
  soup = get_soup(base_url)
  print(soup)

  # Extract table data (logic might need adjustment based on website structure)
  table = soup.find("table")
  rows = table.find_all("tr")[2:]  # Skip header rows
  data = []
  for row in rows:
    cells = row.find_all("td")
    data.append([cell.text.strip() for cell in cells])

  # Save data to file within state and table subfolders
  state_dir = os.path.join(data_dir, state)
  table_dir = os.path.join(state_dir, table_type)
  create_directory(state_dir)
  create_directory(table_dir)
  filename = f"{table_type}.csv"
  filepath = os.path.join(table_dir, filename)
  with open(filepath, "w") as f:
    for row in data:
      f.write(",".join(row) + "\n")

def main():
  """Scrapes data for all states and tables"""
  create_directory(data_dir)
  states = ["Andhra Pradesh", "Arunachal Pradesh", ...]  # Replace with all states

  for state in states:
    get_data(state, "MacroNutrient(Table View)")
    get_data(state, "MicroNutrient(Table View)")

if __name__ == "__main__":
  main()
