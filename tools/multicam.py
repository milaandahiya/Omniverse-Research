import pyrealsense2 as rs
import numpy as np
import cv2
import os


# get all connected camera serials
context = rs.context()
num_cameras = len(context.devices)
camera_serials = []
for i in range(num_cameras):
    serial_num = context.devices[i].get_info(rs.camera_info.serial_number)
    camera_serials.append(serial_num)

# config streams for each camera (assuming same config for each)
pipelines = []
configs = []
for i in range(num_cameras):
    pipeline = rs.pipeline()
    config = rs.config()
    config.enable_device(camera_serials[i])
    config.enable_stream(rs.stream.depth, 1280, 720, rs.format.z16, 30)
    config.enable_stream(rs.stream.color, 1280, 720, rs.format.bgr8, 30)
    pipelines.append(pipeline)
    configs.append(config)

# start streaming from each camera
for i in range(num_cameras):
    pipelines[i].start(configs[i])

# get the first camera intrinsics (assumes others are identical)
intrinsics = pipelines[0].get_active_profile().get_stream(rs.stream.depth).as_video_stream_profile().get_intrinsics()
camera_matrix = np.array([[intrinsics.fx, 0, intrinsics.ppx], [0, intrinsics.fy, intrinsics.ppy], [0, 0, 1]])

last_ch = -1
frame_count = 0
recording = False
sized = False
pwd = os.getcwd()

#NOTE: this loop is currently hard-coded for 2 cameras for speed, but can be easily extended to more cameras
try:
    while True:
        # Camera 1
        # Wait for a coherent pair of frames: depth and color
        frames_1 = pipelines[0].wait_for_frames()
        depth_frame_1 = frames_1.get_depth_frame()
        color_frame_1 = frames_1.get_color_frame()
        if not depth_frame_1 or not color_frame_1:
            continue
        # Convert images to numpy arrays
        depth_image_1 = np.asanyarray(depth_frame_1.get_data())
        color_image_1 = np.asanyarray(color_frame_1.get_data())
        # Apply colormap on depth image (image must be converted to 8-bit per pixel first)
        depth_colormap_1 = cv2.applyColorMap(cv2.convertScaleAbs(depth_image_1, alpha=0.05), cv2.COLORMAP_JET)

        # Camera 2
        # Wait for a coherent pair of frames: depth and color
        frames_2 = pipelines[1].wait_for_frames()
        depth_frame_2 = frames_2.get_depth_frame()
        color_frame_2 = frames_2.get_color_frame()
        if not depth_frame_2 or not color_frame_2:
            continue
        # Convert images to numpy arrays
        depth_image_2 = np.asanyarray(depth_frame_2.get_data())
        color_image_2 = np.asanyarray(color_frame_2.get_data())
        # Apply colormap on depth image (image must be converted to 8-bit per pixel first)
        depth_colormap_2 = cv2.applyColorMap(cv2.convertScaleAbs(depth_image_2, alpha=0.05), cv2.COLORMAP_JET)

        # Stack images
        camera1_images = np.hstack((color_image_1, depth_colormap_1))
        camera2_images = np.hstack((color_image_2, depth_colormap_2))
        images = np.vstack((camera1_images, camera2_images))

        # Show images from both cameras
        cv2.namedWindow('RealSense', cv2.WINDOW_NORMAL)
        cv2.imshow('RealSense', images)
        if not sized:
            cv2.resizeWindow('RealSense', 1280, 720)
            sized = True

        # starts to save images and depth maps from both cameras by pressing 's', stops by pressing 's' again
        # press esc to quit
        # press n to create folders for saving images and depth maps (must do before pressing 's' if folders don't exist)
        ch = cv2.pollKey()
        if ch==27:
            cv2.destroyAllWindows()
            break

        if ch==110:
            os.makedirs(f"{pwd}/camera/rgb", exist_ok=True)
            os.makedirs(f"{pwd}/camera/distance_to_image_plane", exist_ok=True)
            os.makedirs(f"{pwd}/camera_01/rgb", exist_ok=True)
            os.makedirs(f"{pwd}/camera_01/distance_to_image_plane", exist_ok=True)

        if ch==115 and last_ch==-1:
            recording = not recording
            frame_count = 0

        if recording:
            # camera 1
            cv2.imwrite(f"{pwd}/camera/rgb/rgb_{frame_count:{0}{4}}.png", color_image_1, [cv2.IMWRITE_PNG_COMPRESSION, 0])
            np.save(f"{pwd}/camera/distance_to_image_plane/distance_to_image_plane_{frame_count:{0}{4}}.npy", depth_colormap_1)
            # camera 2
            cv2.imwrite(f"{pwd}/camera_01/rgb/rgb_{frame_count:{0}{4}}.png", color_image_2, [cv2.IMWRITE_PNG_COMPRESSION, 0])
            np.save(f"{pwd}/camera_01/distance_to_image_plane/distance_to_image_plane_{frame_count:{0}{4}}.npy", depth_colormap_2)
            # update frame count
            print(frame_count)
            frame_count += 1
        last_ch = ch

finally:
    for i in range(num_cameras):
        pipelines[i].stop()
