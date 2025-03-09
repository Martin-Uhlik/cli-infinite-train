import shutil, time, os


# get resolution of current terminal and return x,y values
def get_resolution():
    return shutil.get_terminal_size()


#determinate OS and wipe screen
def wipe_screen(numlines=100):
    if os.name == "posix":
        # Unix/Linux/MacOS/BSD/etc
        os.system('clear')
    elif os.name in ("nt", "dos", "ce"):
        # DOS/Windows
        os.system('CLS')
    else:
        # Fallback for other operating systems.
        print('\n' * numlines)


#creates a list of lists based of x,y which should correspond with the resolution of current terminal
def create_raster(x, y):
    raster = []
    line = []
    for point in range(x):
        line.append("")
    for point in range(y):
        raster.append(line)
    return raster


#input is list of lists
#from input data creates a single string (lines separed by \n) and print result to terminal, then sleep "refresh rate" seconds and wipe screen
def draw(raster, refresh_rate=0.2):
    screen_data = ""
    for line in raster:
        screen_data += "".join(line)
    print(screen_data)
    time.sleep(refresh_rate)
    #wipe_screen()