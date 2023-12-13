// Given an array of strings, return another array containing all of its longest strings.

// Example

// For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
// solution(inputArray) = ["aba", "vcd", "aba"].

function solution(inputArray){
  let length = 0//find length of each indiviudal array; using let bc we are going to change it
  for(const val of inputArray){//loop through all the values
    //the val is the current string being looked at from the input array
    //val.length is the length of the current value being looked at in the array
    //length is the max value of the string
  length = Math.max(length, val.length)//new length is equal to the length of Math.max of whatever length os equal to and the value . length
  //filter will output anoter array; filtering through the elements //output any elements that has an equal length to the max length  
  return inputArray.filter( element => element.length === length)
}}
