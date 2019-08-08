#include <benchmark/benchmark.h>
#include <PE_0004.hpp>

static void BM_PE_0004_Naive_Solution(benchmark::State& state) 
{
  // Perform setup here
  for (auto _ : state) 
  {
    project_euler::PE_0004_Naive_Solution();
  }
}
// Register the function as a benchmark
BENCHMARK(BM_PE_0004_Naive_Solution);

static void BM_PE_0004_Naive_Solution_Better(benchmark::State& state) 
{
  // Perform setup here
  for (auto _ : state) 
  {
    project_euler::PE_0004_Naive_Solution_Better();
  }
}
// Register the function as a benchmark
BENCHMARK(BM_PE_0004_Naive_Solution_Better);

