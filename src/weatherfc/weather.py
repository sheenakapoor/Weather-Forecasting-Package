#!/usr/bin/env python
"""Python script."""
# pylint: disable=duplicate-code

# Importing Libraries
import sys
import requests


def forecast(zipcode):
    """Take ZIP Code from User.

    Display Current, 'Feels-like' Temp, Weather Description,
    Convert temp from F to C, Display emojis based on current temp,
    and forecast for the next 3 hours.
    """
    zipcode = str(zipcode)
    # zipcode = input("User's US Post Office ZIP Code: ")
    print(f"User's US Post Office ZIP Code: {zipcode} \n")

    # Generating URL based on User's Postal ZIP Code
    url = "http://wttr.in/" + zipcode

    # Checking for valid Zip Code

    # Generating URL with data of valid US Postal ZIP codes
    checkurl = "http://www.zip-codes.com/zip-code/" + zipcode
    status_code = requests.get(checkurl).status_code

    # Test for validity of user's ZIP code
    if status_code == 404:
        print("Invalid Zip Code, Try again")
        sys.exit()

    # Converting to JSON
    params = (("format", "j1"),)
    response = requests.get(url, params=params).json()

    # Getting the Current Temperature, Feels-Like Temperature, and
    # Weather Description for user's ZIP Code

    # Assigning current condition key to a variable and indexing it
    current_condition = response["current_condition"][0]

    # Assigning variables and indexing to get Current Temperature,
    # Feels-Like Temperature and Weather Description for user's ZIP Code
    temp_f = current_condition["temp_F"]
    feelslikef = current_condition["FeelsLikeF"]
    weatherdesc = current_condition["weatherDesc"][0]["value"]

    # Displaying weather conditions with temperatures in Fahrenheit
    print(
        f"""The weather conditions in your location are displayed below:
        Current Temperature: {temp_f}°F
        Feels like Temperature: {feelslikef}°F
        Weather Description: {weatherdesc} \n """
    )

    # Conversion of Current Temperature and Feels-Like Temperature
    # from F to C respectively.

    # Changing type from str to float for Math Operations
    temp_f_float = float(temp_f)
    feelslikef_float = float(feelslikef)

    def f_to_c(f_temp):
        """Convert the units from Fahrenheit to Celsius."""
        c_temp = (5 / 9) * (f_temp - 32)
        # Rounding output to one decimal place
        c_rounded = round(c_temp, 1)
        return c_rounded

    # Displaying Temperatures in Celsius from the defined function f_to_c
    print(f"The Current Temperature in Celsius is {f_to_c(temp_f_float)}°C")
    print(
        f"""The Feels-Like Temperature in Celsius is {f_to_c(feelslikef_float)}°C
        """
    )

    # Initializing variable for the current temperature obtained in Celsius
    num = f_to_c(temp_f_float)

    # Displaying Emojis for Custom Ranges (4 different ranges) of Current
    # Temperature (in Celsius)

    if num <= 0:
        print(f"Today's weather in your location: \u2744\uFE0F {num}°C \n")
    elif 0.1 <= num <= 15:
        print(f"Today's weather in your location: \u2601\uFE0F {num}°C \n")
    elif 15.1 <= num <= 30:
        print(f"Today's weather in your location: \u26C5 {num}°C \n")
    elif num > 30:
        print(f"Today's weather in your location:\u2600\uFE0F {num}°C \n")

    # Since the JSON output has weather forecast data at a 3 hour time step,
    # retrieving data for 1 time step from now at index 1
    hr3 = response["weather"][0]["hourly"][1]

    print(
        f"""Weather forecast for three hours from now is as follows:
        Current Temperature: {hr3["tempF"]}°F = {hr3["tempC"]}°C
        Feels like Temperature: {hr3["FeelsLikeF"]}°F = {hr3["FeelsLikeC"]}°C
        Weather Description: {hr3["weatherDesc"][0]["value"]} \n"""
    )
