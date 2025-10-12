import kagglehub
import pandas as pd
import os

def download_dataset(kaggle_src: str) -> str:
    path = kagglehub.dataset_download(kaggle_src)

    for file in os.listdir(path):
        csv_path = os.path.join(path, file)
        return csv_path

    raise FileNotFoundError("No CSV file found in downloaded dataset directory.")

def save_clean_dataset(source_path: str, dest_path: str):
    df = pd.read_csv(source_path)
    df = df.drop(columns="Unnamed: 0")
    df = df.sample(n=1000, random_state=42)

    df.to_csv(dest_path, index=False)

if __name__ == "__main__":
    file_path = download_dataset("maharshipandya/-spotify-tracks-dataset")
    save_clean_dataset(source_path=file_path, dest_path="spotify_dataset.csv")
