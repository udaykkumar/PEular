#include <PE_0001.hpp>
#include <boost/test/unit_test.hpp>

using namespace boost::unit_test;

BOOST_AUTO_TEST_SUITE( TEST_PE_0001 )

BOOST_AUTO_TEST_CASE( Case_1 )
{
	BOOST_CHECK( project_euler::solution_naive( ) == 233168 );
}
BOOST_AUTO_TEST_SUITE_END()

