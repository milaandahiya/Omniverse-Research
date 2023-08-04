# Scripts

`cameraScript.py` is an example script from Nvidia Omniverse documentation that was used to create `testingScript.py`. It is designed to run standalone, but `testingScript.py` is run inside of the Script Editor inside of Omniverse Code ([More details here](https://docs.omniverse.nvidia.com/app_code/prod_extensions/ext_script-editor.html)). I have not gotten the shortcut to personal snippets to work in Code, only Isaac. I think this is a bug, but it's not a huge deal, you just have to manually copy and paste any script into the Script Editor.

`testingScript.py` uses an Omni [Replicator object](https://docs.omniverse.nvidia.com/prod_extensions/prod_extensions/ext_replicator.html) to create the cameras in the open stage (or open stage from file) and then use a [Basic Writer](https://docs.omniverse.nvidia.com/prod_extensions/prod_extensions/ext_replicator/programmatic_visualization.html) to write the RGB and depth data to a folder. There you can set an arbitrary number of cameras and their intrinsics.

To use `testingScript.py`, I currently load my stage in Omniverse Code, paste the code into the script editor, run the simulation, and the run the code in the script editor *after* starting the simulation. This starts the simulation from the top, however due to a lack of disk speed, memory, or both(?), it is inconsistent in how many frames it gathers before freezing or slowing down considerably. I am trying to figure out a way to slowly step the Ominverse simulation each time data is written, as opposed to the current method.

todo show how to add custom script shortcut also save and load layout
