import vlc
import time
import datetime
import os

outputPath = 'output/'


def get_snapshot_path():
    return outputPath + datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S.%f')[:-3] + '.png'


if not os.path.exists(outputPath):
    os.mkdir(outputPath)

player = vlc.MediaPlayer('rtsp://192.168.0.85:5554/camera')
player.play()

while 1:
    time.sleep(1)
    player.video_take_snapshot(0, get_snapshot_path(), 0, 0)
