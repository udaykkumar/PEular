#include <PE_0055.hpp>

namespace project_euler
{
	size_t non_lychrel_nos()
	{
		large_int n1(1), n2(2);

		while( 1 )
		{
			n1 = n1 + n1 ;
			std::cout << n1.get() << " \n";
		}
	}

}

