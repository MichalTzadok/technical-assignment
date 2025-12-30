# Project Tasks – Assignment Overview

*This repository contains all project tasks.*  
*Each task is implemented in a separate folder, with its own branch, and follows the assignment requirements.*


---

## Table of Contents

* [FastAPI JSON API](#1-fastapi-json-api)  
* [Typer CLI Tool](#2-typer-cli-tool)  
* [VitePress Documentation](#3-vitepress-documentation)  
* [Dockerfile with FFmpeg](#4-dockerfile-with-ffmpeg)  
* [Python Docker Container](#5-python-docker-container)  
* [Coordinate Conversion](#6-coordinate-conversion)  
* [Markdown to PDF](#7-markdown-to-pdf)  
* [Numpy RGB Histogram](#8-numpy-rgb-histogram)  
* [Password Strength Checker](#9-password-strength-checker)  
* [K3s Markdown Description](#10-k3s-markdown-description)  

---

## 1. FastAPI JSON API

**Description:**  
*A simple FastAPI server with two endpoints:*

* `POST /append` → *Append a JSON payload to a local file.*  
* `GET /last` → *Retrieve the last 10 entries from the file.*  

**Folder:** *task1_fastapi*  
**Key Features:** *Timestamp added automatically, data persisted in `data.json`.*

**How to run:**  
```bash
pip install fastapi uvicorn
uvicorn main:app --reload
```

---

## 2. Typer CLI Tool

**Description:**  
*A command-line tool built with Typer to manage JSON data:*

* `add NAME AGE` → *Adds a JSON entry with a timestamp.*  
* `last` → *Shows the last 10 saved entries.*

**Folder:** *task2_typer*  
**Key Features:** *CLI-based JSON management, data persisted in `data.json`.*

**How to run:**  
```bash
pip install typer
python main.py add John 25
python main.py last
```

---

## 3. VitePress Documentation

**Description:**  
*A simple VitePress site with two pages:*

* Landing page describing a fictional software tool (**SuperTool**).  
* Installation guide for the tool.

**Folder:** *task3_vitepress*  
**Key Features:** *Lightweight static documentation website.*

**Notes:**  
* `index.md` → *SuperTool homepage*  
* `install.md` → *Installation guide*

---

## 4. Dockerfile with FFmpeg

**Description:**  
*Dockerfile using an Ubuntu base image that installs `ffmpeg`.*  
*The entrypoint prints the ffmpeg version to verify installation.*

**Folder:** *task4_docker*  

**How to build and run:**  
```bash
docker build -t task4-docker .
docker run --rm task4-docker
```

---

## 5. Python Docker Container

**Description:**  
*Python script using the `docker` package to:*

* Run a BusyBox container.  
* Keep it running with `sleep`.  
* Execute a command inside the container to retrieve the hostname.

**Folder:** *task5_python_docker*  

**How to run:**  
```bash
pip install docker
python main.py
```

---

## 6. Coordinate Conversion

**Description:**  
*Converts geographic coordinates from Decimal Degrees (DD) to Degrees, Minutes, Seconds (DMS).*

**Folder:** *task6_coordinate_conversion*  

**Example Input (`data.json`):**  
```json
{
  "anchorage": {"dd": [-149.9002, 61.2181]},
  "los_angeles": {"dd": [-118.2437, 34.0522]}
}
```

**Output:**  
```json
{
  "anchorage": {"dd": [-149.9002, 61.2181], "dms": [[149, 54, 0.72, "W"], [61, 13, 5.16, "N"]]},
  "los_angeles": {"dd": [-118.2437, 34.0522], "dms": [[118, 14, 37.32, "W"], [34, 3, 7.92, "N"]] }
}
```

**How to run:**  
```bash
python main.py
```

---

## 7. Markdown to PDF

**Description:**  
*Programmatically converts a Markdown document into a PDF file.*

**Folder:** *task7_markdown_to_pdf*  
**Key Features:** *Handles headings, text, and basic formatting.*

**How to run:**  
```bash
pip install markdown pdfkit
python main.py
```

**Output:** *output.pdf*

---

## 8. Numpy RGB Histogram

**Description:**  
*Generates a histogram of RGB values from an image using NumPy and Matplotlib.*

**Folder:** *task8_numpy_histogram*  
**Key Features:** *Visual representation of image color distribution.*

**How to run:**  
```bash
pip install numpy matplotlib opencv-python
python main.py
```

---

## 9. Password Strength Checker

**Description:**  
*Validates passwords based on strict criteria:*

* At least 1 lowercase character  
* At least 1 uppercase character  
* At least 1 digit  
* At least 1 special character  
* Minimum length of 8 characters  
* No character repeated more than twice  
* No sequences of 3 consecutive characters

**Folder:** *task9_password_checker*  

**How to run:**  
```bash
python main.py
```

---

## 10. K3s Markdown Description

**Description:**  
*A short Markdown document describing:*

* What K3s is  
* When it should be used  
* Where it can be used  
* Why it should be used

**Folder:** *task10_k3s_markdown*  

**How to view:**  
*Open `k3s.md` in any Markdown viewer or text editor.*

---

## Instructions for Running Tasks

* Each task has its own folder and can be executed independently.  
* Refer to the `README.md` inside each task folder for detailed instructions.  
* Branches follow the naming convention: `feature/<task-name>`