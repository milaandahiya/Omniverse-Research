#Custom Scripts/testingScript
# from omni.isaac.kit import SimulationApp
# simulation_app = SimulationApp(launch_config={"renderer": "RayTracedLighting", "headless": False})

import omni
import numpy as np
import os
import json
from PIL import Image
from omni.isaac.core import World
from omni.isaac.core.objects import DynamicCuboid
import omni.replicator.core as rep
from omni.isaac.core.utils.semantics import add_update_semantics


context = omni.usd.get_context()
# stage = context.get_stage() # Get the current stage in Omniverse
context.open_stage('/home/gjfh119/Documents/USD Files/alien.usd') # Open saved dancing alien stage
print("Opened Stage")

with rep.new_layer():
    # Create cameras (corners of room are -500 to 500 on the x and -250 to 250 on the y)
    camera1 = rep.create.camera(position=(-4900, -2400, 12500), rotation=(90, 0, -53), focus_distance=(100), f_stop=5.2)
    camera2 = rep.create.camera(position=(0, 100, 12500), rotation=(90, 0, 0), focus_distance=(100), f_stop=5.2)
    # ...
    print("Created Cameras")

    # Render frames at 720p
    render_product1 = rep.create.render_product(camera1, (1280, 720))
    render_product2 = rep.create.render_product(camera2, (1280, 720))
    print("Rendered Frames")

    # Write to file
    writer = rep.WriterRegistry.get("BasicWriter")
    writer.initialize(output_dir=f"~/home/gjfh119/Documents/DataOut/", rgb=True, distance_to_camera=True)
    writer.attach([render_product1, render_product2])
    print("Wrote to file")

    # Preview?
    rep.orchestrator.preview()

    # TODO rescale the creation it's like 10x or 100x too big because the camera physics are messed up