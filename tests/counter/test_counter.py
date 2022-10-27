from src.counter import count_ocurrences


def test_counter():
    assert count_ocurrences("src/jobs.csv", "Python") == 1639
    assert count_ocurrences("src/jobs.csv", "Javascript") == 122
