#include <PE_0053.hpp>
#include <unordered_map>

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
			if( j <= rem )	{ ret /= j++; }
		}

		while( j <= rem )   { ret /= j++; }
		
		return ret;
	}

	size_t PE_0053_Naive_Solution()
	{
		size_t count = 0;
		for( size_t n = 1; n <= 100; n ++ )
			for( size_t r = 1; r <= n; r ++ )
				if( ncr(n,r) > 1000000 )
					count ++;
		return count;
	}

	std::unordered_map<std::string, bool> ncrCache;

	bool is_ncr_more_than_a_million(size_t n, size_t r)
	{
		std::string key;

		if( r < n-r )
		{
				key = std::to_string(n) + "-"+std::to_string(r)+"-"+std::to_string(n-r);
		}
		else
		{
				key = std::to_string(n) + "-"+std::to_string(n-r)+"-"+std::to_string(r);
		}
		 
		std::unordered_map<std::string,bool>::const_iterator got = ncrCache.find(key);
		if( got != ncrCache.end() )
		{
			return got->second;
		}
		
		size_t  ret = 1;
		size_t till = (r > (n-r)) ? r : n-r;
		size_t rem  = (r > (n-r)) ? n-r : r;
		size_t   j  = 2;

		for( size_t i = n; i > till ; i -- )
		{
			ret *= i;
			if( j <= rem )	{ ret /= j++; }
		}

		while( j <= rem )   { ret /= j++; }
		

		if(ret > 1000000)
		{
			ncrCache[key]   = true;
		}
		else
		{
			ncrCache[key]   = false;	
		}

		return ncrCache[key];
	}


	size_t PE_0053_Naive_Solution_Caching()
	{
		size_t count = 0;
		for( size_t n = 1; n <= 100; n ++ )
			for( size_t r = 1; r <= n; r ++ )
				if( is_ncr_more_than_a_million(n,r) )
					count ++;
		return count;
	}
}

