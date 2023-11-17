from setuptools import setup

NAME = 'gro_atm'
SCRIPTS = {'console_scripts': ['gro_atm = gro_atm:script']}
REQUIRES = 'MDRestraintsGenerator'
DESCRIPTION = 'using atm to gromacs'
AUTHOR = '9527567'
AUTHOR_EMAIL = 'z9527567@gmail.com'
setup(name=NAME,
      version="1.0",
      description=DESCRIPTION,
      author=AUTHOR,
      packages=['gro_atm'],
      author_email=AUTHOR_EMAIL,
      entry_points=SCRIPTS,
      requires=REQUIRES,
      )
