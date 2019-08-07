#include <PE_0003.hpp>
#include <cmath>
#include <vector>
#include <list>
namespace project_euler
{

	size_t PE_0003_Naive_Solution()
	{
		std::vector<size_t> primes;
		size_t n = static_cast<size_t>( sqrt(N) );
		bool seive[n];
		for( size_t i = 0; i < n ; i ++ )
		{
			seive[i]= false;
		}

		for( size_t i = 2; i < n ; i ++ )
		{
			if( seive[i] == true )
				continue;

			for( size_t j = i+i; j < n; j += i )
			{
				seive[j] = true;
			}
		}

		for( size_t i = 2; i < n; i ++ )
		{
			if( seive[i] == true )
				continue;
			primes.push_back(i);
		}

		for( auto it = primes.rbegin(); it != primes.rend(); ++ it )
		{
			if( ((N) % (*it)) == 0 )
			{
				return *it;
			}
		}

		return 0;
	}

	size_t PE_0003_Find_Better_Solution_Trial_1()
	{
		std::list<size_t> primes;
		size_t n = static_cast<size_t>( sqrt(N) );
		bool seive[n];
		for( size_t i = 0; i < n ; i ++ )
		{
			seive[i]= false;
		}

		for( size_t i = 2; i < n ; i ++ )
		{
			if( seive[i] == true )
				continue;

			for( size_t j = i+i; j < n; j += i )
			{
				seive[j] = true;
			}
		}

		for( size_t i = 2; i < n; i ++ )
		{
			if( seive[i] == true )
				continue;
			primes.push_front(i);
		}
		
		for( auto it = primes.begin(); it != primes.end(); ++ it )
		{
			if( ((N) % (*it)) == 0 )
			{
				return *it;
			}
		}

		return 0;
	}

	size_t PE_0003_Find_Better_Solution_Trial_2()
	{
		size_t n = static_cast<size_t>( sqrt(N) );
		bool seive[n];

		for( size_t i = 0; i < n ; i ++ )
		{
			seive[i]= false;
		}

		for( size_t i = 2; i < n ; i ++ )
		{
			if( seive[i] == true )
				continue;

			for( size_t j = i+i; j < n; j += i )
			{
				seive[j] = true;
			}
		}

		for( size_t i = n-1; i > 2; i -- )
		{
			if( seive[i] == false  &&  N%i == 0 )
				return i;
		}

		return 0;
	}

	size_t PE_0003_Find_Better_Solution_Trial_3()
	{
		size_t n = static_cast<size_t>( sqrt(N) ) / 2;
		bool seive[n];

		for( size_t i = 0; i < n ; i ++ )
		{
			seive[i]= false;
		}

		for( size_t i = 2; i < n ; i ++ )
		{
			if( seive[i] == true )
				continue;

			for( size_t j = i+i; j < n; j += i )
			{
				seive[j] = true;
			}
		}

		for( size_t i = n-1; i > 2; i -- )
		{
			if( (seive[i] == false)  &&  (N%i == 0) )
				return i;
		}

		return 0;
	}
}

