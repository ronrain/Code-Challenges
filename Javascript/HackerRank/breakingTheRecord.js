function breakingRecords(scores){
  //initialized at the first index of the scores array
  //keeps track of current max and min scores
  let max = scores[0]
  let min = scores[0]
  //counts how many times high and low records are broken
  let hiCount = 0
  let lowCount = 0

  for(let i = 0; i < scores.length; i++){//iterates through the entire array
    if(scores[i] > max){//if the score is greater than the current max
      max = scores[i]; //updates current max to the new score
      hiCount++;//increments by 1 to indicate a high record has been achieved
    } else if(scores[i] < min){//if the score is less than the current max
      min = scores[i]; //updates current min to the new score
      lowCount++ //increments by 1 to indicate a low record has been achieved
    }
  }
  return [lowCount, hiCount]//return the [min, max]
}


