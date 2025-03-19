import cv2
import numpy as np

def cartoonize_image(image_path, save_path):
    # 이미지 불러오기
    img = cv2.imread(image_path)
    if img is None:
        print("이미지를 찾을 수 없습니다.")
        return
    
    img = cv2.resize(img, (600, 600))  # 크기 조정

    # 그레이스케일 변환 및 블러 적용
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)  # 블러 크기를 5로 줄여서 선명도를 높임

    # 엣지 검출 (적응형 이진화)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

    # 색상 단순화 (Bilateral 필터, 강도 감소)
    color = cv2.bilateralFilter(img, 7, 150, 150)  # Bilateral 필터의 강도를 낮춰서 선명도를 유지

    # 엣지와 색상을 합쳐서 만화 스타일 적용
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    # 결과 저장
    cv2.imwrite(save_path, cartoon)
    print(f"변환된 이미지가 {save_path}에 저장되었습니다.")

    # 결과 출력
    cv2.imshow("Cartoonized Image", cartoon)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 입력 및 출력 경로 설정
image_path = r"c:\Users\benet\Desktop\vision\vision2\onepice.jpg"
save_path = r"c:\Users\benet\Desktop\vision\vision2\cartoon_onepice2.png"

# 만화 스타일 변환 실행
cartoonize_image(image_path, save_path)
