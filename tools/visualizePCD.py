import open3d as o3d
from time import sleep
from generatePCD import generatePCD


frames = 20

vis = o3d.visualization.Visualizer()
vis.create_window()

pcd = generatePCD(1, 0, False)
vis.add_geometry(pcd)
vis.poll_events()
vis.update_renderer()

for i in range(1, frames):
    pcd.points = generatePCD(1, i, False).points
    vis.update_geometry(pcd)
    vis.poll_events()
    vis.update_renderer()
