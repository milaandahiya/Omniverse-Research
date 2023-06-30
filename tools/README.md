# Tools

`generateRGBD.py` contains a single function that generates an RGBD image from the data from the cameras in Omniverse. This works as intended.

`generatePLY.py` is supposed to generate a pointcloud from the RGBD images (it imports the generateRGBD function). This does generate a pointcloud from the RGBD images, but that is all I can promise. This is a current WIP, trying to fix: the camera intrinsics, extrinsics to merge multiple point clouds, and the point cloud color. Everything is warped, discolored, and misplaced.