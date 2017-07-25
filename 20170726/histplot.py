import glob
import os

import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

csv_list = glob.glob("*.csv")

#logfile = "mydata.csv"
for logfile in csv_list:
    filename, file_extension = os.path.splitext(logfile)
    time_t, temperature, pwr, tempe_bottom, P, I, D = np.loadtxt(logfile, delimiter=',', unpack=True)
    fig, ax = plt.subplots()
    ax.hist(temperature, bins=50);
    fig.savefig(filename + ".png")
