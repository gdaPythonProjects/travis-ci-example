from unittest import TestCase

from main import addValues


class TestAddValues(TestCase):
    def test_add_values(self):
        result = addValues(4,3)
        assert result == 7, "so sad..."
