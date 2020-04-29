#include<mpi.h>
#include<stdio.h>


int main() {

    int world_size;
    MPI_Comm_size(MPI_COMM_WORLD, &world_size);

    printf("my world rank is: ", world_size);

    if (world_size == 1) {
        printf("doing the task of rank 1");
    }

    if (world_size == 0) {
        printf("doing the task of rank 0");
    }

    if (world_size == 2) {
        printf("doing the task of rank 2");
    }

}