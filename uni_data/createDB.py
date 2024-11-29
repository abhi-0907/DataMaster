from dbConnection import get_db_connnection

# Connect to MySQL
connection = get_db_connnection()

# Create database and table
try:
    with connection.cursor() as cursor:
        # Create database
        cursor.execute("CREATE DATABASE IF NOT EXISTS MASTER_ANALYTICS")

        # Use the database
        cursor.execute("USE MASTER_ANALYTICS")

        # Create table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Courses (
            id INT AUTO_INCREMENT PRIMARY KEY,
            university_name VARCHAR(255),
            state VARCHAR(100),
            country VARCHAR(100),
            course VARCHAR(255),
            course_name VARCHAR(255),
            average_fees FLOAT,
            currency VARCHAR(10),
            average_fees_in_inr FLOAT
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS GeoData (
            id INT AUTO_INCREMENT PRIMARY KEY,
            university_name VARCHAR(255),
            address TEXT,
            lat FLOAT,
            `long` FLOAT,
            geometry GEOMETRY
        )
        """)
finally:
    connection.close()
