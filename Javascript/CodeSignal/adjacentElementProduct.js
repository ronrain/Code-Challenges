function solution(inputArray) {
  let largestProduct= [] //create an empty array that the largest product will go into
  for(let i = 0; 0 < inputArray.length - 1; i++){//loop through the entire array // length-1 bc the first index would be repeated at the end creating unefined bc it loops through the length but the number of pais is one less than the length
    const newArray = inputArray[i] * inputArray[i + 1]//the multiplies the indeces next to each other. adding 1 makes it work
    largestProduct.push(newArray)//pushing the new numbers into the array
  }
    return Math.max(...largestProduct)//Math.max finds the largest number and 
}