#!/usr/bin/env python
"""example file."""

from weatherfc.weather import forecast

zipcode = input("User's US Post Office ZIP Code: ")
forecast(zipcode)  # pylint: disable=E1101
