#Custom Scripts/testingScript
import omni
import omni.replicator.core as rep


context = omni.usd.get_context()
stage = context.get_stage() # Get the current stage in Omniverse
# context.open_stage('/home/gjfh119/Documents/USD Files/alien.usd') # Open saved dancing alien stage
print("Retrieved Stage")

# Create cameras (corners of alien stage are -10 to 10 on the x and -5 to 5 on the y/z -- camera units are 1/10th of world units)
camera1 = rep.create.camera(position=(-990, 0, 250),
                            rotation=(0, 0, 180),
                            focal_length=20.0,
                            focus_distance=1000,
                            f_stop=1.8,
                            clipping_range=(0.1, 2500))

camera2 = rep.create.camera(position=(990, 0, 250),
                            rotation=(0, 0, 0),
                            focal_length=20.0,
                            focus_distance=1000,
                            f_stop=1.8,
                            clipping_range=(0.1, 2500))
print("Created Cameras")

# Render frames at 480p
render_product1 = rep.create.render_product(camera1, (848, 480))
render_product2 = rep.create.render_product(camera2, (848, 480))
print("Rendered Frames")

# Write to file
writer = rep.WriterRegistry.get("BasicWriter")
writer.initialize(output_dir="/home/gjfh119/Documents/OmniverseData/", rgb=True, distance_to_image_plane=True)#, camera_params=True)
writer.attach([render_product1, render_product2])
print("Wrote to file")

rep.orchestrator.run()
