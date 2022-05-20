import numpy as np
from time import perf_counter
import os
from sys import argv
from mpi4py import MPI

hostname = os.uname()[1]

comm = MPI.COMM_WORLD

rank = comm.Get_rank()
size = comm.Get_size()

N = 10000000
repeats = 3
fname = f"bytes.{rank}.{size}.bin"
check_write = False

if len(argv) > 1:
	N = int(argv[1])
if len(argv) > 2:
	repeats = int(argv[2])
if len(argv) > 3:
	fname = argv[3]
if len(argv) > 4:
	check_write = bool(argv[4])


read_performances = []
write_performances = []

print(f"Using N = {N} repeats = {repeats} fname = {fname} check_write = {check_write}")

for iteration in range(repeats):

	A = np.random.rand(N)
	dtype = A.dtype
	byteammount = A.itemsize * A.size

	print(f"Writing {byteammount/1e6} MB")

	with open(fname,"wb") as fid:
		t1 = perf_counter()
		A.tofile(fid)
		t2 = perf_counter()

	write_performance = byteammount/(t2-t1)/1e6
	print(f"Write performance {write_performance:.3f} MB/s")
	write_performances.append(write_performance)

	if not check_write:
		A = None

	t1 = perf_counter()
	B = np.fromfile(fname,dtype=dtype)
	t2 = perf_counter()

	read_performance = byteammount/(t2-t1)/1e6
	print(f"Read performance  {read_performance:.3f} MB/s")
	read_performances.append(read_performance)

	if check_write:
		error = abs(A-B).max()
		print(f"     ---> error = {error}")

with open(f"performance.{rank}.{size}.txt","w") as fid:
	fid.write(f"rank = {rank} size = {size} hostname = {hostname}\n")
	fid.write(f"Write MB/s -- average = {np.mean(write_performances):.3f}  std_dev = {np.std(write_performances):.3f}  min = {np.min(write_performances):.3f} max = {np.max(write_performances):.3f}\n")
	fid.write(f"Read  MB/s -- average = {np.mean(read_performances):.3f}  std_dev = {np.std(read_performances):.3f}  min = {np.min(read_performances):.3f} max = {np.max(read_performances):.3f}\n")
