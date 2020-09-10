import numpy as np
import Render

def Construct(Colours):
    data =[]
    labels = []

    #Read the data from the file
    file = open("data", "r")
    for line in file:
        split = line.split(":")
        labels.append(split[0])
        data.append(split[1].split()[0])

    data = np.array(list(map(int, data)))
    holder = np.array(np.arange(len(data)))

    # Read from the settings file. This could be updated in the future to be
    # editeble from the TKinter window
    file = open("settings", "r")
    Days = int(file.readline().split(":")[1].split()[0])
    Display = file.readline().split(":")[1]

    if (Days > 0 and Days < len(data)):
        limit = len(data) - Days
        data = data[limit:]
        holder = holder[limit:]
        labels = labels[limit:]
    else:
        Days = len(data)

    Render.Render(data, holder, Colours, Days, Display, labels)
