#include <PE_0004.hpp>

namespace project_euler
{
	const size_t MAX_SIX_DIGIT_NO = 999999;

	bool is_pallindrom(size_t n)
	{
		size_t n1 = n;
		size_t n2 = 0;
		for( ; n ; )
		{
			size_t r = n%10;
			n2 		 = ( n2 * 10 ) + r;
			n 		/= 10;
		}

		return n1 == n2;

	}

	size_t PE_0004_Naive_Solution()
	{
		for( size_t n = MAX_SIX_DIGIT_NO; ; --n )
		{
			if( is_pallindrom(n) )
			{
				for( size_t n1 = 999; n1 > 99 ; --n1 )
				{
					if( n%n1 == 0 )
					{
						size_t n2 = n/n1;
						if( n2 > 99 && n2 < 1000 )
							return n;
					}
				}
			}
		}
	}	
}

