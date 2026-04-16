import pandas as pd

def build_excel_profiles(profiles):
    profile_names = list(profiles.keys())
    time_steps = list(range(1, 8761))

    # 3. Build the initial Dictionary for the DataFrame dynamically
    df_dict = {"Profile name": time_steps}

    # Loop through the discovered profiles and add them to our dictionary
    for name in profile_names:
        df_dict[name] = profiles[name]

    # Create the core DataFrame
    df = pd.DataFrame(df_dict)

    # 4. Create the sub-header row ("Time step") to match the screenshot's Row 2
    # Initialize a row with empty strings for all columns
    sub_header = {col: "" for col in df.columns}
    # Set the specific text for the first column
    sub_header["Profile name"] = "Time step"

    # Convert it to a DataFrame
    sub_header_df = pd.DataFrame([sub_header])

    # 5. Concatenate the sub-header row on top of the data
    return pd.concat([sub_header_df, df], ignore_index=True)
