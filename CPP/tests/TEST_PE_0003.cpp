#include <PE_0003.hpp>
#include <boost/test/unit_test.hpp>

using namespace boost::unit_test;

BOOST_AUTO_TEST_SUITE( TEST_PE_0003 )

BOOST_AUTO_TEST_CASE( Case_1 )
{
	BOOST_CHECK( project_euler::PE_0003_Naive_Solution() == 6857 );
}


BOOST_AUTO_TEST_CASE( Case_2 )
{
	BOOST_CHECK( project_euler::PE_0003_Find_Better_Solution_Trial_1() == 6857 );
}

BOOST_AUTO_TEST_CASE( Case_3 )
{
	BOOST_CHECK( project_euler::PE_0003_Find_Better_Solution_Trial_2() == 6857 );
}

BOOST_AUTO_TEST_CASE( Case_4 )
{
	BOOST_CHECK( project_euler::PE_0003_Find_Better_Solution_Trial_3() == 6857 );
}

BOOST_AUTO_TEST_SUITE_END()

