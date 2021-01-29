# MAIC_prototype
Immersion Research Project. Python, PyGTK, and Glade.



# Windows

Requirements: Python ver. 2.7 or newer.

1. Install MSYS2. Follow the instructions for installation in their website.
   https://www.msys2.org/
   
   A prompt will appear. Execute commands: 

	$ pacman -Syu
	
	$ pacman -Su
	
	$ pacman -S --needed base-devel mingw-w64-x86_64-toolchain

	Exit terminal

2. In the search bar, search for and open new MSYS2 MinGW 64-bit terminal. Execute command to install gtk and gobject:

	$ pacman -S mingw-w64-x86_64-gtk3 mingw-w64-x86_64-python3 mingw-w64-x86_64-python3-gobject

3. Execute command to install glade:

	$ pacman -S mingw-w64-x86_64-glade

4. Download MAIC_prototype folder above. Then copy it to C:\msys64\home\<user>.

5. Change directory to 'MAIC_prototype' folder.

	$ cd MAIC_prototype

6. Execute python file.

	$ python3 MAIC_prototype.py
  


    
