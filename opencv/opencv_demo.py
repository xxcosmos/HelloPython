# import cv2
#
# cap = cv2.VideoCapture(0)
#
# sz = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
#
# fps = 20
#
# fourcc = cv2.VideoWriter_fourcc(*'mpeg')
#
# vout  = cv2.VideoWriter()
#
# vout.open('./video//output.mp4',fourcc,fps=fps,frameSize=sz,isColor=True)
#
# cnt = 0
# while cnt <20:
#     cnt+=1
#
#     print(cnt)
#     _,frame = cap.read()
#     cv2.putText(frame,str(cnt),(10,20),cv2.FONT_HERSHEY_PLAIN,1,(0,255,0),1,cv2.LINE_AA)
#     vout.write(frame)
# vout.release()
# cap.release()

import numpy as np
import cv2 as cv


def take_photo():
    cap = cv.VideoCapture(0)
    ret, photo = cap.read()
    if ret:
        print("take photo successfully")
        cv.imwrite("./photo.png", photo)
    else:
        print("error")


def take_video():
    cap = cv.VideoCapture(0)
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    out = cv.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
    while True:
        ret, frame = cap.read()
        gray = cv.cvtColor(frame, 0)
        flip = cv.flip(gray, 1)
        out.write(frame)
        k = cv.waitKey(1)
        if k == ord('q'):
            break


if __name__ == '__main__':
    take_video()
