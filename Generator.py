"""
Training and Test Data Generator
"""
import random
import urllib.request
import os
if not os.path.exists("training"):
    os.makedirs("training")
if not os.path.exists("test"):
    os.makedirs("test") 

#training data
for i in range(10):
    tiling_resolution = 11
    column_num = random.randint(200, 400)
    row_num = random.randint(400, 800)
    url = str("https://gibs.earthdata.nasa.gov/wmts/epsg4326/best/Landsat_WELD_NDVI_Global_Monthly/default/2010-04-01/31.25m/" + str(tiling_resolution) + "/" + str(column_num) + "/" + str(row_num) + ".jpg")
    urllib.request.urlretrieve(url, str(i) + ".jpg")
