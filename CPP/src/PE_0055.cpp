#include <PE_0055.hpp>
#include <boost/algorithm/is_palindrome.hpp>
#include <boost/multiprecision/cpp_int.hpp> 
using boost::multiprecision::cpp_int; 

namespace project_euler
{
	size_t digits(cpp_int x)
	{
		size_t n_digits = 0;
		for( ; x ; x /= 10 )
		{
			n_digits ++;
		}

		return n_digits;
	}

	size_t non_lychrel_nos()
	{
		cpp_int n1 = 1;

		size_t iterations = 0;
		while( iterations++ < 1000 )
		{
			n1 += n1;
		}

		return iterations;
	}

}

