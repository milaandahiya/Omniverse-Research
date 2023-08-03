import open3d as o3d
import numpy as np
from generateRGBD import generateRGBD
import math
import sys


def generatePCD(camera: int, image: int, source: str):
    # Get the RGBD image generated from Omniverse/Realsense data
    rgbd_image = generateRGBD(camera, image, source)

    # check preset intrinsics values
    # NOTE intrinsic parameter may be a string or an o3d.camera.PinholeCameraIntrinsic object
    if source == "omniverse480p":
        intrinsics = o3d.camera.PinholeCameraIntrinsic(848, 480, 809, 627, 424, 240)
    elif source == "omniverse720p":
        intrinsics = o3d.camera.PinholeCameraIntrinsic(1280, 720, 1221, 641, 640, 360)
    elif source == "realsense480p":
        intrinsics = o3d.camera.PinholeCameraIntrinsic(848, 480, np.array([[429.45239258, 0, 425.92871094], [0, 429.45239258, 245.25810242], [0, 0, 1]]))
    elif source == "realsense720p":
        intrinsics = o3d.camera.PinholeCameraIntrinsic(1280, 720, np.array([[648.2300415, 0, 642.91125488], [0, 648.2300415, 367.93676758], [0, 0, 1]]))
    else:
        print("No intrinsics provided")
        return
    
    # Combine point clouds, and display right side up
    pcd = o3d.geometry.PointCloud.create_from_rgbd_image(rgbd_image, intrinsics)
    pcd.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
    return pcd


def combinePCD(pcds: list):
    # do whatever translations necessary to align the point clouds (ex. ICP)
    # this is a specific rotation/translation for omniverse
    angle = math.pi
    pcds[1].rotate([[math.cos(angle), 0, math.sin(angle)], [0, 1, 0], [-math.sin(angle), 0, math.cos(angle)]])
    pcds[1].translate([0, 0, 0.0089])

    # combine point clouds
    pcd = o3d.geometry.PointCloud()
    for p in pcds:
        pcd += p
    
    return pcd


def main():
    pcd = generatePCD(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3])
    o3d.visualization.draw_geometries([pcd])

if __name__ == "__main__":
    main()
