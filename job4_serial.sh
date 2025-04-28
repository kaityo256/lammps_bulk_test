#!/bin/sh

#SBATCH -p i8cpu
#SBATCH -N 4
#SBATCH -n 512

source /home/issp/materiapps/intel/lammps/lammpsvars.sh

srun lammps < test1.input
srun lammps < test2.input

cat test1.log
cat test2.log
