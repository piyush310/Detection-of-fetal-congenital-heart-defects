# Program To Read video 
# and Extract Frames 
import cv2 
  
# Function to extract frames 
def FrameCapture(path): 
      
    # Path to video file 
    vidObj = cv2.VideoCapture(path+"fetal ultrasound of 16 weeks 17 weeks baby boy moving - YouTube (online-video-cutter.com)_5.mp4") 
  
    # Used as counter variable 
    count = 2107
  
    # checks whether frames were extracted 
    success = 1
  
    while success: 
  
        # vidObj object calls read 
        # function extract frames 
        success, image = vidObj.read() 
  
        # Saves the frames with frame-count
        print(path+"frames\\frame1_%d.jpg" % count) 
        cv2.imwrite(path+"frames\\frame1_%d.jpg" % count, image) 
  
        count += 1
  
# Driver Code 
if __name__ == '__main__': 
  
    # Calling the function 
    path="C:\\Users\\user\\Desktop\\philips\\Data\\Non Heart\\fetal ultrasound of 16 weeks 17 weeks baby boy moving - YouTube\\"
    FrameCapture(path) 
