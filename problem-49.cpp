#include <iostream>
#include <vector>
#include <bits/stdc++.h>

std::vector<int> gPrimesList;
void permute( std::vector<int> p, int i, int n  );

std::ostream& operator<<(std::ostream &os, const std::vector<int> &vlist )
{
    for( auto v: vlist ) {
        os << " " << v ;
    }
    return os;
}

std::vector<int> getPrimes(int n = 10000 , int from = 1000)
{
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
            gPrimesList.push_back(i);
    }

    return gPrimesList;
}


std::vector<int> split(int x)
{
    std::vector<int> v;
    for( ;  x > 0 ; x /= 10)
        v.push_back(x%10);
    return v;
}

void permute( std::vector<int> p, std::vector<int> &permutations, int i = 0 )
{
    static int depth = 0;
    if( i == p.size()-1 ) {
        int num = 0;
        for( auto n: p ) {
            num = (num * 10 ) + n;
        }
        if( num >= 1000 ) {
            if(std::find( gPrimesList.begin(), gPrimesList.end(), num ) != gPrimesList.end())
                if( std::find( permutations.begin(), permutations.end(), num) == permutations.end() )
                    permutations.push_back(num);
        }
        return ;
    }
    for( int j = i; j < p.size() ; j ++ )
    {
        std::swap(p[i], p[j]);
        permute(p, permutations, i+1);
        std::swap(p[i], p[j]);
    }

    return ;
}

int main()
{
    gPrimesList = getPrimes() ;

    std::map<int, std::vector<int>> integerMaps;
    for( auto p : gPrimesList ){
        std::vector<int> permutations;
        permute( split( p  ) , permutations);
        std::sort( permutations.begin(), permutations.end() );
        integerMaps[p] = permutations;
    }

    for( auto a : integerMaps ){
        std::vector<int> v = a.second;
        for( int i = 0 ; i < v.size(); i ++ ) {
            for( int j = 0; j < v.size() ; j ++ ) {
                int diff = v[j] - v[i];
                if( diff > 0 ) {
                    int p = v[i];
                    int p1 = p + diff;
                    if( std::find(v.begin(), v.end(), p1) == v.end() ) {
                        break;
                    }
                    int p2 = p1 + diff;
                    if( std::find(v.begin(), v.end(), p2) == v.end() ) {
                        break;
                    }
                    std::cout << p  << p1  << p2 <<  std::endl ;
                    exit(0);
                }
            }
        }
    }

    return 0;
}
