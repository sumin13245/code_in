from PIL import Image

def add_logo_to_png_with_black_background(png_path, logo_path, output_path, logo_scale=0.3, margin=5):
    """
    PNG 이미지에 검은색 배경을 추가하고, 로고를 오른쪽 아래에 위치시킵니다.
    
    png_path: PNG 파일의 경로
    logo_path: 로고 이미지 파일의 경로
    output_path: 결과 PNG 파일의 경로
    logo_scale: 로고 크기 비율 (원본 PNG에 대해)
    margin: 오른쪽 아래에 위치할 때의 여백
    """
    
    # PNG 파일 열기
    image = Image.open(png_path).convert("RGBA")
    
    # 검은색 배경 생성
    black_background = Image.new("RGB", image.size, (0, 0, 0))
    black_background.paste(image, (0, 0), image)
    
    # 로고 이미지 열기 및 크기 조정
    logo = Image.open(logo_path).convert("RGBA")
    logo_width = int(image.width * logo_scale)
    logo_height = int(logo.height * (logo_width / logo.width))
    logo = logo.resize((logo_width, logo_height), Image.LANCZOS)
    
    # 로고를 오른쪽 아래에 배치
    position = (black_background.width - logo.width - margin, black_background.height - logo.height - margin)
    black_background.paste(logo, position, logo)
    
    # 결과 이미지를 저장
    black_background.save(output_path, format="PNG")

# 사용 예시
input_png_path = "output/frame_000.png"  # 처리할 PNG 파일 경로
logo_path = "input/logo.png"  # 로고 이미지 경로
output_png_path = "output/frame_000_with_logo.png"  # 저장할 PNG 파일 경로

add_logo_to_png_with_black_background(input_png_path, logo_path, output_png_path)