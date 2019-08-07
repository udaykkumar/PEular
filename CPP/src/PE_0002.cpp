#include <PE_0002.hpp>

namespace project_euler
{
	const size_t MAX = 4000000; /* Thats 4 million */
	size_t PE_0002_solution_naive()
	{
		size_t f1{1}, f2{1}, f{0}, sum{0};
		for( ; f = f1 + f2; ) 
		{
			if( f > MAX )
				break;

			if( f%2 == 0 )
			{
				sum += f;
			}
			
			f1 = f2;
			f2 = f;
		}

		return sum;
	}
}

