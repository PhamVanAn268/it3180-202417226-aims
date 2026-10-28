import unittest
from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title


class SearchTests(unittest.TestCase):
    def test_title_case_insensitive(self):
        lion = DigitalVideoDisc('The Lion King')
        items = [lion, DigitalVideoDisc('Aladdin')]
        self.assertEqual(search_by_title(items, 'lion'), [lion])
        self.assertEqual(search_by_title(items, 'LION'), [lion])

    def test_empty_and_missing_search(self):
        items = [DigitalVideoDisc('The Lion King')]
        self.assertEqual(search_by_title([], 'lion'), [])
        self.assertEqual(search_by_title(items, 'missing'), [])
        self.assertEqual(search_by_title(items, ''), items)
