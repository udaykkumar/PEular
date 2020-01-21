#include <benchmark/benchmark.h>
#include <PE_0051.hpp>

static void BM_PE_0051_Solution(benchmark::State& state) 
{
  // Perform setup here
  for (auto _ : state) 
  {
    /* Solution Here */
  }
}
// Register the function as a benchmark
BENCHMARK(BM_PE_0051_Solution);

