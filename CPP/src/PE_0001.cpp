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
}

