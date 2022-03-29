#include <iostream>
#include <math.h>

using namespace std;

// bool is_triangular(long long int number)
// {
//     double x = (-1 + pow((1 + 8 * number), .5)) / 2.;
//     return x == (long long int)x;
// }

bool is_pentagonal(long long int number)
{
    double x = (1 + pow((1 + 24 * number), .5)) / 6.;
    return x == (long long int)x;
}

bool is_hexagonal(long long int number)
{
    double x = (1 + pow((1 + 8 * number), .5)) / 4.;
    return x == (long long int)x;
}

int main()
{
    long long int i = 40755;
    while (true)
    {
        i++;
        if (is_pentagonal(i) && is_hexagonal(i))
        {
            cout << i << "\n";
            return 0;
        }
    }
}
