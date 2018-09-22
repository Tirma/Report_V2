#!/usr/bin/env python3
# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
import os

dir = "/home/thomas/Bureau/DBC/polychrom/no_fanout/"


visis = np.zeros((6*9, 23))
i = 0

for file in np.flip(["inter_0_334_1pixel", "inter_20_339_341_1pixel", "inter_40_338_342_1pixel", "inter_50_3375_3425_1pixel", "inter_60_337_343_1pixel", "inter_70_3365_3435_1pixel", "inter_100_335_345_1pixel", "inter_200_35_35_1pixel", "inter_300_325_355_1pixel"], axis=0):

    for BL in ["12", "13", "14", "23", "24", "34"]:
        visis[i] = np.loadtxt(dir+file+"/inter_I"+BL+".csv",
                              skiprows=1, usecols=2, delimiter=',')

        i += 1
visis = np.reshape(visis, 23*6*9)
plt.hist(visis, 25)

plt.show()
