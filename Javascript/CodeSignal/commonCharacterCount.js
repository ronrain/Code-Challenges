function solution(s1, s2){
  let counter = 0 //init counter to keep track of common characters between s1 and s2
  let arrayS1 = s1.split('')//split the string s1 into an array of characters; allows to be process one by one
  let y = s2//copy second string into variable y

  while(arrayS1.length){//start a while loop that runs as long as there are characters in arrayS1
    const x = arrayS1.pop()//remove the last character from arrayS1 and store it in variable x; allows you to examine characters from s1 one at a time
    if(y.includes(x)){//check if the character x exists in variable y using includes
      counter++//if it does exisit increment by 1
      y = y.replace(x,'')// remove the first occurence of x from the string y
    }
  }// repeat loop until all characters have been processed
  return counter
}