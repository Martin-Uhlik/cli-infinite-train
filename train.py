import os, sys, shutil, time, random, glob
import drawer


#convert inpot strings to list of lists, that can be loaded to buffer and readz to print
def create_buffer_data(data):
    buff_data = []
    lst = data.split("\n")
    max_len = len(max(lst))
    
    for line in lst:
        chars = list(line)
        while len(chars) < max_len:
            chars.append(" ")
        buff_data.append(chars)
    return buff_data


#serch current folder for specific named files, which should contain wagoons ASCII art
def get_wagoons():
    wagoons = []
    for file in glob.glob("wagon*.txt"):
        f = open(file, "r")
        wagoons.append(create_buffer_data(f.read()))
        f.close()
    return wagoons


#append data to buffer
def load_buffer(data):
    global buffer

    if len(buffer) > len(data):
        line = []
        for char in data[0]:
                line.append(" ")
        
        while len(buffer) > len(data):
            data.insert(0, line)
    for index,line in enumerate(data):
        buffer[index] += line
    



#creates empty buffer compatible with drawer module
def create_buffer(y):
    buffer = []
    for val in range(y):
        buffer.append([])
    return buffer


#wipe first "lenght" columns from the buffer
def offset_buffer(lenght=1):
    global buffer
    for index in range(len(buffer)):
        del buffer[index][0]



#creates raster from buffer
def load_raster(buffer, x):
    raster = []
    for line in buffer:
        raster.append(line[:x])
    return raster


#MAIN
if __name__ == "__main__":
    x,y = drawer.get_resolution()
    #resolution limits

    wagoons = get_wagoons()
    raster = drawer.create_raster(x, y)
    buffer = create_buffer(y)
    load_buffer(wagoons[0])

    while True:
        while len(buffer[0]) < x:
            load_buffer(random.choice(wagoons[1:]))
        drawer.draw(load_raster(buffer, x))
        offset_buffer()
    






'''
#MAIN
if __name__ == "__main__":
    x,y = drawer.get_resolution()
    #resolution limits

    wagoons = get_wagoons()
    raster = drawer.create_raster(x, y)
    buffer = create_buffer(y)
    load_buffer(wagoons[0])
    print(buffer)

    while True:
        while len(buffer[0]) < x:
            load_buffer(random.choice(wagoons[1:]))
        drawer.draw(load_raster(buffer, x))
        offset_buffer()
'''

