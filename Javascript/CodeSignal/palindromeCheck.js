function palindromeCheck(input){
  let word = input //set the parameter to a variable "racecar" = "racecar"
  let letters = word.split("") //use split to convert string into an array ['r','a','c','e','c','a','r']
  let reversedLetters = letters.reverse() //use reverse method on the array ['r','a','c','e','c','a','r']
  let reversedWord = reversedLetters.join("") //join the strings together to create the word backwards racecar

  if(word.toLowerCase() == reversedWord.toLowerCase()){//its a palindrone of the reveresed words are equal
    //toLowerCase() is used to make sure all the letters are lower case so an error isnt thrown
    return true
  } else{
    return false
  }
}

let word = input //"racecar" = "racecar"
let letters = word.split("") //['r','a','c','e','c','a','r']
let reversedLetters = letters.reverse() //use reverse method on the array['r','a','c','e','c','a','r']
let reversedWord = reversedLetters.join("") //join the strings together to create the word backwardsracecar

