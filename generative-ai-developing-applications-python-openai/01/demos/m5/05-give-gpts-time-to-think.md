# Give GPTs Time to "Think

## Instruct the Model to Derive Its Conclusion through Reasoning from Fundamental Principles

SYSTEM
```
Evaluate whether the student's solution is correct or not.
```


User
```
Problem Statement: I am embarking on a home renovation project and need assistance calculating the expenses.

The cost of flooring is $20 per square foot.
I'm hiring a contractor who charges $50 per hour for labor.
In addition, there are fixed project costs of $1,000 for permits and $500 for equipment rental.
How can I express the total cost of my renovation as a function of the number of hours of labor and the area in square feet?

Student's Solution: Let 'x' represent the area in square feet, and 'y' represent the number of hours of labor.

Flooring cost: 20x
Labor cost: 50y
Fixed costs: 1,000 (permits) + 500 (equipment rental)
Total cost: 20x + 50y + 1,000 + 500 = 20x + 50y + 1,500
```


## Employ Inner Monologue or a Sequence of Queries to Conceal the Model's Reasoning Process

Now use this to allow the GPT to calculate the result and then compare to the student's result.

System
```
To address user queries, follow these steps:

Step 1: Begin by formulating your own solution to the problem independently, without relying on the student's solution. Enclose all your work for this step within triple quotes (""").

Step 2: Compare your solution with the student's solution and evaluate its correctness. Enclose all your work for this step within triple quotes (""").

Step 3: In case the student's solution contains errors, determine a hint that can guide the student without giving away the complete answer. Enclose all your work for this step within triple quotes (""").

Step 4: If the student's solution is incorrect, provide the hint from the previous step to the student (outside of triple quotes). Instead of writing "Step 4 - ...," preface it with "Hint:."
```
  