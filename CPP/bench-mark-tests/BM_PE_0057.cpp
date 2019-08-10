#include <benchmark/benchmark.h>
#include <PE_0057.hpp>

static void BM_PE_0057_Naive_Solution_Arguably_Good_Solution_Too(benchmark::State& state) 
{
  // Perform setup here
  for (auto _ : state) 
  {
   	project_euler::PE_0057_Naive_Solution_Arguably_Good_Solution_Too();
  }
}
// Register the function as a benchmark
BENCHMARK(BM_PE_0057_Naive_Solution_Arguably_Good_Solution_Too);

