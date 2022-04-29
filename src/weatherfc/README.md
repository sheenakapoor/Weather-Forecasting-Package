# Weather Forecasting

Repository for the project: https://github.com/S22-06682/project-sheenakapoor

Deepnote Project Link: https://deepnote.com/project/06682-Project-9f119166-fb10-4b83-9e96-d148b4f2210a/%2Fproject-sheenakapoor

## Weather Forecasting Package
This github repo hosts a simple code for giving the weather forecast for current temperature,
feels like temperature, and provides weather description.

The purpose of this package:
1. Take input of US Post Office ZIP Code from the user.
2. Retrieve weather data for the ZIP code from http://wttr.in/
3. Display current temperature, 'feels like' temperature in Fahrenheit along with weather description.
4. Convert temperature from Fahrenheit to Celsius.
5. Show an emoji based on range of current temperature that was converted to Celsius units.
6. Display weather forecast for three hours from current time.


Installation (from terminal)
-------------
```python
python -m pip install "git+https://github.com/S22-06682/project-sheenakapoor.git#egg=subdir&subdirectory=src"
```
or

```python
pip install src
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

NOTE
-----
The user can also directly import the weatherfc.example_weather module and be able
to input the zipcode and get the results without writing additional lines of code
for inputting the zipcode.


Scope for additional improvements:
In the future, one could work on defining separate functions for each task performed in
the main script (weather.py)