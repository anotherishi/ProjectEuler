#include <iostream>
#include <math.h>

using namespace std;

void *diag(long n, int ds, int *l)
{
    for (long i = 0; i < n; i++)
    {
        l[i + 1] = l[i] + ds;
        ds += 8;
    cout<<i;
    }
}

void parr(int *arr)
{
    cout << "\n";
    for (int i = 0; i <= sizeof(arr); i++)
        cout << arr[i] << ", ";
    cout << "\n";
}

bool isPrime(long n)
{
    for (int i = 2; i < ceil(sqrt(n)); i++)
        if (!(n % i))
            return 0;
    return 1;
}

int main()
{
    int l[400];
    l[0]= 1;
    diag(11, 8, l);
    parr(l);
    cout << sizeof(l);

    return 0;
}
