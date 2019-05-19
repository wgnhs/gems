# gems
WGNHS-developed tools and documentation for working with the USGS Geologic Map Schema (GeMS) 

## What's included:  

__Workflow_Overview (PDF):__ This is a general overview of the steps we followed when converting previously-published maps into GeMS

__metadata-to-tables.py:__ A python script for extracting any Enumerated Domain Values and their corresponding definitions from FGDC metadata in .txt format. Outputs a .csv file for each Enumerated Domain. 

__DecodeCodedDomains.tbx:__ An ArcMap toolbox with one tool in it. It references the .py script of the same name. The tool accepts a geodatabase as input, and it turns every coded domain into a table within the database. 
