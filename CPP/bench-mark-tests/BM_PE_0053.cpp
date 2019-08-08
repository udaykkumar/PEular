#include <benchmark/benchmark.h>
#include <PE_0053.hpp>

static void BM_PE_0053_Solution(benchmark::State& state) 
{
  // Perform setup here
  for (auto _ : state) 
  {
    project_euler::PE_0053_Naive_Solution();
  }
}
// Register the function as a benchmark
BENCHMARK(BM_PE_0053_Solution);

