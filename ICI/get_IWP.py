#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 14:50:28 2020

@author: inderpreet
"""


from data import Profiles
import numpy as np
import glob
import os
import xarray

def get_IWP(files_cs):
    Z = []
    data = []
    first_iteration = True
    for file_clearsky in files_cs:

        file_allsky  = file_clearsky.replace('_clearsky.nc', '.nc')
#        print (file_clearsky, file_allsky)
        
        if os.path.isfile(file_allsky):

            y = xarray.open_dataset(file_allsky)
            y_ici_allsky = y.y_ici
            
            y = xarray.open_dataset(file_clearsky)
    #        print(file_clearsky)
            y_ici_clearsky = y.y_ici
            
            allsky       = y_ici_allsky.shape[0]
            clearsky     = y_ici_clearsky.shape[0]
            
            cases = min(allsky, clearsky)
            
            file_mat = file_allsky.replace('ICI', 'Cases')
            file_mat = file_mat.replace('.nc', '.mat')
            print (file_mat)
                
            dataset = Profiles(file_mat)

            for i in range(cases):
                    dbz = dataset.get_y_cloudsat(i)
                    data.append(list(dbz))

#            if first_iteration:        
#                Z = data
#                first_iteration = False

 #           else:
 #               print (len(data))
 #               Z.append(data)

    return data