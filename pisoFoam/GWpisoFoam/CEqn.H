dimensionedScalar VS
( 
	"VS", 
	dimensionSet(0,1,-1,0,0,0,0), 
	VSMALL
);
dimensionedScalar VSC
(
	"VSC",
	dimensionSet(1,-3,0,0,0,0,0),
	VSMALL
);

				volTensorField DTemp0
				(
					IOobject
					(
						"DTemp0",
						runTime.timeName(),
						mesh,
						IOobject::NO_READ,
						IOobject::NO_WRITE
					),
					mesh,
					tensor(1,0,0,0,0,0,0,0,0)
				);
				
				volTensorField DTemp1
				(
					IOobject
					(
						"DTemp1",
						runTime.timeName(),
						mesh,
						IOobject::NO_READ,
						IOobject::NO_WRITE
					),
					mesh,
					tensor(0,0,0,0,1,0,0,0,0)
				);
				
				volTensorField DTemp2
				(
					IOobject
					(
						"DTemp2",
						runTime.timeName(),
						mesh,
						IOobject::NO_READ,
						IOobject::NO_WRITE
					),
					mesh,
					tensor(0,0,0,0,0,0,0,0,1)
				);
				
				volTensorField Doff1
				(
					IOobject
					(
						"Doff1",
						runTime.timeName(),
						mesh,
						IOobject::NO_READ,
						IOobject::NO_WRITE
					),
					mesh,
					tensor(0,1,0,1,0,0,0,0,0)
				);
				
				volTensorField Doff2
				(
					IOobject
					(
						"Doff2",
						runTime.timeName(),
						mesh,
						IOobject::NO_READ,
						IOobject::NO_WRITE
					),
					mesh,
					tensor(0,0,1,0,0,0,1,0,0)
				);
				
				volTensorField Doff3
				(
					IOobject
					(
						"Doff3",
						runTime.timeName(),
						mesh,
						IOobject::NO_READ,
						IOobject::NO_WRITE
					),
					mesh,
					tensor(0,0,0,0,0,1,0,1,0)
				);
				


				D = 
					//DTemp0*(DmTemp)
					//+DTemp1*(DmTemp)
					//+DTemp2*(DmTemp);
					
					// main Diagonal
					DTemp0*(alphaT*mag(U)+Dm+(alphaL-alphaT)*U.component(0)*U.component(0)/(mag(U)+VS))+
					DTemp1*(alphaT*mag(U)+Dm+(alphaL-alphaT)*U.component(1)*U.component(1)/(mag(U)+VS))+
					DTemp2*(alphaT*mag(U)+Dm+(alphaL-alphaT)*U.component(2)*U.component(2)/(mag(U)+VS))+
					//off Diagonal
					Doff1*((alphaL-alphaT)*U.component(0)*U.component(1)/(mag(U)+VS))+
					Doff2*((alphaL-alphaT)*U.component(0)*U.component(2)/(mag(U)+VS))+
					Doff3*((alphaL-alphaT)*U.component(1)*U.component(2)/(mag(U)+VS));
					




CRmax = (Klang*beta*C)/(1+Klang*C); // langmuir isotherm
Ks = -(1-sign(Cim - CRmax)*1)/2*aa + (1 + sign(Cim-CRmax)*1)/2*ad; // aa is rate adsorbed, ad is rate desorbed
tmp<fvScalarMatrix> CEqn
(
	  fvm::ddt(Rf, C)
	- fvm::laplacian(D, C)
	+ fvm::div(phi/fvc::interpolate(rho),C)
	
);
//CEqn.solve();
//Ctot = C;
solve(CEqn ==  mag(1-Cim/(CRmax+VSC))*CRmax*Ks);
		
fvScalarMatrix CimEq
(
	fvm::ddt(Rf,Cim)
	+ mag(1-Cim/(CRmax+VSC))*CRmax*Ks // changed from + mag(1-Cim/(CRmax+VSC))*C*Ks 6/16/2016

);

CimEq.solve();
Cip = Cim*Km;
Ctot = C+Cip;



