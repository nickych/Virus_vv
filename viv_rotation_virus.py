#

import time, rotatescreen as db  #Time and rotatescreen are libraries

vira = db.get_primary_display()
angles_num = [90, 180, 270, 0]

for virus in angles_num:
  vira.rotate_to(virus)
  time.sleep(20.0)
