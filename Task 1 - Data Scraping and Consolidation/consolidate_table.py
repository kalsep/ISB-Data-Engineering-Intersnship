from configuration import data_dir,pd,os
def consolidate_tables(data_dir, output_file):
    combined_data = []
    for state_folder in os.listdir(data_dir):
        state_dir = os.path.join(data_dir, state_folder)
        if os.path.isdir(state_dir):
            for report_type in ["MacroNutrient", "MicroNutrient"]:
                report_dir = os.path.join(state_dir, report_type)
                if os.path.exists(report_dir):
                    for file_name in os.listdir(report_dir):
                        file_path = os.path.join(report_dir, file_name)
                        if os.path.isfile(file_path) and file_name.endswith('.xlsx'):
                            df = pd.read_excel(file_path)
                             # Add a column indicating the report type
                            df['State'] = state_folder
                            df['Report Type'] = report_type
                            combined_data.append(df)

    if combined_data:
        # Concatenate all dataframes into a single dataframe
        consolidated_df = pd.concat(combined_data, ignore_index=True)
        # Write the consolidated dataframe to a CSV file
        consolidated_df.to_csv(output_file, index=False)
        print(f"Consolidated data saved to {output_file}")
    else:
        print("No data found for consolidation.")
consolidate_tables(data_dir, output_csv="consolidated_data.csv")
