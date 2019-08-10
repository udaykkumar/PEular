#include <PE_0056.hpp>
#include <boost/multiprecision/cpp_int.hpp> 
using boost::multiprecision::cpp_int; 

namespace project_euler
{
	size_t digit_sum(cpp_int n)
	{
		size_t sum = 0;
		while( n )
		{
			sum += static_cast<size_t>(n%10);
			n /= 10;
		}

		return sum;
	}

	size_t PE_0056_Naive_Solution()
	{
		size_t max_digit_sum = 0;
		for( cpp_int n = 1; n <= 100 ; n ++ )
		{
			cpp_int idx = 1;
			for( cpp_int jdx = 1; jdx <= 100; jdx ++ )
			{
				idx *= n;
				size_t power_sum = digit_sum(idx);
				if( power_sum > max_digit_sum )
				{
					max_digit_sum = power_sum;
				}
			}
		}
			
		return max_digit_sum;
	}

	size_t PE_0056_Naive_Solution_With_Tweeks()
	{
		size_t max_digit_sum = 0;
		for( cpp_int n = 1; n <= 100 ; n ++ )
		{
			if( n%10 == 0 )
				continue;
			
			cpp_int idx = 1;
			for( cpp_int jdx = 1; jdx <= 100; jdx ++ )
			{
				idx *= n;
				size_t power_sum = digit_sum(idx);
				if( power_sum > max_digit_sum )
				{
					max_digit_sum = power_sum;
				}
			}
		}
			
		return max_digit_sum;
	}
}

