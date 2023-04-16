from PIL import Image
import os
import random
import argparse

# define the paths to your six subfolders
folder_paths = [
    "C:/Users/Hutch/Pictures/GreedyGeckoz_Layers/Background",
    "C:/Users/Hutch/Pictures/GreedyGeckoz_Layers/Clothing",
    "C:/Users/Hutch/Pictures/GreedyGeckoz_Layers/Body",
    "C:/Users/Hutch/Pictures/GreedyGeckoz_Layers/Eyez",
    "C:/Users/Hutch/Pictures/GreedyGeckoz_Layers/Head",
]
image = Image.open ("C:/Users/Hutch/Pictures/GreedyGeckoz_Layers/Background",)

# Path: geckoz_generator.py
from PIL import Image
import os
import random
import argparse

def generate_image():
    # create an empty image to start with
    base_image = Image.new("RGBA", (1000, 1000), (0, 0, 0, 0))

    # loop through each subfolder and randomly pick one layer image file
    for folder_path in folder_paths:
        layer_files = [f for f in os.listdir(folder_path) if f.endswith(".png")]
        if not layer_files:
            raise ValueError(f"No PNG files found in folder {folder_path}")
        layer_path = os.path.join(folder_path, random.choice(layer_files))
        layer_image = Image.open(layer_path).convert("RGBA")

        # resize the layer image if necessary to match the dimensions of the base image
        if layer_image.size != base_image.size:
            layer_image = layer_image.resize(base_image.size)

        # overlay the current layer onto the base image
        base_image = Image.alpha_composite(base_image, layer_image)

    # return the final image
    return base_image

