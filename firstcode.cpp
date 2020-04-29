#include<bits/stdc++.h>
#include "mpi.h"

using namespace std;

int main(int argc , char* arg[])
{

  MPI::Init(argc , argv);

  auto mpisize = MPI::COMM_WORLD.Get_size();
  auto mpirank = MPI::COMM_WORLD.Get_rank();

  cout<<"Hello world "<<mpirank<<" out of "<<mpisize<<endl;

  MPI::Finalize();

  return 0;
}
