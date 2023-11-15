import json
from .FlatBottomRestraint import find_plat_bottom

class Config():
    def __init__(self, args, template=None) -> None:
        self.config = {}
        if template is None:
            self.init_config()
        else:
            self.config = json.load(open(template, 'r'))
        find_plat_bottom(args=args)
        site = json.load(open(args.outfile, 'r'))
        self.config['LIGAND_ATOMS'] = site['lig_ids']
        self.config['LIGAND_CM_ATOMS'] = site['lig_ids']
        self.config['RCPT_CM_ATOMS'] = site['binding_sites']
        self.config['POS_RESTRAINED_ATOMS'] = site['prot_ids']
        self.__dict__.update(self.config)
    def init_config(self):
        # const
        self.config['JOB_TRANSPORT'] = 'LOCAL_OPENMM'
        self.config['TEMPERATURES'] = '300'
        self.config['BASENAME'] = ''
        self.config['LAMBDAS'] = '0.00, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 1.00'
        self.config['DIRECTION'] = '   1,    1,    1,    1,    1,    1,    1,    1,    1,    1,    1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1'
        self.config['INTERMEDIATE'] = '   0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    1,    1,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0'
        self.config['LAMBDA1'] = '0.00, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.50, 0.45, 0.40, 0.35, 0.30, 0.25, 0.20, 0.15, 0.10, 0.05, 0.00'
        self.config['LAMBDA2'] = '0.00, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.50, 0.45, 0.40, 0.35, 0.30, 0.25, 0.20, 0.15, 0.10, 0.05, 0.00'
        self.config['ALPHA'] = '0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00'
        self.config['U0'] = '0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00'
        self.config['W0COEFF'] = '0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00'

        self.config['DISPLACEMENT'] = '22,22,22'
        self.config['LIGOFFSET'] = ' 0, 0, 0 '
        self.config['WALL_TIME'] = 120
        self.config['CYCLE_TIME'] = 10
        self.config['CHECKPOINT_TIME'] = 1200
        self.config['NODEFILE'] = 'nodefile'
        self.config['SUBJOBS_BUFFER_SIZE'] = '1.000000'
        self.config['PRODUCTION_STEPS'] = '5000'
        self.config['PRNT_FREQUENCY'] = '5000'
        self.config['TRJ_FREQUENCY'] = '5000'
        self.config['LIGAND_ATOMS'] = '<LIGATOMS>'
        self.config['LIGAND_CM_ATOMS'] = '<LIGATOMS>'
        self.config['RCPT_CM_ATOMS'] = '<VSITERECEPTORATOMS>'
        self.config['CM_KF'] = 25.00
        self.config['CM_TOL'] = 5
        self.config['POS_RESTRAINED_ATOMS'] = '<RESTRAINEDATOMS>'
        self.config['POSRE_FORCE_CONSTANT'] = 25.0
        self.config['POSRE_TOLERANCE'] = 1.5
        self.config['UMAX'] = 100.00
        self.config['ACORE'] = 0.062500
        self.config['UBCORE'] = 50.0
        self.config['FRICTION_COEFF'] = 0.500000
        self.config['TIME_STEP'] = 0.002
        self.config['OPENMM_PLATFORM'] = 'CUDA'
        self.config['VERBOSE'] = 'no'

    def write_config(self, config_file):
        with open(config_file, 'w') as f:
            for key, value in self.config.items():
                f.write(f'{key} = {value}\n')