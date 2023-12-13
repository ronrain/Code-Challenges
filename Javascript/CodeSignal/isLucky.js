// Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

// Given a ticket number n, determine if it's lucky or not.

// Example

// For n = 1230, the output should be
// solution(n) = true;
// For n = 239017, the output should be
// solution(n) = false.

function solution(n){
  const s = n.toString()//convert the number into a string
  const firstHalf = s.slice(0,s.length/2)//cutting in half; giving us the range of the cut; s.length/2 gives us half the lenth of the string
  const secondHalf = s.slice(s.length/2, s.length)//starts at the front of the second half and contunes the legth
  const array1 = firstHalf.split('')//make an array of individual strings
  const array2 = secondHalf.split('')//make array for individual strings
  const x = array1.reduce((a,b) => Number(a)+Number(b))//use reduce to find value of strings
  //change string to number using Number()
  const y = array1.reduce((a,b) => Number(a)+Number(b))

  return x === y
}