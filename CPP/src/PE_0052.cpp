#include <PE_0052.hpp>

namespace project_euler
{

	bool contains_same_digits(size_t x, size_t y)
	{
		size_t hash_data[10] = {0,};
		for( ; x ; x /= 10)
		{
			hash_data[x%10] += 1;
		}

		for( ; y ; y /= 10)
		{
			hash_data[y%10] -= 1;
		}
		
		for( size_t i = 0 ; i < 10; i ++ )
		{
			if( hash_data[i] != 0 )
				return false;
		}

		return true;
	}

	size_t PE_0052_Naive_Solution()
	{
		for( size_t x = 1; ; x ++ )
		{
			if( contains_same_digits( x, x*2 ) )
			{
				if( contains_same_digits( x, x*3 ) )
				{
					if( contains_same_digits( x, x*4 ) )
					{
						if( contains_same_digits( x, x*5 ) )
						{
							if( contains_same_digits( x, x*6 ) )
							{
								return x;
							}	
						}
					}
				}
			}	
		}
		return 0;
	}
}

