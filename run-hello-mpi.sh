#!/bin/bash
#SBATCH --job-name=hello-mpi    # Job name
#SBATCH --ntasks=8                    # Run on a single CPU
#SBATCH --output=hellompi_%j.log   # Standard output and error log
pwd; hostname; date

mpirun python hello-mpi.py

date
