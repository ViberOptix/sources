# Name: CreateDataLoadingWorkspace.py
# Description: Creates a new DataLoadingWorkspace

# Import required modules
import os
import arcpy

# Source and target workspaces with the mapping of table name to table name.
source = 'D:/data/BKH_Phase6_Cable_Route/BKH_Phase6_Cable_Route/'
target = 'D:/data/BKH_AssetPackage/'
mapping = []

# Fully qualify the table names.
source_target = [(os.path.join(source, a), os.path.join(target, b))
                 for a, b in mapping]
output_workspace = 'D:/data/data'
calc_stats = True

arcpy.dlt.CreateDataLoadingWorkspace(source_target=source_target, output_workspace=output_workspace, calc_stats=calc_stats)
