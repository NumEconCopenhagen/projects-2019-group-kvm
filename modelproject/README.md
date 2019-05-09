# Model project

In this project we analyze a consumer problem with a CES utility function and two goods, x1 and x2.

The utility function: alpha is a preference parameter and rho is the elasticity parameter
The income is 30 and the prices of the goods are: \\[ p_1=2, p_2=4\\].

First we investigate the jacobian and hessian matrix and how to use gradient based optimizers. In this section we use the *minimize_gradient_descent()* method.

In the next section the budget constraint is introduced and we try to solve the consumer problem using a *Multi-dimensional constrained solver*.

After this the consumer problem is solved by using the **SLSQP** optimizer.

In the last section we introduce an extension to the problem where we impose a tax on good x2, which increases the price p2 with 0.5 for each consumed x2. 

We find that the tax on good x2 increases the optimal amount of consumed x1 in order to maximize the utility and therefore the consumer wish to consume almost as much of x1 as x2. x1=3.7 and x2=3.8. 
