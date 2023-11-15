from typing import List

from openmm import XmlSerializer, app, unit


def to_openmm(topfile, coordfile, xmloutfile, pdboutfile, hmass: float = 1.0) -> List[str]:
    try:
        crd = app.GromacsGroFile(coordfile)
        top = app.GromacsTopFile(
            topfile, periodicBoxVectors=crd.getPeriodicBoxVectors())
    except Exception:
        try:
            top = app.AmberPrmtopFile(topfile)
            crd = app.AmberInpcrdFile(coordfile)
        except Exception:
            raise RuntimeError('can not read top and crd files!')
    system = top.createSystem(nonbondedMethod=app.PME, nonbondedCutoff=0.9*unit.nanometer,
                              constraints=app.HBonds, hydrogenMass=hmass * unit.amu)
    with open(xmloutfile, 'w') as output:
        output.write(XmlSerializer.serialize(system))
    if pdboutfile is not None:
        app.PDBFile.writeFile(top.topology, crd.positions,
                              open(pdboutfile, 'w'))


if __name__ == "__main__":
    pass
    # to_openmm('com.prmtop', 'com.gro', 'test.xml', 'test.pdb')
