import os
from PIL import Image, ImageDraw, ImageFont, ImageSequence
from tqdm import tqdm  
import colorsys

def img_to_ascii_art(gif_path, output_folder, font_size=10, distance=5, output_height=300):
    # Open GIF file
    with Image.open(gif_path) as img:
        os.makedirs(output_folder, exist_ok=True)

        # Show progress bar as each frame is processed
        for frame_number, frame in tqdm(enumerate(ImageSequence.Iterator(img)), total=img.n_frames, desc="Processing frames"):
            
            frame = frame.convert("RGBA")
            # Calculate horizontal size while maintaining aspect ratio
            aspect_ratio = frame.width / frame.height
            output_width = int(output_height * aspect_ratio)
            frame = frame.resize((output_width, output_height)) #Convert frame to RGBA and resize
            
            # ASCII 
            ascii_image = Image.new("RGBA", (output_width, output_height), ('#000'))  #if you set this code to #00ff0000, You can get a transparent background image
            draw = ImageDraw.Draw(ascii_image)

            
            try:
                font_path = "/Library/Fonts/Arial.ttf"  
                font = ImageFont.truetype(font_path, font_size)
            except IOError:
                font = ImageFont.load_default() 

            
            char_spacing = distance  

            
            for y in range(0, frame.height, font_size + char_spacing):  
                for x in range(0, frame.width, font_size + char_spacing): 
                    r, g, b, a = frame.getpixel((x, y))
                    if a > 0: 
                        # Select letters based on brightness
                        brightness = (r + g + b) / 3
                        
                        if brightness < 51:
                            char = " "
                        elif brightness < 102:
                            char = "'"
                        elif brightness < 140:
                            char = ":"
                        elif brightness < 170:
                            char = "i"
                        elif brightness < 200:
                            char = "I"
                        elif brightness < 210:
                            char = "J"
                        else:
                            char = "$"
                         
                       
                        if not char == " ":
                            draw.text(
                                (x * output_width // frame.width, y * output_height // frame.height), 
                                char, fill="green", font=font
                            )

            # Save frame PNG
            ascii_image.save(os.path.join(output_folder, f"frame_{frame_number:03d}.png"), format="PNG")

def rgb_to_saturation(r, g, b):
    r_scaled = r / 255.0
    g_scaled = g / 255.0
    b_scaled = b / 255.0

    # Convert RGB to HSV
    h, s, v = colorsys.rgb_to_hsv(r_scaled, g_scaled, b_scaled)

    return s

def frames_to_gif(frames_folder, output_gif_path, duration=100):
    #Get list of PNG frame files (in sorted order)
    frame_files = sorted([f for f in os.listdir(frames_folder) if f.endswith('.png')])
    
    # Load image into frame list
    frames = []
    for file in frame_files:
        frame_path = os.path.join(frames_folder, file)
        frame = Image.open(frame_path).convert("RGBA")  
        # Create a black background image and then composite it
        background = Image.new("RGBA", frame.size, (0, 0, 0, 255))  # If you want a transparent background, set it to 0,0,0,0.
        frame = Image.alpha_composite(background, frame)  
        frames.append(frame.convert("RGB"))  # RGBA support is limited in GIF, so convert to RGB

    # GIF로 저장
    if frames:
        frames[0].save(
            output_gif_path,
            save_all=True,
            append_images=frames[1:],
            duration=duration,
            loop=0
        )
        print(f"GIF saved at {output_gif_path}")
    else:
        print("No frames found to create GIF.")

# 사용 예시
gif_file_path = "input/input.gif"  # GIF file path to convert
output_folder = "output"  #  path to output
output_height = 700  # Set only the vertical size of the output PNG

img_to_ascii_art(gif_file_path, output_folder, font_size= 12, distance= -3, output_height=output_height) 

frames_to_gif(output_folder,output_folder+"/output.gif")