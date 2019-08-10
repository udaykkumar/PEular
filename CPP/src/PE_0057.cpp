#include <PE_0057.hpp>
#include <boost/multiprecision/cpp_int.hpp> 
using boost::multiprecision::cpp_int; 
namespace project_euler
{


	size_t digits(cpp_int n)
	{
		size_t n_digits = 0;
		while(n)
		{
			n_digits ++;
			n /= 10;
		}
		return n_digits;
	}

	/*
		1 + 1/2 = 3/2 = 1.5
		1 + 1/(2 + 1/2) = 7/5 = 1.4
		1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
		1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

		Numerator Series = 3, 7, 17, 41, 99, 239, 577, ... 
		Denom     Series = 2, 5, 12, 29, 70, 169, 408, ...

		Num(n) = Num(n-1)*2 + Num(n-2) [ Num[0] == 3, Num[1] == 7 ]
		Den(n) = Den(n-1)*2 + Den(n-2) [ Den[0] == 2, Den[1] == 5 ]


	*/
	size_t PE_0057_Naive_Solution_Arguably_Good_Solution_Too()
	{

		size_t count = 0;
		cpp_int num1 = 3, num2 = 7, num = 0;
		cpp_int den1 = 2, den2 = 5, den = 0;

		for( size_t i = 3 ; i < 1000; i ++ )
		{
			num = num2*2 + num1;
			den = den2*2 + den1;
			size_t digits_num = digits(num);
			size_t digits_den = digits(den);

			if( digits_num > digits_den )
			{
				count ++;
			}

			num1 = num2;
			num2 = num;

			den1 = den2;
			den2 = den;

		}
		
		return count;
	}
}

