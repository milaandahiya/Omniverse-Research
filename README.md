# SMU-Omniverse

## Getting started with Omniverse

Download Omniverse [here](https://www.nvidia.com/en-us/omniverse/download/). Once you have the Omniverse launcher running, go to the exchange tab and install the Code app (the Isaac Sim app also contains the Script Editor but has more robotics-related features, so I've found it easier to deal with Code).

Pixar's Universal Scene Description (USD) is the primary scene descriptor used by Nvidia Omniverse. Any programs that can export in USD should be able to import into Omniverse. The dancing alien stage I use is provided in the [example_stage](example_stage) directory.

For example, if you want to import an asset from Blender, Nvidia built a branch of Blender v4.0 (currently in alpha) with improved USD exporting functionality. You can download it at [here](https://builder.blender.org/download/experimental/universal-scene-description/) and select the version for your operating system. [This guide](https://docs.omniverse.nvidia.com/con_connect/con_connect/blender.html) from Nvidia shows you the process for exporting a USD file from Blender (v3.6 but still applicable) and importing it to Omniverse. The documentation from Blender for exporting USD files is [here](https://docs.blender.org/manual/en/4.0/files/import_export/usd.html).

Once you have a stage built (or using the example stage), you may open it in Omniverse Code (or any other Omniverse application) by going to "File" and then "Open", and selecting your USD file. Then you can follow the instructions in the [scripts readme](scripts/README.md) to generate data in Omniverse.

After you have generated data in Omniverse (or used some of the example data provided), you can use any of the Python scripts in [tools](tools) to turn it into RGBD images, point clouds, and visualize them. You can use the same process using the tools after generating RealSense data.

## Notes

You may run `pip install -r requirements.txt` in your environment.

The .vscode directory isn't necessary, but prevents the `import omni` statements from being shown as an error in VSCode. It uses the [app](app) symlink to link to an Omniverse install (Code, Isaac, etc) to get the omni packages. This is only functionally necessary if you are running Omniverse code outside of the Script Editor, which I am not (yet). I would recommend changing the symlink to your path, again, to make it easier to use VSCode.

The [scripts](scripts) directory contains scripts that you can use in the Script Editor inside of Omniverse Code (or Isaac Sim). More info in the `scripts` Readme.

The [tools](tools) directory contains standalone Python scripts for creating a RGBD images, and subsequently point clouds, from the sensor data generated. More info in the `tools` Readme.

The recommended driver versions / hardware for Omniverse can be found [here](https://docs.omniverse.nvidia.com/platform/latest/common/technical-requirements.html). I recommend you install the recommended nvidia driver version on Ubuntu via the "Software & Updates" - "Additional Drivers" settings, by selecting the matching major version (currently 525 on Linux).