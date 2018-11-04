#!/usr/bin/python3

import requests
# If you are using a Jupyter notebook, uncomment the following line.
#%matplotlib inline
import matplotlib.pyplot as plt
import json
from PIL import Image
from io import BytesIO

from matplotlib.collections import PatchCollection
from matplotlib.patches import Rectangle

import private.py

# Make sure to define this in private.py
assert image_folder

# Replace <Subscription Key> with your valid subscription key.
assert prediction_key

# You must use the same region in your REST call as you used to get your
# subscription keys. For example, if you got your subscription keys from
# westus, replace "westcentralus" in the URI below with "westus".
#
# Free trial subscription keys are generated in the westcentralus region.
# If you use a free trial subscription key, you shouldn't need to change
# this region.
assert vision_base_url

# Set image_path to the local path of an image that you want to analyze.
image_path = image_folder + "messy_wallet.jpg" 

# Read the image into a byte array
image_data = open(image_path, "rb").read()
headers = {'Prediction-Key': prediction_key, 
           'Content-Type': 'application/octet-stream'}
response = requests.post(vision_base_url, headers=headers, data=image_data)
response.raise_for_status()

# The 'analysis' object contains various fields that describe the image. The most
# relevant caption for the image is obtained from the 'description' property.
analysis = response.json()
print(json.dumps(response.json()))

image_caption = analysis["predictions"][0]["tagName"]

# Display the image and overlay it with the caption.
image = Image.open(BytesIO(image_data))
fig, ax = plt.subplots(1)
ax.imshow(image)
width, height = image.size

# Draw all bounding boxes for the image
boxes = []
#for item in analysis["predictions"]:
#    box = item["boundingBox"]
#    bottom_edge = height*(box["top"] + box["height"])
#    left_edge = width*(box["left"])
#    bottom_left = (bottom_edge, left_edge)
#    bound_height = height * box["height"]
#    bound_width = width * box["width"]
#    rect = Rectangle(bottom_left, bound_width, bound_height, fill=False)
#    boxes.append(rect)

analysis["predictions"][0]:
box = item["boundingBox"]
bottom_edge = height*(box["top"] + box["height"])
left_edge = width*(box["left"])
bottom_left = (bottom_edge, left_edge)
bound_height = height * box["height"]
bound_width = width * box["width"]
rect = Rectangle(bottom_left, bound_width, bound_height, fill=False)
boxes.append(rect)

pc = PatchCollection(boxes)
ax.add_collection(pc)

ax.axis("off")
_ = ax.set_title(image_caption, size="x-large", y=-0.1)
plt.show()
