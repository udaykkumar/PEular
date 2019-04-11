#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
#include <bits/stdc++.h>

std::vector<int> primes;

void generatePrimes(int n = INT_MAX)
{
    bool *primesArry = new bool[n];
        memset( primesArry, true, n );

    for( int idx = 2; ( idx * idx ) < n ; idx ++ )
    {
        if( primesArry[idx] == true )
        {
            for( int jdx  = idx *2 ; jdx < n; jdx += idx )
                primesArry[jdx] = false;
        }
    }

    for( int idx = 2 ; idx < n ; idx ++  ){
        if( primesArry[idx] )
            primes.push_back(idx);
    }
    free(primesArry);
}

int distinctPrimeFactors(int x)
{
    int distPrimes = 0;
    for( auto p : primes ){
        if( x < 2 )
            return distPrimes;
        if( x%p == 0 ) {
            distPrimes ++;
            while( x%p == 0 )
                x /= p;
        }
    }
    return distPrimes;
}

int main()
{
    /** 1234 is a trial and error initially started with 123456 took about 2 seconds to complete  **/
    generatePrimes(1235);

    int list[4];
    list[0] = (distinctPrimeFactors(2));
    list[1] = (distinctPrimeFactors(3));
    list[2] = (distinctPrimeFactors(4));
    for( int i = 5;  ; i ++  ) {
         list[3] = distinctPrimeFactors(i);

         /** This is better than Looping ... just 4 statements so makes sense */
         if( list[3] == 4 && list[2] == 4 && list[1] == 4 && list[0] == 4 ){
             std::cout << i << "\n";
             exit(0);
         }

        /* Better than Looping */
        list[0] = list[1];
        list[1] = list[2];
        list[2] = list[3];
        list[3] = 0;
    }
   return 0;
}
