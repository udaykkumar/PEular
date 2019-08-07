#include <benchmark/benchmark.h>
#include <PE_0001.hpp>

static void BM_PE_001_Naive_Solution(benchmark::State& state) 
{
  // Perform setup here
  for (auto _ : state) 
  {
    project_euler::solution_naive( );
  }
}
// Register the function as a benchmark
BENCHMARK(BM_PE_001_Naive_Solution);


static void BM_PE_001_Const_Time_Solution(benchmark::State& state) 
{
  for (auto _ : state)
  {
  	project_euler::solution_const_time();
  }
}
BENCHMARK(BM_PE_001_Const_Time_Solution);
