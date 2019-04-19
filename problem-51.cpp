#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <bits/stdc++.h>

std::unordered_map<int, int> gPrimesList;

void permute( std::vector<int> p, int i, int n  );

std::ostream& operator<<(std::ostream &os, const std::vector<int> &vlist )
{
    for( auto v: vlist ) {
        os << " " << v ;
    }
    return os;
}

std::unordered_map<int, int> getPrimes(int n = 1000000 , int from = 10000)
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
            gPrimesList.insert( std::make_pair( i, 1 ) );
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

void permute( std::vector<int> p, std::unordered_map<int, int> &permutations, size_t i = 0 )
{
    if( i == p.size()-1 ) {
        int num = 0;
        for( auto n: p ) {
            num = (num * 10 ) + n;
        }
        if( gPrimesList.find( num ) != gPrimesList.end()) {
            if( permutations.find(num%100) == permutations.end() )
            {
                permutations[ num%100 ] = 1;
            }
            else 
            {
                permutations[ num%100 ] += 1;

            }
        }
        return ;
    }
    for( size_t j = i; j < p.size() ; j ++ )
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
    std::map<int,int> m(gPrimesList.begin(), gPrimesList.end());
    
    std::map<int, std::unordered_map<int,int>> integerMaps;
    int idx = 0;
    for( auto p : gPrimesList ){
        if( idx ++% 1000 == 0 ) {
            std::cout << "step  " << idx << "\n";
        }
        std::unordered_map<int, int> permutations;
        permute( split( p.first  ) , permutations);
        integerMaps[p.first] = permutations;
    }

    int maxrepetitions = 0;
    for( auto a : integerMaps ){
        int              p = a.first;
        std::unordered_map<int,int> v = a.second;
        std::cout << " Prime P " << p << " Size " << v.size()  ;
        for( auto n : v ) {
            if( n.second >= 8 ) {
                std::cout << p << " " << n.first << ":" << " "<< n.second << std::endl;
                exit(0);
            }
        } 
        std::cout << std::endl;

    }

    return 0;
}
