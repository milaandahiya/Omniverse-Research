import pyrealsense2 as rs
import numpy as np
import cv2
import os


# NOTE set values
resolution = [848, 480]
framerate = 60
min_distance = 0.1
max_distance = 4


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
    config.enable_stream(rs.stream.depth, resolution[0], resolution[1], rs.format.z16, framerate)
    config.enable_stream(rs.stream.color, resolution[0], resolution[1], rs.format.bgr8, framerate)
    pipelines.append(pipeline)
    configs.append(config)

# start streaming from each camera
for i in range(num_cameras):
    pipelines[i].start(configs[i])

# get the first camera's intrinsics
# intrinsics = pipelines[0].get_active_profile().get_stream(rs.stream.depth).as_video_stream_profile().get_intrinsics()
# camera_matrix = np.array([[intrinsics.fx, 0, intrinsics.ppx], [0, intrinsics.fy, intrinsics.ppy], [0, 0, 1]])
# print(camera_matrix)

# vars
last_ch = -1
frame_count = 0
recording = False
sized = False
pwd = os.getcwd()
# NOTE The spatial and temporal filters reduce framerate, and I haven't gotten the decimation filter to work
# dec_filter = rs.decimation_filter ()   # Decimation - reduces depth frame density
# spat_filter = rs.spatial_filter()          # Spatial    - edge-preserving spatial smoothing
# temp_filter = rs.temporal_filter()       # Temporal   - reduces temporal noise
colorizer = rs.colorizer(0) # 0 = jet colormap
colorizer.set_option(rs.option.visual_preset, 1) # 0=Dynamic, 1=Fixed, 2=Near, 3=Far
colorizer.set_option(rs.option.min_distance, min_distance) # min distance in meters
colorizer.set_option(rs.option.max_distance, max_distance) # max distance in meters


# NOTE: this loop is currently hard-coded for 2 cameras, but can be easily extended to more cameras
try:
    while True:
        # Camera 1
        # Wait for a coherent pair of frames: depth and color
        frames_1 = pipelines[0].wait_for_frames()
        depth_frame_1 = frames_1.get_depth_frame()
        color_frame_1 = frames_1.get_color_frame()
        if not depth_frame_1 or not color_frame_1:
            continue
        # depth_frame_1 = dec_filter.process(depth_frame_1)
        # depth_frame_1 = spat_filter.process(depth_frame_1)
        # depth_frame_1 = temp_filter.process(depth_frame_1)

        # Convert images to numpy arrays
        depth_image_1 = np.asanyarray(colorizer.colorize(depth_frame_1).get_data())
        color_image_1 = np.asanyarray(color_frame_1.get_data())

        # Camera 2
        # Wait for a coherent pair of frames: depth and color
        frames_2 = pipelines[1].wait_for_frames()
        depth_frame_2 = frames_2.get_depth_frame()
        color_frame_2 = frames_2.get_color_frame()
        if not depth_frame_2 or not color_frame_2:
            continue
        # depth_frame_2 = dec_filter.process(depth_frame_2)
        # depth_frame_2 = spat_filter.process(depth_frame_2)
        # depth_frame_2 = temp_filter.process(depth_frame_2)

        # Convert images to numpy arrays
        depth_image_2 = np.asanyarray(colorizer.colorize(depth_frame_2).get_data())
        color_image_2 = np.asanyarray(color_frame_2.get_data())

        # Stack images
        camera1_images = np.hstack((color_image_1, depth_image_1))
        camera2_images = np.hstack((color_image_2, depth_image_2))
        images = np.vstack((camera1_images, camera2_images))

        # Show images from both cameras
        cv2.namedWindow('RealSense', cv2.WINDOW_NORMAL)
        cv2.imshow('RealSense', images)
        if not sized:
            cv2.resizeWindow('RealSense', 1280, 720)
            sized = True

        # NOTE:
        # starts to save "record" images and depth maps from both cameras by pressing 's', stops by pressing 's' again
        # prints index of frame being saved
        # press n to create folders for saving images and depth maps (must do before pressing 's' if folders don't exist)
        # press esc to quit
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
            np.save(f"{pwd}/camera/distance_to_image_plane/distance_to_image_plane_{frame_count:{0}{4}}.npy", depth_image_1)
            # camera 2
            cv2.imwrite(f"{pwd}/camera_01/rgb/rgb_{frame_count:{0}{4}}.png", color_image_2, [cv2.IMWRITE_PNG_COMPRESSION, 0])
            np.save(f"{pwd}/camera_01/distance_to_image_plane/distance_to_image_plane_{frame_count:{0}{4}}.npy", depth_image_2)
            # update frame count
            print(frame_count)
            frame_count += 1
        last_ch = ch

finally:
    for i in range(num_cameras):
        pipelines[i].stop()
