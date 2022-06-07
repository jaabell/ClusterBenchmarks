from mpi4py import MPI

comm = MPI.COMM_WORLD

rank = comm.Get_rank()
size = comm.Get_size()

write_path = "./results-hello-mpi"

with open(write_path+f"/hello-{rank}-of-{size}.txt","w") as fid:

	fid.write(f"Hi from rank {rank} of {size}.")
