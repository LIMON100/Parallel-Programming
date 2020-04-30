from mpi4py import MPI

comm = MPI.COMM_WORLD

rank = comm.Get_rank()
size = comm.Get_size()

print(rank)
print(size)

if rank == 0:
    data = [(x+1)**x for x in range(size)]
    print("We will be scattering" , data)
    
else:
    data = None
    
data = comm.scatter(data , root = 0)
print("rank " , rank , "has data " , data)

data = data+5

newdata = comm.gather(data , root = 0)

if rank == 0:
    print("Master collected: " , newdata)