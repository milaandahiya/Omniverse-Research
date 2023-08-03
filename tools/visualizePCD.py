import open3d as o3d
from time import sleep
from generatePCD import generatePCD
from generatePCD import combinePCD


frames = 117
source = "realsense480p"

vis = o3d.visualization.VisualizerWithKeyCallback()
vis.create_window()

# pcd1 = generatePCD(0, 0, source)
# pcd2 = generatePCD(1, 0, source)
# pcd = combinePCD([pcd1, pcd2])
pcd = generatePCD(0, 0, source)
vis.add_geometry(pcd)
vis.poll_events()
vis.update_renderer()

i = 1
while True:
    if i == frames:
        i = 0
    # pcd1 = generatePCD(0, i, source)
    # pcd2 = generatePCD(1, i, source)
    # tmp = combinePCD([pcd1, pcd2])
    tmp = generatePCD(0, i, source)
    pcd.points = tmp.points
    pcd.colors = tmp.colors
    vis.update_geometry(pcd)
    vis.poll_events()
    vis.update_renderer()
    i += 1
    sleep(0.0167)
