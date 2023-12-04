function plusMinus(arr){
  //define what we are looking for
  var positive = 0
  var negative = 0
  var zero = 0

  //loop through each element in the array
  for (var i = 0; i < arr.length; i++){
    if (arr[i] > 0){//if the element at position i is greater than 0, add 1 to positive
      positive += 1
    } else if (arr[i] < 0){
      negative += 1
    } else{
      zero += 1
    }
  }
  //outside of for loop
  //will gove us a fraction value
  var pos = positive / arr.length
  var neg = negative / arr.length
  var zer = zero / arr.length

  //toFixed makes it into a decimal to a certain amount of decimal places
  //"\n" puts it on a new line
  console.log(pos.toFixed(6) + "\n" + neg.toFixed(6) + "\n" + zer.toFixed(6))
}

