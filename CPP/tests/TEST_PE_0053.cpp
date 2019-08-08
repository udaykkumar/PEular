#include <PE_0053.hpp>
#include <boost/test/unit_test.hpp>

using namespace boost::unit_test;

BOOST_AUTO_TEST_SUITE( TEST_PE_0053 )

BOOST_AUTO_TEST_CASE( Case_1 )
{
	BOOST_CHECK( project_euler::PE_0053_Naive_Solution() == 4075 );
}

BOOST_AUTO_TEST_CASE( Case_2 )
{
	BOOST_CHECK( project_euler::PE_0053_Naive_Solution_Caching() == 4075 );
}
BOOST_AUTO_TEST_SUITE_END()

