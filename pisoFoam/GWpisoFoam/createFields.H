    Info<< "Reading thermophysical properties\n" << endl;

    autoPtr<rhoThermo> pThermo
    (
        rhoThermo::New(mesh)
    );
    rhoThermo& thermo = pThermo();
    thermo.validate(args.executable(), "h", "e");

    volScalarField rho
    (
        IOobject
        (
            "rho",
            runTime.timeName(),
            mesh,
            IOobject::READ_IF_PRESENT,
            IOobject::AUTO_WRITE
        ),
        thermo.rho()
    );

    volScalarField& p = thermo.p();

    Info<< "Reading field U\n" << endl;
    volVectorField U
    (
        IOobject
        (
            "U",
            runTime.timeName(),
            mesh,
            IOobject::MUST_READ,
            IOobject::AUTO_WRITE
        ),
        mesh
    );
    
     Info<< "Reading field C\n" << endl;
    volScalarField C
    (
        IOobject
        (
            "C",
            runTime.timeName(),
            mesh,
            IOobject::MUST_READ,
            IOobject::AUTO_WRITE
        ),
        mesh
    );
      
    Info<< "Reading field beta\n" << endl;
    volScalarField beta
    (
        IOobject
        (
            "beta",
            runTime.timeName(),
            mesh,
            IOobject::MUST_READ,
            IOobject::AUTO_WRITE
        ),
        mesh
    );
    
    Info<< "Reading field Cim\n" << endl;
    volScalarField Cim
    (
        IOobject
        (
            "Cim",
            runTime.timeName(),
            mesh,
            IOobject::MUST_READ,
            IOobject::AUTO_WRITE
        ),
        mesh
    );
    
    Info<< "Reading field Cip\n" << endl;
    volScalarField Cip
    (
        IOobject
        (
            "Cip",
            runTime.timeName(),
            mesh,
            IOobject::MUST_READ,
            IOobject::AUTO_WRITE
        ),
        mesh
    );
        
     Info<< "Reading field Ctot\n" << endl;
    volScalarField Ctot
    (
        IOobject
        (
            "Ctot",
            runTime.timeName(),
            mesh,
            IOobject::MUST_READ,
            IOobject::AUTO_WRITE
        ),
        mesh
    );
    
     Info<< "Reading field CRmax\n" << endl;
    volScalarField CRmax
    (
        IOobject
        (
            "CRmax",
            runTime.timeName(),
            mesh,
            IOobject::MUST_READ,
            IOobject::AUTO_WRITE
        ),
        mesh
    );
        
    Info<< "Reading field Ks\n" << endl;
    volScalarField Ks
    (
        IOobject
        (
            "Ks",
            runTime.timeName(),
            mesh,
            IOobject::MUST_READ,
            IOobject::AUTO_WRITE
        ),
        mesh
    );

    Info<< "Reading field aa\n" << endl;
    volScalarField aa
    (
        IOobject
        (
            "aa",
            runTime.timeName(),
            mesh,
            IOobject::MUST_READ,
            IOobject::AUTO_WRITE
        ),
        mesh
    );

    Info<< "Reading field ad\n" << endl;
    volScalarField ad
    (
        IOobject
        (
            "ad",
            runTime.timeName(),
            mesh,
            IOobject::MUST_READ,
            IOobject::AUTO_WRITE
        ),
        mesh
    );

        
    Info<< "Reading field Klang\n" << endl;
    volScalarField Klang
    (
        IOobject
        (
            "Klang",
            runTime.timeName(),
            mesh,
            IOobject::MUST_READ,
            IOobject::AUTO_WRITE
        ),
        mesh
    );
    
    Info<< "Reading field Km\n" << endl;
    volScalarField Km
    (
        IOobject
        (
            "Km",
            runTime.timeName(),
            mesh,
            IOobject::MUST_READ,
            IOobject::AUTO_WRITE
        ),
        mesh
    );  
    
	Info<< "   Reading field D\n" << endl;
    volTensorField D
    (
    	IOobject
    	(
			"D",
            runTime.timeName(),
            mesh,
            IOobject::MUST_READ,
            IOobject::AUTO_WRITE
        ),
        mesh
    );
    
    Info<< "   Reading field Dm\n" << endl;
    volScalarField Dm
    (
    	IOobject
    	(
			"Dm",
            runTime.timeName(),
            mesh,
            IOobject::MUST_READ,
            IOobject::AUTO_WRITE
        ),
        mesh
    );
    
    Info<< "   Reading field alphaT\n" << endl;
    volScalarField alphaT
    (
    	IOobject
    	(
			"alphaT",
            runTime.timeName(),
            mesh,
            IOobject::MUST_READ,
            IOobject::AUTO_WRITE
        ),
        mesh
    );
    
    Info<< "   Reading field alphaL\n" << endl;
    volScalarField alphaL
    (
    	IOobject
    	(
			"alphaL",
            runTime.timeName(),
            mesh,
            IOobject::MUST_READ,
            IOobject::AUTO_WRITE
        ),
        mesh
    );
    
    Info<< "   Reading field Rf\n" << endl;
    volScalarField Rf
    (
    	IOobject
    	(
			"Rf",
            runTime.timeName(),
            mesh,
            IOobject::MUST_READ,
            IOobject::AUTO_WRITE
        ),
        mesh
    );
    
    Info<< "   Reading field perm\n" << endl;
    volScalarField perm
    (
    	IOobject
    	(
			"perm",
            runTime.timeName(),
            mesh,
            IOobject::MUST_READ,
            IOobject::AUTO_WRITE
        ),
        mesh
    );
    
     Info<< "   Reading field rhof\n" << endl;
    volScalarField rhof
    (
    	IOobject
    	(
			"rhof",
            runTime.timeName(),
            mesh,
            IOobject::MUST_READ,
            IOobject::AUTO_WRITE
        ),
        mesh
    );
    
    Info<< "   Reading field T\n" << endl;
    volScalarField T
    (
    	IOobject
    	(
			"T",
            runTime.timeName(),
            mesh,
            IOobject::MUST_READ,
            IOobject::AUTO_WRITE
        ),
        mesh
    );

    Info<< "   Reading field M\n" << endl;
    volScalarField M
    (
    	IOobject
    	(
			"M",
            runTime.timeName(),
            mesh,
            IOobject::MUST_READ,
            IOobject::AUTO_WRITE
        ),
        mesh
    );

    #include "compressibleCreatePhi.H"


    label pRefCell = 0;
    scalar pRefValue = 0.0;

    //dimensionedScalar rhoMax(simple.dict().lookup("rhoMax"));
    //dimensionedScalar rhoMin(simple.dict().lookup("rhoMin"));

	Info<< "Creating turbulence model\n" << endl;
	autoPtr<compressible::turbulenceModel> turbulence
	(
		compressible::turbulenceModel::New
		(
			rho,
			U,
			phi,
			thermo
		)
	);
	dimensionedScalar initialMass = fvc::domainIntegrate(rho);
    
    IOdictionary transportProperties
    (
        IOobject
        (
            "transportProperties",
            runTime.constant(),
            mesh,
            IOobject::MUST_READ_IF_MODIFIED,
            IOobject::NO_WRITE
        )
    );
    
    
  
#include "readGravitationalAcceleration.H"
#include "readhRef.H"
#include "gh.H"

