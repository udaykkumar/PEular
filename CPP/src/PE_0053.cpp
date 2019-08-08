#include <PE_0053.hpp>

namespace project_euler
{

	size_t ncr(size_t n, size_t r)
	{
		size_t  ret = 1;
		size_t till = (r > (n-r)) ? r : n-r;
		size_t rem  = (r > (n-r)) ? n-r : r;
		size_t   j  = 2;

		for( size_t i = n; i > till ; i -- )
		{
			ret *= i;
			if( j <= rem )
			{
				ret /= j++;
			}
		}

		while( j <= rem )
		{
			ret /= j++;
		}
		
		return ret;
	}

	size_t PE_0053_Naive_Solution()
	{
		size_t count = 0;
		for( size_t n = 1; n <= 100; n ++ )
		{
			for( size_t r = 1; r <= n; r ++ )
			{
				size_t res = ncr(n,r);
				if( res > 1000000 )
				{
					count ++;
				}
			}
		}
		return count;
	}
}

