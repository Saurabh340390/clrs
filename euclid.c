/*
 * euclid.c
 *
 *  Created on: 19 Jan 2025
 *      Author: saurabh
 */
#define swap(a,b) {int temp = a; a=b; b=temp; }
int x, y;
int gcd(int a, int b){
	if(a<b){
		swap(a,b);
	}
	if(b==0)
		return a;
	else
		return gcd(b, a%b);
	return a;
}
int ext_euclid(int a, int b){
	int X0 = 1, Y0 = 0;
	int X1 = 0, Y1 = 1;
	if (a < b)
		swap(a,b);
	while(b != 0){
		int q = a/b; //quotient
	    int r = a%b;
		a = b;
		b = r;
		int temp_x = X1;
		int temp_y = Y1;
		X1 = X0 - q*X1;
		Y1 = Y0 - q*Y1;
		X0 = temp_x;
		Y0 = temp_y;
	}
	x = X0;
	y = Y0;
	return a;
}
