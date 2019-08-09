#include <benchmark/benchmark.h>
#include <PE_0055.hpp>

static void BM_PE_0055_Naive_Solution_Boost_Palindrome(benchmark::State& state) 
{
  // Perform setup here
  for (auto _ : state) 
  {
   	project_euler::PE_0055_Naive_Solution_Boost_Palindrome();
  }
}
// Register the function as a benchmark
BENCHMARK(BM_PE_0055_Naive_Solution_Boost_Palindrome);


static void BM_PE_0055_Naive_Solution_with_reverse(benchmark::State& state) 
{
  // Perform setup here
  for (auto _ : state) 
  {
   	project_euler::PE_0055_Naive_Solution_with_reverse();
  }
}
// Register the function as a benchmark
BENCHMARK(BM_PE_0055_Naive_Solution_with_reverse);


static void BM_PE_0055_reverse(benchmark::State& state) 
{
  // Perform setup here
  for (auto _ : state) 
  {
   	project_euler::reverse_bm();
  }
}
// Register the function as a benchmark
BENCHMARK(BM_PE_0055_reverse);



static void BM_PE_0055_palindrom(benchmark::State& state) 
{
  // Perform setup here
  for (auto _ : state) 
  {
   	project_euler::palindrom_bm();
  }
}
// Register the function as a benchmark
BENCHMARK(BM_PE_0055_palindrom);
