#include <benchmark/benchmark.h>
#include <PE_0056.hpp>

static void BM_PE_0056_Naive_Solution(benchmark::State& state) 
{
  // Perform setup here
  for (auto _ : state) 
  {
    project_euler::PE_0056_Naive_Solution();
  }
}
// Register the function as a benchmark
BENCHMARK(BM_PE_0056_Naive_Solution);


static void BM_PE_0056_Naive_Solution_With_Tweeks(benchmark::State& state) 
{
  // Perform setup here
  for (auto _ : state) 
  {
    project_euler::PE_0056_Naive_Solution_With_Tweeks();
  }
}
// Register the function as a benchmark
BENCHMARK(BM_PE_0056_Naive_Solution_With_Tweeks);
