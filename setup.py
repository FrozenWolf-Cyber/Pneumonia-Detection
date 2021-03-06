# Downloading dataset:
from zipfile import ZipFile
import os
os.environ['KAGGLE_USERNAME'] = "KAGGLE_USERNAME" # username from the json file
os.environ['KAGGLE_KEY'] = "KAGGLE_KEY" # key from the json file
!kaggle datasets download -d paultimothymooney/chest-xray-pneumonia # api copied from kaggle

# Create a ZipFile Object and load chest-xray-pneumonia.zip in it
with ZipFile('chest-xray-pneumonia.zip', 'r') as zipObj:
   # Extract all the contents of zip file in current directory
   zipObj.extractall()
   
# KAGGLE LINK: https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia?rvi=1
   
