import cv2
import numpy as np


import multiprocessing


#inspiration: https://dontrepeatyourself.org/post/color-based-object-detection-with-opencv-and-python/

#got hsv colors from: https://pinetools.com/image-color-picker

#connect to iphone camera
cap = cv2.VideoCapture(0)


fBLUE = open("wordLists/childhood.txt", "r")

wholefileBLUE = fBLUE.read()
fBLUE.close()
listlinesBLUE = wholefileBLUE.splitlines(False)


fGREEN = open("wordLists/youngadult.txt", "r")

wholefileGREEN = fGREEN.read()
fGREEN.close()
listlinesGREEN = wholefileGREEN.splitlines(False)



def words(queue):
    i=0
    
    while True:

        queue.put(i)
        i+=1



def capture(queue):

    while True: 

        ret, frame = cap.read()

        # flipping frame vertically and horizontally

        frame_v = cv2.flip(frame, 0)

        frame_v_h = cv2.flip(frame_v, 1)

        key = cv2.waitKey(1)

        #color space
        hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 

        font = cv2.FONT_HERSHEY_SIMPLEX 

        #text on video w properties
        cv2.putText(frame,  
                    "Drawing",
                    (100, 50),  
                    font, 1,  
                    (0, 255, 255),  
                    2,  
                    cv2.LINE_4) 
        

    

        # convert from BGR to HSV color spaces
        hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)



        # for blue / childhood

        # lower and upper limits
        lower_limit = np.array([110, 100, 100])
        upper_limit = np.array([130, 255, 255])

        # create a mask for the specified color range
        mask = cv2.inRange(hsv_image, lower_limit, upper_limit)
        # get the bounding box from the mask image
        bbox = cv2.boundingRect(mask)

        # if we get a bounding box, use it to draw a rectangle on the image
        if bbox is not None:
            #print("Object detected")
            x, y, w, h = bbox

            # dont need rectangle, but this is the code
            cv2.rectangle(frame, (x+5, y+5), (x+5 + w, y+5 + h), (255, 0, 0), 2)

        
            cv2.putText(frame,  
                    listlinesBLUE[round((queue.get() / 22) % 49)] ,
                    (x+20, y-20),  
                    font, 1,  
                    (255, 0, 0),  
                    2,  
                    cv2.LINE_4) 
            
        else:
            print("Object not detected")

        cv2.imshow('image', frame)


        # for green / older

        lower_limit = np.array([50, 100, 100])
        upper_limit = np.array([70, 255, 255])

        # create a mask for the specified color range
        mask = cv2.inRange(hsv_image, lower_limit, upper_limit)
        # get the bounding box from the mask image
        bbox = cv2.boundingRect(mask)

        # if we get a bounding box, use it to draw a rectangle on the image
        if bbox is not None:
            #print("Object detected")
            x, y, w, h = bbox

            # dont need rectangle, but this is the code
            cv2.rectangle(frame, (x+5, y+5), (x+5 + w, y+5 + h), (113, 179, 60), 2)

        
            cv2.putText(frame,  
                    listlinesGREEN[round((queue.get() / 22) % 49)] ,
                    (x+20, y-20),  
                    font, 1,  
                    (113, 179, 60),  
                    2,  
                    cv2.LINE_4) 
            
        else:
            print("Object not detected")

        cv2.imshow('image', frame)

        if key ==27:
            #if escape key, break
            break








#nonblocking proccesses trunn
if __name__ == '__main__':
    q = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=words, args=(q,))
    p2 = multiprocessing.Process(target=capture, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

