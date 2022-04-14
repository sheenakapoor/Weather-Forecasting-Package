from setuptools import setup

setup(
    name="weatherfc",
    version="0.0.1",
    description="weather forecasting",
    maintainer="Sheena Kapoor",
    maintainer_email="sheenak@andrew.cmu.edu",
    license="GPL",
    packages=["weatherfc"],
    scripts=["weatherfc/weatherfc.py", "weatherfc/main.py"],
    setup_requires=[],
    data_files=["LICENSE"],
    # install_requires=[],
    long_description="""\
Weather Description
==============
Handy scripts for the weather forecasting project.
      """,
)

