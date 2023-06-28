#Custom Scripts/testingScript
import omni
import omni.replicator.core as rep


context = omni.usd.get_context()
stage = context.get_stage() # Get the current stage in Omniverse
# context.open_stage('/home/gjfh119/Documents/USD Files/alien.usd') # Open saved dancing alien stage
print("Retrieved Stage")

# Create cameras (corners of room are -10 to 10 on the x and -5 to 5 on the y/z -- camera units are 10x world units)
camera1 = rep.create.camera(position=(-990, 0, 250),
                            rotation=(0, 0, 180),
                            focal_length=20.0,
                            focus_distance=1000,
                            f_stop=1.8,
                            clipping_range=(0.1, 1800))

camera2 = rep.create.camera(position=(-990, -490, 250),
                            rotation=(0, 0, 217),
                            focal_length=20.0,
                            focus_distance=1000,
                            f_stop=1.8,
                            clipping_range=(0.1, 1800))

# ...
print("Created Cameras")

# Render frames at 720p
render_product1 = rep.create.render_product(camera1, (1280, 720))
render_product2 = rep.create.render_product(camera2, (1280, 720))
print("Rendered Frames")

# Write to file
writer = rep.WriterRegistry.get("BasicWriter")
writer.initialize(output_dir="/home/gjfh119/Documents/DataOut/", rgb=True, distance_to_camera=True)
writer.attach([render_product1, render_product2])
print("Wrote to file")

# Preview?
rep.orchestrator.run()
