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

std::vector<int> getPrimes(int n = 1000000 , int from = 2)
{
    std::vector<int> plist;
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
            plist.push_back(i);
    }

    return plist;
}




int main()
{
    std::vector<int> plist = getPrimes() ;
    size_t maxList = 0;
        int maxP = 0;
        for( size_t i = 0 ; i < 4 /*this is purely on trial and error, yet to figure a better way */; i ++ ) {
            size_t listCount = 1;
            int            p = plist[i];
            for( size_t j = i+1; j < plist.size() ; j ++ ) {
                p = p + plist[j];
                if( p > 1000000 )
                    break;

                listCount ++;
                if( std::find( plist.begin(), plist.end(), p) != plist.end() ) {
                    if( maxList < listCount ) {
                        maxList = listCount; 
                        maxP = p;
                    }

                }
            }
        }
    std::cout << maxP << std::endl;
    return 0;
}
