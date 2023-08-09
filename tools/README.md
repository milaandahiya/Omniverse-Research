# Tools

[generateRGBD.py](generateRGBD.py) contains a single function that generates an RGBD image from a png file (color) and numpy file (depth). You can view any RGBD image by running the file with the command line arguments of which camera to use and which frame to see (ex. `python3 generateRGBD.py 0 50 omniverse`). This views the 50th frame of the first (0) camera in the Omniverse directory. The directory to look for the frames is specified in the file.

[generatePCD.py](generatePCD.py) generates a pointcloud from the RGBD images. There is also a function to align 2 pointclouds, but is based on a manual translation in 3D space between the two. You can also view any pointcloud by running the same command line command as [generateRGBD.py](generateRGBD.py). The difference is the last argument must contain a source and resolution combination that matches one of the intrinsics values in the code (ex. `python3 generatePCD.py 0 50 realsense480p`).

> The preset intrinsics values are for the Omniverse cameras in `testingScript.py` and the Intel RealSense D455 depth cameras, both at 480p and 720p.

[visualizePCD.py](visualizePCD.py) loops through each frame in the directory and plays the recorded data as a pointcloud "video". This uses [generatePCD.py](generatePCD.py), and you must set the source/resolution and number of frames in the code, and whether or not you want to combine 2 different cameras. You must set a translation between the 2 different cameras in the **combinePCD** function inside of [generatePCD.py](generatePCD.py), otherwise the center of both of the point clouds will in the same spot and they will overlap. Ctrl-C in the terminal to quit this program, I could not get 'Esc' keypresses to register in the loop.

## For RealSense Cameras

[read_bag_example.py](read_bag_example.py) will display the color and depth feeds from a RealSense recording .bag file

[multicam.py](multicam.py) will record color .png and depth .npy files from multiple RealSense cameras. It uses the same file and directory naming and structure as Omniverse's basic writer, but this is customizable. While viewing the camera feeds and setting the proper values, you can press 's' to start/stop recording. Recording requires the camera output directories to be present in your current working directory, so you can press 'n' to create them. 'Esc' closes the viewer. It also contains code to print out the intrinsic matrices of the connected cameras.