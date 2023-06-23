import open3d as o3d
from PIL import Image
from generateRGBD import generateRGBD
import numpy as np

# Get the RGBD image generated from Omniverse data
rgbd1 = generateRGBD(camera=0, image=10, display=True)
rgbd2 = generateRGBD(camera=1, image=10, display=True)

# Set camera intrinsic values
intrinsic = o3d.camera.PinholeCameraIntrinsic(1280, 720, 1500, 1500, 640, 360)

# Create point cloud, translate right side up, and display
pcd1 = o3d.geometry.PointCloud.create_from_rgbd_image(rgbd1, intrinsic)
pcd2 = o3d.geometry.PointCloud.create_from_rgbd_image(rgbd2, intrinsic)

# Combine the two point clouds TODO fix orientation with camera extrinsics
pcd = pcd1 + pcd2
pcd.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
o3d.visualization.draw_geometries([pcd])

# pcd1.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
# pcd2.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
# o3d.visualization.draw_geometries([pcd1])
# o3d.visualization.draw_geometries([pcd2])
