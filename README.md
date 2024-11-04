# nRecorder

![](https://github.com/user-attachments/assets/e96d1286-b9d9-465b-b885-8fd0ff7719b6)

# DISCLAIMER
* nRecorder eat a lot of CPU, i made nRec. for experemental
* nRecorder work only on X11
* Infinity mode has bugs, at exit maybe mp4 will be broken -> please use default mode

# About
* nRecorder - ScreenRecorder where video consists of screenshots
* nRecord saves videos in mp4
* nRecord records video in 30fps

# Need to install
* python3 and pip
* pyutogui(python lib)
* datetime(python lib)
* numpy(python lib)
* imageio(python lib)
* gnome-screenshot

# How to use

## Download
```bash
git clone https://github.com/KriperPlay/nRecorder/
cd nRecorder
```

## Modes
* Default mode
* * ```
    python3 nrecord.py -r [time in seconds]
    ```
    at this mode u record in certain time
* Infinity mode
* * check DISCLAIMER in top
    ```
    python3 nrecord.py -rinf
    ```
    at this mode u record infinity time, until u will want to exit
    exit = crtl+c
    check DISCLAIMER
* Help menu
* * ```
    python3 nrecord.py -h
    ```

