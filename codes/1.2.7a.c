/* 1.2.7a  f(x) = 3x^4 - 4x^3 - 12x^2 + 5
 * Critical points: Newton-Raphson on f'(x) = 12x^3 - 12x^2 - 24x with
 * f''(x) = 36x^2 - 24x - 24, iterated until successive iterates differ by
 * less than TOL; the roots are then verified.
 */
#include <stdio.h>
#include <math.h>

#define TOL      1e-12
#define MAX_ITER 100

static double d1(double x) { return 12 * x * x * x - 12 * x * x - 24 * x; }
static double d2(double x) { return 36 * x * x - 24 * x - 24; }

static double newton(double x, int *iters)
{
    for (*iters = 1; *iters <= MAX_ITER; (*iters)++) {
        double x_new = x - d1(x) / d2(x);
        if (fabs(x_new - x) < TOL)
            return x_new;
        x = x_new;
    }
    return x;
}

int main(void)
{
    double x0[3] = {-1.5, 0.4, 2.5}, exact[3] = {-1.0, 0.0, 2.0};
    for (int k = 0; k < 3; k++) {
        int iters;
        double x = newton(x0[k], &iters);
        printf("x0 = %4.1f : x = %.10f after %d iterations, f'(x) = %.2e, ", x0[k], x, iters, d1(x));
        printf("%s\n", fabs(x - exact[k]) < 1e-9 ? "verified (root of 12x(x+1)(x-2))" : "NOT verified");
    }
    return 0;
}
