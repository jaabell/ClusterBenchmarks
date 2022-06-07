#!/bin/bash
#SBATCH --job-name=mpi-hello    # Job name
#SBATCH --ntasks=8                    # Run on a single CPU
#SBATCH --output=serial_test_%j.log   # Standard output and error log
pwd; hostname; date

mpirun python hello_mpi.py

date
