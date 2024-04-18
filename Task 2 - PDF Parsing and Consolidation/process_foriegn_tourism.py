import pandas as pd
import tabula

# Function to extract and consolidate tables from PDF


def extract_tables_from_pdf(pdf_path, output_csv, table_names):
    # Initialize an empty DataFrame to store consolidated data
    consolidated_data = pd.DataFrame()

    # Extract and consolidate tables
    for table_name in table_names:
        # Find pages containing the table
        pages_with_table = find_table_pages(pdf_path, table_name)
        # Extract tables from PDF
        for page_num in pages_with_table:
            df_list = tabula.read_pdf(
                pdf_path, pages=page_num, lattice=True, multiple_tables=True)
            for df_idx, df in enumerate(df_list):
                # Remove rows with all NaN values
                df.dropna(how="all", inplace=True)
                # Append table with a new column specifying the table name
                df["Table Name"] = f"{
                    table_name} - Page {page_num} - Table {df_idx + 1}"
                # Append to consolidated data
                consolidated_data = pd.concat(
                    [consolidated_data, df], ignore_index=True)

    # Write consolidated data to CSV
    consolidated_data.to_csv(output_csv, index=False)



def find_table_pages(pdf_path, table_name):
    pages_with_table = []
    for page_num in range(1, 100):  # Assuming a maximum of 100 pages
        tables_on_page = tabula.read_pdf(
            pdf_path, pages=page_num, lattice=True, multiple_tables=True)
        for df_idx, df in enumerate(tables_on_page):
            # Check if table name exists in the DataFrame
            if table_name in df.columns:
                pages_with_table.append(page_num)
                break  # No need to check further tables on the same page
    return pages_with_table


# Path to the PDF file
pdf_file_path = "India Tourism Statistics English 2022.pdf"
# Output CSV file
output_csv_file = "foreign_tourism_statistics.csv"
# Specify the table names
table_names = ["Table 2.3.4",
               "Table 2.6.2",
               "Table 2.7.2",
               "Table 2.8.1",
               "Table 2.9.2"]

# Call function to extract and consolidate tables
extract_tables_from_pdf(pdf_file_path, output_csv_file, table_names)

print("Tables extracted and consolidated successfully!")
