#include <stdio.h>

int main(void)
{
    int s, sum=0;
    int a[51], b[51], c[51][51], d[51] = {0,};

    scanf("%d", &s);
    for(int k=0; k<s; k++){
        scanf("%d", &a[k]);
    }
    for(int k=0; k<s; k++){
        scanf("%d", &b[k]);
    }
    for(int k=0; k<s; k++){
        d[k]= b[k];
    }

    for(int k=0; k<s; k++){
        for(int j=0; j<s-1; j++){
            if(a[j] < a[j+1]){
                int tmp = a[j];
                a[j] = a[j+1];
                a[j+1] = tmp;
            }
            if(d[j] > d[j+1]){
                int tmp = d[j];
                d[j] = d[j+1];
                d[j+1] = tmp;
            }
        }
    }
    for(int k=0; k<s; k++){
        c[k][0] = a[k];
        c[k][1] = d[k];
        sum += (c[k][0] * c[k][1]);
    }
    printf("%d\n", sum); 
    return 0;   
}
