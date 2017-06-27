# pySOT optimization

# Import the necessary modules
from pySOT import *
#from pySOT import MARSInterpolant
from poap.controller import SerialController, ThreadController, BasicWorkerThread
import numpy as np
from MRI_Opt import *
import time
from Gen_Set_Field import Set_Field
import os

start = time.time()
# Decide how many evaluations we are allowed to use
maxeval = 250

try:
	os.remove('results.csv')
except:
	pass

# (1) Optimization problem
data = MRI_Opt(dim=12)

# (2) Experimental design
# Use a symmetric Latin hypercube with 2d + 1 samples
exp_des = SymmetricLatinHypercube(dim=data.dim, npts=2*data.dim+1)

# (3) Surrogate model
# Use a cubic RBF interpolant, with the domain scaled to the unit box
#surrogate = RSUnitbox(RBFInterpolant(surftype=CubicRBFSurface, maxp=maxeval), data)
surrogate = RBFInterpolant(kernel=CubicKernel, tail=LinearTail, maxp=maxeval)
#surrogate = RSUnitbox(MARSInterpolant(maxp=500), data)

# (4) Adaptive sampling
# Use DYCORS with 100d candidate points
adapt_samp = CandidateDYCORS(data=data, numcand=100*data.dim)

# Use the serial controller (uses only one thread)
controller = SerialController(data.objfunction)

# (5) Use the sychronous strategy without non-bound constraints
strategy = SyncStrategyNoConstraints(worker_id=0, data=data, maxeval=maxeval, nsamples=1, exp_design=exp_des, response_surface=surrogate, sampling_method=adapt_samp)#,extra = np.array([[-10.0969,-9.347,-9.222,1,2.25,1.665,.1,.7,.34,-6,-5.523,-5.824,-6,-6.456,-8,1,4,4]]))#([[8e-11,4.5e-10,6e-10,1,2.25,1.665,.1,.7,.34,1e-6,3e-6,1.5e-6,1e-6,3.5e-7,1e-8,1,4,4]]))
controller.strategy = strategy

# Run the optimization strategy
result = controller.run()

# Print the final result
print('Best value found: {0}'.format(result.value))
print('Best solution found with powers: {0}'.format(np.array_str(result.params[0], max_line_width=np.inf,precision=16, suppress_small=True)))
act_result = np.copy(result.params[0])
act_result[0:4] = 10**act_result[0:4]
act_result[8:12] = 10**act_result[8:12]
print('Best solution found real numbers: {0}'.format(np.array_str(act_result, max_line_width=np.inf,precision=16, suppress_small=True)))


end = time.time()
print end - start

# set field to the best result
Set_Field(act_result)
# run final result
# call ./Allclean and then ./Allrun
os.system("./Allclean")
os.system("./Allrun")
            
#%matplotlib inline
import matplotlib.pyplot as plt

# Extract function values from the controller
fvals = np.array([o.value for o in controller.fevals])

f, ax = plt.subplots()
ax.plot(np.arange(0,maxeval), fvals, 'bo')  # Points
ax.plot(np.arange(0,maxeval), np.minimum.accumulate(fvals), 'r-', linewidth=4.0)  # Best value found
plt.xlabel('Evaluations')
plt.ylabel('Function Value')
plt.title(data.info)
plt.show()
