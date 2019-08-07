#include <PE_0001.hpp>

namespace project_euler
{

	constexpr size_t	N = 1000;

	size_t solution_naive()
	{
		size_t sum = 0;
		for( size_t i = 0 ; i < N ; i ++ )
		{
			if( i%3 == 0 || i%5 == 0 )
				sum += i;
		}
		return sum;
	}

	size_t solution_const_time()
	{
		size_t sum = 0;
		size_t   n = 0;	

							    n = (N-1)/3;	
		size_t sum_multiples_of_3 = 3 *  n * ( n + 1 ) / 2 ;


							    n = (N-1)/5;	
		size_t sum_multiples_of_5 = 5 *  n * ( n + 1 ) / 2 ;

								 n = (N-1)/15;	
		size_t sum_multiples_of_15 = 15 *  n * ( n + 1 ) / 2 ;


		sum = sum_multiples_of_3 + sum_multiples_of_5 - sum_multiples_of_15 ;
		return sum;
	}
}

