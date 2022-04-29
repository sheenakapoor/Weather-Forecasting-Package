#!/usr/bin/env python
"""test file."""
# pylint: disable=duplicate-code
# pylint: disable=E0401

import requests
import pytest
from src.weatherfc.weather import forecast


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
