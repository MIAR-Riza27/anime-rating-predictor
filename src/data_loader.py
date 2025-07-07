import requests
from time import sleep
from tqdm import tqdm


def get_top_anime_all(delay=1, verbose=True):
    """
    Fetch all top anime from Jikan API across all pages.

    Parameters:
        delay (int): Delay in seconds between requests to avoid rate limiting.
        verbose (bool): Print progress and errors.

    Returns:
        list: A list of dictionaries containing anime data.
    """
    anime_list = []
    page = 1

    while True:
        url = f"https://api.jikan.moe/v4/top/anime?page={page}"
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json().get("data", [])
            if not data:
                if verbose:
                    print(f"No more data at page {page}")
                break
            anime_list.extend(data)
            if verbose:
                tqdm.write(f"Fetched page {page}, total anime: {len(anime_list)}")
            page += 1
        except requests.RequestException as e:
            if verbose:
                print(f"Stopped at page {page}, error: {e}")
            break
        sleep(delay)

    return anime_list
