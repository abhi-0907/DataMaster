import pandas as pd
import numpy as np
from dbConnection import get_db_connnection


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


# Function to insert data into the Courses table
def insert_data_from_csv(csv_file):
    try:
        connection = get_db_connnection()
        df = pd.read_csv(csv_file)

        # Replace NaN values with None
        df = df.replace({np.nan: None})
        
        with connection.cursor() as cursor:
            cursor.execute("USE MASTER_ANALYTICS")
            
            # Insert data into the table
            for _, row in df.iterrows():
                cursor.execute("""
                    INSERT INTO Courses (university_name, state, country, course, course_name, average_fees, currency, average_fees_in_inr)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """, (
                    row['University Name'],
                    row['State'],
                    row['Country'] ,
                    row['course'],
                    row['Course Name'],
                    row['Average Fees (Per Year)'],
                    row['Currency'],
                    row['Average Fees in INR']
                ))

            # Commit the transaction
            connection.commit()
            print(f"Data from {csv_file} inserted successfully")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            connection.close()


# Function to insert data into UniversityLocations
def insert_location_data(csv_file):
    try:
        # Connect to the database
        connection = get_db_connnection()

        # Read the CSV file
        df = pd.read_csv(csv_file)

        with connection.cursor() as cursor:
            cursor.execute("USE MASTER_ANALYTICS")
            cursor.execute("TRUNCATE GeoData")
            # Insert data into the table
            for _, row in df.iterrows():
                # Insert the data into the table with POINT geometry
                cursor.execute("""
                INSERT INTO GeoData (university_name, address, lat, `long`, geometry)
                VALUES (%s, %s, %s, %s, ST_GeomFromText(%s))
                """, (
                    row['University Name'],
                    row['Address'],
                    row['lat'],
                    row['long'],
                    row['geometry']  # MySQL geometry format
                ))
            # Commit the transaction
            connection.commit()
            print(f"Location data from {csv_file} inserted successfully")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            connection.close()




csv_files = list(courses.values())
for file in csv_files:
    insert_data_from_csv(file)

insert_location_data("uni_data\geo_data\geo_data.csv") 

