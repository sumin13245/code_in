import os
from PIL import Image, ImageDraw, ImageFont
import moviepy.editor as mp
from tqdm import tqdm
import colorsys
import natsort


def video_to_ascii_art(video_path, output_folder, font_size=10, distance=5, output_height=300):
    video = mp.VideoFileClip(video_path)
   
    os.makedirs(output_folder, exist_ok=True)

    for frame_number, frame in tqdm(enumerate(video.iter_frames()), total=video.reader.nframes, desc="Processing frames"):
        # 프레임을 이미지로 변환
        frame_image = Image.fromarray(frame)
        frame_image = frame_image.convert("RGBA")
        
        aspect_ratio = frame_image.width / frame_image.height
        output_width = int(output_height * aspect_ratio)
        frame_image = frame_image.resize((output_width, output_height))


        ascii_image = Image.new("RGBA", (output_width, output_height), (0, 0, 0, 0))  # 새로운 투명한 이미지 생성
        draw = ImageDraw.Draw(ascii_image)

        try:
            font_path = "/Library/Fonts/Arial.ttf" 
            font = ImageFont.truetype(font_path, font_size)
        except IOError:
            font = ImageFont.load_default()  

        for y in range(0, frame_image.height, font_size + distance):  
            for x in range(0, frame_image.width, font_size + distance): 
                r, g, b, a = frame_image.getpixel((x, y))
                if a > 0: 
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
                        
                    if char != " ":
                        draw.text(
                            (x * output_width // frame_image.width, y * output_height // frame_image.height),
                            char, fill="#00ff22", font=font
                        )

        
        ascii_image.save(os.path.join(output_folder, f"frame_{frame_number:03d}.png"), format="PNG")
    return frame_number - 1


def make_mp4(frame_num,video_file_path,output_folder):
    video = mp.VideoFileClip(video_file_path)
    audio = video.audio
    ascii_frame_files = sorted([os.path.join(output_folder, f"frame_{i:03d}.png") for i in range(frame_num)])
    ascii_frame_files = natsort.natsorted(ascii_frame_files)

    ascii_clip = mp.ImageSequenceClip(ascii_frame_files, fps=video.fps)

    # add original sound
    final_video = ascii_clip.set_audio(audio)

  
    final_video.write_videofile(os.path.join(output_folder, "ascii_art_video.mp4"), codec="libx264", audio_codec="aac")


def rgb_to_saturation(r, g, b):
    r_scaled = r / 255.0
    g_scaled = g / 255.0
    b_scaled = b / 255.0
    h, s, v = colorsys.rgb_to_hsv(r_scaled, g_scaled, b_scaled)
    return s

## 사용 예시
video_file_path = "input/input.mp4"  
output_folder = "output_video"  
output_height = 700  
frame_num = video_to_ascii_art(video_file_path, output_folder, font_size=8, distance=-3, output_height=output_height)

make_mp4(frame_num,video_file_path,output_folder)

