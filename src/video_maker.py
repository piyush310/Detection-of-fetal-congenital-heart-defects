
import cv2
import numpy as np
from time import time as timer

x = np.load('predictions.npy')
x = x.astype(np.float64)

vid_fol = '/C:/Users/Piyush/Desktop/Final/'
vid_name = '3a.mp4'
#******************************************************************************
cap = cv2.VideoCapture(vid_fol + vid_name)

#******************************************************************************
w = int(cap.get(3))
h = int(cap.get(4))
#******************************************************************************
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
out = cv2.VideoWriter('result.mp4', fourcc, 5, (w, h))

# fps = cap.get(cv2.CAP_PROP_FPS)
# fps /= 100
ret, _ = cap.read()
cap.set(0, 0)
i = 0
print("######################",w," ",h)
while ret:
    start = timer()
    ret, I = cap.read()
    if not ret:
        break
    

    cv2.putText(I, 'Heart: %.3f'%x[i, 0], (0, 30), cv2.FONT_HERSHEY_SIMPLEX, 1,
                (255, 0, 0), 2)
    cv2.putText(I, 'NonHeart: %.3f'%x[i, 1], (0, 60), cv2.FONT_HERSHEY_SIMPLEX, 1,
                (0, 255, 0), 2)
    i += 1
#########################################################################
      # Display the resulting frame 
    # cv2.imshow('Frame', I)
    print("################## Frame: ",i)
    out.write(I) 
     
      # Press Q on keyboard to  exit 
    # if cv2.waitKey(25) & 0xFF == ord('q'): 
    #     break
    # diff = timer() - start
    # while  diff < fps:
    #     diff = timer() - start

#########################################################################    

cap.release()
out.release()
cv2.destroyAllWindows() 