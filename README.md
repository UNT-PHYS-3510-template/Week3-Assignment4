# Week 3 Assignment 4

As we can use python to calculate definite integrals of a function, we can also design algorithms to compute the derivative of a function. In the previous week, assignment 1, you implemented the analytic formula for the force between two Argon atoms, taking the derivative of the Lennard-Jones potential. In this assignment, you will implement an approximate estimate of the force using finite differences. If you remember your Calculus course, the derivative of a function can be written as the limit of the difference quotient:

<a href="https://www.codecogs.com/eqnedit.php?latex=f'(x)=\lim_{h\rightarrow0}\frac{f(x&plus;h)-f(x)}{h}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f'(x)=\lim_{h\rightarrow0}\frac{f(x&plus;h)-f(x)}{h}" title="f'(x)=\lim_{h\rightarrow0}\frac{f(x+h)-f(x)}{h}" /></a>

Using this formula, we can compute the LJ force at a given separation between the atoms as 

<a href="https://www.codecogs.com/eqnedit.php?latex=F^{LJ}(r)=-\lim_{h\rightarrow0}\frac{U^{LJ}(r&plus;h)-U^{LJ}(r)}{h}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?F^{LJ}(r)=-\lim_{h\rightarrow0}\frac{U^{LJ}(r&plus;h)-U^{LJ}(r)}{h}" title="F^{LJ}(r)=-\lim_{h\rightarrow0}\frac{U^{LJ}(r+h)-U^{LJ}(r)}{h}" /></a>

TASK: Given the expression for the Lennard-Jones potential energy (see Week 1 Assignment 3), compute the associated magnitude of the force between two atoms using the formula above. Find a value of the parameter h small enough to provide an error smaller than 1.e-8 with respect to the analytic result (see Week 2 Assignment 1). 

EXPECTED OUTCOME: For a value of the separation between the atoms equal to sigma (6 a.u.), the analytic LJ force is equal to 4\*epsilon (1.6e-3 a.u.). A finite-difference estimate with h = 0.001 a.u. should give an error smaller than the given threshold.
