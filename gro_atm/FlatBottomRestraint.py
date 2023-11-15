import argparse
import json
import warnings

import MDAnalysis as mda
from MDRestraintsGenerator import search
from MDRestraintsGenerator.restraints import (FindBoreschRestraint,
                                              FindFlatBottomRestraint)


def find_plat_bottom(args):

    u = mda.Universe(args.top, args.traj)
    lig = u.select_atoms(args.ligand_selection)
    prot = u.select_atoms(args.host_selection)
    finder = search.FindBindingSite(ligand=lig, host=prot)
    finder.run()

    flat_bottom = FindFlatBottomRestraint(lig, finder.binding_site)

    # Run the restraint analysis
    flat_bottom.run()

    result = {}
    lig_ids = flat_bottom.restraint.atomgroups[0].ids
    binding_site = flat_bottom.restraint.atomgroups[1].ids
    dG_off = flat_bottom.restraint.standard_state()

    result['lig_ids'] = lig_ids.tolist()
    result['binding_site'] = binding_site.tolist()
    result['prot_ids'] = prot.tolist()
    result['dG_off'] = dG_off
    with open(args.outfile, 'w') as f:
        json.dump(result, f)
