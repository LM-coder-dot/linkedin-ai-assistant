# LinkedIn AI Assistant 🤖

Ein KI-gestützter Assistent zur Analyse von LinkedIn-Posts und zur Empfehlung von:
- Kommentaren
- Reposts (mit längeren, kontextbezogenen Texten)
- oder Ignorieren von Beiträgen

## Features
- Relevanz- & Highlight-Scoring
- Unterscheidung Comment vs. Repost
- Integration von Autor & Post-Link
- Dashboard zur Übersicht

## Projektstruktur
# LinkedIn AI Assistant 🤖

Ein KI-gestützter Assistent zur Analyse von LinkedIn-Posts und zur Empfehlung von:
- Kommentaren
- Reposts (mit längeren, kontextbezogenen Texten)
- oder Ignorieren von Beiträgen

## Features
- Relevanz- & Highlight-Scoring
- Unterscheidung Comment vs. Repost
- Integration von Autor & Post-Link
- Dashboard zur Übersicht

## Projektstruktur
analyzer/ # Post-Analyse
collector/ # Feed-Sammlung
llm/ # LLM-Anbindung
recommender/ # Entscheidungslogik
run/ # Run-Skripte
notes/ # Setup & TODOs
storage/ # Persistenz


## Setup
```bash
pip install -r requirements.txt
python run/run_pipeline.py
