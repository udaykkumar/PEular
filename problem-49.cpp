#include <iostream>
#include <vector>
#include <bits/stdc++.h>


std::ostream& operator<<(std::ostream &os, const std::vector<int> &vlist )
{
    for( auto v: vlist ) {
        os << " " << v ;
    }
    return os;
}

std::vector<int> getPrimes(int n = 10000 , int from = 1000)
{
    std::vector<int> primes;
    bool *seive = new bool[n];
    memset( seive, true, n );

    for( int i{2} ; i <= n ; i ++ )
    {
        if( seive[i] == true )
        {
            for( int j = i + i ; j <= n ; j += i )
                seive[j] = false;
        }
    }

    for( int i{2} ; i <= n ; i ++ )
    {
        if( seive[i] && ( i >= from && i <= n ) )
            primes.push_back(i);
    }

    return primes;
}


std::vector<int> split(int x)
{
    std::vector<int> v;
    for( ;  x > 0 ; x /= 10)
        v.push_back(x%10);
    return v;
}

void permuations( std::vector<int> p, int i, int n )
{
  (void)p;
  (void)i;
  (void)n;
}

int main()
{
    std::vector<int> primes { getPrimes() };
    for( auto p : primes ){
        std::vector<int> digits = split( p );
        permuations( digits, 0, digits.size() );
    }
    return 0;
}
