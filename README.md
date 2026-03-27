# Project Description
`miniAnaPipeline` aims to do the following:
- numerically examine combinations and transformations of random variables.
- generate cartesian coordinates and save them to a `csv` file.
- transform them to spherical coordinates and examime the resulting distribution by plotting it and calculating its interesting properties (e.g. mean & mode).

## Prerequisites
To run the code you need `python` minimum version `XX.YY.ZZ`
Additionally, plotting library `matplotlib`


**run** `pip install -r "requirements.txt"`


## `generator.py` 
- Generates cartesian coordinates and saves them to a file.
- create_coords() creates a list of cartesian coordinates.
- save_coords() saves the coordinates to a file.

## "analyze.py" 
- Creates a boxplot