# NOV-Rig-Analytics_Challange
* Include a `README` with:
  * Instructions to run the code and install any necessary dependencies.

  Data set must be in appropriate location for solution to run. 
  No dependencies needed.

  * Description of the problem and solution.

  The problem presented is there are x customers and less y tellers. Each teller can help any customer but can speed up a customer interaction if the customers need fits the tellers specialty. We want to find the most optimal solution that will allow all customers to be seen and tellers to go home in the quickest time.

  The solution I used to approach this problem was to split the customers and tellers according to their question type/specialty. Since there are 4 question types, I had 4 different lines. My thought process was to have each question type get helped by the corresponding specialist first. Once a line of questions had been solved the next longest line would then fill the spots with tellers to have a even spread. I used a nested loop with the outer while loop to iterate through all of the 5000 customers, then the inner for loops would iterate through each specialtist. I would add the toal time to each teller and adjust multipliers when applicable. For each of the inner loops the corresponding customers for a specialty teller went first to maximize the savings. This loop continued until all customers were helped. The longest time a teller a teller had was 810 minutes.

  * Reasoning behind your technical choices.

  My reasononing for choosing this approach was to evenly didstribibute the customers while trying to prioritize and maxamize time. 

  * Assumptions you made.

  The data is already sorted by customer/teller type and duration. 
  There are only the 4 customer type and teller specialty. Them being 1,  2, 3, 4, and 0.
  Only 149 tellers from data sheet.


  * If there are features you didn't have time to implement or would improve or do differently next time, describe the intended behavior.

  I would make the code a little neater and less redundant would be something to look into. I would then make the code identify questions instead of group them instead of hard coded in. Lastly, for the actual solution, I would try to implement a way to indentify the next longest line rather then knowing before hand and hard coding it in to assign to the tellers. Overall, I know the solution is not the most efficient and can be better optimized.

