#include <PE_0058.hpp>
#include <boost/test/unit_test.hpp>

using namespace boost::unit_test;

BOOST_AUTO_TEST_SUITE( TEST_PE_0058 )

BOOST_AUTO_TEST_CASE( Case_1 )
{
	BOOST_CHECK( project_euler::PE_0058_Naive_Solution_Part_1() == 26241 );
}

BOOST_AUTO_TEST_CASE( Case_2 )
{
	BOOST_CHECK( project_euler::PE_0058_Naive_Solution_Part_2() == 26241 );
}

BOOST_AUTO_TEST_CASE( Case_3 )
{
	BOOST_CHECK( project_euler::PE_0058_Naive_Solution_Part_3() == 26241 );
}

BOOST_AUTO_TEST_SUITE_END()

