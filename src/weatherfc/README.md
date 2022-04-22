# Weather Forecasting

Repository for the project: https://github.com/S22-06682/project-sheenakapoor




have a readme.md file that explains what it is, and how to use it. If you
    have a command line utility, there should be examples of how to use it, and
    the output. If your package is for a notebook you should provide an example
    notebook, including data if it is needed.

## Weather Forecasting Package
This github repo hosts a simple code for giving the weather forecast for current temperature,
feels like temperature, Weather Description.

How to install in another (notebook/ terminal) - 

Installation
-------------
```python
!pip install git+https://github.com/S22-06682/project-sheenakapoor
```

Argument
----------
zipcode: str
         valid US Postal Zip Code

Returns
-------
out: NoneType

Once installed, you can import the weather forecasting module as follows:

Example
--------
```python
>>> from src.weatherfc.weather import forecast
>>> forecast(15213)                               #enter user zipcode
```

The output would look something like this - 
```python
User's US Post Office ZIP Code: 15213 

The weather conditions in your location are displayed below:
        Current Temperature: 51°F
        Feels like Temperature: 51°F
        Weather Description: Sunny 
 
The Current Temperature in Celsius is 10.6°C
The Feels-Like Temperature in Celsius is 10.6°C
        
Today's weather in your location: ☁️ 10.6°C 

Weather forecast for three hours from now is as follows:
        Current Temperature: 46°F = 8°C
        Feels like Temperature: 45°F = 7°C
        Weather Description: Clear 
```