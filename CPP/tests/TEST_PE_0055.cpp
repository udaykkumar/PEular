#include <PE_0055.hpp>
#include <boost/test/unit_test.hpp>

using namespace boost::unit_test;

BOOST_AUTO_TEST_SUITE( TEST_PE_0055 )

BOOST_AUTO_TEST_CASE( Case_1 )
{
	BOOST_CHECK(project_euler::PE_0055_Naive_Solution_Boost_Palindrome() == 249 );
}


BOOST_AUTO_TEST_CASE( Case_2 )
{
	BOOST_CHECK(project_euler::PE_0055_Naive_Solution_with_reverse() == 249 );
}

BOOST_AUTO_TEST_SUITE_END()

