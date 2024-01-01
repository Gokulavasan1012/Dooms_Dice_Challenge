# Dooms_Dice_Challenge
"Dooms Dice Challenge is a problem to find the number of spots on each face of the dices by following the given constraints"" 

The total number of spots removed in both the dice is 42 (2*(1+2+3+4+5+6)).
And so we conclude that any solution for this question will have the sum of spots as 42.

The only combination of getting sum 2 before removing the spots is (1,1) which is the only way for getting the sum 2.
So it is a fact that each die must have only one occurrence of 1 in it to ensure the probability of getting 2 before and after removing the spots are the same. 

Let’s consider two lists,
new_die_A=[1,]
new_die_B=[1,]

As we it is considered that value 1 should be present in both the dice in order to satisfy the probability of 2 and hence, by following the specified constraints the new_die_A  and new_die_B initially contains,

new_die_A=[1,2,3,4,]
 
new_die_B=[1,]

The approach that we are using is the increasing and decreasing of numbers

Initially we had Die_A as [1,2,3,4,5,6]
The only two numbers that don't follow the constraints are 5 and 6 and so we remove them from the set.

Now we have removed a sum of 11 i.e 5+6 we need to compensate for that.

The possibilities for the remaining two spots in Die_A are as follows
2,2
2,3
2,4
3,3
3,4
4,4

Now by these limited number of possibilities the time consumed for the program to run is highly reduced since the number of combinations to be checked is reduced.

For example let us 2,2 as our combination,
Die_A becomes [1,2,3,4,2,2]

We have added 2+2 =4 spots into the dice. We have to add 7 (11-4) more spots into them as well.
Inorder to compensate the sum we can add the 7 in the Die_B 

Die_B initially is [1,2,3,4,5,6]

Obviously it is not possible to add that 7 in 1 or 5 or 6.

The possible numbers that the 7 can be added to are 2,3,4 and by checking these combinations we can arrive at an answer.


Let us assume that we take 2,
Die_A is [1,2,3,4,2,2]
Die_B becomes [1,9,3,4,5,6]

In this case the probability of getting 11 is not the same as the original probability.

Similarly we can check for 3 and 4 as well.

The desired solution arrives when we assume the two spots in Die_A as 2,3 and adding the remainder sum to the number 2

So, the solution is:
New_Die_A [1,2,3,4,2,3]
New_Die_B [1,8,3,4,5,6]

This is the optimized approach for arriving at an answer




