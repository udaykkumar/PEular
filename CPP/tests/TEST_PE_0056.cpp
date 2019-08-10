#include <PE_0056.hpp>
#include <boost/test/unit_test.hpp>

using namespace boost::unit_test;

BOOST_AUTO_TEST_SUITE( TEST_PE_0056 )

BOOST_AUTO_TEST_CASE( Case_1 )
{
	BOOST_CHECK( project_euler::PE_0056_Naive_Solution() == 972 );
}

BOOST_AUTO_TEST_CASE( Case_2 )
{
	BOOST_CHECK( project_euler::PE_0056_Naive_Solution_With_Tweeks() == 972 );
}


BOOST_AUTO_TEST_SUITE_END()

