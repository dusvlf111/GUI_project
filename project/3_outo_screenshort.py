from PIL import (
    ImageGrab
)

import time

time.sleep(5)   # 5초 대기 : 사용자가 준비하는 시간
path = 'C:\\Users\\a\\Desktop\\GUI_project\\project\\img_Save\\' #경로
photo_range = 25

for i in range(1, photo_range+1):  # 2초 간격으로 10개 이미지 저장
    img = ImageGrab.grab()
    img.save(path+'image{}.png'.format(i))
    print(
        '{:.1f}%'.format(i/photo_range*100),
        '----------------------image{}.png'.format(i)
        )
    
    time.sleep(3)   # 2초 단위
    