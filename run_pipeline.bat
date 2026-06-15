@echo off

echo Starting Weather Pipeline...

call venv\Scripts\activate

python scripts\weather_ingestion.py

echo Pipeline Completed Successfully

pause