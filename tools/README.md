# Tools

`generateRGBD.py` contains a single function that generates an RGBD image from a png file (color) and numpy file (depth). You can view any RGBD image by running the file with the command line arguments of which camera to use and which frame to see (ex. `python3 generateRGBD.py 0 50 omniverse`). This views the 50th frame of the first (0) camera in the Omniverse directory. The directory to look for the frames is specified in the file.

`generatePCD.py` generates a pointcloud from the RGBD images. There is also a function to align 2 pointclouds, but is based on a manual translation in 3D space between the two. You can also view any pointcloud by running the same command line command as `generateRGBD.py`. The difference is the last argument must contain a source and resolution combination that matches one of the intrinsics values in the code. The preset intrinsics values are for the Omniverse cameras in `testingScript.py` and the Intel RealSense D455 depth cameras, both at 480p and 720p.

`visualizePCD.py` loops through each frame in the directory and plays the recorded data as a pointcloud "video". This uses `generatePCD.py`, and you must set the source/resolution and number of frames in the code.

## For RealSense

`read_bag_example.py` will display the color and depth feeds from a RealSense recording .bag file

`multicam.py` will record color .png and depth .npy files from multiple RealSense cameras. It uses the same file and directory naming and structure as Omniverse's basic writer, but this is customizable.