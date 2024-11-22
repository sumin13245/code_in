import os
from PIL import Image
import moviepy.editor as mp
from tqdm import tqdm

image_num = 0

def video_to_ascii_art(video_path, output_folder, font_size=10, density=5, output_height=300, frames_per_file=100):
    video = mp.VideoFileClip(video_path)
    # 출력 폴더가 없으면 생성
    os.makedirs(output_folder, exist_ok=True)
    frame_data = []
    for frame_number, frame in tqdm(enumerate(video.iter_frames()), total=video.reader.nframes, desc="Processing frames"):
       
        frame_image = Image.fromarray(frame)
        frame_image = frame_image.convert("RGBA")
        
        
        aspect_ratio = frame_image.width / frame_image.height
        output_width = int(output_height * aspect_ratio)
        frame_image = frame_image.resize((output_width, output_height))

        
        ascii_frame = ""
        for y in range(0, frame_image.height, font_size + density):  # y축도 간격을 고려하여 증가
            for x in range(0, frame_image.width, font_size + density):  # x축도 간격을 고려하여 증가
                r, g, b, a = frame_image.getpixel((x, y))
                if a > 0:  # 알파 값이 0이 아닐 경우
                    # 색상에 따라 문자 선택
                    brightness = (r + g + b) / 3
                    # 문자 선택
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
                        
                    ascii_frame += char
            ascii_frame += "\n"  # 각 행 끝에서 줄 바꿈

       
        frame_data.append(ascii_frame)

    
    file_num = 0
    for i in range(0, len(frame_data), frames_per_file):
        file_name = os.path.join(output_folder, f"ascii_frames_{file_num}.txt")
        with open(file_name, "w") as file:
            for frame in frame_data[i:i+frames_per_file]:
                file.write(frame + "\n\n")  # 각 프레임 사이에 빈 줄 추가
        file_num += 1



video_file_path = "input/input.mp4"  
output_folder = "output_txt"  
output_height = 700 

video_to_ascii_art(video_file_path, output_folder, font_size=7, density=1, output_height=output_height)