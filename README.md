# Energy Efficiency of Piped Water Supply Systems

M.Tech Project — IIT Bombay (CTARA)  
Kartheek Kolanupaka  

## Overview
This project develops a data-driven framework to assess energy efficiency in rural piped water supply (PWS) systems under India's National Rural Drinking Water Program.

## Key Contributions
- Analyzed energy data from 600+ PWS schemes in Shahpur Taluka
- Built a reusable framework to compute pump-motor efficiency from field measurements:
  - Flow rate (ultrasonic sensors)
  - Electrical power (monitoring units)
  - Pressure and hydraulic head
- Validated on two real systems (Khardi, Rahnvir)

## Key Findings
- Actual energy consumption was **1.4–1.6× higher than design estimates**
- Root causes:
  - Operation away from Best Efficiency Point (BEP)
  - Voltage imbalances
  - Pipeline leakage shifting system duty points

## Code
Includes a Python module for:
- Hydraulic power computation
- Efficiency estimation
- Expected vs actual performance comparison

## Code

This repository includes a modular analysis pipeline:

- `physics.py` – hydraulic and efficiency calculations  
- `features.py` – feature engineering  
- `model.py` – regression model for efficiency prediction  
- `visualize.py` – plots and trend analysis  
- `main.py` – end-to-end pipeline  

The code operationalizes field measurements into a computational framework for analyzing energy efficiency in PWS systems.

## Report
See full report: [PDF link]
