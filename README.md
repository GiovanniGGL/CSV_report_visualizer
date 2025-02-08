# CSV Report Generator

## Overview
A Python-based desktop application for generating visual reports from CSV data files. This tool provides an intuitive interface for loading, viewing, and visualizing time-series data with customizable chart options.

## Features
- **Multiple CSV File Support**: Load and combine multiple CSV files
- **Interactive Data View**: Table view of loaded data
- **Dynamic Chart Generation**: Create customizable line charts
- **Time Series Analysis**: Automatic date parsing and sorting
- **Flexible Data Selection**: Choose specific parameters to visualize
- **Interactive GUI**: User-friendly Tkinter interface
- **Data Export**: Save generated charts

## Data Parameters Supported
- Date/Time
- Power Levels
- MER (Modulation Error Ratio)
- Temperature
- Received Field Strength
- Additional parameters can be added through CSV columns

## Technical Specifications

### Dependencies
- Python 3.x
- tkinter
- pandas
- numpy
- matplotlib

### Data Format Requirements
- CSV files with semicolon (;) delimiter
- Required column: "DATA" (date/time)
- Date format: DD/MM/YYYY


### Data Requirements
CSV files must contain:
```csv
DATA;POTENZA;MER;TEMPERATURA;CAMPO_RICEVUTO
01/01/2024;50;30;25;-65
02/01/2024;51;31;26;-64
...
```
![reportdacsv](https://github.com/user-attachments/assets/5895055f-314d-45cb-98fd-bab53279795e)
