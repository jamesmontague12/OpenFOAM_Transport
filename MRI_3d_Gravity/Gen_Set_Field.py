# Generate set fields dict
import numpy as np

def Set_Field(x):
	f = open('system/setFieldsDict','r+')
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
	f.write('    location    "system";\n')
	f.write('    object      setFieldsDict;\n')
	f.write('}\n')
	f.write('// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //\n\n')
	f.write('defaultFieldValues\n')
	f.write('(\n')
	f.write('    volScalarFieldValue alphaT 2.5e-5\n')
	f.write('    volScalarFieldValue alphaL 2.5e-4\n')
	f.write('    volScalarFieldValue Rf 1\n')
	f.write('    volScalarFieldValue C 0\n')
	f.write('    volScalarFieldValue am 1e-16\n')
	f.write('    volScalarFieldValue aim 1\n')
	f.write('    volScalarFieldValue vcrit 1e-10\n')
	f.write('    volScalarFieldValue diam 100e-6\n')
	f.write('    volScalarFieldValue Dm '+str(x[2])+'\n')
	f.write('    volScalarFieldValue Klang '+str(x[4])+'\n')
	f.write('    volScalarFieldValue beta '+str(x[6])+'\n')
	f.write('    volScalarFieldValue aa '+str(x[8])+'\n')
	f.write('    volScalarFieldValue ad '+str(x[10])+'\n')
	f.write('    volScalarFieldValue Km 1\n')
	f.write(');\n\n')
	f.write('regions\n')
	f.write('(\n')
	f.write('    // fine sand\n')
	f.write('    cylinderToCell\n')
	f.write('    {\n')
	f.write('        p1 (0 0 0.0616666667);\n')
	f.write('        p2 (0 0 -0.0616666667);\n')
	f.write('        radius .0365125;\n')
	f.write('        fieldValues\n')
	f.write('        (\n')
	f.write('            volScalarFieldValue alphaT 2e-6\n')
	f.write('    \t\tvolScalarFieldValue alphaL 2e-5\n')
	f.write('           \tvolScalarFieldValue am 1e-3\n')
	f.write('           \tvolScalarFieldValue aim 5\n')
	
	# Ctot = 2.9, so need to set Ctot = C + Cim
	Ctot = 2.9
	b = x[5]*x[7]-Ctot*x[5]+1
	a = x[5]
	c = -Ctot
	cp = (-b+np.sqrt(np.power(b,2)-4*a*c))/(2*a)
	cm = (-b-np.sqrt(np.power(b,2)-4*a*c))/(2*a)
	conc=0
	if cp>=0 and cp<=Ctot:
		conc=cp
	elif cm>=0 and cm<=Ctot:
		conc=cm
	else:
		conc=Ctot
	cim = (Ctot-conc)
	print('conc: '+str(conc))
	print('cim: '+str(cim))
	
	f.write('           \tvolScalarFieldValue C '+str(conc)+'\n')
	f.write('           \tvolScalarFieldValue Cim '+str(cim)+'\n')
	f.write('           \tvolScalarFieldValue Ctot '+str(Ctot)+'\n')
	f.write('           \tvolScalarFieldValue diam 7e-6\n')
	f.write('           \tvolScalarFieldValue n 0.2\n')
	f.write('           \tvolScalarFieldValue rhoS 2837\n')
	f.write('           \tvolScalarFieldValue Dm '+str(x[3])+'\n')
	f.write('           \tvolScalarFieldValue Klang '+str(x[5])+'\n')
	f.write('           \tvolScalarFieldValue beta '+str(x[7])+'\n')
	f.write('           \tvolScalarFieldValue aa '+str(x[9])+'\n')
	f.write('           \tvolScalarFieldValue ad '+str(x[11])+'\n')
	f.write('           \tvolScalarFieldValue Km 1\n')
	f.write('        );\n')
	f.write('    }\n')
	f.write('        \n')
	f.write(');\n\n')
	f.write('\n//************************************************************************* //\n')
	f.close()
	return
