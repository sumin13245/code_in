import os
from PIL import Image, ImageSequence

def add_logo(gif_path, logo_path,output_path, logo_scale=0.5, margin=5):

    gif = Image.open(gif_path)
    logo = Image.open(logo_path).convert("RGBA")
    logo_width = int(gif.width * logo_scale)
    logo_height = int(logo.height * (logo_width / logo.width))
    logo = logo.resize((logo_width, logo_height), Image.LANCZOS)
    
    frames = []
    for frame in ImageSequence.Iterator(gif):
        
        frame = frame.convert("RGBA")
        
        position = (frame.width - logo.width - margin, frame.height - logo.height - margin)
        
        frame_with_logo = frame.copy()
        frame_with_logo.paste(logo, position, logo)
        frames.append(frame_with_logo)
        
    if frames:
        frames[0].save(
            output_path,
            save_all=True,
            append_images=frames[1:],
            duration=100,
            loop=0
        )
        print(f"GIF saved at {output_path}")
    else:
        print("No frames found to create GIF.")
    

input_gif_path = "output/output.gif"  # 변환할 GIF 파일 경로
logo_path = "input/logo.png"  # 로고 이미지 경로
output_gif_path = "output/output_logo.gif"  # 저장할 GIF 파일 경로

add_logo(input_gif_path, logo_path, output_gif_path)