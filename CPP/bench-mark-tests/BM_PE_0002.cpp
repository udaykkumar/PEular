#include <benchmark/benchmark.h>
#include <PE_0002.hpp>

static void PE_0002_Naive_Solution(benchmark::State& state) 
{
  // Perform setup here
  for (auto _ : state) 
  {
    project_euler::PE_0002_solution_naive();
  }
}
// Register the function as a benchmark
BENCHMARK(PE_0002_Naive_Solution);

