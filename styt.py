import os
import logging
import time
import config
import subprocess
import re

this_key = config.rtmp_key
exe_ff = config.ffmpeg_exe

def this():
  t = time.localtime()
  current_time = time.strftime("%H:%M:%S", t)
  command = r'py ./yt_dlp/__main__.py -f b -g "https://www.youtube.com/channel/' + config.username + '/live"'
  output = subprocess.check_output(command, shell=True).decode()
  output = re.search(r"(?P<url>https?://[^\s]+)", output).group("url")
  print(output)
  command = exe_ff + ' -i ' + output + ' -c:v copy -c:a aac -ar 44100 -ab 128k -ac 2 -strict -2 -flags +global_header -bsf:a aac_adtstoasc -b:v 6300k -preset fast -f flv rtmp://a.rtmp.youtube.com/live2/' + this_key
  print(command)
  os.system(command)
  logging.info('stream has finish no loop it')

if __name__ == "__main__":
   logging.basicConfig(filename="styt.log", level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
   logging.getLogger().addHandler(logging.StreamHandler())
   logging.info('script is started now')
   this()
   exit()
