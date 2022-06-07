#!/bin/bash
#SBATCH --job-name=test-bcast    # Job name
#SBATCH --nodes=8
#SBATCH --ntasks-per-node=16
#SBATCH --output=log-test-bcast-%j.log   # Standard output and error log
pwd; hostname; date

mpirun python test-bcast.py

date
