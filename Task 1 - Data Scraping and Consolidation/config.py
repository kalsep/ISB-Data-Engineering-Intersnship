import os
import time
import shutil
import openpyxl
import pandas as pd
from openpyxl import load_workbook

# Selenium
import codecs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup

district_wise_selector = ".btn_segmented_container.MuiBox-root.css-0 button:not(.active)"
base_path = os.getcwd()
try:
    os.makedirs(os.path.join(base_path, "Data"))
except:
    pass
# data_dir = os.path.join(base_path, "Data")
data_dir = os.path.join(base_path, "data2")
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
