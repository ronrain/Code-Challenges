// Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.

// Note: sequence a0, a1, ..., an is considered to be a strictly increasing if a0 < a1 < ... < an. Sequence containing only one element is also considered to be strictly increasing.

// Example

// For sequence = [1, 3, 2, 1], the output should be
// solution(sequence) = false.

// There is no one element in this array that can be removed in order to get a strictly increasing sequence.

// For sequence = [1, 3, 2], the output should be
// solution(sequence) = true.

// You can remove 3 from the array to get the strictly increasing sequence [1, 2]. Alternately, you can remove 2 to get the strictly increasing sequence [1, 3].


function solution(sequence) {
  let counter = 0 //init a variable to track the number of elements that re needed to be removed
  const s = sequence
  for(let i = 1; i < s.length; i++){ //inititates a for loop of s starting at the second element and continuing up to the last element
      if(s[i-1] >= s[i]){ //checks if the previous element is less than or equal to the current element
          counter++ //if true adds 1 to the counter variable
          if(counter > 1) return false //if tbe counter becomes greater than 1, indicating that more than ne element needs to be remvoed, the function immediately returns false bc it is not possible to return a strictly increasing sequence
          
          if(s[i-2] >=s[i] && s[i-1] >= s[i+1]) return false //if the 2 element positions before the current element s[i-2] is greater than or equal to the current element and if the element after the current elelemt s[i+1] is less than or equal to the previous element. returns false if this condition is true. 
          //ensures remvoing any singlke element would result in a strictly increasing sequence
      }
  }
  return true //if nothing was returned false, returns true
}