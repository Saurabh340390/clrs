/*
 * diophant.c
 *
 *  Created on: 19 Jan 2025
 *      Author: saurabh
 */


#include"euclid.h"
#include<stdio.h>
#include<stdlib.h>
int main(){
int a, b, c, g, grow;
puts("enter the value of a, b and c for ax + by = c ");
scanf("%d %d %d", &a, &b, &c);
/* compute g = gcd(a,b) */
g = gcd(a,b);
/* compute x and y using extended euclidean alg. */
g = ext_euclid(a,b);

/*rescale so ax+by = c */
grow = c/g;
x *= grow;
y *= grow;

printf("the value of gcd of a and b is %d\n", g);
printf("value of x and y after rescale is %d, %d\n", x, y);

return 0;
}
