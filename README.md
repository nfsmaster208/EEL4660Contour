# EEL4660Contour
Final Project for EEL4660 - Contour Object Tracking

Object Recognition and Tracking in Video
from Quadcopter Flight | EEL 4660

December 11, 2016

Authors:
Chelsea Greene
Marcus Rivera

The foundation for the code, written in Python using OpenCV, revolved around previous experience with image matching and finding techniques learned throughout the course as well as examples and techniques found online. The primary objective of our project is to be able to analyze video streams and track objects of interest. A challenge with OpenCV that arose during implementation of the project was through the process of testing various code samples, including sample OpenCV projects, where simply opening videos proved challenging. It is necessary to ensure that for each project, documentation is observed with regard to several aspects. One aspect includes appropriate codec packs being installed to enable the encoding of videos, where in the experience of Windows users may include the K-Lite Master Codec Pack which includes the ability to encode in H.264, which is how the included .avi files in our project were encoded. Cooperation across operating systems may also at times prove difficult, as for Mac users, it may not be possible to use a workaround to an issue that users of OpenCV 2.4.x, the version our team used, to specify the encoder for the video output files. Instead, the -1 flag was used, as shown in the code below:
The figure to the left shows the context menu that appears before the video output file is created, where we specify the H.264 encoder to compress the video output file most efficiently.


With regard to opening videos, it is necessary to be aware that copying the contents of the ‘opencv\sources\3rdparty\ffmpeg’, included in the latest OpenCV package, into the root of the Python system directory folder is required to be able to open video files, at least in the case of Windows users, as is renaming dlls to the OpenCV version:

With these initial requirements and quirks of the OpenCV 2.4.13 notwithstanding (which may be alleviated by switching to OpenCV 3.x+), the project was ultimately able to be executed in the Windows environment highly consistently.
Core functionality starts outside of modifying and saving video files, however. As previously mentioned, with guidance from online resources, including Adrian Rosebrock’s article on finding targets in drone video streams, the project was largely rooted in functionality and inspired by the previous work, which includes aspects covered in the class, such as image pre-processing with frame-by-frame conversion to grayscale, gaussian blurring to remove noise and to reveal image features, and canny edge detection to extract object outlines in the image frame.
Finding contours, similar to the concept of finding Harris Corners and determining ‘cornerness’, is the most central idea to distinguishing the template from other objects, e.g. a refrigerator or door. Since squares have four vertices, and while circles by definition have none, we improve upon the existing algorithm (using len(approx) > 2 in our code) and logic to be able to discover both squares, and circles, because circles appear imperfectly enough with similar width and height, aspect ratio (equal to width/height), and solidity (the object’s current bounding box/convex hull (the smallest area containing the area of the object).
We tested and researched other methods to track, including the use of meanshift, and ultimately found meanshift alone incapable of tracking the object overtime when the template fell out of frame, or in other words, poor full occlusion handling. Although we discovered camshift is far more robust, with the ability to adjust the bounding box according to the movement of the object over time (also unlike our primary contour method, which is frame-by-frame and does not keep track of previous position), it too had issues with occlusion. We ultimately decided to look elsewhere, outside of OpenCV methods, to compare qualitative performance, and we tested our results against the Consensus-based Matching and Tracking of Keypoints for Object Tracking (CMT), open-source method, which allows us to start a video frame, selecting the object we wish to track and begins its algorithm, as follows: Track key points from frame-to-frame optic flow, compare global KP descriptors, vote for the object center, and reject outliers.
A potential improvement to the contour program that we used in our primary method may include frame-to-frame optic-flow tracking, or perhaps more useful and less performance intensive, adaptive correlation filters combined with Kalman filter prediction. This combination of techniques is a trend in the object tracking research spaces, and would improve the ability to reduce flickering from the contour method by being able to handle frame distortions through movement with the adaptive coorelation filter, and prediction of where the object is and improving robustness of occlusion with the Kalman filter.
