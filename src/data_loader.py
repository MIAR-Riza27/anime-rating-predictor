import requests
from time import sleep
from tqdm import tqdm


def get_top_anime(limit=250, per_page=25, delay=1, verbose=True):
    """
    Fetch top anime data from Jikan API with pagination.

    Parameters:
        limit (int): Total number of anime to fetch.
        per_page (int): Max 25 per API docs.
        delay (int): Delay in seconds between requests to avoid rate limiting.
        verbose (bool): Print progress and errors.

    Returns:
        list: List of anime data dictionaries.
    """
    anime_list = []
    total_pages = (limit + per_page - 1) // per_page

    for page in tqdm(
        range(1, total_pages + 1), desc="Fetching anime", disable=not verbose
    ):
        url = f"https://api.jikan.moe/v4/top/anime?page={page}&limit={per_page}"
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json().get("data", [])
            if not data:
                if verbose:
                    print(f"No data returned at page {page}")
                break
            anime_list.extend(data)
        except requests.RequestException as e:
            if verbose:
                print(f"Request failed at page {page}: {e}")
            break
        sleep(delay)

    return anime_list


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
