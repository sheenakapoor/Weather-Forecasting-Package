#!/usr/bin/env python
"""example file."""
# pylint: disable=duplicate-code

from weatherfc.weather import forecast

zipcode = input("User's US Post Office ZIP Code: ")
forecast(zipcode)
