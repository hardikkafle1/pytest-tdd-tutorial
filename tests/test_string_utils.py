import pytest
from src.string_utils import StringUtils

class TestStringUtils:

    @pytest.fixture
    def util(self):
        return StringUtils()

    def test_reverse(self, util):
        assert util.reverse("hello") == "olleh"
        assert util.reverse("") == ""
        assert util.reverse("a") == "a"

    def test_palindrome(self, util):
        assert util.is_palindrome("racecar") == True
        assert util.is_palindrome("hello") == False
        assert util.is_palindrome("A man a plan a canal Panama") == True

    def test_count_words(self, util):
        assert util.count_words("hello world") == 2
        assert util.count_words("") == 0
        assert util.count_words("   hello   world   ") == 2

    @pytest.mark.parametrize("text, char, expected", [
        ("hello", "l", 2),
        ("hello", "z", 0),
        ("", "a", 0),
        ("aaa", "a", 3)
    ])
    def test_count_character(self, util, text, char, expected):
        assert util.count_character(text, char) == expected