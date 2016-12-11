# Chelsea Greene and Marcus Rivera

# import the necessary packages
import cv2

# load the video    
camera = cv2.VideoCapture('C:\Video Files-20161209T025004Z\Video Files\Flight Videos_ Grayscale Symbol\Gray-Stuff.avi')

# Method for specifying encoder, using old CV method, reqired for OpenCV 2.4.13
# fourcc = cv2.cv.CV_FOURCC('D', 'I', 'V', 'X')

# Important Note: If the source video is *not* 30FPS, or 720x480px,
# you must update the fields as appropriate (-1 may only work in Windows environments)
out = cv2.VideoWriter('Gray-Stuff-output.avi',-1, 30.0, (640,480), True)


# keep looping
while True:
    # grab the current frame and initialize the status text
    (grabbed, frame) = camera.read()
    status = "Seeking Targets..."

    # check to see if we have reached the end of the
    # video
    if not grabbed:
        break

    # convert the frame to grayscale, blur it, and detect edges
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (7, 7), 0)
    edged = cv2.Canny(blurred, 50, 150)

    # find contours in the edge map
    (cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
                                 cv2.CHAIN_APPROX_SIMPLE)

    # loop over the contours
    for c in cnts:
        # approximate the contour
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.01 * peri, True)

        # ensure that the approximated contour is "roughly" rectangular
        if  len(approx) > 2:
            # compute the bounding box of the approximated contour and
            # use the bounding box to compute the aspect ratio
            (x, y, w, h) = cv2.boundingRect(approx)
            aspectRatio = w / float(h)

            # compute the solidity of the original contour
            area = cv2.contourArea(c)
            hullArea = cv2.contourArea(cv2.convexHull(c))
            solidity = area / float(hullArea)

            # compute whether or not the width and height, solidity, and
            # aspect ratio of the contour falls within appropriate bounds
            keepDims = w > 25 and h > 25
            keepSolidity = solidity > 0.9
            keepAspectRatio = aspectRatio >= 0.8 and aspectRatio <= 1.2

            # ensure that the contour passes all our tests
            if keepDims and keepSolidity and keepAspectRatio:
                # draw an outline around the target and update the status
                # text
                cv2.drawContours(frame, [approx], -1, (0, 0, 255), 4)
                status = "Target(s) Acquired"

                # compute the center of the contour region and draw the
                # crosshairs
                M = cv2.moments(approx)
                (cX, cY) = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
                (startX, endX) = (int(cX - (w * 0.15)), int(cX + (w * 0.15)))
                (startY, endY) = (int(cY - (h * 0.15)), int(cY + (h * 0.15)))
                cv2.line(frame, (startX, cY), (endX, cY), (0, 0, 255), 3)
                cv2.line(frame, (cX, startY), (cX, endY), (0, 0, 255), 3)

    # draw the status text on the frame
    cv2.putText(frame, status, (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                (0, 0, 255), 2)

    # show the frame and record if a key is pressed
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    # send the frame to encoder
    out.write(frame)

    # quit when the 'q' key is pressed, exiting the loop
    if key == ord("q"):
        break

# cleanup the camera and close any open windows
cv2.destroyAllWindows()
camera.release()
out.release()