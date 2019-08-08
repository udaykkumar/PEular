#include <PE_0052.hpp>
#include <boost/test/unit_test.hpp>

using namespace boost::unit_test;

BOOST_AUTO_TEST_SUITE( TEST_PE_0052 )

BOOST_AUTO_TEST_CASE( Case_1 )
{
	BOOST_CHECK( project_euler::PE_0052_Naive_Solution() == 142857 );
}
BOOST_AUTO_TEST_SUITE_END()

