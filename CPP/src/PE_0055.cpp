#include <PE_0055.hpp>
#include <boost/algorithm/is_palindrome.hpp>
#include <boost/multiprecision/cpp_int.hpp> 
#include <sstream>
using boost::multiprecision::cpp_int; 

namespace project_euler
{
	bool check_if_pallindrome(cpp_int n)
	{
		std::ostringstream s1;
		s1 << n ;
		std::string s = s1.str();
		return boost::algorithm::is_palindrome( s );
	}

	cpp_int reverse(cpp_int n)
	{
		cpp_int x = 0;
		while(n)
		{
			x = x*10 + n%10;
			n /= 10;
		}
		return x;
	}

	size_t PE_0055_Naive_Solution()
	{
		size_t count = 0;
		for( cpp_int i = 1 ; i < 10000; i ++ )
		{
			cpp_int lychrel = i;
			bool   found_pallindrome = false;
			size_t iteration = 2;
			for( ; (iteration < 50) && (found_pallindrome == false) ; iteration ++ )
			{
				lychrel += reverse(lychrel);
				if( check_if_pallindrome(lychrel) == true )
				{
					found_pallindrome = true;
					break;	
				}
			}
			if( found_pallindrome == false)
				count++;
		}
		return count;
	}

}

