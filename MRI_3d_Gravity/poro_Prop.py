# Generate fvOptions dict
import numpy as np

def poro_Prop(x):
	f = open('constant/fvOptions','r+')
	# delete all contents of setFieldsDict
	f.seek(0)
	f.truncate()
	
	# write new file
	f.write('/*--------------------------------*- C++ -*----------------------------------*\\\n')
	f.write('| =========                 |                                                 |\n')
	f.write('| \\\\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |\n')
	f.write('|  \\\\    /   O peration     | Version:  2.3.0                                 |\n')
	f.write('|   \\\\  /    A nd           | Web:      www.OpenFOAM.org                      |\n')
	f.write('|    \\\\/     M anipulation  |                                                 |\n')
	f.write('\\*---------------------------------------------------------------------------*/\n')
	f.write('FoamFile\n')
	f.write('{\n')
	f.write('    version     2.0;\n')
	f.write('    format      ascii;\n')
	f.write('    class       dictionary;\n')
	f.write('    location    "constant";\n')
	f.write('    object      fvOptions;\n')
	f.write('}\n')
	f.write('// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //\n\n')
	f.write('porosity1\n')
	f.write('{\n')
	f.write('	type		explicitPorositySource;\n')
	f.write('	active		yes;\n')
	f.write('\n')
	f.write('	explicitPorositySourceCoeffs\n')
	
	# calculate course sand darcy-forchheimer coeff = porosity/perm
	dfc = .25/x[0]
	f.write('	{\n')
	f.write('		selectionMode cellZone;\n')
	f.write('		cellZone      fineSand;\n')
	f.write('		type          DarcyForchheimer;\n')
	f.write('		DarcyForchheimerCoeffs\n')
	f.write('		{\n')
	
	f.write('			d	d [0 -2 0 0 0 0 0] ('+str(dfc)+' '+str(dfc)+' '+str(dfc)+');\n')
	f.write('			f	f [0 -1 0 0 0 0 0] (0 0 0);\n')
	f.write('			coordinateSystem\n')
	f.write('			{\n')
	f.write('				type	cartesian;\n')
	f.write('				origin	(0 0 0);\n')
	f.write('				coordinateRotation\n')
	f.write('				{\n')
	f.write('					type	axesRotation;\n')
	f.write('					e1		(0 0 1);\n')
	f.write('					e2		(0 1 0);\n')
	f.write('				}\n')
	f.write('			}\n')
	f.write('		}\n')
	f.write('	}\n')
	f.write('}\n')
	
	f.write('porosity2\n')
	f.write('{\n')
	f.write('	type		explicitPorositySource;\n')
	f.write('	active		yes;\n')
	f.write('\n')
	f.write('	explicitPorositySourceCoeffs\n')
	
	# calculate course sand darcy-forchheimer coeff = porosity/perm
	dfc = .25/x[1]
	f.write('	{\n')
	f.write('		selectionMode cellZone;\n')
	f.write('		cellZone      courseSand;\n')
	f.write('		type          DarcyForchheimer;\n')
	f.write('		DarcyForchheimerCoeffs\n')
	f.write('		{\n')
	
	f.write('			d	d [0 -2 0 0 0 0 0] ('+str(dfc)+' '+str(dfc)+' '+str(dfc)+');\n')
	f.write('			f	f [0 -1 0 0 0 0 0] (0 0 0);\n')
	f.write('			coordinateSystem\n')
	f.write('			{\n')
	f.write('				type	cartesian;\n')
	f.write('				origin	(0 0 0);\n')
	f.write('				coordinateRotation\n')
	f.write('				{\n')
	f.write('					type	axesRotation;\n')
	f.write('					e1		(0 0 1);\n')
	f.write('					e2		(0 1 0);\n')
	f.write('				}\n')
	f.write('			}\n')
	f.write('		}\n')
	f.write('	}\n')
	f.write('}\n')
	
	f.close()
	return	
