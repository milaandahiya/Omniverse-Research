# Tools

## For Omniverse

`generateRGBD.py` contains a single function that generates an RGBD image from the data from the cameras in Omniverse. This works as intended.

`generatePLY.py` generates a pointcloud from the RGBD images (it imports the generateRGBD function). It attempts to align two pointclouds. This is a current WIP, multiway registration could potentially make this alignment automatic?

## For RealSense

`read_bag_example.py` will read and display the color and depth feeds from a RealSense recording .bag file

`multicam.py` will record color .png and depth .npy files from two RealSense cameras.
