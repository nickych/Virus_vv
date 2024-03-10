"""

For the code to run, you need to install rotatescreen, to do that, follow the following:
On windows simply open Command-Line/Shell and type (pip install rotate-screen)
------------------------------------------------------------------------------------------------------------

on Linux system simply open Terminal and type (sudo pip install rotate-screen)

After that you also need to install pywin32, to do that on:

Linux, open Terminal then type (sudo pip install pywin32)
------------------------------------------------------------------------------------------------------------
Windows, open Command-Line/Shell then type (pip install pywind)

"""


import time, rotatescreen as db  #Time and rotatescreen are libraries

vira = db.get_primary_display()
angles_num = [90, 180, 270, 0]

for virus in angles_num:
  vira.rotate_to(virus)
  time.sleep(20.0)
