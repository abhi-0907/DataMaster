from flask import Flask, render_template, jsonify, request
import pandas as pd
import folium
from App.static.gemini_model import generate_insights 
import mysql.connector
import json
from cachetools import cached, TTLCache
import os
from dotenv import load_dotenv
load_dotenv()

cache = TTLCache(maxsize=100, ttl=3600)  # Cache up to 100 results for 1 hour

app = Flask(__name__)

@cached(cache)
def get_data(course, country, fees):
    conn = get_db_connection()
    cur = conn.cursor(prepared=True)

    # Use parameterized query without quotes around placeholders
    query = """
        SELECT university_name, state, country, course_name, average_fees_in_inr 
        FROM COURSES
        WHERE course = %s AND country = %s AND average_fees_in_inr <= %s;
    """
    
    # Execute the query with parameters
    cur.execute(query, (course, country, fees))

    # Fetch all results
    x = cur.fetchall()
    print(len(x))

    # Check if any data was fetched
    if not x:
        print("No data found.")
    else:
        print(f"Fetched {len(x)} rows.")

    # Fetch column names (assuming you want them as keys in the JSON result)
    columns = [desc[0] for desc in cur.description]

    # Convert the result into a list of dictionaries
    result = [dict(zip(columns, row)) for row in x]

    universities = [item["university_name"] for item in result]

    # Convert the result to JSON
    json_result = json.dumps(result, indent=4)

    # Getting geo data
    query2 = """
            SELECT university_name, lat, `long` FROM geoData
            WHERE university_name IN ({})
                """

    # Format the universities list as a comma-separated string for the IN clause
    format_strings = ','.join(['%s'] * len(universities))
    query2 = query2.format(format_strings)

    # Execute the query with the list of universities as parameters
    cur.execute(query2, tuple(universities))

    geodata = cur.fetchall()


    # Close the connection
    conn.close()

    return json_result,geodata


def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
        )
        print("Database connection established.")
        return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to the database: {err}")
        raise

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


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/DataFinder")
def datafinder():
    return render_template('datafinder.html')

@app.route("/DataFinder/Results", methods=["POST"])
def datafinder_results():
    # Get form data
    course = request.form['course_preference']
    country = request.form['country_preference']
    max_fees = float(request.form['max_fees'])

    # querying results from database
    json_results, geodata = get_data(course, country, max_fees)

    # # Read the CSV file based on the selected course
    # df = pd.read_csv(courses[course])
    # filtered_df = df[(df["Country"] == country) & (df["Average Fees in INR"] <= max_fees)]
    # # Filter geo_df based on filtered universities
    # universities = filtered_df["University Name"].tolist()
    # geo_df = geo_df[geo_df["University Name"].isin(universities)]
    # # Convert filtered DataFrame to JSON records
    # table_json = filtered_df.to_json(orient="records")

    # Read geo data
    geo_df = pd.read_csv("uni_data/geo_data/geo_data.csv")
    # Create Folium map
    map = folium.Map(location=[20, 0], zoom_start=1)
    # for _, row in geo_df.iterrows():
    #     folium.Marker(
    #         location=[row["lat"], row["long"]],
    #         popup=row["University Name"]
    #     ).add_to(map)

    for row in geodata:
        folium.Marker(
            location=[row[1], row[2]],
            popup=row[0]
        ).add_to(map)
    
    map_html = map._repr_html_()

    # Render the template with the map and data
    return render_template('datafinder_results.html', map_html=map_html, table_json=json_results, course=course, country=country, max_fees=max_fees)

@app.route("/DataInsights")
def datainsights():
    return render_template('datainsights.html')

@app.route("/DataInsights/Results", methods=['POST'])
def datainsights_results():
    course = request.form['course_preference']
    country = request.form['country_preference']
    budget = request.form['budget_preference'] #budget_preference
    content = generate_insights(course, country, budget)
    return render_template('datainsights_results.html', html = content)


if __name__ == "__main__":
    app.run(debug=True)
