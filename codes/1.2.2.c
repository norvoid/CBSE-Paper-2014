/* 1.2.2  |2x 5; 8 x| = |6 -2; 7 3|  ->  f(x) = 2x^2 - 72 = 0
 * Newton-Raphson with f'(x) = 4x from x0 = 2 and x0 = -8, iterated until
 * successive iterates differ by less than TOL; the roots are then verified.
 */
#include <stdio.h>
#include <math.h>

#define TOL      1e-12
#define MAX_ITER 100

static double f(double x)  { return 2 * x * x - 72; }
static double df(double x) { return 4 * x; }

static double newton(double x, int *iters)
{
    for (*iters = 1; *iters <= MAX_ITER; (*iters)++) {
        double x_new = x - f(x) / df(x);
        if (fabs(x_new - x) < TOL)
            return x_new;
        x = x_new;
    }
    return x;
}

int main(void)
{
    double x0[2] = {2.0, -8.0}, exact[2] = {6.0, -6.0};
    for (int k = 0; k < 2; k++) {
        int iters;
        double x = newton(x0[k], &iters);
        printf("x0 = %5.1f : x = %.10f after %d iterations, f(x) = %.2e, ", x0[k], x, iters, f(x));
        printf("%s\n", fabs(x - exact[k]) < 1e-9 ? "verified (root of 2(x-6)(x+6))" : "NOT verified");
    }
    return 0;
}
