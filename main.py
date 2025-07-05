from src.data_loader import get_top_anime
import json
import os

if __name__ == "__main__":
    print("Fetching top anime data from Jikan API...")
    data = get_top_anime(limit=250)

    os.makedirs("data/raw", exist_ok=True)

    with open("data/raw/top_anime.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("Done! Data saved to data/raw/top_anime.json")