import json
from dbConnection import get_db_connection
import mysql.connector

def get_data(course, country, fees):
    conn = get_db_connection()
    cur = conn.cursor(prepared=True)

    try:
        # First query
        query = """
            SELECT university_name, state, country, course_name, average_fees_in_inr 
            FROM COURSES
            WHERE course = %s AND country = %s AND average_fees_in_inr <= %s;
        """
        cur.execute(query, (course, country, fees))
        x = cur.fetchall()
        
        if not x:
            print("No data found.")
            return None, None

        # Fetch column names
        columns = [desc[0] for desc in cur.description]
        result = [dict(zip(columns, row)) for row in x]

        # Collect university names for the next query
        universities = [item["university_name"] for item in result]

        # Convert to JSON
        json_result = json.dumps(result, indent=4)

        # Second query
        query2 = """
            SELECT university_name, lat, `long` FROM geoData
            WHERE university_name IN ({})
        """.format(','.join(['%s'] * len(universities)))
        cur.execute(query2, tuple(universities))
        geodata = cur.fetchall()

    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        return None, None
    finally:
        conn.close()

    return json_result, geodata

# Example usage
print(get_data("Artificial Intelligence", "Australia", 2500000)[1])
