import pandas as pd

courses = {
    "Artificial Intelligence": 'uni_data/courses_data/MS_IN_AI.csv',
    "Architecture": 'uni_data/courses_data/MS_IN_Arch.csv',
    "Civil": 'uni_data/courses_data/MS_IN_CIVIL.csv',
    "Computer Science and Engineering": 'uni_data/courses_data/MS_IN_CSE (2).csv',
    "Data Science": 'uni_data/courses_data/MS_IN_DS.csv',
    "Electrical and Electronics": 'uni_data/courses_data/MS_IN_EEE.csv',
    "Electrical and Computers": 'uni_data/courses_data/MS_IN_ELEC_CS (1).csv',
    "Environmental Science": 'uni_data/courses_data/MS_IN_Env_Sci.csv',
    "Finance and Accounts": 'uni_data/courses_data/MS_IN_Fin_Acc.csv',
    "International Relations": 'uni_data/courses_data/MS_IN_Int_Rel.csv',
    "MBA": 'uni_data/courses_data/MS_IN_MBA.csv',
    "Psychology": 'uni_data/courses_data/MS_IN_Pshy.csv',
    "Public health": 'uni_data/courses_data/MS_IN_Pub_health.csv',
    "Software Engineering": 'uni_data/courses_data/MS_IN_SOFT_Eng.csv'
}

# Iterate through each course and process the respective CSV file
for c, i in courses.items():
    try:
        # Read the CSV file
        df = pd.read_csv(i)
        
        # Check if the file has enough columns to insert the new column at index 4
        if len(df.columns) >= 4:
            # Insert the 'course' column at the 4th position (index 4)
            df.insert(4, 'course', c)
        else:
            # If there aren't enough columns, add it at the end or handle accordingly
            df['course'] = c
        
        # Save the modified DataFrame back to the same file
        df.to_csv(i, index=False)
        print(f"Updated {c} data successfully.")
    except Exception as e:
        print(f"Error processing {c} data: {e}")
