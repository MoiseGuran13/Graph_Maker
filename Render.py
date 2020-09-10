import matplotlib.pylab as plt

# This function divides an array into chunks to be used in the graph
# as alternating colours. This is achieved by having each colour have
# its own set of data and graph all taken from the original graoh
def Filter(array, nr_colours, choice):
    result = []
    for i in range(len(array)):
        if(i % nr_colours == choice):
            result.append(array[i])
    return result

# Renders the different coloured chunks of graphs all onto the same
# canvas, essentially splicing it togheter
def Render(data, holder, Colours, Days, Display, labels):
    choice = -1
    nr_colours = len(Colours)
    for colour in Colours:
        choice += 1
        _data = Filter(data, nr_colours, choice)
        _holder = Filter(holder, nr_colours, choice)
        plt.bar(_holder, _data, color = colour)

    title = "Covid cases in the past " + str(Days) + " " + Display

    plt.title(title)
    plt.xticks(holder, labels)
    plt.show()
