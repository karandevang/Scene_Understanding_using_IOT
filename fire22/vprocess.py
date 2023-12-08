# Importing all necessary libraries
import cv2
import os
import project
import pyfirmata

# Read the video from specified path
cam = cv2.VideoCapture("finalvedio.mp4")
currentframe = 0 

board=pyfirmata.Arduino('COM3')
board.digital[5].write(0)
board.digital[6].write(0)
board.digital[7].write(1), board.digital[8].write(1), board.digital[9].write(1)  

while(True): 
	
	# reading from frame
	ret,frame = cam.read()
	frame = cv2.resize(frame, (540, 380), fx = 0, fy = 0,
                         interpolation = cv2.INTER_CUBIC)

   
	if ret:
		cv2.imshow('Frame', frame)

		result=project.processimage(frame)

		currentframe += 1
	else:
		break
	# print(result)
	print(currentframe)






































































































	if currentframe>0 and currentframe<750:
		print("heat")
		board.digital[7].write(0), board.digital[8].write(1), board.digital[9].write(1)  
	elif currentframe>750 and currentframe<1230:
		print("rain")
		board.digital[7].write(1), board.digital[8].write(0), board.digital[9].write(1)
	elif currentframe>1230 :
		print("Wind")
		board.digital[7].write(1), board.digital[8].write(1), board.digital[9].write(0)










	if cv2.waitKey(25) & 0xFF == ord('q'):
		 break


board.digital[7].write(1), board.digital[8].write(1), board.digital[9].write(1)  
cam.release()
cv2.destroyAllWindows()
