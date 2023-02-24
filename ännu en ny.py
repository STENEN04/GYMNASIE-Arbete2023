import cv2
import sys
import keyboard 
import pyautogui

(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')

# Sätter start värden för tiden spenderat på varje sida
statsV = 0
statsH = 0

Tr = True
lista = []
while Tr: 
    if __name__ == '__main__' :
    
        # Set up tracker.
        # Instead of MIL, you can also use
    
        tracker_types = ['BOOSTING', 'MIL','KCF', 'TLD', 'MEDIANFLOW', 'CSRT', 'MOSSE']
        tracker_type = tracker_types[2]
    
        if int(minor_ver) < 3:
            tracker = cv2.Tracker_create(tracker_type)
        else:
            if tracker_type == 'BOOSTING':
                tracker = cv2.TrackerBoosting_create()
            if tracker_type == 'MIL':
                tracker = cv2.TrackerMIL_create()
            if tracker_type == 'KCF':
                tracker = cv2.TrackerKCF_create()
            if tracker_type == 'TLD':
                tracker = cv2.TrackerTLD_create()
            if tracker_type == 'MEDIANFLOW':
                tracker = cv2.TrackerMedianFlow_create()
            if tracker_type == 'CSRT':
                tracker = cv2.TrackerCSRT_create()
            if tracker_type == 'MOSSE':
                tracker = cv2.TrackerMOSSE_create()
    
        # Read video
        # video = cv2.VideoCapture("./videos/chaplin.mp4")
        # video = cv2.VideoCapture(0)
        # video = cv2.VideoCapture("/Hockey-Video.mp4")

        # video = cv2.VideoCapture("C:/Users/Adam.stenestrand/Downloads/Hockey-Video.mp4")
        video = cv2.VideoCapture("C:/Users/Adam.stenestrand/Downloads/AIRHOCKEY.mov")
        # video = cv2.VideoCapture("C:/Users/Adam.stenestrand/Downloads/Ny_Vid.mov")

        
        # video = video = cv2.VideoCapture("movie_resized1.mp4")

        # Exit if video not opened.
        if not video.isOpened():
            print("Could not open video")
            sys.exit()
    
        # Read first frame.
        ok, frame = video.read()
        
        if not ok:
            print('Cannot read video file')
            sys.exit()
        
        # Define an initial bounding box
        bbox = (287, 23, 86, 320)
    
        # Uncomment the line below to select a different bounding box
        bbox = cv2.selectROI(frame, False)
    
        # Initialize tracker with first frame and bounding box
        ok = tracker.init(frame, bbox)

        
        while True:
            # Read a new frame
            ok, frame = video.read()
            if not ok:
                break
            
            # Start timer
            timer = cv2.getTickCount()
    
            # Update tracker
            ok, bbox = tracker.update(frame)
    
            # Calculate Frames per second (FPS)
            fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
    
            # Draw bounding box
            if ok:
                # Tracking success
                p1 = (int(bbox[0]), int(bbox[1]))
                p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
                cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)
            else :
                # Tracking failure
                cv2.putText(frame, "Tracking failure detected", (100,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)
                tr = False
                

            # Display tracker type on frame
            cv2.putText(frame, tracker_type + " Tracker", (100,20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50),2);
        
            # Display FPS on frame
            cv2.putText(frame, "FPS : " + str(int(fps)), (100,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);
    
            # Display result
            cv2.imshow("Tracking", frame)
    
            # Exit if ESC pressed
            k = cv2.waitKey(1) & 0xff
            if k == 27 : break
        
            # print(boundingRect(cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1))) 
            # print(p1)
            # print(p2)
            cords1 = p1[0]
            cords2 = p2[0]

            # print(cords1)
            # print(cords2)

            new = (cords1 + cords2)/2

            # print (new)
            lista.append(new)
            
            if(new > 964.5):
                 statsH += 1
            
            else: 
                statsV +=1
            
            
        


            #  Så fixa så man kan klicka "R" för att sätta om the bounding box, beräkna ut mitt punkt 
            #  Fixa en cropped video så den blir över skärmen och inte på nån annan pixelstorlek
            
            try:  # used try so that if user pressed other than the given key error will not be shown
                if keyboard.is_pressed('q'):  # if key 'q' is pressed 
                    print('You Pressed A Key!')
                    
                    myScreenshot = pyautogui.screenshot()
                    myScreenshot.save(r'C:\Users\Adam.stenestrand\Downloads\screenshot.png')
                    new_frame = 'C:/Users/Adam.stenestrand/Downloads/screenshot_1.png'
                    # frame = 'C:/Users/Adam.stenestrand/Downloads/screenshot_1.png'
                    # new_ok = tracker.init(new_frame, bbox)
                    # new_ok, new_frame = video.read()
                    # ok, frame = new_frame




                    break  # finishing the loop
            except:
                break  # if user pressed a key other than the given key the loop will break
    print(max(lista))
    print(min(lista))

    H = statsH/(statsV + statsH) * 100
    V = statsV/(statsV + statsH) * 100    

    print ("Procentuell tid Spenderad på Vänster sida: ",round(V),"%")
    print ("Procentuell tid Spenderad på Höger sida: ",round(H),"%")

print("Koden tog slut")


    