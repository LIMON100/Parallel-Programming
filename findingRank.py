from mpi4py import MPI

comm = MPI.COMM_WORLD

print('Hi , My rank is: ',comm.rank)


#include<mpi.h>

comm = MPI.COMM_WORLD

printf("my world rank is: " , comm.rank);

if(comm.rank == 1){
    printf("doing the task of rank 1");
}

if(comm.rank == 0){
    printf("doing the task of rank 0");
}

if(comm.rank == 2){
    printf("doing the task of rank 2");
}
    
    
