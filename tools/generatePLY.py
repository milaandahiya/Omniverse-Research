import open3d as o3d
from generateRGBD import generateRGBD
import math

# Get the RGBD image generated from Omniverse data
# TODO maybe input params
numCameras = 2
image = 1
rgbd_images = []
all = False
for i in range(numCameras):
    rgbd_images.append(generateRGBD(i, image, all))

# Set camera intrinsic values
intrinsic = o3d.camera.PinholeCameraIntrinsic(848, 480, 809, 627, 424, 240) # fx, fy = 1221, 641 for 720p

# Create point clouds
pcds = []
for i in range(numCameras):
    pcds.append(o3d.geometry.PointCloud.create_from_rgbd_image(rgbd_images[i], intrinsic))

# rotate pcd2
# angle = -37.2 * math.pi / 180
angle = math.pi
pcds[1].rotate([[math.cos(angle), 0, math.sin(angle)], [0, 1, 0], [-math.sin(angle), 0, math.cos(angle)]])
pcds[1].translate([0, 0, -0.089])
# pcd[1].translate([-0.035, 0, -0.026])

# multiway registration


# Combine point clouds, and display right side up
pcd = o3d.geometry.PointCloud()
for i in range(numCameras):
    pcd += pcds[i]
pcd.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
o3d.visualization.draw_geometries([pcd])
