import os
import logging
import time
import config
import webbrowser

def this():
  t = time.localtime()
  current_time = time.strftime("%H:%M:%S", t)
  command = 'streamlink https://youtube.com/channel/' + config.username + '/live best -o - | live_state.exe -re -i pipe:0 -c:v copy -c:a aac -ar 44100 -ab 128k -ac 2 -strict -2 -flags +global_header -bsf:a aac_adtstoasc -b:v 6300k -preset fast -f flv rtmp://a.rtmp.youtube.com/live2/60gx-c1yq-1vrm-t3qg-dh6f'
  os.system(command)
  time.sleep(180)
  logging.info('stream has finish no loop it')
  os.system('start check_styt.py')
  os.system('start streamfromyt.py')

if __name__ == "__main__":
   logging.basicConfig(filename="check_styt_offine.log", level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
   logging.getLogger().addHandler(logging.StreamHandler())
   logging.info('script is started now')
   this()
   exit()
