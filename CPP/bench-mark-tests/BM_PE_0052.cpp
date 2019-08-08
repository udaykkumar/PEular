#include <benchmark/benchmark.h>
#include <PE_0052.hpp>

static void BM_PE_0052_Solution(benchmark::State& state) 
{
  // Perform setup here
  for (auto _ : state) 
  {
    project_euler::PE_0052_Naive_Solution();
  }
}
// Register the function as a benchmark
BENCHMARK(BM_PE_0052_Solution);

