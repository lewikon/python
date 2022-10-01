from datetime import datetime
from controller import req

def logg(req):
    with open('logger.txt', 'a') as l:
        dt_now = datetime.now()
        l.writelines(f"{req}:{str(dt_now)}\n")