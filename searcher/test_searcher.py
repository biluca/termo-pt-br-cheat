import pytest
import json
from searcher import searcher


class TestSearcher:
    @pytest.mark.parametrize(
        "scenario,",
        [
            "001",
            "002",
            "003",
        ],
    )
    def test_searcher(self, scenario):
        with open(f"searcher/tests/{scenario}/expected.json") as json_file:
            expected_words_collection = json.load(json_file)

        actual_words_collection = searcher.main(
            f"searcher/tests/{scenario}/rules.json",
            f"searcher/tests/{scenario}/input.txt",
        )
        assert actual_words_collection == expected_words_collection

    @pytest.mark.parametrize(
        "scenario,",
        [
            "004",
            "005",
        ],
    )
    def test_should_raise_error(self, scenario):
        with pytest.raises(OverflowError):
            searcher.main(
                f"searcher/tests/{scenario}/rules.json",
                f"searcher/tests/{scenario}/input.txt",
            )
