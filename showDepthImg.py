from PIL import Image
import numpy as np

img = np.load("/home/gjfh119/Documents/DataOut/RenderProduct_Replicator/distance_to_camera/distance_to_camera_0000.npy")
pil_img = Image.fromarray(img)
pil_img.show()