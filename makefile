PYTHON = python

install:
	$(PYTHON) -m pip install -r requirements.txt

build:
	$(PYTHON) -m MODELS.createTable
	$(PYTHON) -m MODELS.populateTable

run:
	$(PYTHON) controller.py
	del /Q league_averages.csv league.csv next_games.csv 2>nul || exit 0

show:
	cmd /c start /B $(PYTHON) -m http.server 8000
	cmd /c timeout /t 2 /nobreak > nul
	cmd /c start "" "http://localhost:8000/VIEW/dashboard.html"