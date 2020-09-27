import cv2

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

stone_counter = 0
paper_counter = 0
scissors_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 115 or k%256 == 83:
        # S or s pressed
        img_name = "stone_{}.png".format(stone_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        stone_counter += 1
    elif k%256 == 112 or k%256 == 80:
        # P or p pressed
        img_name = "paper_{}.png".format(paper_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        paper_counter += 1
    elif k%256 == 99 or k%256 == 67:
        # C or c pressed
        img_name = "scissors_{}.png".format(scissors_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        scissors_counter += 1
    

cam.release()

cv2.destroyAllWindows()