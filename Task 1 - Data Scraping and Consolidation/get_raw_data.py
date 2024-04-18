from configuration import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium import webdriver
import os

def get_soup(html_content):
    """
    Returns BeautifulSoup object for provided HTML content.

    Args:
        html_content (str): HTML content to parse.

    Returns:
        BeautifulSoup: Parsed BeautifulSoup object.
    """
    return BeautifulSoup(html_content, 'lxml')


def scrap_data(html_content):
    """
    Scrapes data from HTML content and returns a list of rows.

    Args:
        html_content (str): HTML content to scrape data from.

    Returns:
        list: List of lists containing scraped data.
    """
    soup = get_soup(html_content)
    main_content = soup.find("div", class_='main_container')
    grid_container = main_content.find(
        "div", class_="custom-data-grid MuiDataGrid-root MuiDataGrid-root--densityStandard MuiDataGrid-withBorderColor css-12dkb5y")
    data_element = grid_container.find(
        "div", class_="MuiDataGrid-virtualScrollerRenderZone css-1inm7gi")
    rows = data_element.find_all(class_="MuiDataGrid-row")
    data = []
    for row in rows:
        cells = row.find_all(class_="MuiDataGrid-cell")
        row_data = [cell.text.strip() for cell in cells]
        data.append(row_data)
    return data


def create_dataframe(data, desired_state, table):
    """
    Creates a DataFrame from scraped data and saves it as a CSV file.

    Args:
        data (list): List of lists containing scraped data.
        desired_state (str): Desired state for which data is scraped.
        table (str): Identifier for the table (macro or micro nutrient).

    Returns:
        None
    """
    df_ = pd.DataFrame(data)
    state_dir = os.path.join(data_dir, desired_state)
    os.makedirs(state_dir, exist_ok=True)
    if table == "tab-1":
        report_dir = os.path.join(state_dir, "MacroNutrient")
    else:
        report_dir = os.path.join(state_dir, "MicroNutrient")

    os.makedirs(report_dir, exist_ok=True)

    if table == "tab-1":
        file_name = 'MacroNutrient.csv'
    else:
        file_name = 'MicroNutrient.csv'
    df_.to_csv(os.path.join(report_dir, file_name), index=False)


def process_table(driver, desired_state, table_id, selector, wait):
    """
    Processes table data for a desired state and saves it as a CSV file.

    Args:
        driver: Selenium WebDriver instance.
        desired_state (str): Desired state for which data is processed.
        table_id (str): Identifier for the table (macro or micro nutrient).
        selector (str): CSS selector for district-wise data.
        wait: WebDriverWait instance.

    Returns:
        None
    """
    click_button = driver.find_element(By.ID, table_id)
    click_button.click()
    wait.until(EC.presence_of_element_located((By.ID, table_id)))
    district_wise_button = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, district_wise_selector)))
    district_wise_button.click()
    if desired_state != "ANDAMAN AND NICOBAR ISLANDS":
        wait.until(EC.visibility_of_all_elements_located(
            (By.XPATH, '//*[@id="wrapper"]/div[2]/div/div[2]/div[2]/div[2]/div/div')))
        dropdown = driver.find_element(
            By.XPATH, '//*[@id="wrapper"]/div[2]/div/div[2]/div[2]/div[2]/div/div')
        dropdown.click()
        actions = ActionChains(driver)
        actions.move_to_element(dropdown).perform()
        element = wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"//*[text()='{desired_state}']")))
        element.click()
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '.css-opb0c2')))
    html_content = driver.page_source
    if html_content:
        print(f"Got HTML Content for {table_id} and Processing the Table Request")
        data = scrap_data(html_content)
        create_dataframe(data, desired_state, table_id)


def main():
    """
    Main function to iterate through Indian states and scrape data for each state.

    Returns:
        None
    """
    for desired_state in indian_state:
        print("desired_state: ", desired_state)
        if desired_state != "ANDAMAN AND NICOBAR ISLANDS":
            try:
                options = Options()
                options.headless = True
                driver = webdriver.Chrome(service=Service(
                    ChromeDriverManager().install()), options=options)
                driver.get(base_url)
                wait = WebDriverWait(driver, 10)
                wait.until(EC.presence_of_element_located((By.ID, "root")))
                process_table(driver, desired_state, "tab-1", district_wise_selector, wait)
                process_table(driver, desired_state, "tab-2", district_wise_selector, wait)
                driver.quit()
            except Exception as e:
                print(e)
        else:
            try:
                options = Options()
                options.headless = True
                driver = webdriver.Chrome(service=Service(
                    ChromeDriverManager().install()), options=options)
                driver.get(base_url)
                wait = WebDriverWait(driver, 10)
                wait.until(EC.presence_of_element_located((By.ID, "root")))
                process_table(driver, desired_state, "tab-1", district_wise_selector, wait)
                process_table(driver, desired_state, "tab-2", district_wise_selector, wait)
                driver.quit()
            except Exception as e:
                print(e)


if __name__ == "__main__":
    main()
