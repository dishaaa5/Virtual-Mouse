import cv2
import mediapipe as mp
import pyautogui

web = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width , screen_height = pyautogui.size()
index_y = 0

while True:
    _, img = web.read()
    img = cv2.flip(img , 1)
    img_height , img_width , _ = img.shape
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_img)
    hands = output.multi_hand_landmarks

    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(img, hand)
            landmarks = hand.landmark
            for id , landmarks in enumerate(landmarks):
                x = int(landmarks.x * img_width)
                y = int(landmarks.y * img_height)
                
                if id == 8:
                    cv2.circle(img , (x,y) , radius = 20 ,color = (0 , 255 , 255))
                    index_x = screen_width/img_width*x
                    index_y = screen_height/img_height*y
                    pyautogui.moveTo(index_x,index_y)
                if id == 4:
                    cv2.circle(img , (x,y) , radius = 20 ,color = (0 , 255 , 255))
                    thumb_x = screen_width/img_width*x
                    thumb_y = screen_height/img_height*y  
                    print(abs (index_y - thumb_y))
                    if abs(index_y - thumb_y) <20:
                        pyautogui.click()
                        pyautogui.sleep(1)
                    
    cv2.imshow("Virtual Mouse", img)
    if cv2.waitKey(1) & 0xff == 27:
        break

web.release()
cv2.destroyAllWindows()
