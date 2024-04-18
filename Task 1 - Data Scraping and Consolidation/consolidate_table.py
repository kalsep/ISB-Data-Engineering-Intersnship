from configuration import *

def consolidate_tables(data_directory, output_file):
    final_df_row1 = ['','', 'Nitrogen', 'Nitrogen', 'Nitrogen', 'Phosphorous', 'Phosphorous', 'Phosphorous',
                                   'Potassium', 'Potassium', 'Potassium', 'OC', 'OC', 'EC', 'EC', 'pH', 'pH', 'pH', 'Copper', 'Copper', 'Boron', 'Boron', 'Sulphur', 'Sulphur',
                                   'Sulphur', 'Iron', 'Iron', 'Zinc', 'Zinc', 'Manganese', 'Manganese']
    final_df_row2 = ['State','District', 'High', 'Medium', 'Low', 'High', 'Medium', 'Low', 'High', 'Medium', 'Low',
                                    'Sufficient', 'Deficient', 'Saline', 'Non Saline', 'Acidic', 'Neutral', 'Alkaline', 'Sufficient', 'Deficient', 'Sufficient', 'Deficient', 'High', 'Medium', 'Low',
                                    'Sufficient', 'Deficient', 'Sufficient', 'Deficient', 'Sufficient', 'Deficient']

    # Create a multi-level column index
    final_df_multindex_columns = pd.MultiIndex.from_arrays([final_df_row1, final_df_row2])
    # List to hold dataframes
    all_dataframes = []

    # Loop through each state directory
    for state_dir in os.listdir(data_directory):
        # Define the paths to the micronutrients and macronutrients CSV files
        micro_path = os.path.join(data_directory, state_dir, 'MacroNutrient', 'MacroNutrient.csv')
        macro_path = os.path.join(data_directory, state_dir, 'MicroNutrient', 'MicroNutrient.csv')
        
        try:
            # Read the CSV files
            micro_df = pd.read_csv(micro_path)
            micro_df.insert(0, "State", state_dir)
            macro_df = pd.read_csv(macro_path)
            macro_df = macro_df.iloc[:, 1:]  # Skip the first column which is the index
            
            # Skip if either dataframe is empty
            if micro_df.empty or macro_df.empty:
                continue
            
            # Combine the dataframes side by side
            combined_df = pd.concat([micro_df, macro_df], axis=1)
            
            # Append the combined dataframe to the list
            all_dataframes.append(combined_df)
        except pd.errors.EmptyDataError:
            print(f"Skipping empty or invalid file: {micro_path} or {macro_path}")

    # Concatenate all dataframes into one
    final_dataframe = pd.concat(all_dataframes, ignore_index=True)
    final_dataframe.columns = final_df_multindex_columns
    
    # Save the consolidated data to an Excel file
    output_path = os.path.join(base_path, output_file)
    final_dataframe.to_excel(output_path, engine='openpyxl')

# Call the function with appropriate arguments
consolidate_tables(data_dir, output_file="consolidated_data.xlsx")
