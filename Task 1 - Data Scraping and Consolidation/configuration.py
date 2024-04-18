from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import os
import time


district_wise_selector = ".btn_segmented_container.MuiBox-root.css-0 button:not(.active)"
base_path = os.getcwd()
os.makedirs(os.path.join(base_path, "Data"),exist_ok=True)
data_dir = os.path.join(base_path, "Data")
base_url = "https://soilhealth.dac.gov.in/piechart"

indian_state = [
    "ANDAMAN AND NICOBAR ISLANDS", "ANDHRAPRADESH", "ARUNACHAL PRADESH", "ASSAM",
    "BIHAR", "CHANDIGARH", "CHHATTISGARH", "DELHI", "GOA", "GUJARAT", "HARYANA", "HIMACHAL PRADESH",
    "JAMMU AND KASHMIR", "JHARKHAND", "KARNATAKA", "KERALA", "LADAKH", "LAKSHADWEEP", "MADHYA PRADESH",
    "MAHARASHTRA", "MANIPUR", "MEGHALAYA", "MIZORAM", "NAGALAND", "ODISHA", "PUDUCHERRY", "PUNJAB",
    "RAJASTHAN", "SIKKIM", "TAMILNADU", "TELANGANA", "THE DADRA AND NAGAR HAVELI AND DAMAN AND DIU",
    "TRIPURA", "UTTAR PRADESH", "UTTARAKHAND", "WEST BENGAL"
]
# Example column names for the two header rows
header_row1_macronutrient_table = ['', 'Nitrogen', 'Nitrogen', 'Nitrogen', 'Phosphorous', 'Phosphorous', 'Phosphorous',
                                   'Potassium', 'Potassium', 'Potassium', 'OC', 'OC', 'EC', 'EC', 'pH', 'pH', 'pH']
header_row2_macronutrient_table = ['District', 'High', 'Medium', 'Low', 'High', 'Medium', 'Low', 'High', 'Medium', 'Low',
                                   'Sufficient', 'Deficient', 'Saline', 'Non Saline', 'Acidic', 'Neutral', 'Alkaline']

# Create a multi-level column index
multiindex_columns_macronutrient_table = pd.MultiIndex.from_arrays(
    [header_row1_macronutrient_table, header_row2_macronutrient_table])


# Example column names for the two header rows
header_row1_micronutrient_table = ['', 'Copper', 'Copper', 'Boron', 'Boron', 'Sulphur', 'Sulphur',
                                   'Sulphur', 'Iron', 'Iron', 'Zinc', 'Zinc', 'Manganese', 'Manganese']
header_row2_micronutrient_table = ['District', 'Sufficient', 'Deficient', 'Sufficient', 'Deficient', 'High', 'Medium', 'Low',
                                   'Sufficient', 'Deficient', 'Sufficient', 'Deficient', 'Sufficient', 'Deficient']

# Create a multi-level column index
multiindex_columns_micronutrient_table = pd.MultiIndex.from_arrays(
    [header_row1_micronutrient_table, header_row2_micronutrient_table])
