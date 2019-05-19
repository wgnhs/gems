# Script to extract metadata from some standardized .txt metadata files
# this script accepts FGDC metadata in .txt format, and extracts every enumerated domain to a .csv file. 
# Change the infile and outfolder variables to appropriate values for your project. 

# Python 3.6.7
# Caroline Rose | caroline.rose@wisc.edu | Nov 9, 2018

import re                           # Import the regex module.
import csv                          #csv module
import os               #operating system module


infile = "P:\\Map_Data_Model\\MAPS\\Forest_Co_Pleisto\\Forest_InitialData\\fr_pleis_metadata_mod.txt"
outfolder = "P:\\Map_Data_Model\\MAPS\\Forest_Co_Pleisto\\extracted domains\\"


def findDomains(infile):
    with open (infile, 'rt') as in_file:          # open file for reading text.       
        fileparts = in_file.read().split('Detailed Description:') # split into separate sections, using the phrase "Detailed Description" as a delimiter.    

        for i in fileparts: 
            if "Entity Type:" in i:               #this item contains the description of a layer. 
                layerName = (re.search('Entity Type Label:(.*)\n', i)).group(1)          #extract the name of the layer, which falls between the string "Entity Type Label:" and the next newline. 
                attributeName = (re.search('Attribute Label:(.*)\n', i)).group(1) 
                extractDomain(layerName.strip(), attributeName.strip(), i)

def extractDomain(layerName, attributeName, text):  
    #create empty lists to hold domain values and definitions. 
    domainvalues = []                         # The list where we will store results.
    domaindefs = []
    
    pattern1 = re.compile("Enumerated Domain Value: ", re.IGNORECASE) # Compile regular expression to match lines containing the string
    pattern2 = re.compile("Enumerated Domain Value Definition: ", re.IGNORECASE)
    
    for line in text.split('\n'):
        if pattern1.search(line) != None:          # If pattern search finds a match,
            value = line.split("Value:")[1]        # isolate the text after the string "Value:" 
            v = value.rstrip('\n')                 # strip newline character from the end of the string
            e = v.lstrip()
            domainvalues.append(e) 
        
        if pattern2.search(line) != None: 
            definition = line.split("Definition:")[1]
            d = definition.rstrip('\n')     #strip newlines from the right side of the string
            f = d.lstrip(' ')               #strip spaces from the left side of the string
            domaindefs.append(f)
            
    print("Domain values:", domainvalues)
    # print("Domain defs:", domaindefs)
    
    #Combine the two lists 
    pairedVals = [] #empty list 
    for v in domainvalues: 
        pairList = [v, domaindefs[domainvalues.index(v)]]
        pairedVals.append(pairList)

    

    #output to csv 
    with open(outfolder+layerName+"_"+attributeName+'_domain.csv', 'w') as outfile: 
        writer = csv.writer(outfile, lineterminator='\n')
        writer.writerows(pairedVals)

            
findDomains(infile)
