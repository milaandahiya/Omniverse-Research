import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt

def generateRGBD(camera: int, image: int, display: bool = False):
    # Get color image
    camera_str = "" if camera == 0 else f"_{camera:{0}{2}}"
    color_img = o3d.io.read_image(f"/home/gjfh119/Documents/DataOut/RenderProduct_Replicator{camera_str}/rgb/rgb_{image:{0}{4}}.png")

    # Load numpy array with depth values, scale (doesn't change pointcloud), and convert to depth image
    depth_array = np.load(f"/home/gjfh119/Documents/DataOut/RenderProduct_Replicator{camera_str}/distance_to_camera/distance_to_camera_{image:{0}{4}}.npy")
    depth_array *= 50
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
