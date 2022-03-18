# Author: Jack Wagner
# Date: 3/18/2022
# LING 50.06

import sys
import pandas as pd
from scipy.special import logsumexp
import numpy as np
import math
import matplotlib.pyplot as plt



if __name__ == '__main__':
    filename = sys.argv[1]

    outfilename = "ratios/" + str(filename[8:-4]) + ".txt"

    df = pd.read_csv(filename)

    outfile = open(outfilename, "w")

    x = []
    y = []

    for index, row in df.iterrows():
        ratio = row[1] / row[2]
        if np.isnan(ratio):
            outfile.write(str(int(row[0])) + "\tNone\n")
        elif math.isinf(ratio):
            outfile.write(str(int(row[0])) + "\tInfinity\n")
        else:
            x.append(int(row[0]))
            y.append(ratio)
            outfile.write(str(int(row[0])) + "\t" + str(ratio) + "\n")

    np_x = np.array(x)
    np_y = np.array(y)

    phrase = filename[8:-4].split("-")
    words = phrase[0].split("_")

    first = words[0].split("and")
    alphabetical = str(first[0]) + " and " + str(first[1])

    second = words[1].split("and")
    rev_alphabetical = str(second[0]) + " and " + str(second[1])

    title = str(alphabetical) + " : " + str(rev_alphabetical)

    plt.scatter(np_x, np_y)
    plt.plot(np_x, np_y)
    plt.xlabel("Year")
    plt.ylabel("Ratio")
    plt.title(title)

    plotfilename = "ratios/" + str(filename[8:-4]) + ".png"
    plt.savefig(plotfilename)

    print("COMPLETED " + str(outfilename))
    outfile.close()
