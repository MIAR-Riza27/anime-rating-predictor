import requests
from time import sleep
from tqdm import tqdm

def get_top_anime_all(limit=250, per_page=25):
    """
    Fetch top anime data from Jikan API with pagination.

    Parameters:
        limit (int): Total number of anime to fetch.
        per_page (int): Max 25 per API docs.

    Returns:
        list: List of anime data dictionaries.
    """
    anime_list = []
    total_pages = (limit + per_page - 1) // per_page

    for page in tqdm(range(1, total_pages + 1), desc="Fetching anime"):
        url = f"https://api.jikan.moe/v4/top/anime?page={page}&limit={per_page}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json().get("data", [])
            anime_list.extend(data)
        else:
            print(f"Failed at page {page}, status code: {response.status_code}")
            break

        sleep(1)  # prevent hitting rate limit

    return anime_list