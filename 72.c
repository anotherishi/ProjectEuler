#include <stdio.h>
#include <math.h>

int hcf(int a, int b)
{
    if (a == b)
        return a;
    if (a > b)
        return hcf(a - b, b);
    return hcf(a, b - a);
}

int main(int argc, char const *argv[])
{
    int c = 0;

    for (int i = 1; i < 1000000; i++)
    {
        for (int j = i + 1; i < 1000001; i++)
        {
            if (hcf(i, j) == 1)
                c++;
        }
    }
    printf("%d", c);

    return 0;
}
