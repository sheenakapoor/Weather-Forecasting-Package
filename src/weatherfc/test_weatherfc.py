#!/usr/bin/env python

import weatherfc
zipcode = input("User's US Post Office ZIP Code: ")
# print(f"ZIP Code: {zipcode} \n")
weatherfc.forecast(zipcode)