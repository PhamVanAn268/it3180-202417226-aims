def search_by_category(dvds, category):
    """Return DVDs with the exact category, ignoring case."""
    return [dvd for dvd in dvds if dvd.category.lower() == category.lower()]


def search_by_title(dvds, keyword):
    """Return DVDs whose titles contain the case-insensitive keyword."""
    return [dvd for dvd in dvds if keyword.lower() in dvd.title.lower()]
