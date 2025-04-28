#!/bin/sh

#SBATCH -p i8cpu
#SBATCH -N 1
#SBATCH -n 128

source /home/issp/materiapps/intel/lammps/lammpsvars.sh

srun lammps < test1.input
cat test1.log

