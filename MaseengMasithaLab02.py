# Clipping park shape file from whole study area to the zip area
arcpy.Clip_analysis("parks", "zip", "C://Users/MMasitha/Downloads/Lab_2_Geoprocessing_Python/Lab_2_Geoprocessing_Python/Results/parks_Clip.shp")
# setting up work evironment
from arcpy import env
env.workspace = "C://Users/MMasitha/Downloads/Lab_2_Geoprocessing_Python/Lab_2_Geoprocessing_Python"
# Creating buffer of 500 meters around the facilities and then overlapping them (dissolve tool)
arcpy.Buffer_analysis("Data_Lab_2_Geoprocessing_Python/facilities.shp", "Results/facilities_buffer.shp", "500 METERS")
arcpy.Buffer_analysis("Data_Lab_2_Geoprocessing_Python/facilities.shp", "Results/facilities_buffer.shp", "500 METERS", "", "", "ALL")
# Clipping the bike routes to the zip area 
in_features = "Data_Lab_2_Geoprocessing_Python/bike_routes.shp"
clip_features = "Data_Lab_2_Geoprocessing_Python/zip.shp"
out_features = "Results/bike_Clip.shp"
xy_tolerance = ""
arcpy.Clip_analysis(in_features, clip_features, out_features, xy_tolerance)
