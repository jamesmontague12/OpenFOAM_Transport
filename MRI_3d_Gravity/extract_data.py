import numpy as np

def extract_mod_data():
	# extract data from cases in the correct locations
	try:
	    fname = 'postProcessing/probes/0/Ctot'
	    data = np.loadtxt(fname,comments='#')
	except IOError:
	    print('IO Error')
	    data = np.array([86400, 0, 0, 0, 0, 0])
	# convert first column of data to days rather than seconds
	# check for correct shape
	if data.size == data.shape[0]:
	    data[0] = data[0]/86400
	else:
	    for i in range(0,data.shape[0]):
		    data[i][0] = data[i][0]/86400
		
	return data
	
def extract_act_data():
	# extract data from mri results
	fname = 'MRI_Act_Results'
	data = np.loadtxt(fname,comments='#')
	return data
