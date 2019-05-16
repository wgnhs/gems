def main():  
    import arcpy, os  
    #~~~~~

    #get parameters from dialog box
    gdb = arcpy.GetParameterAsText(0)

    #~~~~~


    # global variables
    arcpy.env.workspace = gdb	

    #gdb = r"P:\Map_Data_Model\MAPS\Pierce-StCroix_Bedrock\Pierce-StCroix_Working_V1.gdb"  
    arcpy.env.overwriteOutput = True  
  
    for dom in arcpy.da.ListDomains(arcpy.env.workspace):  
        if dom.domainType == 'CodedValue':  
            arcpy.DomainToTable_management(in_workspace=arcpy.env.workspace,  
                                          domain_name=dom.name,  
                                          out_table=os.path.join(arcpy.env.workspace, dom.name),  
                                          code_field=dom.name + "Code",  
                                          description_field= dom.name + "Description",  
                                          configuration_keyword="")  
  
            print " - domain '{0}' of type '{1}' exported to table".format(dom.name, dom.domainType)  

        elif dom.domainType == 'Range':  
            arcpy.DomainToTable_management(in_workspace=arcpy.env.workspace,  
                                          domain_name=dom.name,  
                                          out_table=os.path.join(arcpy.env.workspace, dom.name),  
                                          code_field=dom.name + "Code",  
                                          description_field= dom.name + "Description",  
                                          configuration_keyword="")  

            print('Min: {0}'.format(dom.range[0]))
            print('Max: {0}'.format(dom.range[1]))

        else:  
            print " - domain '{0}' of type '{1}' skipped".format(dom.name, dom.domainType)  
  
if __name__ == '__main__':  
    main()  