import unittest

from src.custom_language import CustomLanguage


class TestCustomLanguage(unittest.TestCase):
    def test_arithmetic_precedence(self):
        lang = CustomLanguage()
        self.assertEqual(lang.run("1 + 2 * 3"), 7)

    def test_assignment_persists_between_runs(self):
        lang = CustomLanguage()
        lang.run("x = 5")
        self.assertEqual(lang.run("x + 2"), 7)

    def test_reassignment_replaces_value(self):
        lang = CustomLanguage()
        lang.run("x = 5")
        lang.run("x = 10")
        self.assertEqual(lang.run("x"), 10)


if __name__ == "__main__":
    unittest.main()
