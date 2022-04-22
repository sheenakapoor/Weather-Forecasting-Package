"""Install package."""
# pylint: disable=duplicate-code

from setuptools import setup

setup(
    name="weather",
    version="0.0.1",
    description="weather forecasting",
    maintainer="Sheena Kapoor",
    maintainer_email="sheenak@andrew.cmu.edu",
    license="GPL",
    packages=["weatherfc"],
    scripts=[
        "src/weatherfc/weather.py",
        "src/weatherfc/test_weather.py",
        "src/weatherfc/example_weather.py",
        "src/weatherfc/bin/wfc.py",
    ],
    setup_requires=[],
    data_files=["LICENSE"],
    install_requires=[
        "requests",
    ],
    long_description="""\
Weather Description
==============
Handy scripts for the weather forecasting project.
      """,
)
