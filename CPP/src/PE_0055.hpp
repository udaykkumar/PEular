#ifndef __PE_0055_HPP_INCLUDED__
#define __PE_0055_HPP_INCLUDED__

#include <iostream>

namespace project_euler
{
	struct large_int
	{
	private:
		int num[1024];
		size_t numLen;

	public:
		large_int(const int n)
		{
			for( numLen = 0 ; n /= 10 )
			{
				num[ numLen++] = n%10 ;
			}
		}

		large_int& operator +(const large_int& n1)
		{
			int carry = 0;
			for( size_t i = 0, j = 0 ; 
				i < numLen && j < n1.length() ; i ++, j ++ )
			{
				num[i] = (carry + digit_at(i) + n1.digit_at(j))%10;
				carry  = (carry + digit_at(i) + n1.digit_at(j))/10;
			}
		}

		int digit_at(size_t i) {
			return num[i];
		}

		std::string get() const { 
			std::string s;
			for( size_t i = numLen; i >= 0 ; i -- )
				s.append( s.to_string(num[i]));
			return s;
		}

		size_t length() const { return numLen; }


	};

	size_t non_lychrel_nos();
}

#endif
