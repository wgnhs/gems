# gems
WGNHS-developed tools and documentation for working with the USGS Geologic Map Schema (GeMS) 

## What's included:  

__Workflow_Overview (PDF):__ This is a general overview of the steps we followed when converting previously-published maps into GeMS

__metadata-to-tables.py:__ A python script for extracting any Enumerated Domain Values and their corresponding definitions from FGDC metadata in .txt format. Outputs a .csv file for each Enumerated Domain. 

__DecodeCodedDomains.tbx:__ An ArcMap toolbox with one tool in it. It references the .py script of the same name. The tool accepts a geodatabase as input, and it turns every coded domain into a table within the database. 

__GeMS Layers and Tables Quick Reference:__ This document summarizes all fields for any GeMS layer or table. This mostly reproduces the text in the [GeMS manuscript](https://ngmdb.usgs.gov/Info/standards/GeMS/docs/GeMSv2_draft7g_ProvisionalRelease.pdf). It is meant to be printed so that one layer is summarized on one sheet of paper. We found this useful because it helps narrow down the reference material.
Provided in both .doc and .pdf format. 
