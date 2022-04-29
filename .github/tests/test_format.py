"""GitHub Actions tests."""
import os


def test_black():
    """Test for black."""
    # Assume this is run in the lecture-09 directory
    assert 0 == os.system("black --check .")


def test_flake8():
    """Test for flake8."""
    assert 0 == os.system("flake8 --count .")


def test_pylint():
    """Test for pylint."""
    assert 0 == os.system("pylint src/")
