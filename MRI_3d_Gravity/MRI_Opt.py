#!/usr/bin/env python
import numpy as np
import time
import os
from Gen_Set_Field import Set_Field
from poro_Prop import poro_Prop
from extract_data import *


class MRI_Opt:
	# using 18 parameters = dimensions
	# log(Dm), Kd, osmo, log(af), log(as), Km for outer, boundary, and mid sands
    def __init__(self, dim=12):
    	# xlow = lower dimension value?
    	# xup = upper dimension value?
       	# self.xlow = np.array([0,0,0,.5,.5,.5,0,0,0,0,0,0,0,0,0,0,0,0])
       	# self.xup = np.array([1e-2,1e-2,1e-2,5,5,5,1,1,1,1e-3,1e-3,1e-3,1e-3,1e-3,1e-3,10,10,10])
       	self.xlow = np.array([-13,-11,-11.3,-11.3,0,0,0,0,-12,-12,-12,-12])
       	self.xup = np.array([-11,-10,-10.3,-10.3,10,10,10,10,-5,-5,-5,-5])
        self.dim = dim
        self.info = str(dim)+" fitting parameters,  perm x2, Dm x2, Kd x2, osmo x2, af x2, as x2\n"
        self.integer = []
        self.continuous = np.arange(0, dim)
       
		
    def objfunction(self, x):
        if len(x) != self.dim:
            raise ValueError('Dimension mismatch')
        
        # convert x to the appropriate values for entries
        print('x values: ')
        print(x)
        y = np.copy(x)
        print('y values: ')
        print(y)
        y[0:4] = 10.0**y[0:4]
        y[8:12] = 10.0**y[8:12]
        print('updated y values: ')
        print(y)
        
        # double check range constraints
        for i in range(0,y.size):
            if i < 4 or (i>=8 and i<12):
                # compare values that are exponential
                if y[i] > 10**self.xup[i]:
                    print('out of range, upper log '+ str(i) +'x: '+str(x[i])+' '+str(y[i])+' >? '+str(10**self.xup[i]))
                    y[i] = 10**self.xup[i]
                    x[i] = self.xup[i]
                elif y[i] < 10**self.xlow[i]:
                    print('out of range, lower log '+ str(i) +'x: '+str(x[i])+' '+str(y[i])+' <? '+str(10**self.xlow[i]))
                    y[i] = 10**self.xlow[i]
                    x[i] = self.xow[i]
            else:
                # compare values that are not exponential
                if y[i] > self.xup[i]:
                    print('out of range, upper '+ str(i) +'x: '+str(x[i])+' '+str(y[i])+' >? '+str(self.xup[i]))
                    y[i] = self.xup[i]
                    x[i] = self.xup[i]
                elif y[i] < self.xlow[i]:
                    print('out of range, lower '+ str(i) +'x: '+str(x[i])+' '+str(y[i])+' <? '+str(self.xlow[i]))
                    y[i] = self.xlow[i]
                    x[i] = self.xup[i]
		    		
       	
       	print('Setting Field')
       	print(str(y))
       	
        # generate setfields input file
        Set_Field(y)
        poro_Prop(y)
        
        # call ./Allclean and then ./Allrun
        os.system("./Allclean")
        os.system("./Allrun")
        
        # extract values to compare for root mean squared error
        # handle case where openfoam failed to run
        try:
        	mod_data = extract_mod_data()
        except:
        	return 1000
        	
        act_data = extract_act_data()
        
        # check to make sure we have enough mod data
        if mod_data.size < act_data.size:
            return 1000
        else:        
            # take only the values from mod_data that match act_data
            j = 0
            nmod_data = np.zeros((act_data.shape[0],act_data.shape[1]))
            for i in range(0,mod_data.shape[0]):
            	if act_data[j][0] < mod_data[i][0]:
            		j = j+1
            	if mod_data[i][0] == act_data[j][0]:
            		nmod_data[j] = mod_data[i]
            
            # flatten data for comparison
            mod = np.reshape(nmod_data,(nmod_data.size))
            act = np.reshape(act_data,(act_data.size))
            
            # check to make sure that mod_data and act_data are the same size
            if mod.shape == act.shape:
            	# write data to file
            	fname = 'results.csv'
            	comb = np.concatenate((y,mod))
            	comb = np.reshape(comb,(1,comb.size))
            	f = open(fname,'a')
            	np.savetxt(f,comb,delimiter=",")
            	f.close()
                return np.sqrt(((mod - act) ** 2).mean())
            else:
                return 1000
