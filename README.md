Include a `README` with:
  * Instructions to run the code and install any necessary dependencies.

  Data set must be in the appropriate location for the solution to run. 
  No dependencies needed.

  * Description of the problem and solution.

 	The problem presented is there are x customers and fewer y tellers. Each teller can help any customer but customer interaction can be sped up if the customers' needs fit the teller's specialty. The tellers are only released to go home once every customer has been helped. The objective is to find the most optimal solution that will allow all customers to be seen and tellers to go home in the quickest amount of time.

   This problem was approached by splitting the customers and tellers according to their question type/specialty. Since there are four question types, there are four different lines. Each question type was addressed by the corresponding specialist first. Once a line of questions has been solved, the next longest line of customers with another question type would then fill the spots with available tellers to have an even distribution. 

A nested loop with the outer while loop was used to iterate through all of the 5000 customers, then the inner for loops would iterate through each specialist. The total time was added to each teller along with adjusted multipliers when applicable. For each of the inner loops, the corresponding customers for a specialty teller were helped first to maximize the savings. This loop continued until all customers were helped. The longest time a teller had was 810 minutes.

  * Reasoning behind your technical choices.

  My reasoning for choosing this approach was to evenly distribute the customers while trying to prioritize and maximize time. 

  * Assumptions you made.

  The data is already sorted by customer/teller type and duration. 
  There are only 4 customer types and teller specialties. Them being 1,  2, 3, 4, and 0.
  There are only 149 tellers, from the data sheet.


  * If there are features you didn't have time to implement or would improve or do differently next time, describe the intended behavior.

 Making the code a neater with fewer redundancies would be something to look into. I would then make the code identify question types instead of assuming and hard coding it in. Lastly, I would implement a way to identify the next longest line rather than knowing beforehand and hard coding it in to assign to the tellers. 


