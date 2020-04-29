from mpi4py import MPI

comm = MPI.COMM_WORLD

print('Hi , My rank is: ',comm.rank)
