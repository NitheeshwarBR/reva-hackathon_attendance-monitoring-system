# Numerical Methods 

## Bisection Method

1. Find the interval $(a,b)$ such that $f(a), f(b)<0$.

2. For the interval $(a,b)$ find the approximation.

3. Identify the interval for the root in the next stage and repeat the **Step 2**.

The below formula is used to approximate

$$x=\frac{a+b}{2}$$



## Regular Falsi Method (or) Method of false postion

The steps are similar to the Bisection method, but the approximation formula is different.

$$x=\frac{a\,f(b)-b\,f(a)}{f(b)-f(a)}$$

## Newton's Raphson Method

$$x_{n+1}=x_n-\frac{f(x_n)}{f'(x_n)}$$

where $f'(x_n)\neq0$ and $n=0,1,2,3,.....$


## Fixed point method of iteration

1. Given $f(x)=0$. Find $(a,b)$ such that $f(a), f(b)<0$ and locate the initial approximation $x_0=\frac{a+b}{2}$.

2. Rewrite the given equation as $x=\phi(x)$.

3. Verify $|\phi'(x)|<1$ at $a,b$ in $(a,b)$.

4. The approximate root is found using the formula

$$x_{n+1}=\phi(x_n)$$

## Gauss Sidel iterative method

To solve system of equations which are **diagnolly dominant**.

Considering,
$$a_{11}x+a_{12}y+a_{13}z=b_1$$
$$a_{21}x+a_{22}y+a_{23}z=b_2$$
$$a_{31}x+a_{32}y+a_{33}z=b_3$$

Diagnolly dominant,
$$|a_{11}|>|a_{12}|+|a_{13}|$$
$$|a_{22}|>|a_{21}|+|a_{23}|$$
$$|a_{33}|>|a_{31}|+|a_{32}|$$

The general approximation formula is

$$x_{n+1}=\frac{1}{a_{11}}[b_1-a_{12}\,y_n-a_{13}\,z_n]$$
$$y_{n+1}=\frac{1}{a_{22}}[b_2-a_{21}\,x_{n+1}-a_{23}\,z_n]$$
$$z_{n+1}=\frac{1}{a_{33}}[b_3-a_{31}\,x_{n+1}-a_{32}\,y_{n+1}]$$


## Relaxation method 

Considering,
$$a_{11}x+a_{12}y+a_{13}z=d_1\implies R_{x}$$
$$a_{21}x+a_{22}y+a_{23}z=d_2\implies R_{y}$$
$$a_{31}x+a_{32}y+a_{33}z=d_3\implies R_{z}$$
