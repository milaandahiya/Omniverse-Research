# Getting started with Omniverse

Download Omniverse from here: https://www.nvidia.com/en-us/omniverse/download/. Once you have Omniverse running, go to the exchange tab and install the Code app (The Isaac Sim app also works but has more unnecessary robotics bloat, so I've found it easier to deal with Code.)

Pixar's Universal Scene Description (USD) is the primary scene descriptor used by Nvidia Omniverse. Nvidia built a branch of Blender v4.0 (currently in alpha) with improved USD exporting functionality. You can download it at: https://builder.blender.org/download/experimental/universal-scene-description/ and select the version for your operating system. You can use this (or anything else that supports USD I think) to import your existing assets into Omniverse.

This guide from Nvidia shows you the process for exporting a USD file from Blender (v3.6 but still applicable) and importing it to Omniverse: https://docs.omniverse.nvidia.com/con_connect/con_connect/blender.html. The documentation for exporting this from Blender is here: https://docs.blender.org/manual/en/4.0/files/import_export/usd.html.

You may also use the Nvidia Nucleus connector in Omniverse to import/export USDs to a local or remote Omniverse server: https://docs.omniverse.nvidia.com/con_connect/con_connect/blender/nucleus-connector.html#blender-nucleus-connector. I have not tested this yet as I am working on everything locally.

## Notes

The .vscode isn't necessary but prevents the `import omni` statements from being shown as an error in VSCode. It uses the `app` symlink to link to an Omniverse install (Code, Isaac, etc) to get the omni packages. This is only functionally necessary if you are running Omniverse code outside of the Script Editor, which I am not (yet).

`scripts` contains scripts that you can paste into the Script Editor inside of Omniverse Code (or Isaac Sim). More info in the `scripts` Readme.

`tools` contains standalone Python scripts for creating a RGBD images, and subsequently point clouds, from the sensor data generated. More info in the `tools` Readme.