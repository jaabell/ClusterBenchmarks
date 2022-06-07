from mpi4py import MPI
import numpy as np
from time import perf_counter
import os

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()


check = False
write_path = "./results-bcast"
sizes_of_sends = [10**i for i in range(1,8)]
nrepeats = 4


time_taken = []

for repeat in range(nrepeats):
    for sz in sizes_of_sends:

        if rank == 0:
            print(f"Broadcast test for sz={sz}")
            data = np.arange(sz, dtype='i')
        else:
            data = np.empty(sz, dtype='i')

        t1 = perf_counter()
        comm.Bcast(data, root=0)
        t2 = perf_counter()

        if check:
            for i in range(sz):
                assert data[i] == i


        if rank == 0:

            print(f"Rank 0 writing data for sz={sz} repeat={repeat}")
            if not os.path.exists(write_path):
                os.makedirs(write_path)
            with open(write_path+f"/test-bcast-size-{size}.txt","a") as fid:
                fid.write(f"{sz} {t2-t1}\n")



    # print(f"Rank {rank} of {size} done with repeat {repeat}")
