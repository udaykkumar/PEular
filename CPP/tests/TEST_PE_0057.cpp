#include <PE_0057.hpp>
#include <boost/test/unit_test.hpp>

using namespace boost::unit_test;

BOOST_AUTO_TEST_SUITE( TEST_PE_0057 )

BOOST_AUTO_TEST_CASE( Case_1 )
{
	BOOST_CHECK( project_euler::PE_0057_Naive_Solution_Arguably_Good_Solution_Too() == 153 );
}
BOOST_AUTO_TEST_SUITE_END()

