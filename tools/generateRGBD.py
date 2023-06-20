import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt


# Get color image
color_img = o3d.io.read_image("/home/gjfh119/Documents/DataOut/RenderProduct_Replicator/rgb/rgb_0000.png")

# Load numpy array with depth values and convert to depth image
depth_array = np.load("/home/gjfh119/Documents/DataOut/RenderProduct_Replicator/distance_to_camera/distance_to_camera_0000.npy")
print(depth_array.shape)
depth_img = o3d.geometry.Image(depth_array)

#Create RGBD image from color and depth images
rgbd_img = o3d.geometry.RGBDImage.create_from_color_and_depth(color_img, depth_img, convert_rgb_to_intensity=False)

# Display RGBD image components
f, axarr = plt.subplots(1,2)
axarr[0].imshow(rgbd_img.color)
axarr[1].imshow(rgbd_img.depth)
plt.show()
