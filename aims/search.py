def search_by_title(dvds, keyword):
    """Return DVDs whose titles contain the case-sensitive keyword."""
    return [dvd for dvd in dvds if keyword in dvd.title]
