#include <benchmark/benchmark.h>
#include <PE_0003.hpp>

static void BM_PE_0003_Naive_Solution(benchmark::State& state) 
{
  // Perform setup here
  for (auto _ : state) 
  {
    project_euler::PE_0003_Naive_Solution() ;
  }
}
// Register the function as a benchmark
BENCHMARK(BM_PE_0003_Naive_Solution);


static void BM_PE_0003_Find_Better_Solution_Trial_1(benchmark::State& state) 
{
  // Perform setup here
  for (auto _ : state) 
  {
    project_euler::PE_0003_Find_Better_Solution_Trial_1() ;
  }
}
// Register the function as a benchmark
BENCHMARK(BM_PE_0003_Find_Better_Solution_Trial_1);


static void BM_PE_0003_Find_Better_Solution_Trial_2(benchmark::State& state) 
{
  // Perform setup here
  for (auto _ : state) 
  {
    project_euler::PE_0003_Find_Better_Solution_Trial_2() ;
  }
}
// Register the function as a benchmark
BENCHMARK(BM_PE_0003_Find_Better_Solution_Trial_2);


static void BM_PE_0003_Find_Better_Solution_Trial_3(benchmark::State& state) 
{
  // Perform setup here
  for (auto _ : state) 
  {
    project_euler::PE_0003_Find_Better_Solution_Trial_3() ;
  }
}
// Register the function as a benchmark
BENCHMARK(BM_PE_0003_Find_Better_Solution_Trial_3);
