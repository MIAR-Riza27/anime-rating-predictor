import pandas as pd


def fill_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Fill missing values in the DataFrame with specified defaults.
    This function fills missing values for specific columns with predefined values.
    - year: -1
    - season: "Unknown"
    - score: -1
    - scored_by: 0
    - rank: 99999
    - episodes: 0
    - rating: "Unknown"
    - type: "Unknown"
    Args:
        df (pd.DataFrame): The DataFrame to process.
    Returns:
        pd.DataFrame: The DataFrame with missing values filled.
    """
    fill_values = {
        "year": -1,
        "season": "Unknown",
        "score": -1,
        "scored_by": 0,
        "rank": 99999,
        "episodes": 0,
        "rating": "Unknown",
        "type": "Unknown",
    }
    return df.fillna(fill_values)


def convert_types(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert specific columns to appropriate data types.
    This function converts:
    - year, episodes, rank to int
    - type, season, status, source to str (with title case)
    - rating to str (with upper case)
    Args:
        df (pd.DataFrame): The DataFrame to process.
    Returns:
        pd.DataFrame: The DataFrame with converted types.
    """
    for col in ["year", "episodes", "rank"]:
        df[col] = df[col].astype(int)
    return df


def clean_string_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean up string columns: strip, title/upper case.
    This function processes the following columns:
    - type, season, status, source: strip whitespace and convert to title case
    - rating: strip whitespace and convert to upper case
    Args:
        df (pd.DataFrame): The DataFrame to process.
    Returns:
        pd.DataFrame: The DataFrame with cleaned string columns."""
    for col in ["type", "season", "status", "source"]:
        df[col] = df[col].astype(str).str.strip().str.title()
    df["rating"] = df["rating"].astype(str).str.strip().str.upper()
    return df


def list_to_names_str(items):
    """
    Convert a list of dictionaries to a comma-separated string of names.
    If the input is not a list, return an empty string.
    Args:
        items (list): List of dictionaries with a "name" key.
    Returns:
        str: Comma-separated string of names or empty string if input is not a list.
    """
    if isinstance(items, list):
        return ", ".join(i.get("name", "") for i in items if "name" in i)
    return ""


def convert_list_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert list columns (genres, demographics) to comma-separated strings.
    This function processes the following columns:
    - genres: Convert list of dictionaries to a comma-separated string of names.
    - demographics: Convert list of dictionaries to a comma-separated string of names.
    Args:
        df (pd.DataFrame): The DataFrame to process.
    Returns:
        pd.DataFrame: The DataFrame with list columns converted to strings.
    """
    df["genres"] = df["genres"].apply(list_to_names_str)
    df["demographics"] = df["demographics"].apply(list_to_names_str)
    return df


def add_missing_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add indicators for missing year and season.
    This function adds two new columns:
    - has_year: 1 if year is not missing, 0 otherwise
    - has_season: 1 if season is not missing, 0 otherwise
    Args:
        df (pd.DataFrame): The DataFrame to process.
    Returns:
        pd.DataFrame: The DataFrame with new indicator columns added.
    """
    df["has_year"] = df["year"].notna().astype(int)
    df["has_season"] = df["season"].notna().astype(int)
    return df


def drop_duplicates_by_title(df: pd.DataFrame) -> pd.DataFrame:
    """
    Drop duplicate rows based on the 'title' column.
    This function removes rows that have the same title, keeping only the first occurrence.
    Args:
        df (pd.DataFrame): The DataFrame to process.
    Returns:
        pd.DataFrame: The DataFrame with duplicates removed based on title.
    """
    return df.drop_duplicates(subset=["title"])


def filter_impossible_scores(df: pd.DataFrame) -> pd.DataFrame:
    """
    Filter out rows with impossible scores.
    This function keeps rows where:
    - score is -1 (indicating no score)
    - score is between 0 and 10 (inclusive)
    Args:
        df (pd.DataFrame): The DataFrame to process.
    Returns:
        pd.DataFrame: The DataFrame with impossible scores filtered out.
    """
    return df[(df["score"] == -1) | ((df["score"] >= 0) & (df["score"] <= 10))]


def reorder_columns(df: pd.DataFrame, desired_order: list) -> pd.DataFrame:
    """
    Reorder DataFrame columns to a specified order.
    This function rearranges the columns of the DataFrame according to the provided list.
    Args:
        df (pd.DataFrame): The DataFrame to process.
        desired_order (list): List of column names in the desired order.
    Returns:
        pd.DataFrame: The DataFrame with columns reordered.
    """
    return df[desired_order]
