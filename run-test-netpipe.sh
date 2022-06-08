#!/bin/bash
#SBATCH --job-name=test-disk    # Job name
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --output=log-test-disk-%j.log   # Standard output and error log
pwd; hostname; date

mpirun python test-disk-mpi.py

date
