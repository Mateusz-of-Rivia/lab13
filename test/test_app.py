from app import bubble_sort
import pytest

testdata1 = [
    ([4, 2, 5, 3, 1], [1, 2, 3, 4, 5]),
    ([8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8])]


@pytest.mark.parametrize('sample, expected_output', testdata1)
def test_extract_sentiment(sample, expected_output):
    assert bubble_sort(sample) == expected_output
