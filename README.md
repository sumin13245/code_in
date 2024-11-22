README

Code-in

This project provides a suite of tools to transform images, GIFs, and videos into ASCII art. The toolkit includes functionality for adding logos, handling different formats, and exporting results. Below is a brief guide to the main scripts and their purposes.

Features

	1.	Image to ASCII Art Conversion 
	•	Converts each frame of a GIF into ASCII art PNGs.
	•	Combines frames back into an ASCII-styled GIF.
	•	Allows for custom font sizes, distances, and output dimensions.
	2.	Video to ASCII Art Conversion 
	•	Processes videos into ASCII art frame sequences.
	•	Exports results as MP4 videos with synchronized audio 
	•	Supports detailed text-only ASCII frame exports 
	3.	Add Logo to GIFs 
	•	Overlays a logo on GIF frames, maintaining transparency and alignment.
	•	Saves the output as a new GIF.
	4.	Add Logo to PNGs with Background 
	•	Adds a black background to PNGs and overlays a logo in the bottom-right corner.
	•	Outputs results as PNG files.

Installation

	1.	Dependencies: Install required Python libraries.

pip install 

pillow 
moviepy 
tqdm 
natsort

	2.	Fonts: Ensure a compatible font file (e.g., Arial) is accessible on your system. Update the script paths if necessary.

Notes
	•	Output settings, such as font size, spacing, and colors, can be customized within each script.
	•	Ensure all input files (GIFs, videos, logos) are placed in the appropriate directories.

For further assistance or contributions, feel free to improve or modify the scripts as needed!
