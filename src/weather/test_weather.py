#!/usr/bin/env python
"""example file."""

import weather

zipcode = input("User's US Post Office ZIP Code: ")
weather.forecast(zipcode)   # pylint: disable=E1101
