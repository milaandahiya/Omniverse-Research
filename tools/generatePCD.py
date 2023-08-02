import open3d as o3d
import numpy as np
from generateRGBD import generateRGBD
import math
import sys


def generatePCD(numCameras: int, image: int, display: bool = True):
    # Get the RGBD image generated from Omniverse/Realsense data
    rgbd_images = []
    for i in range(numCameras):
        rgbd_images.append(generateRGBD(i, image, False))

    # Set camera intrinsic values
    # intrinsics = o3d.camera.PinholeCameraIntrinsic(848, 480, 809, 627, 424, 240) # fx, fy = 1221, 641 for 720p Omniverse
    intrinsics = o3d.camera.PinholeCameraIntrinsic(1280, 720, np.array([[648.2300415, 0, 642.91125488], [0, 648.2300415, 367.93676758], [0, 0, 1]])) # for RealSense

    # Create point clouds
    pcds = []
    for i in range(numCameras):
        pcds.append(o3d.geometry.PointCloud.create_from_rgbd_image(rgbd_images[i], intrinsics))

    # rotate pcd2
    # angle = -37.2 * math.pi / 180
    angle = math.pi
    # pcds[1].rotate([[math.cos(angle), 0, math.sin(angle)], [0, 1, 0], [-math.sin(angle), 0, math.cos(angle)]])
    # pcds[1].translate([0, 0, -0.089])
    # pcd[1].translate([-0.035, 0, -0.026])

    # multiway registration


    # Combine point clouds, and display right side up
    pcd = o3d.geometry.PointCloud()
    for i in range(numCameras):
        pcd += pcds[i]
    pcd.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
    if display:
        o3d.visualization.draw_geometries([pcd])
    return pcd


def main():
    generatePCD(int(sys.argv[1]), int(sys.argv[2]), True)

if __name__ == "__main__":
    main()
