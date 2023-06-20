import open3d as o3d
from generateRGBD import generateRGBD

rgbd = generateRGBD(image="0030", display=True)
# pinhole_camera_intrinsic = {}
# pinhole_camera_extrinsic = {}
# pcd = o3d.geometry.PointCloud.create_from_rgbd_image(rgbd, pinhole_camera_intrinsic)
# o3d.visualization.draw_geometries([pcd])
