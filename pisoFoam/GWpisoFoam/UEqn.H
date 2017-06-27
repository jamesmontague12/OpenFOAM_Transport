// Solve the Momentum equation

MRF.correctBoundaryVelocity(U);
std::cout<<"here"<<std::endl;
fvVectorMatrix UEqn
(
    fvm::ddt(rho, U) + fvm::div(phi, U)
  + MRF.DDt(rho, U)
  + turbulence->divDevRhoReff(U)
 ==
    fvOptions(rho, U)
);
std::cout<<"here1"<<std::endl;
UEqn.relax();

fvOptions.constrain(UEqn);

if (piso.momentumPredictor())
{
    solve
        (
            UEqn
         ==
            fvc::reconstruct
            (
                (
                  - ghf*fvc::snGrad(rho)
                  - fvc::snGrad(p)
                )*mesh.magSf()
            )
        );

    fvOptions.correct(U);
}
