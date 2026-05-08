IMAGE = bestbet

build-image:
	docker build -t $(IMAGE) .

build-tables:
	docker run --rm $(IMAGE) python -m MODELS.createTable
	docker run --rm $(IMAGE) python -m MODELS.populateTable

run:
	docker run --rm -v "$(CURDIR):/app" $(IMAGE) python controller.py
	cmd /c del /Q league_averages.csv league.csv next_games.csv 2>nul

show:
	cmd /c start /B docker run --rm -p 8000:8000 -v "$(CURDIR):/app" bestbet python -m http.server 8000
	cmd /c timeout /t 2 /nobreak > nul
	cmd /c start "" "http://localhost:8000/VIEW/dashboard.html"