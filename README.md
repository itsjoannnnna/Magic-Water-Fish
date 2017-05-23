South Bay Underwater ROV
The South Bay Underwater ROV is an underwater ROV that will detect and differentiate different types of salmon in the South Bay creeks. 

Getting Started
All of the files are inside the Rasperry Pi 3's microSD card.
Accessing all the files:
Click on the Raspberry in the lefthand side of the screen. 
Accessories>File Manager>opencv-3.1.0>build>lib>MWF
chinook.py is the main file that is being run for our program. Only file that needs to be used
In the folders Chinook and Steelhead, these are the folders used for training OpenCV
old_files holds all the Python files that did not work
extra_neg holds all the extra negative photos we used for training OpenCV
Accessing s.sh:
Accessories>File Manager>s.sh

Prerequisites
Raspberry Pi's microSD card has everything needed to work

Deployment
If you want to use the script for starting the program:
$ bash s.sh
Open terminal
$ source ~/.profile
$ workon cv
$ cd opencv-3.1.0/build/lib/MWF
$ python chinook.py

Built With
OpenCV
Python 2.7

Authors
Jo-Anna Marie Reyes
Gustavo Ramirez
Braulio Oceguera