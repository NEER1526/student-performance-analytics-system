from data_cleaning import clean_data
from database import create_database
from analysis import run_analysis

def main():
    print("Starting Student Performance Analytics System...\n")

    print("Step 1: Cleaning Data...")
    clean_data()

    print("\nStep 2: Creating Database...")
    create_database()

    print("\nStep 3: Running Analysis & Visualizations...")
    run_analysis()

    print("\nProject Execution Completed Successfully!")

if __name__ == "__main__":
    main()