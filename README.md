# gems readme:
Tools and documentation for working with the USGS Geologic Map Schema (GeMS), developed at the Wisconsin Geological and Natural History Survey (WGNHS). 
Please direct questions to Caroline at caroline.rose@wisc.edu

All of these compliment the **USGS GeMS official documentation:** https://ngmdb.usgs.gov/Info/standards/GeMS/  

## Resources developed by WGNHS:  


__[Workflow_Overview (PDF)](https://github.com/wgnhs/gems/blob/master/Workflow_Overview_05-19-19.pdf):__ This is a general overview of the steps we followed when converting previously-published maps into GeMS


__[GeMS Layers and Tables Quick Reference](https://github.com/wgnhs/gems/blob/master/GeMS%20Layers%20and%20Tables%20Quick%20Reference_05-31-19.pdf):__ This document summarizes all fields for any GeMS layer or table. This mostly reproduces the text in the [GeMS manuscript](https://ngmdb.usgs.gov/Info/standards/GeMS/docs/GeMSv2_draft7g_ProvisionalRelease.pdf). It is meant to be printed so that one layer is summarized on one sheet of paper. We found this useful because it helps narrow down the reference material.
Provided in both .doc and .pdf format. 

__[GeMS Fields Checklist](https://github.com/wgnhs/gems/blob/master/GeMS_Fields_Checklist_2020-06-08.pdf):__ Checklist for looking through every attribute in a GeMS database; use in concert with the Validate Database script in the USGS GeMS Toolkit. 


### Creating Metadata:  

__[Metadata For GeMS Maps - Step by Step in ArcCatalog](https://github.com/wgnhs/gems/blob/master/Metadata%20For%20GeMS%20Maps%20-%20Step%20by%20Step%20in%20ArcCatalog.pdf):__ Moving step by step through the ArcCatalog interface, correlates the ArcCatalog elements with their eventual FGDC elements. Use this prior to using the USGS Toolkit "FGDC CSDGM2 Metadata" Script. 


__[GeMS Attributes and Metadata](https://github.com/wgnhs/gems/blob/master/MetadataSummaryforGeMSFields_2020-06-05.pdf):__ Summarizes how the attributes in GeMS are described in the metadata after using the USGS GeMS Toolbox script called "FGDC CSDGM2 Metadata". 


### Conference Presentations: 


__DMT2019-Moving-Maps-to-GeMS:__ [Slides](https://github.com/wgnhs/gems/blob/master/DMT2019-Moving-Maps-to-GeMS.pdf) and the [script](https://github.com/wgnhs/gems/blob/master/DMT2019-moving-maps-to-gems-script.pdf) from a presentation at the Digital Mapping Techniques meeting, May 2019, Butte, Montana. An almost identical presentation was given at the NGGDPP workshop in Golden, CO in September of 2019. 

__DMT2020: Moving Maps to GeMS, part2:__ [Slides](https://github.com/wgnhs/gems/blob/master/DMT2020-Moving-Maps-to-GeMS-Part2.pdf) and [script](https://github.com/wgnhs/gems/blob/master/DMT2020-Script-Moving-Maps-to-GeMS-Part2.pdf) from a presentation at the Digital Mapping Techniques web conference, June 2020. 


### Specialty tools: 

__[metadata-to-tables.py](https://github.com/wgnhs/gems/blob/master/metadata-to-tables.py):__ A python script for extracting any Enumerated Domain Values and their corresponding definitions from FGDC metadata in .txt format. Outputs a .csv file for each Enumerated Domain. 

__DecodeCodedDomains.tbx:__ An ArcMap toolbox with one tool in it. It references the .py script of the same name. The tool accepts a geodatabase as input, and it turns every coded domain into a table within the database. 




## Other resources: 


**USGS GeMS Toolkit:** https://github.com/usgs/GeMS_Tools/  

**NCGMP09 on Github:** https://github.com/ncgmp09 

**National Geological and Geophysical Data Preservation Program (NGGDPP) on GitHub:** https://github.com/nggdpp 

**Arizona GS web map of a NCGMP09 map:** https://github.com/azgs/geologic-map-of-arizona
