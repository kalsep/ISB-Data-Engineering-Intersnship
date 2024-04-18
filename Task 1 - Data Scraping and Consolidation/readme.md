```markdown
# Soil Health Data Scraping Project and Consolidation

This project aims to scrape soil health data from a website and consolidate it into a single Excel file. It consists of three main Python scripts:

1. `configuration.py`: Configuration module containing variables and constants used in the data scraping process.
2. `get_raw_data.py`: Module to scrape raw data from the soil health website and save it as CSV files.
3. `consolidate_tables.py`: Module to consolidate the scraped data from individual state directories into a single Excel file.

## Getting Started

To get started with this project, follow these steps:

1. Clone the repository to your local machine:

```bash
git clone https://github.com/kalsep/ISB-Data-Engineering-Intersnship.git
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Run the `get_raw_data.py` script to scrape raw data from the soil health website and save it as CSV files:

```bash
python get_raw_data.py
```

4. Run the `consolidate_tables.py` script to consolidate the scraped data into a single Excel file:

```bash
python consolidate_tables.py
```

## Project Structure

```
.
├── configuration.py
├── get_raw_data.py
├── consolidate_tables.py
├── data
│   ├── State1
│   │   ├── MacroNutrient
│   │   │   └── MacroNutrient.csv
│   │   └── MicroNutrient
│   │       └── MicroNutrient.csv
│   ├── State2
│   │   ├── MacroNutrient
│   │   │   └── MacroNutrient.csv
│   │   └── MicroNutrient
│   │       └── MicroNutrient.csv
│   └── ...
├── README.md
└── requirements.txt
```

## Dependencies

- `pandas`: Library for data manipulation and analysis.
- `selenium`: Library for automating web browsers.
- `webdriver-manager`: Library for managing web driver binaries.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
```