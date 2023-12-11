// Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, each statue having an non-negative integer size. Since he likes to make things perfect, he wants to arrange them from smallest to largest so that each statue will be bigger than the previous one exactly by 1. He may need some additional statues to be able to accomplish that. Help him figure out the minimum number of additional statues needed.

// Example

// For statues = [6, 2, 3, 8], the output should be
// solution(statues) = 3.

// Ratiorg needs statues of sizes 4, 5 and 7.


function solution(statues) {
  const sorted = statues.sort((a,b) => a - b) //sort the array into ascending order; using sort() and the comparator function ((a,b) => a - b)
  let counter = 0 //iitializes the count of missing statues
  for (i = 0; i < statues.length - 1; i++){ //loops through the array; continues when the length of the array is one less than the length of the array = iterates upto the second to last element in the array
      if(statues[i+1] - statues[i] !== 1){ //takes the difference of the next element and the current element = checks if there are missing statues
          let missingStatues = 0 // initializes the variable if there are missing statues
          missingStatues = statues[i+1] -statues[i] - 1 //calculates the missing number of statues by subtracting the current statues height and then subtracting 1 to account for the missing statue itself
          counter += + missingStatues //the count of missing statues is added to the counter; the + i to ensure the value is treated as a number and added to the counter
      }
  }
  return counter //represents the total count of missing statues
}