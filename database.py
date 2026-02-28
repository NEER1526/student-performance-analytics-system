import sqlite3
import pandas as pd

def create_database():
    # Connect to SQLite database (creates file if not exists)
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    # Drop table if already exists (so we can rerun safely)
    cursor.execute("DROP TABLE IF EXISTS students")

    # Create table
    cursor.execute("""
        CREATE TABLE students (
            gender TEXT,
            race_ethnicity TEXT,
            parental_level_of_education TEXT,
            lunch TEXT,
            test_preparation_course TEXT,
            math_score INTEGER,
            reading_score INTEGER,
            writing_score INTEGER,
            average_score REAL
        )
    """)

    # Load cleaned data
    df = pd.read_csv("cleaned_data.csv")

    # Insert data into table
    df.to_sql("students", conn, if_exists="append", index=False)

    conn.commit()
    conn.close()

    print("Database created and data inserted successfully.")

if __name__ == "__main__":
    create_database()