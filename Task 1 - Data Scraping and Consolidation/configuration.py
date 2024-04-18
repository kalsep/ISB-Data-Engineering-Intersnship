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

# Set maximum number of columns to display
pd.set_option("display.max_columns", 100)

# CSS selector for district-wise data
district_wise_selector = ".btn_segmented_container.MuiBox-root.css-0 button:not(.active)"

# Base directory path
base_path = os.getcwd()

# Create 'Data' directory if not exists
os.makedirs(os.path.join(base_path, "Data"), exist_ok=True)

# Directory path for storing data
data_dir = os.path.join(base_path, "Data")

# Base URL for the soil health data website
base_url = "https://soilhealth.dac.gov.in/piechart"

# List of Indian states
indian_state = [
    "ANDAMAN AND NICOBAR ISLANDS", "ANDHRAPRADESH", "ARUNACHAL PRADESH", "ASSAM",
    "BIHAR", "CHANDIGARH", "CHHATTISGARH", "DELHI", "GOA", "GUJARAT", "HARYANA", "HIMACHAL PRADESH",
    "JAMMU AND KASHMIR", "JHARKHAND", "KARNATAKA", "KERALA", "LADAKH", "LAKSHADWEEP", "MADHYA PRADESH",
    "MAHARASHTRA", "MANIPUR", "MEGHALAYA", "MIZORAM", "NAGALAND", "ODISHA", "PUDUCHERRY", "PUNJAB",
    "RAJASTHAN", "SIKKIM", "TAMILNADU", "TELANGANA", "THE DADRA AND NAGAR HAVELI AND DAMAN AND DIU",
    "TRIPURA", "UTTAR PRADESH", "UTTARAKHAND", "WEST BENGAL"
]