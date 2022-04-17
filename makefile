black: 
	black src

flake8:
	flake8 src

coverage:
	coverage run -m pytest src/weatherfc -s
	coverage report src/weatherfc/*.py

clean:
	rm -fr src/weather.egg-info
	find . -name *.pyc -delete
	find . -type d -name "__pycache__" -exec rm -rf {} +

all: black flake8 coverage clean
