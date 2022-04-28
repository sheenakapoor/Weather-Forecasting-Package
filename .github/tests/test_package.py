"""GitHub Actions tests."""
# pylint: disable=duplicate-code

import os
import requests
import pytest
from weatherfc.weather import forecast


def test_src_dir():
    """Check that src directory exists."""
    assert os.path.exists("src")


def test_pkg_dir():
    """Check that package directory exists."""
    assert os.path.exists("src/weatherfc")


def test_setup():
    """Check that setup script exists."""
    assert os.path.exists("src/setup.py")


def test_license():
    """Check that license exists."""
    assert os.path.exists("src/LICENSE")
    with open("src/LICENSE", encoding="utf-8") as fname:
        assert len(fname.read().strip()) > 0


def test_init():
    """Check that __init__.py exists."""
    assert os.path.exists("src/weatherfc/__init__.py")


def test_bin():
    """Check that executable script in bin exists."""
    assert os.path.exists("src/weatherfc/bin/wfc.py")


def test_package_install():
    """Check that package is installable."""
    assert 0 == os.system("pip install src/")


def test_makefile():
    """Check that makefile file exists."""
    assert os.path.exists("makefile")


def test_precommit_yml():
    """Make sure .pre-commit-config.yaml was made."""
    assert os.path.exists(".pre-commit-config.yaml")


def test_1():
    """Check that the Zip Code is valid."""
    response1 = requests.get("http://www.zip-codes.com/zip-code/15232")
    assert response1.status_code != 404
    response2 = requests.get("http://www.zip-codes.com/zip-code/11111")
    assert response2.status_code == 404


def test_2():
    """Check for valid zip code in function forecast."""
    assert forecast("15232") != 404
    zipcode = "11111"
    resp = requests.get("http://www.zip-codes.com/zip-code/" + zipcode)
    if resp.status_code == 404:
        print(f"Zipcode = {zipcode}, Invalid Zip Code, Try again")


def test_f(capsys):
    """Check for invalid zip code in function forecast."""
    with pytest.raises(SystemExit):
        forecast(111)
    out, err = capsys.readouterr()
    assert (
        out
        == "User's US Post Office ZIP Code: 111 \n\nInvalid Zip Code, Try again\n"  # noqa: E501
    )
    print(out, err)
