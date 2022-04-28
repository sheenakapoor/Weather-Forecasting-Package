# Weather Forecasting

Repository for the project: https://github.com/S22-06682/project-sheenakapoor

## Weather Forecasting Package
This github repo hosts a simple code for giving the weather forecast for current temperature,
feels like temperature, Weather Description.

How to install in another (notebook/ terminal) - 

Installation (from terminal)
-------------
```python
python -m pip install "git+https://github.com/S22-06682/project-sheenakapoor.git#egg=subdir&subdirectory=src"
```

Argument
----------
zipcode: str

         Valid US Postal Zip Code

Returns
-------
out: NoneType

Once installed, you can import the weather forecasting module as follows:

Examples
--------
After typing python in the terminal,

```python
>>> from weatherfc.weather import forecast
>>> forecast(15213)                               #enter user zipcode
```

The output would look something like this - 
```console
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


In the case of an incorrect zipcode, the output looks something like this:

```python
>>> from weatherfc.weather import forecast
>>> forecast(10)
```
```console
User's US Post Office ZIP Code: 10 

Invalid Zip Code, Try again
```

## Command Line Utility
As a command line utility, to use the same function, type wfc.py [zipcode]
For example, wfc.py 15232 would give the following output:

```console
(venv) root@deepnote:~/work/random-directory # wfc.py 15217
User's US Post Office ZIP Code: 15217 

The weather conditions in your location are displayed below:
        Current Temperature: 32°F
        Feels like Temperature: 26°F
        Weather Description: Partly cloudy 
 
The Current Temperature in Celsius is 0.0°C
The Feels-Like Temperature in Celsius is -3.3°C
        
Today's weather in your location: ❄️ 0.0°C 

Weather forecast for three hours from now is as follows:
        Current Temperature: 29°F = -2°C
        Feels like Temperature: 22°F = -5°C
        Weather Description: Clear 

None
```

But in the case of an invalid zipcode, the output looks something like this:

```console
(venv) root@deepnote:~/work # wfc.py 10
User's US Post Office ZIP Code: 10 

Invalid Zip Code, Try again
```