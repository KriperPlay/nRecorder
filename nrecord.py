# ╱╱╱╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╭╮
# ╱╱╱┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱┃┃
# ╭━╮┃╰━╯┣━━┳━━┳━━┳━┳━╯┣━━┳━╮
# ┃╭╮┫╭╮╭┫┃━┫╭━┫╭╮┃╭┫╭╮┃┃━┫╭╯
# ┃┃┃┃┃┃╰┫┃━┫╰━┫╰╯┃┃┃╰╯┃┃━┫┃
# ╰╯╰┻╯╰━┻━━┻━━┻━━┻╯╰━━┻━━┻╯

import imageio
import pyautogui as pg
import numpy as np
import datetime
import sys

def start_record(time:int) -> None:
    fps = 30
    '''time: int -> time must be in second'''
    with imageio.get_writer(f'{datetime.datetime.now()}.mp4', mode='I',fps=fps) as writer:
        for second in range(time):
            for i in range(fps):
                writer.append_data(np.array(pg.screenshot()))

def start_record_infinity() -> None:
    fps = 30
    with imageio.get_writer(f'{datetime.datetime.now()}.mp4', mode='I',fps=fps) as writer:
        while True:
            for i in range(fps):
                writer.append_data(np.array(pg.screenshot()))

if __name__ == "__main__":
    try:
        if sys.argv[1] == "-r":
            start_record(int(sys.argv[2]))
        if sys.argv[1] == '-rinf':
            start_record_infinity()
        if sys.argv[1] == '-h':
            print("Arguments:\nStart Record: -r [seconds]\nInfinity Record: -rinf\nExit of Infinity Mode - ctrl+c (maybe broken mp4)\nHelp Menu: -h")
    except IndexError:
        print("Argument fail, please use -h for help menu")
    except ValueError:
        print("Argument fail, please use -h for help menu")
