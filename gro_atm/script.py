#! python
import argparse
import json

from .common import to_openmm
from .config import Config

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--top', required=True, help='gromacs top file')
parser.add_argument('-g', '--gro', required=True, help='gromacs gro file')
parser.add_argument('-c', "--config", required=True, default=None,
                    help='Configuration file, in JSON format.')
parser.add_argument("--config_out", required=True,
                    help='Configuration out file, in ini format.')
parser.add_argument('--tpr', default='file.tpr',
                    help=('path to input structure topology file '
                          '(e.g. TPR, PARM7, etc...)'))
parser.add_argument('--traj', default='file.xtc',
                    help=('path to input trajectory file'
                          '(e.g. XTC, NC, TRJ'))
parser.add_argument('--ligand_selection', default="resname LIG",
                    help='ligand selection string')
parser.add_argument('--host_selection', default="protein and name CA",
                    help='host atom selection string')
parser.add_argument('--temperature', type=float, default=298.15,
                    help='simulation temperature')
parser.add_argument('--force_constant', type=float, default=10.0,
                    help='restraint force constant')
parser.add_argument('--outfile', default='result.json',
                    help='output path for writing files')
args = parser.parse_args()


if __name__ == '__main__':
    config = Config(args, args.c)
    basename = config.BASENAME + '_atm'
    to_openmm(args.p, args.g, basename + '_sys.xml', basename + '.pdb')

    config.write_config('asyncre.cntl')

    # config = json.load(open(sys.argv[1], 'r'))
