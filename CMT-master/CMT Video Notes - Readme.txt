cd "C:\Users\marcu_000\Downloads\CMT-master"

Use of CMT constitutes performance benchmarking with respect to the primary implementation. The code is not modified from the open source project available at https://github.com/gnebehay/CMT.

Commands used to run CMT on Square Template video *.avi files:
**Unable to output with CMT for Square-Dark: Keypoint array overflow due to lack of luminance in picture**
python run.py --with-rotation --skip 710 "C:\Video Files-20161209T025004Z\Video Files\Flight Videos_ Black Square\Square-Bright.avi"
python run.py --with-rotation --skip 150 "C:\Video Files-20161209T025004Z\Video Files\Flight Videos_ Black Square\Square-Stuff.avi"

Commands used to run CMT on Circle Template video files:
**Unable to output with CMT for Circle-Dark: Keypoint array overflow due to lack of luminance in picture**
**Unable to output with CMT for Circle-Light: Keypoint array overflow due to lack of contrast in picture**
python run.py --with-rotation --skip 840 "C:\Video Files-20161209T025004Z\Video Files\Flight Videos_ Black Outline Circle\Circle-stuff.avi"
*Conclusion - Unique Keypoints are difficult to identify with this template, due to its lack of distinctive features, or solid color*

Commands used to run CMT on Color Symbol Template video files:
**Unable to output with CMT for Color-Dark: Keypoint array overflow due to lack of luminance in picture**
python run.py --with-rotation --skip 1100 "C:\Video Files-20161209T025004Z\Video Files\Flight Videos_ Color Symbol\Color-Light.avi"
python run.py --with-rotation --skip 275 "C:\Video Files-20161209T025004Z\Video Files\Flight Videos_ Color Symbol\Color-Stuff.avi"

Commands used to run CMT on Grayscale Symbol Template video files:
**Unable to output with CMT for Gray-dark: Keypoint array overflow due to lack of luminance in picture**
python run.py --with-rotation --skip 1200 "C:\Video Files-20161209T025004Z\Video Files\Flight Videos_ Grayscale Symbol\Gray-Light.avi" *Note: Video could not be recorded - record latency too high, due to late frame start*
python run.py --with-rotation --skip 170 "C:\Video Files-20161209T025004Z\Video Files\Flight Videos_ Grayscale Symbol\Gray-stuff.avi"