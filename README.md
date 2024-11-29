# DataMaster: Master’s Degree Explorer and Insights Application

DataMaster is a Flask-based web application designed to assist users in exploring and analyzing Master’s degree programs. It provides valuable insights and personalized recommendations to help users make informed decisions about their academic journey.  

---

## Features

- **Comprehensive Course Data**: Scraped and processed data from reliable websites using BeautifulSoup.
- **User-Friendly Filters**: Search for programs based on course preferences, country, and tuition fees.
- **Interactive Map**: View university locations from search results on a dynamic map powered by Folium.
- **Personalized Suggestions**: Get tailored program recommendations through the Gemini-Flash model API integration.
- **Efficient Data Management**: Utilizes a MySQL database for secure and optimized storage and querying of data.

---

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript  
- **Backend**: Flask (Python), REST APIs  
- **Database**: MySQL  
- **Data Processing**: BeautifulSoup (for web scraping), Pandas (for cleaning and transformation)  
- **Data Visualization**: Folium (for interactive maps)

---

## Setup Instructions

Follow these steps to run the application locally:

### Prerequisites
1. Python 3.7+ installed on your system.
2. MySQL installed and a running instance.
3. A virtual environment tool like `venv`.

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repo_url>
   cd <project_directory>
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # For Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**:
   - Create a `.env` file in the project root directory and add the following variables:
     ```plaintext
     FLASK_APP=app.py
     FLASK_ENV=development
     MYSQL_USER=<your_mysql_user>
     MYSQL_PASSWORD=<your_mysql_password>
     MYSQL_HOST=<your_mysql_host>
     MYSQL_DB=<your_database_name>
     GEMINI_API_KEY=<your_gemini_flash_api_key>
     ```

5. **Set up the MySQL database**:
   - Import the database schema:
     ```bash
     mysql -u <user> -p <database_name> < schema.sql
     ```

6. **Run the application**:
   ```bash
   flask run
   ```

   The app will be accessible at `http://127.0.0.1:5000`.

---

## Usage

1. **Search for Programs**: Use filters to refine search results by course, country, and tuition fees.
2. **Explore Recommendations**: Get personalized suggestions using the integrated Gemini-Flash model.
3. **View Interactive Map**: Visualize university locations on a dynamic map.

---

## Future Enhancements

- Add user authentication for personalized dashboards.
- Enable real-time updates of program data.
- Expand data scraping sources for broader coverage.

---

## Contributions

Contributions are welcome! If you'd like to improve this project, feel free to fork the repository and submit a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
