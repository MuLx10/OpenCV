import cv2
ORANGE={'min':(),'max':()}
PINK={'min':(),'max':()}
'''
Orange_min_dx=0
Orange_max_dx=0
Pink_min_dx=0
Pink_max_dx=0
'''


def bot__Det(image):
    global ORANGE,orange,PINK,pink
    img=copy(image)
    #new_img=copy(newimg)
    height, width, channels = img.shape
    new_img=np.ones((height,width,channels), np.uint8)
    HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


    orange_part=cv2.inRange(HSV,orange['min'],orange['max'])
    pink_part=cv2.inRange(HSV,pink['min'],pink['max'])
    
    new_img=cv2.add(pink,orange)
    
    return new_img


def change():
 global ORANGE,orange,PINK,pink
 TrackbarPos = cv2.getTrackbarPos('Orangemin', WindowName)
 orange['min'][0]=ORANGE['min'][0]+TrackbarPos

 TrackbarPos = cv2.getTrackbarPos('Orangemax', WindowName)
 orange['max'][0]=ORANGE['max'][0]+TrackbarPos

 TrackbarPos = cv2.getTrackbarPos('Pinkmin', WindowName)
 pink['min'][0]=PINK['min'][0]+TrackbarPos

 TrackbarPos = cv2.getTrackbarPos('Pinkmax', WindowName)
 pink['max'][0]=PINK['max'][0]+TrackbarPos
 
'''   
cv2.createTrackbar('Orangemin','orange',Orange_min_dx,orange_min_MAX,orange_change)
cv2.createTrackbar('Orangemax','orange',Orange_max_dx,orange_max_MAX,orange_change)
cv2.createTrackbar('Pinkmin','orange',Pink_min_dx,orange_min_MAX,Pink_change)
cv2.createTrackbar('Pinkmin','orange',Pink_max_dx,orange_max_MAX,Pink_change)
'''
cv2.createTrackbar('Orangemin','image',0,50,change)
cv2.createTrackbar('Orangemax','image',0,50,change)
cv2.createTrackbar('Pinkmin','image',0,50,change)
cv2.createTrackbar('Pinkmax','image',0,50,change)




