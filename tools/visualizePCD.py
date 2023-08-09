import open3d as o3d
from time import sleep
from generatePCD import generatePCD
from generatePCD import combinePCD


frames = 70         # make sure you have this many frames in the data directory
source = "realsense480p"       # picks the right intrinsics in generatePCD and tells generateRGBD which directory to use
combined = False        # use two cameras and combine them, NOTE must have a translation for the 2 in combinePCD function
singleCamera = 1        # when combined = False, this is the camera to use, ex. 0 or 1

vis = o3d.visualization.Visualizer()
vis.create_window()

# necessary to get first frame of pointcloud to add_geometry outside of loop
if combined:
    pcd1 = generatePCD(0, 0, source)
    pcd2 = generatePCD(1, 0, source)
    pcd = combinePCD([pcd1, pcd2])
else:
    pcd = generatePCD(singleCamera, 0, source)
vis.add_geometry(pcd)
vis.poll_events()
vis.update_renderer()

# NOTE Ctrl-C in the terminal to quit, couldn't get keypresses to register in while loop
i = 1
while True:
    if i == frames:
        i = 0
    if combined:
        pcd1 = generatePCD(0, i, source)
        pcd2 = generatePCD(1, i, source)
        tmp = combinePCD([pcd1, pcd2])
    else:
        tmp = generatePCD(singleCamera, i, source)
    pcd.points = tmp.points
    pcd.colors = tmp.colors
    vis.update_geometry(pcd)
    vis.poll_events()
    vis.update_renderer()
    i += 1
    sleep(0.0167) # set value to get the desired framerate for viewing
