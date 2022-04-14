#!/usr/bin/env python

import weather

zipcode = input("User's US Post Office ZIP Code: ")
# print(f"ZIP Code: {zipcode} \n")
weather.forecast(zipcode)
