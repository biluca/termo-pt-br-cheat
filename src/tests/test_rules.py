import searcher
import json
import pytest


class TestCase:
    @pytest.fixture
    def root(self):
        return "src/tests"

    @pytest.mark.parametrize(
        "scenario",
        (
            ("001"),
            ("002"),
            ("003"),
            ("004"),
        ),
    )
    def test_rules(self, scenario, root):
        rule_file_path = f"{root}/success/{scenario}/rules.json"
        input_file_path = f"{root}/success/{scenario}/input.txt"
        expected_file_path = f"{root}/success/{scenario}/expected.json"

        actual_words_collection = searcher.main(rule_file_path, input_file_path)

        with open(expected_file_path) as expected_file:
            expected_words_colletion = json.load(expected_file)

        assert actual_words_collection == expected_words_colletion

    @pytest.mark.parametrize(
        "scenario",
        (
            ("001"),
            ("002"),
        ),
    )
    def test_should_raise_error(self, scenario, root):
        rule_file_path = f"{root}/error/{scenario}/rules.json"
        input_file_path = f"{root}/error/{scenario}/input.txt"

        with pytest.raises(OverflowError):
            searcher.main(rule_file_path, input_file_path)
