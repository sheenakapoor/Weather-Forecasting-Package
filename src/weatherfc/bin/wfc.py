#!/usr/bin/env python
"""The executable script."""
import sys
from weatherfc.weather import forecast

if __name__ == "__main__":
    print(forecast(sys.argv[1]))
