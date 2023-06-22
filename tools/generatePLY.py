import open3d as o3d
from PIL import Image
from generateRGBD import generateRGBD
import numpy as np

# Get the RGBD image generated from Omniverse data
rgbd = generateRGBD(image=10, display=True)

# Set camera intrinsic values
intrinsic = o3d.camera.PinholeCameraIntrinsic(1280, 720, 1500, 1500, 640, 360)

# Create point cloud, translate right side up, and display
pcd = o3d.geometry.PointCloud.create_from_rgbd_image(rgbd, intrinsic)
print(pcd.has_colors())
# pcd.colors = o3d.utility.Vector3dVector(np.array(rgbd.color))
pcd.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
o3d.visualization.draw_geometries([pcd])
