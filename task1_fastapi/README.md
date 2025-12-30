# Task 1 – FastAPI JSON API

## Description
This task implements a simple FastAPI server with two endpoints:
- POST endpoint to receive and store JSON data
- GET endpoint to retrieve the last 10 saved records

## Endpoints

### POST /append
Receives a JSON object and stores it in a local file.
The server saves the data to a local JSON file (data.json).

### GET /last

Returns the last 10 saved records from the file, in the order they were added.


