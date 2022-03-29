#include <stdio.h>

int hcf(int a, int b)
{
    if (a == b)
        return a;
    if (a > b)
        return hcf(a - b, b);
    return hcf(a, b - a);
}

float phi(int n)
{
    int c = 1;
    for (int i = 2; i < n; i++)
    {
        if (hcf(i, n) == 1)
            c += 1;
    }
    return n / (float)c;
}

int main()
{
    float max=0;
    int ni = 0;
    for (int i = 2; i < 1000001; i++)
    {
        ni = phi(i);
        if (ni > max)
        {
            max = ni;
            ni = i;
}
            printf("%d\n", max);
        
    }

    printf("%f,  %d", max, ni);
    return 0;
}
