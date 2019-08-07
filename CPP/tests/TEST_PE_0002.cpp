#include <PE_0002.hpp>
#include <boost/test/unit_test.hpp>

using namespace boost::unit_test;

BOOST_AUTO_TEST_SUITE( TEST_PE_0002 )

BOOST_AUTO_TEST_CASE( PE_0002_Naive_Solution )
{
	BOOST_CHECK( project_euler::PE_0002_solution_naive() == 4613732 );
}
BOOST_AUTO_TEST_SUITE_END()

