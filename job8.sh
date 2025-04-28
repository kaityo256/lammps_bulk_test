#!/bin/sh

#SBATCH -p i8cpu
#SBATCH -N 8

source /home/issp/materiapps/intel/lammps/lammpsvars.sh

srun --exclusive --mem-per-cpu=1840 -n 512 -c 1 lammps < test1.input &
srun --exclusive --mem-per-cpu=1840 -n 512 -c 1 lammps < test2.input &

wait
cat test1.log
cat test2.log
