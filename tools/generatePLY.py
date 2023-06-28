import open3d as o3d
from PIL import Image
from generateRGBD import generateRGBD
import numpy as np

# Get the RGBD image generated from Omniverse data
rgbd1 = generateRGBD(camera=0, image=1)#, display=True)
rgbd2 = generateRGBD(camera=1, image=1, display=True)

# Set camera intrinsic values
intrinsic = o3d.camera.PinholeCameraIntrinsic(1280, 720, 1500, 1500, 640, 360)

# Create point clouds
pcd1 = o3d.geometry.PointCloud.create_from_rgbd_image(rgbd1, intrinsic)
pcd2 = o3d.geometry.PointCloud.create_from_rgbd_image(rgbd2, intrinsic)

# Compute odometry between RGBD images (not strictly necessary for Omniverse cameras with known translations, but
# probably is necessary for real world cameras)
option = o3d.pipelines.odometry.OdometryOption() # TODO maybe set options
odo_init = np.identity(4)
[success_color_term, trans_color_term, info] = o3d.pipelines.odometry.compute_rgbd_odometry(rgbd1, rgbd2, intrinsic,
                                        odo_init, o3d.pipelines.odometry.RGBDOdometryJacobianFromColorTerm(), option) # colorterm
[success_hybrid_term, trans_hybrid_term, info] = o3d.pipelines.odometry.compute_rgbd_odometry(rgbd1, rgbd2, intrinsic,
                                        odo_init, o3d.pipelines.odometry.RGBDOdometryJacobianFromHybridTerm(), option) # hybridterm

if success_color_term:
    print("RGBD Odometry")
    source_pcd_color_term = o3d.geometry.PointCloud.create_from_rgbd_image(rgbd1, intrinsic)
    source_pcd_color_term.transform(trans_color_term)
    o3d.visualization.draw_geometries([pcd2, source_pcd_color_term])

if success_hybrid_term:
    print("Hybrid RGBD Odometry")
    source_pcd_hybrid_term = o3d.geometry.PointCloud.create_from_rgbd_image(rgbd1, intrinsic)
    source_pcd_hybrid_term.transform(trans_hybrid_term)
    o3d.visualization.draw_geometries([pcd2, source_pcd_hybrid_term])


# Translate right side up, and display
# pcd.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
# o3d.visualization.draw_geometries([pcd])

# pcd1.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
# pcd2.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
# o3d.visualization.draw_geometries([pcd1])
# o3d.visualization.draw_geometries([pcd2])
