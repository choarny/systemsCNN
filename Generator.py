import random
import os
import urllib
import requests

if not os.path.exists('training'):
    os.makedirs('training')
if not os.path.exists('test'):
    os.makedirs('test')

#training data

for i in range(10):
    #tiling_resolution = random.randint(0, 11)
    tiling_resolution = 11
    column_num = 320
    row_num = 640
    #column_num = random.randint(200, 400)
    #row_num = random.randint(400, 800)
    url = str("https://gibs.earthdata.nasa.gov/wmts/epsg4326/best/Landsat_WELD_NDVI_Global_Monthly/default/2010-04-01/31.25m/" + str(tiling_resolution) + "/" + str(column_num) + "/" + str(row_num) + ".jpg")
    r = requests.get(url)
    print(r.content)
    f = open("/Users/ryancho/Documents/Github/systemsCNN/training/" + str(i) + ".jpeg", "w")
    f.write(r.content)
    f.close()
##    os.system("cd training")
##    urllib.urlretrieve(url, str(i) + ".jpg")
##    os.rename("Documents/Github/systemsCNN/"+str(i)+".jpg", "Documents/Github/systemsCNN/training/"+str(i)+".jpg")


#test data
##for i in range(10):
##    tiling_resolution = 11
##    column_num = 320
##    row_num = 640
##    #tiling_resolution = random.randint(0, 11)
##    #column_num = random.randint(200, 400)
##    #row_num = random.randint(400, 800)
##    url = str("https://gibs.earthdata.nasa.gov/wmts/epsg4326/best/Landsat_WELD_NDVI_Global_Monthly/default/2010-04-01/31.25m/" + str(tiling_resolution) + "/" + str(column_num) + "/" + str(row_num) + ".jpg")
##    urllib.requests.urlretrieve(url, str(i) + ".jpg")
