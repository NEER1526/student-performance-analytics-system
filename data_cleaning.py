import pandas as pd

def clean_data():
    
    df = pd.read_csv("data.csv")

    
    df.columns = (df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace("/", "_"))

    
    print("Missing values:\n", df.isnull().sum())

    
    df = df.drop_duplicates()

    df["average_score"] = (
        df["math_score"] +
        df["reading_score"] +
        df["writing_score"]
    ) / 3

    
    df.to_csv("cleaned_data.csv", index=False)

    print("Data cleaned and saved as cleaned_data.csv")

if __name__ == "__main__":
    clean_data()