function miniMaxSum(arr){
  let sum = 0 //define the total sum of the array 
  let newArr = arr.sort() //put the array in order by using sort (will be put fromleast to greatest)
//sort manipulates the array (changes it)
  for(let i = 0; i < newArr.length; i++){ //loop through the array
    sum += newArr[i] //add the element at the particular index to the sum
  }
//define the max and min
//you have to use the newArr bc that is the ordered array
  let max = sum - newArr[0] //subract the lowest number from the sum
  let min = sum - newArr[newArr.length - 1] //the newArr.length is the total number of elements in the array, to find out what the index is, you subtract 1 from the length of the array. Must put in square brackets to find the new index
  console.log(min, max)
}