#include <PE_0058.hpp>
#include <cstring>
namespace project_euler
{

	size_t PE_0058_Naive_Solution_Part_3()
	{
		/* This seive is turning out to be a bad Idea, yet The best I have at this moment */
		const size_t MAX_PRIMES = 1000000000;
		bool   *seive= new bool[MAX_PRIMES];
		memset( seive, 0, MAX_PRIMES);

		for( size_t i = 2; ( i*i ) < MAX_PRIMES; i ++ )
		{
			if( seive[i] == true )
				continue;

			for( size_t j = i + i; (j*j) < MAX_PRIMES; j += i )
				seive[j] = true;	
			
		}

		size_t offset = 2;
		size_t corner = 1;
		size_t side_len = 3;
		size_t n_corners = 1;
		size_t primes = 0;
		double primerate = 100;

		for( ; (corner < MAX_PRIMES) && (primerate > 10) ;  offset += 2, side_len += 2)
		{
			for( size_t j = 0; j < 4 ; ++j ) {
				corner += offset;
				++ n_corners;
				if( corner < MAX_PRIMES && seive[corner] == false)
						primes ++;
			}

			primerate = (( (double)primes / (double)n_corners ) * 100 );
			if( primerate < 10 )
				break;
		}

		delete seive;
		return side_len;

	}

	size_t PE_0058_Naive_Solution_Part_2()
	{
		/* This seive is turning out to be a bad Idea, yet The best I have at this moment */
		const size_t MAX_PRIMES = 1000000000;
		bool   *seive= new bool[MAX_PRIMES];
		memset( seive, 0, MAX_PRIMES);

		for( size_t i = 2; ( i*i ) < MAX_PRIMES; i ++ )
		{
			if( seive[i] == true )
				continue;

			for( size_t j = i + i; j < MAX_PRIMES; j += i )
				seive[j] = true;	
			
		}

		size_t offset = 2;
		size_t corner = 1;
		size_t side_len = 3;
		size_t n_corners = 1;
		size_t primes = 0;
		double primerate = 100;

		for( ; (corner < MAX_PRIMES) && (primerate > 10) ;  offset += 2, side_len += 2)
		{
			for( size_t j = 0; j < 4 ; ++j ) {
				corner += offset;
				++ n_corners;
				if( corner < MAX_PRIMES && seive[corner] == false)
						primes ++;
			}

			primerate = (( (double)primes / (double)n_corners ) * 100 );
			if( primerate < 10 )
				break;
		}

		delete seive;
		return side_len;

	}


	size_t PE_0058_Naive_Solution_Part_1()
	{
		/* This seive is turning out to be a bad Idea, yet The best I have at this moment */
		const size_t MAX_PRIMES = 1000000000;
		bool   *seive= new bool[MAX_PRIMES];
		memset( seive, 0, MAX_PRIMES);

		for( size_t i = 2; i < MAX_PRIMES; i ++ )
		{
			if( seive[i] == true )
				continue;

			for( size_t j = i + i; j < MAX_PRIMES; j += i )
				seive[j] = true;	
			
		}

		size_t offset = 2;
		size_t corner = 1;
		size_t side_len = 3;
		size_t n_corners = 1;
		size_t primes = 0;
		double primerate = 100;

		for( ; (corner < MAX_PRIMES) && (primerate > 10) ;  offset += 2, side_len += 2)
		{
			for( size_t j = 0; j < 4 ; ++j ) {
				corner += offset;
				++ n_corners;
				if( corner < MAX_PRIMES && seive[corner] == false)
						primes ++;
			}

			primerate = (( (double)primes / (double)n_corners ) * 100 );
			if( primerate < 10 )
				break;
		}

		delete seive;
		return side_len;

	}

	void time_seive_generation_part_1()
	{
		const size_t MAX_PRIMES = 1000000000;
		bool   *seive= new bool[MAX_PRIMES];
		memset( seive, 0, MAX_PRIMES);

		for( size_t i = 2; i < MAX_PRIMES; i ++ )
		{
			if( seive[i] == true )
				continue;

			for( size_t j = i + i; j < MAX_PRIMES; j += i )
				seive[j] = true;	
			
		}

		delete seive;
		return ;
	}

	void time_seive_generation_part_2()
	{
		const size_t MAX_PRIMES = 1000000000;
		bool   *seive= new bool[MAX_PRIMES];
		memset( seive, 0, MAX_PRIMES);

		for( size_t i = 2; (i *i)  < MAX_PRIMES; i ++ )
		{
			if( seive[i] == true )
				continue;

			for( size_t j = i + i; j < MAX_PRIMES; j += i )
				seive[j] = true;	
			
		}

		delete seive;
		return ;
	}

	void time_seive_generation_part_3()
	{
		const size_t MAX_PRIMES = 1000000000;
		bool   *seive= new bool[MAX_PRIMES];
		memset( seive, 0, MAX_PRIMES);

		for( size_t i = 2; (i *i)  < MAX_PRIMES; i ++ )
		{
			if( seive[i] == true )
				continue;

			for( size_t j = i + i; (j*j) < MAX_PRIMES; j += i )
				seive[j] = true;	
			
		}

		delete seive;
		return ;
	}
}

