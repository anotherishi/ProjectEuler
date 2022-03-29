#include <stdio.h>

int main(int argc, char const *argv[])
{
    long int n=8564543535976608;
    for (long int i=1; i<n+1; i++) {
        if (!(n%i)) {
            printf("%d, ", i);
        }
    }
    return 0;
}
