#include <basic/binomial.h>
#include <cmath>

const char * ProbabilityError::what() const NOEXCEPT
{ return "a probability must be in the interval [0,1]"; }

DiscreteDistribution::DiscreteDistribution()
{}

DiscreteDistribution::~DiscreteDistribution()
{}

double DiscreteDistribution::pmf(const double value) const
{ return 0; }

double pmf(const DiscreteDistribution& distribution, const unsigned int value)
{ return distribution.pmf(value); }

BinomialDistribution::BinomialDistribution(const unsigned int n, const double pi)
{ 
    this->n = n;
    set_pi(pi);
}

BinomialDistribution::BinomialDistribution(const BinomialDistribution& binomial)
{
    n = binomial.n;
    _pi = binomial._pi;
}

BinomialDistribution::~BinomialDistribution()
{}

double BinomialDistribution::pmf(const unsigned int value) const
{
    double p;
    if(value > n)
    { p = 0; }
    else
    { p = factorial(n)/(factorial(n-value) * factorial(value)) * pow(1-_pi, (double)(n-value)) * pow(_pi, (double)(value)); }
    return p;
}

double BinomialDistribution::get_pi() const
{ return _pi; }

void BinomialDistribution::set_pi(const double pi)
{
    if(pi < 0. || pi > 1.)
    { throw ProbabilityError(); }
    _pi = pi;
}

unsigned int BinomialDistribution::factorial(const unsigned int n) const
{ return (n == 1 || n == 0) ? 1 : factorial(n - 1) * n; }