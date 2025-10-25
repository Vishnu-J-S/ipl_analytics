# IPL Analytics

A simple project that analyzes IPL data from 2008 to 2017.

## Overview

This project explores various insights and statistics from the Indian Premier League (IPL) dataset.  
The analysis includes trends such as match outcomes, team performances, and individual records over the years.

## Dataset

The data used in this project is obtained from:  
[https://www.kaggle.com/manasgarg/ipl]

It contains detailed match and delivery data from all IPL seasons between **2008 and 2017**.
This data has already been processed and stored in the bundled **SQLite database (`db.sqlite3`)**,  
so you can view results immediately after setting up.

## Features

- Data analysis of IPL seasons (2008–2017)
- Visualization of match trends and team performance
- Insights into batting and bowling efficiency
- Built using **Django** for data APIs and **Google Charts** for visualization

## Tools Used

- Python  
- Django Framework  
- SQLite3  
- Google Charts  

## Setup Instructions
### 1. Create and activate a virtual environment
### 2. Install dependencies
pip install -r requirements.txt
### 4. Run the server directly (database already included)
Since the `db.sqlite3` file is provided, you do not need to run migrations or data import steps.
python manage.py runserver
### 5.Access the application
Open your browser and go to:
http://127.0.0.1:8000/
