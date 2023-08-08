import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt
import sys

# Returns one RGBD image generated from Omniverse data
# camera and image are both ints formatted to strings with the proper padding
# camera is an int representing which camera to use, using 0-based indexing
# image is an int representing which image to use, using 0-based indexing and always 4 digits (e.g. 0000, 0001, etc.)
# display is a bool representing whether or not to display the RGB and depth image components
def generateRGBD(camera: int, image: int, source: str, display: bool = False):
    # NOTE path is hardcoded
    path = ""
    if source.startswith("omniverse"):
        path = "/home/gjfh119/Documents/example_data/omniverse/RenderProduct_Replicator"
    elif source.startswith("realsense"):
        path = "/home/gjfh119/Documents/example_data/realsense_1/camera"
    else:
        print("Invalid source")
        return
 
    # Get color image
    camera_str = "" if camera == 0 else f"_{camera:{0}{2}}"
    color_img = o3d.io.read_image(f"{path}{camera_str}/rgb/rgb_{image:{0}{4}}.png")

    # Load numpy array with depth values, scale (doesn't change pointcloud), and convert to depth image
    depth_array = np.load(f"{path}{camera_str}/distance_to_image_plane/distance_to_image_plane_{image:{0}{4}}.npy")
    depth_img = o3d.geometry.Image(depth_array)

    #Create RGBD image from color and depth images
    rgbd_img = o3d.geometry.RGBDImage.create_from_color_and_depth(color_img, depth_img, convert_rgb_to_intensity=False)

    # Display RGBD image components
    if display:
        f, plot = plt.subplots(1,2)
        plot[0].imshow(rgbd_img.color)
        plot[1].imshow(rgbd_img.depth)
        f.set_figwidth(12)
        plt.show()

    return rgbd_img


def main():
    generateRGBD(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], True)

if __name__ == "__main__":
    main()
