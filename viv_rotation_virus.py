"""

For the code to run, you need to install rotatescreen, to do that, follow the following:
On windows simply open command line and type (pip install rotate-screen)
------------------------------------------------------------------------------------------------------------

on Linux system simply open terminal and type (sudo pip install rotate-screen)

"""

import time, rotatescreen as db  #Time and rotatescreen are libraries

vira = db.get_primary_display()
angles_num = [90, 180, 270, 0]

for virus in angles_num:
  vira.rotate_to(virus)
  time.sleep(20.0)
