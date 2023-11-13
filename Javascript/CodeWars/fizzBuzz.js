function fizzbuzz(n){
  //crrate an empty array that will hold the new array
  const result = []
  //loop through list of numbers
  for(let i = 1; i<=n ; i++){
    //first condition is if it is a remainder of bith 3 and 5, 15 works for both
    if(i%15 === 0){
      //you push the string into the result array if that matches
      result.push("FizzBuzz")
      //for 3
    }else if(i%3=== 0){
      result.push("Fizz")
      //for 5
    }else if(i%5 ===0){
      result.push("Buzz")
      //push the number that was not divisible by 3 and/or 5 inot the new array
    }else {
      result.push(i)
    }
  }
  //return the new array
  return result
}
