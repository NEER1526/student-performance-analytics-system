import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def run_analysis():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    print("\n--- Average Score by Gender ---")
    cursor.execute("""
        SELECT gender, AVG(average_score)
        FROM students
        GROUP BY gender
    """)
    for row in cursor.fetchall():
        print(row)

    print("\n--- Test Preparation Impact ---")
    cursor.execute("""
        SELECT test_preparation_course, AVG(average_score)
        FROM students
        GROUP BY test_preparation_course
    """)
    for row in cursor.fetchall():
        print(row)

    print("\n--- Top 5 Students ---")
    cursor.execute("""
        SELECT math_score, reading_score, writing_score, average_score
        FROM students
        ORDER BY average_score DESC
        LIMIT 5
    """)
    for row in cursor.fetchall():
        print(row)

    print("\n--- Students Below Overall Average ---")
    cursor.execute("""
        SELECT COUNT(*)
        FROM students
        WHERE average_score < (
            SELECT AVG(average_score) FROM students
        )
    """)
    print("Count:", cursor.fetchone()[0])
    df = pd.read_sql_query("SELECT * FROM students", conn)

    # Average Score by Gender
    gender_avg = df.groupby("gender")["average_score"].mean()
    plt.figure()
    gender_avg.plot(kind="bar")
    plt.title("Average Score by Gender")
    plt.ylabel("Average Score")
    plt.show()

    # Test Preparation Impact
    prep_avg = df.groupby("test_preparation_course")["average_score"].mean()
    plt.figure()
    prep_avg.plot(kind="bar")
    plt.title("Impact of Test Preparation Course")
    plt.ylabel("Average Score")
    plt.show()

    # Score Distribution
    plt.figure()
    df["average_score"].plot(kind="hist", bins=20)
    plt.title("Distribution of Average Scores")
    plt.xlabel("Average Score")
    plt.show()


    conn.close()

if __name__ == "__main__":
    run_analysis()