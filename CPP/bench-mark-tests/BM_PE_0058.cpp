#include <benchmark/benchmark.h>
#include <PE_0058.hpp>

static void BM_PE_0058_Solution_Part_1(benchmark::State& state) 
{
  // Perform setup here
  for (auto _ : state) 
  {
    project_euler::PE_0058_Naive_Solution_Part_1();
  }
}
// Register the function as a benchmark
BENCHMARK(BM_PE_0058_Solution_Part_1);


static void BM_PE_0058_Solution_Part_2(benchmark::State& state) 
{
  // Perform setup here
  for (auto _ : state) 
  {
    project_euler::PE_0058_Naive_Solution_Part_2();
  }
}
// Register the function as a benchmark
BENCHMARK(BM_PE_0058_Solution_Part_2);


static void BM_PE_0058_Solution_Part_3(benchmark::State& state) 
{
  // Perform setup here
  for (auto _ : state) 
  {
    project_euler::PE_0058_Naive_Solution_Part_3();
  }
}
// Register the function as a benchmark
BENCHMARK(BM_PE_0058_Solution_Part_3);

static void BM_PE_0058_time_seive_generation_part_1(benchmark::State& state) 
{
  // Perform setup here
  for (auto _ : state) 
  {
    project_euler::time_seive_generation_part_1();
  }
}
// Register the function as a benchmark
BENCHMARK(BM_PE_0058_time_seive_generation_part_1);


static void BM_PE_0058_time_seive_generation_part_2(benchmark::State& state) 
{
  // Perform setup here
  for (auto _ : state) 
  {
    project_euler::time_seive_generation_part_2();
  }
}
// Register the function as a benchmark
BENCHMARK(BM_PE_0058_time_seive_generation_part_2);



static void BM_PE_0058_time_seive_generation_part_3(benchmark::State& state) 
{
  // Perform setup here
  for (auto _ : state) 
  {
    project_euler::time_seive_generation_part_3();
  }
}
// Register the function as a benchmark
BENCHMARK(BM_PE_0058_time_seive_generation_part_3);