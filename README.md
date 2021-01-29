# MAIC_prototype
Immersion Research Project. Python, PyGTK, and Glade.



# Windows

Requirements: Python ver. 2.7 or newer.

1. Install MSYS2. Follow the instructions for installation in their website.
   https://www.msys2.org/

2. Download MAIC_prototype folder above. Then copy it to C:/msys64/home/user.

3. Open MSYS2 Min GW 64-bit terminal. Execute command to install glade:

	$ pacman -S mingw-w64-x86_64-glade
 
4. Execute command to install gtk and gobject:

	$ pacman -S mingw-w64_x86_64-gcc mingw-w64_x86_64-gtk3 mingw-w64-x86_64-python3 mingw-w64-x86_64-python3-gobject

5. Change directory to 'MAIC_prototype' folder.

	$ cd MAIC_prototype

6. Execute python file.

	$ python3 MAIC_prototype.py
  


    
